# 第1章: Python基礎復習

## 学習目標

- Python基本文法の確認と復習
- オブジェクト指向プログラミングの理解
- 型ヒントの活用方法
- モダンなPythonコーディング規約

## 内容

### 1.1 Python基本文法

#### データ型と変数
```python
# 基本的なデータ型
name: str = "FastAPI"
age: int = 5
price: float = 99.99
is_active: bool = True

# コレクション型
numbers: list[int] = [1, 2, 3, 4, 5]
user: dict[str, str] = {"name": "Alice", "email": "alice@example.com"}
unique_ids: set[int] = {1, 2, 3}
coordinates: tuple[float, float] = (35.6762, 139.6503)
```

#### 制御構文
```python
# if文
if age >= 18:
    print("成人です")
elif age >= 13:
    print("未成年です")
else:
    print("子供です")

# for文
for num in numbers:
    print(num)

# リスト内包表記
squares = [x ** 2 for x in range(10)]
even_numbers = [x for x in range(20) if x % 2 == 0]
```

### 1.2 関数とデコレータ

#### 関数の定義
```python
def greet(name: str) -> str:
    """挨拶メッセージを返す関数"""
    return f"Hello, {name}!"

# デフォルト引数
def create_user(name: str, age: int = 18, active: bool = True) -> dict:
    return {"name": name, "age": age, "active": active}

# 可変長引数
def sum_all(*args: int) -> int:
    return sum(args)

def create_profile(**kwargs: str) -> dict:
    return kwargs
```

#### デコレータ
```python
from functools import wraps
import time

def timer(func):
    """関数の実行時間を計測するデコレータ"""
    @wraps(func)
    def wrapper(*args, **kwargs):
        start = time.time()
        result = func(*args, **kwargs)
        end = time.time()
        print(f"{func.__name__} took {end - start:.2f} seconds")
        return result
    return wrapper

@timer
def slow_function():
    time.sleep(1)
    return "Done"
```

### 1.3 オブジェクト指向プログラミング

#### クラスの定義
```python
class User:
    """ユーザークラス"""

    def __init__(self, name: str, email: str):
        self.name = name
        self.email = email
        self._password: str = ""  # プライベート属性

    def set_password(self, password: str) -> None:
        """パスワードを設定"""
        self._password = password

    def check_password(self, password: str) -> bool:
        """パスワードを検証"""
        return self._password == password

    def __str__(self) -> str:
        return f"User({self.name}, {self.email})"
```

#### 継承
```python
class AdminUser(User):
    """管理者ユーザークラス"""

    def __init__(self, name: str, email: str, role: str = "admin"):
        super().__init__(name, email)
        self.role = role

    def delete_user(self, user_id: int) -> bool:
        """ユーザーを削除する管理者専用メソッド"""
        print(f"Deleting user {user_id}")
        return True
```

### 1.4 型ヒント

#### 基本的な型ヒント
```python
from typing import Optional, Union, List, Dict, Any

def get_user(user_id: int) -> Optional[dict]:
    """ユーザーを取得（存在しない場合はNone）"""
    if user_id > 0:
        return {"id": user_id, "name": "Alice"}
    return None

def process_data(data: Union[str, int]) -> str:
    """文字列または整数を処理"""
    return str(data)

def filter_users(users: List[Dict[str, Any]], active_only: bool = True) -> List[Dict[str, Any]]:
    """ユーザーリストをフィルタリング"""
    if active_only:
        return [u for u in users if u.get("active", False)]
    return users
```

### 1.5 例外処理

```python
class InvalidAgeError(Exception):
    """年齢が無効な場合のカスタム例外"""
    pass

def validate_age(age: int) -> None:
    if age < 0:
        raise InvalidAgeError("年齢は0以上である必要があります")
    if age > 150:
        raise InvalidAgeError("年齢が異常に大きいです")

try:
    validate_age(-5)
except InvalidAgeError as e:
    print(f"エラー: {e}")
finally:
    print("処理完了")
```

### 1.6 コンテキストマネージャー

```python
from contextlib import contextmanager

@contextmanager
def open_file(filename: str):
    """ファイルを開くコンテキストマネージャー"""
    f = open(filename, 'r')
    try:
        yield f
    finally:
        f.close()

# 使用例
with open_file('data.txt') as f:
    content = f.read()
```

## サンプルコード

`examples/`ディレクトリに実践的なサンプルコードがあります。

## 演習問題

`exercises/`ディレクトリに10問の演習問題があります。各問題に取り組んで、`solutions/`ディレクトリで解答を確認してください。

## 次のステップ

Python基礎を復習したら、[第2章: FastAPI入門](../02-fastapi-intro/README.md)に進みましょう。
