# 第3章: ルーティングとHTTPメソッド

## 学習目標

- HTTPメソッド（GET, POST, PUT, DELETE）の理解と使い分け
- APIRouterを使ったルーティングの分割
- パスオペレーションの詳細設定
- タグとメタデータの活用

## HTTPメソッド

### GET - データの取得
```python
@app.get("/items")
def get_items():
    return [{"id": 1, "name": "Item 1"}]
```

### POST - データの作成
```python
@app.post("/items")
def create_item(name: str):
    return {"id": 1, "name": name}
```

### PUT - データの更新（完全置換）
```python
@app.put("/items/{item_id}")
def update_item(item_id: int, name: str):
    return {"id": item_id, "name": name}
```

### PATCH - データの部分更新
```python
@app.patch("/items/{item_id}")
def partial_update_item(item_id: int, name: str = None):
    return {"id": item_id, "name": name}
```

### DELETE - データの削除
```python
@app.delete("/items/{item_id}")
def delete_item(item_id: int):
    return {"message": "Item deleted"}
```

## APIRouter

### ルーターの作成と分割

```python
# routers/users.py
from fastapi import APIRouter

router = APIRouter(
    prefix="/users",
    tags=["users"]
)

@router.get("/")
def get_users():
    return [{"id": 1, "name": "Alice"}]

# main.py
from fastapi import FastAPI
from routers import users

app = FastAPI()
app.include_router(users.router)
```

## パスオペレーションの設定

```python
@app.get(
    "/items/{item_id}",
    summary="Get an item",
    description="Get an item by its ID",
    response_description="The item details",
    tags=["items"]
)
def get_item(item_id: int):
    return {"id": item_id}
```

## 次のステップ

[第4章: リクエストとレスポンス](../04-request-response/README.md)に進みましょう。
