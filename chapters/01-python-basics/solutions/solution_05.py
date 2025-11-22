"""
問題5の模範解答: クラスの基本実装
"""

from typing import List
from datetime import datetime


class InsufficientFundsError(Exception):
    """残高不足エラー"""
    pass


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

    def __init__(self, account_number: str, owner: str, initial_balance: float = 0):
        """
        銀行口座を初期化

        Args:
            account_number: 口座番号
            owner: 所有者名
            initial_balance: 初期残高
        """
        self.account_number = account_number
        self.owner = owner
        self._balance = initial_balance
        self.transaction_history: List[dict] = []

        if initial_balance > 0:
            self._add_transaction("初期入金", initial_balance)

    def deposit(self, amount: float) -> None:
        """
        入金する

        Args:
            amount: 入金額

        Raises:
            ValueError: 入金額が0以下の場合
        """
        if amount <= 0:
            raise ValueError("入金額は0より大きい必要があります")

        self._balance += amount
        self._add_transaction("入金", amount)
        print(f"¥{amount:,.0f} を入金しました。残高: ¥{self._balance:,.0f}")

    def withdraw(self, amount: float) -> None:
        """
        出金する

        Args:
            amount: 出金額

        Raises:
            ValueError: 出金額が0以下の場合
            InsufficientFundsError: 残高不足の場合
        """
        if amount <= 0:
            raise ValueError("出金額は0より大きい必要があります")

        if amount > self._balance:
            raise InsufficientFundsError(
                f"残高不足です。残高: ¥{self._balance:,.0f}, 出金額: ¥{amount:,.0f}"
            )

        self._balance -= amount
        self._add_transaction("出金", -amount)
        print(f"¥{amount:,.0f} を出金しました。残高: ¥{self._balance:,.0f}")

    def get_balance(self) -> float:
        """残高を取得"""
        return self._balance

    def _add_transaction(self, transaction_type: str, amount: float) -> None:
        """取引履歴に記録（内部メソッド）"""
        self.transaction_history.append({
            "type": transaction_type,
            "amount": amount,
            "balance": self._balance,
            "timestamp": datetime.now()
        })

    def print_transaction_history(self) -> None:
        """取引履歴を表示"""
        print(f"\n=== {self.owner}さんの取引履歴 ===")
        print(f"口座番号: {self.account_number}")
        for i, transaction in enumerate(self.transaction_history, 1):
            print(
                f"{i}. {transaction['timestamp'].strftime('%Y-%m-%d %H:%M:%S')} - "
                f"{transaction['type']}: ¥{abs(transaction['amount']):,.0f} "
                f"(残高: ¥{transaction['balance']:,.0f})"
            )

    def __str__(self) -> str:
        return f"BankAccount({self.account_number}, {self.owner}, balance=¥{self._balance:,.0f})"


# テストコード
if __name__ == "__main__":
    print("=== 銀行口座のテスト ===\n")

    # 口座作成
    account = BankAccount("123-456-789", "山田太郎", 10000)
    print(f"口座作成: {account}\n")

    # 入金テスト
    account.deposit(5000)
    assert account.get_balance() == 15000

    # 出金テスト
    account.withdraw(3000)
    assert account.get_balance() == 12000

    # 残高不足のテスト
    try:
        account.withdraw(20000)
        assert False, "InsufficientFundsError が発生すべき"
    except InsufficientFundsError as e:
        print(f"\n期待通りのエラー: {e}")

    # 不正な入金額のテスト
    try:
        account.deposit(-1000)
        assert False, "ValueError が発生すべき"
    except ValueError as e:
        print(f"期待通りのエラー: {e}")

    # さらに取引を追加
    account.deposit(8000)
    account.withdraw(5000)

    # 取引履歴の表示
    account.print_transaction_history()

    # 最終残高の確認
    print(f"\n最終残高: ¥{account.get_balance():,.0f}")
    assert account.get_balance() == 15000

    print("\n全てのテストが成功しました！")
