"""
FastAPI Hello World アプリケーション

最もシンプルなFastAPIアプリケーションの例
"""

from fastapi import FastAPI
from typing import Optional

app = FastAPI(
    title="Hello World API",
    description="FastAPI学習用の最初のアプリケーション",
    version="1.0.0"
)


@app.get("/")
def read_root():
    """
    ルートエンドポイント

    Returns:
        dict: 挨拶メッセージ
    """
    return {"message": "Hello World", "framework": "FastAPI"}


@app.get("/hello/{name}")
def say_hello(name: str):
    """
    名前を指定して挨拶

    Args:
        name: 挨拶する相手の名前

    Returns:
        dict: パーソナライズされた挨拶メッセージ
    """
    return {"message": f"Hello, {name}!"}


@app.get("/items/{item_id}")
def read_item(item_id: int, q: Optional[str] = None):
    """
    アイテムを取得

    Args:
        item_id: アイテムID
        q: オプションのクエリパラメータ

    Returns:
        dict: アイテム情報
    """
    result = {"item_id": item_id}
    if q:
        result["query"] = q
    return result


@app.get("/users")
def list_users(skip: int = 0, limit: int = 10):
    """
    ユーザーリストを取得

    Args:
        skip: スキップするアイテム数
        limit: 取得するアイテムの最大数

    Returns:
        dict: ページネーション情報とユーザーリスト
    """
    # ダミーデータ
    users = [
        {"id": i, "name": f"User{i}", "email": f"user{i}@example.com"}
        for i in range(1, 21)
    ]

    # ページネーション
    paginated_users = users[skip: skip + limit]

    return {
        "skip": skip,
        "limit": limit,
        "total": len(users),
        "users": paginated_users
    }


# 実行方法:
# uvicorn 01_hello_world:app --reload
#
# アクセス:
# http://localhost:8000/
# http://localhost:8000/hello/FastAPI
# http://localhost:8000/items/42?q=test
# http://localhost:8000/users?skip=5&limit=5
#
# ドキュメント:
# http://localhost:8000/docs
# http://localhost:8000/redoc
