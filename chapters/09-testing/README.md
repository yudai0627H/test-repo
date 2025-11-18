# 第9章: テストコード

## 学習目標

- pytestの基礎
- TestClientの使用方法
- モックとフィクスチャ
- カバレッジの測定

## pytestのセットアップ

```bash
pip install pytest pytest-cov httpx
```

## TestClientの使用

```python
from fastapi.testclient import TestClient
from main import app

client = TestClient(app)

def test_read_root():
    response = client.get("/")
    assert response.status_code == 200
    assert response.json() == {"message": "Hello World"}
```

## フィクスチャの使用

```python
import pytest

@pytest.fixture
def test_db():
    # テスト用DBのセットアップ
    db = create_test_database()
    yield db
    # クリーンアップ
    db.close()

def test_create_user(test_db):
    response = client.post("/users", json={"name": "Test User"})
    assert response.status_code == 201
```

## データベースのモック

```python
from unittest.mock import Mock

def test_get_users():
    mock_db = Mock()
    mock_db.query().all.return_value = [
        {"id": 1, "name": "User1"},
        {"id": 2, "name": "User2"}
    ]
    # テスト実行
```

## カバレッジ測定

```bash
pytest --cov=app --cov-report=html
```
