"""
問題3の模範解答: ログインエンドポイント
JWTトークンを使った完全な認証システム

【重要な修正ポイント】
1. datetime.utcnow() → datetime.now(timezone.utc) に変更（Python 3.12で非推奨）
2. SECRET_KEY は環境変数から読み込むべき（本番環境）
3. Optional[str] → str | None に変更（Python 3.10+）
"""

import os
from datetime import datetime, timedelta, timezone
from fastapi import FastAPI, Depends, HTTPException, status
from fastapi.security import OAuth2PasswordBearer, OAuth2PasswordRequestForm
from jose import JWTError, jwt
from passlib.context import CryptContext
from pydantic import BaseModel

# 設定
# 本番環境では必ず環境変数から読み込む
# 学習用のため、デフォルト値を設定しているが、本番ではエラーにすべき
SECRET_KEY = os.getenv("SECRET_KEY", "development-secret-key-change-in-production")
ALGORITHM = "HS256"
ACCESS_TOKEN_EXPIRE_MINUTES = 30

# 本番環境では環境変数が必須
if SECRET_KEY == "development-secret-key-change-in-production":
    print("⚠️ 警告: 本番環境ではSECRET_KEY環境変数を設定してください")

# パスワードハッシュ化の設定
pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")

# OAuth2設定
oauth2_scheme = OAuth2PasswordBearer(tokenUrl="token")

app = FastAPI(
    title="認証システムデモ",
    description="JWT認証の学習用アプリケーション"
)


# データモデル（Python 3.10+ の型ヒント）
class Token(BaseModel):
    access_token: str
    token_type: str


class TokenData(BaseModel):
    username: str | None = None


class User(BaseModel):
    username: str
    email: str | None = None
    full_name: str | None = None
    disabled: bool | None = None


class UserInDB(User):
    hashed_password: str


# ダミーデータベース（本番環境では実際のDBを使用）
fake_users_db = {
    "johndoe": {
        "username": "johndoe",
        "full_name": "John Doe",
        "email": "johndoe@example.com",
        "hashed_password": "$2b$12$EixZaYVK1fsbw1ZfbX3OXePaWxn96p36WQoeG6Lruj3vjPGga31lW",  # "secret"
        "disabled": False,
    },
    "alice": {
        "username": "alice",
        "full_name": "Alice Wonderland",
        "email": "alice@example.com",
        "hashed_password": "$2b$12$EixZaYVK1fsbw1ZfbX3OXePaWxn96p36WQoeG6Lruj3vjPGga31lW",  # "secret"
        "disabled": False,
    }
}


# パスワード関連関数
def verify_password(plain_password: str, hashed_password: str) -> bool:
    """プレーンテキストのパスワードとハッシュを比較"""
    return pwd_context.verify(plain_password, hashed_password)


def get_password_hash(password: str) -> str:
    """パスワードをハッシュ化"""
    return pwd_context.hash(password)


def get_user(db: dict, username: str) -> UserInDB | None:
    """データベースからユーザーを取得"""
    if username in db:
        user_dict = db[username]
        return UserInDB(**user_dict)
    return None


def authenticate_user(fake_db: dict, username: str, password: str) -> UserInDB | bool:
    """ユーザーを認証"""
    user = get_user(fake_db, username)
    if not user:
        return False
    if not verify_password(password, user.hashed_password):
        return False
    return user


def create_access_token(data: dict, expires_delta: timedelta | None = None) -> str:
    """
    JWTアクセストークンを生成

    【重要】datetime.utcnow() は Python 3.12 で非推奨
    代わりに datetime.now(timezone.utc) を使用
    """
    to_encode = data.copy()

    # ✅ 正しい書き方
    if expires_delta:
        expire = datetime.now(timezone.utc) + expires_delta
    else:
        expire = datetime.now(timezone.utc) + timedelta(minutes=15)

    to_encode.update({"exp": expire})
    encoded_jwt = jwt.encode(to_encode, SECRET_KEY, algorithm=ALGORITHM)
    return encoded_jwt


async def get_current_user(token: str = Depends(oauth2_scheme)) -> User:
    """トークンから現在のユーザーを取得"""
    credentials_exception = HTTPException(
        status_code=status.HTTP_401_UNAUTHORIZED,
        detail="Could not validate credentials",
        headers={"WWW-Authenticate": "Bearer"},
    )
    try:
        payload = jwt.decode(token, SECRET_KEY, algorithms=[ALGORITHM])
        username: str | None = payload.get("sub")
        if username is None:
            raise credentials_exception
        token_data = TokenData(username=username)
    except JWTError:
        raise credentials_exception

    user = get_user(fake_users_db, username=token_data.username)
    if user is None:
        raise credentials_exception
    return user


async def get_current_active_user(current_user: User = Depends(get_current_user)) -> User:
    """アクティブなユーザーのみを許可"""
    if current_user.disabled:
        raise HTTPException(status_code=400, detail="Inactive user")
    return current_user


# エンドポイント
@app.post("/token", response_model=Token)
async def login_for_access_token(form_data: OAuth2PasswordRequestForm = Depends()):
    """ログインしてアクセストークンを取得"""
    user = authenticate_user(fake_users_db, form_data.username, form_data.password)
    if not user:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Incorrect username or password",
            headers={"WWW-Authenticate": "Bearer"},
        )
    access_token_expires = timedelta(minutes=ACCESS_TOKEN_EXPIRE_MINUTES)
    access_token = create_access_token(
        data={"sub": user.username}, expires_delta=access_token_expires
    )
    return {"access_token": access_token, "token_type": "bearer"}


@app.get("/users/me", response_model=User)
async def read_users_me(current_user: User = Depends(get_current_active_user)):
    """現在のユーザー情報を取得"""
    return current_user


@app.get("/users/me/items")
async def read_own_items(current_user: User = Depends(get_current_active_user)):
    """現在のユーザーのアイテムを取得"""
    return [{"item_id": "Foo", "owner": current_user.username}]


# テスト用エンドポイント
@app.post("/register")
async def register_user(username: str, password: str, email: str, full_name: str):
    """新しいユーザーを登録（テスト用）"""
    if username in fake_users_db:
        raise HTTPException(status_code=400, detail="Username already registered")

    hashed_password = get_password_hash(password)
    fake_users_db[username] = {
        "username": username,
        "full_name": full_name,
        "email": email,
        "hashed_password": hashed_password,
        "disabled": False,
    }
    return {"message": "User created successfully"}


if __name__ == "__main__":
    import uvicorn

    print("\n=== FastAPI 認証システムのデモ ===")
    print("\n【セキュリティ注意事項】")
    print("- SECRET_KEY は環境変数から設定してください")
    print("- 本番環境では必ずHTTPSを使用してください")
    print("\n使用方法:")
    print("1. ユーザー登録（オプション）:")
    print("   POST /register")
    print("   パラメータ: username, password, email, full_name")
    print("\n2. ログイン:")
    print("   POST /token")
    print("   Form Data: username=johndoe, password=secret")
    print("\n3. 保護されたエンドポイントにアクセス:")
    print("   GET /users/me")
    print("   Header: Authorization: Bearer <token>")
    print("\nデフォルトユーザー:")
    print("  username: johndoe, password: secret")
    print("  username: alice, password: secret")
    print("\nサーバーを起動しています...")

    uvicorn.run(app, host="0.0.0.0", port=8000)
