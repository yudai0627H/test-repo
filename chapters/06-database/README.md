# 第6章: データベース連携

## 学習目標

- SQLAlchemy 2.0の基礎
- データベースモデルの定義
- CRUD操作の実装
- トランザクション管理

## 重要: SQLAlchemy 2.0 について

このコースでは **SQLAlchemy 2.0** を使用します。主な変更点：
- `declarative_base()` → `DeclarativeBase` クラスを継承
- `Query` API → `select()` 文を使用
- `Session.execute()` で結果を取得

## SQLAlchemy 2.0 セットアップ

```python
from sqlalchemy import create_engine, String
from sqlalchemy.orm import DeclarativeBase, Mapped, mapped_column, sessionmaker

SQLALCHEMY_DATABASE_URL = "sqlite:///./app.db"
# PostgreSQL: "postgresql://user:password@localhost/dbname"
# PostgreSQL Async: "postgresql+asyncpg://user:password@localhost/dbname"

engine = create_engine(
    SQLALCHEMY_DATABASE_URL,
    connect_args={"check_same_thread": False}  # SQLiteのみ必要
)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)


# SQLAlchemy 2.0 スタイルのベースクラス
class Base(DeclarativeBase):
    pass
```

## モデル定義（SQLAlchemy 2.0 スタイル）

```python
from datetime import datetime
from sqlalchemy import String, Boolean, DateTime, func
from sqlalchemy.orm import Mapped, mapped_column, relationship
from typing import Optional

class User(Base):
    __tablename__ = "users"

    # SQLAlchemy 2.0 の Mapped 型ヒント
    id: Mapped[int] = mapped_column(primary_key=True, index=True)
    name: Mapped[str] = mapped_column(String(100), index=True)
    email: Mapped[str] = mapped_column(String(255), unique=True, index=True)
    hashed_password: Mapped[str] = mapped_column(String(255))
    is_active: Mapped[bool] = mapped_column(Boolean, default=True)
    created_at: Mapped[datetime] = mapped_column(
        DateTime(timezone=True),
        server_default=func.now()
    )
    updated_at: Mapped[Optional[datetime]] = mapped_column(
        DateTime(timezone=True),
        onupdate=func.now(),
        nullable=True
    )

    # リレーションシップ
    posts: Mapped[list["Post"]] = relationship(back_populates="author")


class Post(Base):
    __tablename__ = "posts"

    id: Mapped[int] = mapped_column(primary_key=True, index=True)
    title: Mapped[str] = mapped_column(String(200))
    content: Mapped[str] = mapped_column(String)
    author_id: Mapped[int] = mapped_column(ForeignKey("users.id"))

    author: Mapped["User"] = relationship(back_populates="posts")
```

## データベースセッション管理

```python
from fastapi import Depends
from sqlalchemy.orm import Session
from typing import Generator

def get_db() -> Generator[Session, None, None]:
    """データベースセッションの依存関係"""
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()
```

## CRUD操作（SQLAlchemy 2.0 スタイル）

```python
from sqlalchemy import select
from sqlalchemy.orm import Session
from fastapi import HTTPException

# Create
def create_user(db: Session, name: str, email: str, password: str) -> User:
    """ユーザーを作成"""
    db_user = User(
        name=name,
        email=email,
        hashed_password=get_password_hash(password)
    )
    db.add(db_user)
    db.commit()
    db.refresh(db_user)
    return db_user

# Read (単一)
def get_user(db: Session, user_id: int) -> User | None:
    """IDでユーザーを取得"""
    # SQLAlchemy 2.0 スタイル
    stmt = select(User).where(User.id == user_id)
    return db.execute(stmt).scalar_one_or_none()

# Read (複数)
def get_users(db: Session, skip: int = 0, limit: int = 100) -> list[User]:
    """ユーザー一覧を取得"""
    stmt = select(User).offset(skip).limit(limit)
    return list(db.execute(stmt).scalars().all())

# Read (条件検索)
def get_user_by_email(db: Session, email: str) -> User | None:
    """メールアドレスでユーザーを検索"""
    stmt = select(User).where(User.email == email)
    return db.execute(stmt).scalar_one_or_none()

# Update
def update_user(db: Session, user_id: int, name: str | None = None) -> User:
    """ユーザーを更新"""
    db_user = get_user(db, user_id)
    if not db_user:
        raise HTTPException(status_code=404, detail="User not found")

    if name is not None:
        db_user.name = name

    db.commit()
    db.refresh(db_user)
    return db_user

# Delete
def delete_user(db: Session, user_id: int) -> bool:
    """ユーザーを削除"""
    db_user = get_user(db, user_id)
    if not db_user:
        return False

    db.delete(db_user)
    db.commit()
    return True
```

## FastAPIとの統合

```python
from fastapi import FastAPI, Depends, HTTPException
from sqlalchemy.orm import Session

app = FastAPI()

# テーブル作成（開発時のみ、本番ではマイグレーションを使用）
Base.metadata.create_all(bind=engine)

@app.post("/users", response_model=UserResponse, status_code=201)
def create_user_endpoint(
    user: UserCreate,
    db: Session = Depends(get_db)
):
    """ユーザーを作成"""
    # 重複チェック
    existing_user = get_user_by_email(db, user.email)
    if existing_user:
        raise HTTPException(status_code=400, detail="Email already registered")
    return create_user(db, user.name, user.email, user.password)

@app.get("/users", response_model=list[UserResponse])
def read_users(
    skip: int = 0,
    limit: int = 100,
    db: Session = Depends(get_db)
):
    """ユーザー一覧を取得"""
    return get_users(db, skip=skip, limit=limit)

@app.get("/users/{user_id}", response_model=UserResponse)
def read_user(user_id: int, db: Session = Depends(get_db)):
    """特定のユーザーを取得"""
    user = get_user(db, user_id)
    if not user:
        raise HTTPException(status_code=404, detail="User not found")
    return user
```

## トランザクション管理

```python
from sqlalchemy.exc import SQLAlchemyError

def transfer_points(db: Session, from_user_id: int, to_user_id: int, points: int):
    """ポイントを転送（トランザクション例）"""
    try:
        from_user = get_user(db, from_user_id)
        to_user = get_user(db, to_user_id)

        if not from_user or not to_user:
            raise HTTPException(status_code=404, detail="User not found")

        if from_user.points < points:
            raise HTTPException(status_code=400, detail="Insufficient points")

        from_user.points -= points
        to_user.points += points

        db.commit()
        return {"message": "Transfer successful"}

    except SQLAlchemyError as e:
        db.rollback()
        raise HTTPException(status_code=500, detail="Database error")
```

## 非同期データベース操作

```python
from sqlalchemy.ext.asyncio import create_async_engine, AsyncSession, async_sessionmaker

ASYNC_DATABASE_URL = "postgresql+asyncpg://user:password@localhost/dbname"

async_engine = create_async_engine(ASYNC_DATABASE_URL)
AsyncSessionLocal = async_sessionmaker(async_engine, expire_on_commit=False)

async def get_async_db():
    async with AsyncSessionLocal() as session:
        yield session

@app.get("/async/users")
async def get_users_async(db: AsyncSession = Depends(get_async_db)):
    stmt = select(User)
    result = await db.execute(stmt)
    return result.scalars().all()
```

## 次のステップ

データベース連携を理解したら、[第7章: 依存性注入](../07-dependency-injection/README.md)に進みましょう。
