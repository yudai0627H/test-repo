# 第2章: FastAPI入門

## 学習目標

- FastAPIの基本概念と特徴の理解
- 最初のAPIアプリケーションの作成
- 自動ドキュメント生成の活用
- 基本的なエンドポイントの実装

## FastAPIとは

FastAPIは、Pythonで高速にAPIを構築するための、モダンで高性能なWebフレームワークです。

### 主な特徴

- **高速**: NodeJSやGoと同等の非常に高いパフォーマンス
- **型安全**: Python型ヒントによる自動バリデーション
- **自動ドキュメント**: Swagger UI とReDocの自動生成
- **開発効率**: 最小限のコードで強力な機能を実現
- **標準準拠**: OpenAPI、JSON Schemaなどの標準に準拠

## 最初のFastAPIアプリケーション

### インストール

```bash
pip install fastapi uvicorn[standard]
```

### Hello Worldアプリケーション

```python
from fastapi import FastAPI

app = FastAPI()

@app.get("/")
def read_root():
    return {"message": "Hello World"}

@app.get("/items/{item_id}")
def read_item(item_id: int, q: str = None):
    return {"item_id": item_id, "q": q}
```

### アプリケーションの実行

```bash
uvicorn main:app --reload
```

- `main`: Pythonファイル名（main.py）
- `app`: FastAPIインスタンス名
- `--reload`: コード変更時の自動リロード（開発時のみ）

### 自動ドキュメント

アプリケーション起動後、以下のURLでドキュメントにアクセス可能：

- Swagger UI: `http://localhost:8000/docs`
- ReDoc: `http://localhost:8000/redoc`

## パスパラメータとクエリパラメータ

### パスパラメータ

```python
@app.get("/users/{user_id}")
def get_user(user_id: int):
    return {"user_id": user_id}
```

### クエリパラメータ

```python
@app.get("/items")
def list_items(skip: int = 0, limit: int = 10):
    return {"skip": skip, "limit": limit}
```

### 複数のパラメータ

```python
@app.get("/users/{user_id}/items")
def get_user_items(user_id: int, skip: int = 0, limit: int = 10):
    return {
        "user_id": user_id,
        "skip": skip,
        "limit": limit
    }
```

## レスポンスの返却

### 辞書の返却

```python
@app.get("/data")
def get_data():
    return {"name": "FastAPI", "version": "0.100.0"}
```

### リストの返却

```python
@app.get("/items")
def get_items():
    return [
        {"id": 1, "name": "Item 1"},
        {"id": 2, "name": "Item 2"}
    ]
```

### ステータスコードの指定

```python
from fastapi import status

@app.post("/items", status_code=status.HTTP_201_CREATED)
def create_item(name: str):
    return {"name": name}
```

## アプリケーション設定

```python
app = FastAPI(
    title="My API",
    description="This is my FastAPI application",
    version="1.0.0",
    docs_url="/documentation",
    redoc_url="/redocumentation"
)
```

## 起動イベント

```python
@app.on_event("startup")
async def startup_event():
    print("アプリケーションが起動しました")

@app.on_event("shutdown")
async def shutdown_event():
    print("アプリケーションが終了します")
```

## 実践例

`examples/`ディレクトリに以下のサンプルがあります：
- 基本的なAPIアプリケーション
- パスパラメータとクエリパラメータの活用
- レスポンスモデルの定義

## 演習問題

`exercises/`ディレクトリに10問の演習問題があります。

## 次のステップ

FastAPIの基本を学んだら、[第3章: ルーティングとHTTPメソッド](../03-routing/README.md)に進みましょう。
