# 第1章 演習問題

## 問題1: 基本的なデータ型の操作

次の要件を満たす関数を作成してください：

```python
def process_user_data(name: str, age: int, hobbies: list[str]) -> dict:
    """
    ユーザーデータを処理して辞書を返す

    Args:
        name: ユーザー名
        age: 年齢
        hobbies: 趣味のリスト

    Returns:
        以下のキーを持つ辞書:
        - name: ユーザー名（大文字）
        - age: 年齢
        - is_adult: 成人かどうか（18歳以上）
        - hobby_count: 趣味の数
        - primary_hobby: 最初の趣味（存在しない場合は"なし"）
    """
    pass
```

## 問題2: リスト内包表記

1から100までの数値のうち、3または5で割り切れる数値のリストを返す関数を作成してください。

```python
def get_divisible_numbers() -> list[int]:
    """3または5で割り切れる数値のリストを返す"""
    pass
```

## 問題3: 辞書操作

商品リストから特定の条件を満たす商品をフィルタリングする関数を作成してください。

```python
def filter_products(products: list[dict], min_price: float, max_price: float) -> list[dict]:
    """
    価格範囲内の商品をフィルタリング

    Args:
        products: 商品リスト [{"name": str, "price": float, "stock": int}, ...]
        min_price: 最低価格
        max_price: 最高価格

    Returns:
        価格範囲内の商品リスト
    """
    pass
```

## 問題4: デコレータの実装

関数の実行回数をカウントするデコレータを実装してください。

```python
def count_calls(func):
    """関数の実行回数をカウントするデコレータ"""
    pass

@count_calls
def say_hello():
    print("Hello!")

# say_hello.call_count で実行回数を取得できるようにする
```

## 問題5: クラスの基本実装

銀行口座を表すクラスを実装してください。

```python
class BankAccount:
    """
    銀行口座クラス

    機能:
    - 口座番号、所有者名、残高を持つ
    - 入金（deposit）メソッド
    - 出金（withdraw）メソッド（残高不足の場合はエラー）
    - 残高照会（get_balance）メソッド
    - 取引履歴（transaction_history）を記録
    """
    pass
```

## 問題6: 継承とポリモーフィズム

図形の基底クラスとその派生クラスを実装してください。

```python
from abc import ABC, abstractmethod

class Shape(ABC):
    """図形の基底クラス"""

    @abstractmethod
    def area(self) -> float:
        """面積を計算"""
        pass

    @abstractmethod
    def perimeter(self) -> float:
        """周囲の長さを計算"""
        pass

class Rectangle(Shape):
    """長方形クラス"""
    pass

class Circle(Shape):
    """円クラス"""
    pass
```

## 問題7: 例外処理

カスタム例外を使用した年齢検証関数を実装してください。

```python
class AgeValidationError(Exception):
    """年齢検証エラー"""
    pass

def validate_age(age: int) -> None:
    """
    年齢を検証する

    条件:
    - 0歳未満の場合、"年齢は0以上である必要があります"
    - 150歳より大きい場合、"年齢が異常に大きいです"
    - 上記以外の場合は何もしない

    Raises:
        AgeValidationError: 年齢が無効な場合
    """
    pass
```

## 問題8: コンテキストマネージャー

タイマーのコンテキストマネージャーを実装してください。

```python
from contextlib import contextmanager
import time

@contextmanager
def timer(name: str):
    """
    コードブロックの実行時間を計測するコンテキストマネージャー

    使用例:
        with timer("処理A"):
            # 何らかの処理
            time.sleep(1)

    出力例: "処理A: 1.00秒"
    """
    pass
```

## 問題9: 型ヒントを使った関数

ユーザーデータを扱う関数群を型ヒント付きで実装してください。

```python
from typing import Optional, List, Dict, Any

def find_user_by_id(users: List[Dict[str, Any]], user_id: int) -> Optional[Dict[str, Any]]:
    """IDでユーザーを検索（見つからない場合はNone）"""
    pass

def get_active_users(users: List[Dict[str, Any]]) -> List[Dict[str, Any]]:
    """アクティブなユーザーのみを返す"""
    pass

def merge_user_data(user: Dict[str, Any], updates: Dict[str, Any]) -> Dict[str, Any]:
    """ユーザーデータを更新して新しい辞書を返す"""
    pass
```

## 問題10: 総合問題 - タスク管理システム

タスク管理システムを実装してください。

```python
from enum import Enum
from typing import List, Optional
from datetime import datetime

class Priority(Enum):
    """タスクの優先度"""
    LOW = 1
    MEDIUM = 2
    HIGH = 3

class Task:
    """
    タスククラス

    属性:
    - id: タスクID（自動採番）
    - title: タイトル
    - description: 説明
    - priority: 優先度
    - completed: 完了フラグ
    - created_at: 作成日時
    - completed_at: 完了日時
    """
    pass

class TaskManager:
    """
    タスク管理クラス

    機能:
    - タスクの追加（add_task）
    - タスクの削除（remove_task）
    - タスクの完了（complete_task）
    - 未完了タスクの取得（get_pending_tasks）
    - 優先度別タスクの取得（get_tasks_by_priority）
    - タスクの検索（search_tasks）- タイトルまたは説明で検索
    """
    pass
```

---

各問題に取り組んだら、`solutions/`ディレクトリで模範解答を確認してください。
