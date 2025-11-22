# 第4章: リクエストとレスポンス

## 学習目標

- リクエストボディの処理
- レスポンスモデルの定義
- ステータスコードの使い分け
- ヘッダーとCookieの操作

## リクエストボディ

### Pydanticモデルの使用
```python
from pydantic import BaseModel

class Item(BaseModel):
    name: str
    price: float
    description: str = None

@app.post("/items")
def create_item(item: Item):
    return item
```

## レスポンスモデル

```python
class ItemResponse(BaseModel):
    id: int
    name: str
    price: float

@app.post("/items", response_model=ItemResponse)
def create_item(item: Item):
    return {"id": 1, **item.dict()}
```

## ステータスコード

```python
from fastapi import status

@app.post("/items", status_code=status.HTTP_201_CREATED)
def create_item(item: Item):
    return item

@app.get("/items/{item_id}", status_code=status.HTTP_200_OK)
def get_item(item_id: int):
    return {"id": item_id}
```

## ヘッダーとCookie

```python
from fastapi import Header, Cookie

@app.get("/headers")
def read_headers(user_agent: str = Header(None)):
    return {"User-Agent": user_agent}

@app.get("/cookies")
def read_cookies(session_id: str = Cookie(None)):
    return {"session_id": session_id}
```
