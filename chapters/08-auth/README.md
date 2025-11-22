# 第8章: 認証認可

## 学習目標

- JWTトークンの生成と検証
- OAuth2フローの実装
- パスワードのハッシュ化
- ロールベースアクセス制御（RBAC）
- セキュリティベストプラクティス

## 重要: セキュリティに関する注意事項

**絶対に守るべきルール:**
1. SECRET_KEYは必ず環境変数から読み込む（ハードコード禁止）
2. パスワードは必ずハッシュ化して保存
3. 本番環境ではHTTPS必須
4. トークンの有効期限は短く設定

## 環境変数の設定

```python
import os
from pydantic_settings import BaseSettings

class Settings(BaseSettings):
    """アプリケーション設定"""
    secret_key: str  # 環境変数 SECRET_KEY から読み込み
    algorithm: str = "HS256"
    access_token_expire_minutes: int = 30

    class Config:
        env_file = ".env"

settings = Settings()
```

`.env` ファイル（**必ず.gitignoreに追加**）:
```
SECRET_KEY=your-super-secret-key-at-least-32-characters-long
```

## パスワードのハッシュ化

```python
from passlib.context import CryptContext

pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")

def verify_password(plain_password: str, hashed_password: str) -> bool:
    """プレーンパスワードとハッシュを比較"""
    return pwd_context.verify(plain_password, hashed_password)

def get_password_hash(password: str) -> str:
    """パスワードをハッシュ化"""
    return pwd_context.hash(password)
```

## JWTトークンの生成

**注意: `datetime.utcnow()` は Python 3.12 で非推奨です**

```python
from datetime import datetime, timedelta, timezone
from jose import JWTError, jwt
from typing import Optional

def create_access_token(
    data: dict,
    expires_delta: Optional[timedelta] = None
) -> str:
    """JWTアクセストークンを生成"""
    to_encode = data.copy()

    # ✅ 正しい書き方: datetime.now(timezone.utc)
    # ❌ 非推奨: datetime.utcnow()
    if expires_delta:
        expire = datetime.now(timezone.utc) + expires_delta
    else:
        expire = datetime.now(timezone.utc) + timedelta(minutes=15)

    to_encode.update({"exp": expire})
    encoded_jwt = jwt.encode(
        to_encode,
        settings.secret_key,
        algorithm=settings.algorithm
    )
    return encoded_jwt
```

## OAuth2認証

```python
from fastapi import Depends, HTTPException, status
from fastapi.security import OAuth2PasswordBearer, OAuth2PasswordRequestForm
from pydantic import BaseModel

oauth2_scheme = OAuth2PasswordBearer(tokenUrl="token")

class Token(BaseModel):
    access_token: str
    token_type: str

class User(BaseModel):
    username: str
    email: str | None = None
    disabled: bool | None = None


async def get_current_user(token: str = Depends(oauth2_scheme)) -> User:
    """トークンから現在のユーザーを取得"""
    credentials_exception = HTTPException(
        status_code=status.HTTP_401_UNAUTHORIZED,
        detail="Could not validate credentials",
        headers={"WWW-Authenticate": "Bearer"},
    )
    try:
        payload = jwt.decode(
            token,
            settings.secret_key,
            algorithms=[settings.algorithm]
        )
        username: str = payload.get("sub")
        if username is None:
            raise credentials_exception
    except JWTError:
        raise credentials_exception

    user = get_user(username)  # DBからユーザーを取得
    if user is None:
        raise credentials_exception
    return user


@app.post("/token", response_model=Token)
async def login_for_access_token(
    form_data: OAuth2PasswordRequestForm = Depends()
):
    """ログインしてアクセストークンを取得"""
    user = authenticate_user(form_data.username, form_data.password)
    if not user:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Incorrect username or password",
            headers={"WWW-Authenticate": "Bearer"},
        )
    access_token_expires = timedelta(minutes=settings.access_token_expire_minutes)
    access_token = create_access_token(
        data={"sub": user.username},
        expires_delta=access_token_expires
    )
    return {"access_token": access_token, "token_type": "bearer"}


@app.get("/users/me", response_model=User)
async def read_users_me(current_user: User = Depends(get_current_user)):
    """現在のユーザー情報を取得"""
    return current_user
```

## ロールベースアクセス制御（RBAC）

```python
from enum import Enum

class UserRole(str, Enum):
    ADMIN = "admin"
    MODERATOR = "moderator"
    USER = "user"
    GUEST = "guest"


def require_role(required_roles: list[UserRole]):
    """指定されたロールを持つユーザーのみ許可"""
    def role_checker(current_user: User = Depends(get_current_user)):
        if current_user.role not in required_roles:
            raise HTTPException(
                status_code=status.HTTP_403_FORBIDDEN,
                detail="Insufficient permissions"
            )
        return current_user
    return role_checker


# 使用例: 管理者のみがユーザーを削除可能
@app.delete("/users/{user_id}")
def delete_user(
    user_id: int,
    current_user: User = Depends(require_role([UserRole.ADMIN]))
):
    return {"message": f"User {user_id} deleted"}
```

## パスワードポリシー（Pydantic v2）

```python
import re
from pydantic import BaseModel, field_validator

class UserCreate(BaseModel):
    username: str
    email: str
    password: str

    @field_validator('password')
    @classmethod
    def validate_password(cls, v: str) -> str:
        """パスワード強度を検証"""
        if len(v) < 8:
            raise ValueError('パスワードは8文字以上必要です')
        if not re.search(r'[A-Z]', v):
            raise ValueError('大文字を含める必要があります')
        if not re.search(r'[a-z]', v):
            raise ValueError('小文字を含める必要があります')
        if not re.search(r'\d', v):
            raise ValueError('数字を含める必要があります')
        return v
```

## 次のステップ

認証認可を理解したら、[第9章: テストコード](../09-testing/README.md)に進みましょう。
