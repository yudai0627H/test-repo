# 第7章: 依存性注入

## 学習目標

- Depends()の理解と活用
- データベースセッション管理
- カスタム依存関係の作成
- 依存関係の再利用

## 基本的な依存性注入

```python
from fastapi import Depends

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

@app.get("/users")
def get_users(db: Session = Depends(get_db)):
    return db.query(User).all()
```

## 依存関係の階層化

```python
def get_current_user(token: str = Depends(oauth2_scheme)):
    user = decode_token(token)
    return user

def get_current_active_user(current_user: User = Depends(get_current_user)):
    if not current_user.is_active:
        raise HTTPException(status_code=400, detail="Inactive user")
    return current_user

@app.get("/me")
def read_users_me(current_user: User = Depends(get_current_active_user)):
    return current_user
```

## クラスベースの依存関係

```python
class CommonQueryParams:
    def __init__(self, skip: int = 0, limit: int = 100):
        self.skip = skip
        self.limit = limit

@app.get("/items")
def read_items(commons: CommonQueryParams = Depends()):
    return {"skip": commons.skip, "limit": commons.limit}
```
