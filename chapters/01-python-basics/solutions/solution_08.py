"""
問題8の模範解答: コンテキストマネージャー
"""

from contextlib import contextmanager
import time


@contextmanager
def timer(name: str):
    """
    コードブロックの実行時間を計測するコンテキストマネージャー

    Args:
        name: 処理の名前

    使用例:
        with timer("処理A"):
            # 何らかの処理
            time.sleep(1)

    出力例: "処理A: 1.00秒"
    """
    start_time = time.time()
    try:
        yield
    finally:
        end_time = time.time()
        elapsed_time = end_time - start_time
        print(f"{name}: {elapsed_time:.2f}秒")


# 別の実装方法: クラスベースのコンテキストマネージャー
class Timer:
    """クラスベースのタイマーコンテキストマネージャー"""

    def __init__(self, name: str):
        self.name = name
        self.start_time = None
        self.elapsed_time = None

    def __enter__(self):
        self.start_time = time.time()
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        end_time = time.time()
        self.elapsed_time = end_time - self.start_time
        print(f"{self.name}: {self.elapsed_time:.2f}秒")
        return False  # 例外を再送出する

    def get_elapsed_time(self) -> float:
        """経過時間を取得"""
        return self.elapsed_time if self.elapsed_time is not None else 0.0


# テストコード
if __name__ == "__main__":
    print("=== タイマーコンテキストマネージャーのテスト ===\n")

    # テスト1: 基本的な使用
    print("テスト1: 関数ベースのコンテキストマネージャー")
    with timer("処理A"):
        time.sleep(0.5)
        total = sum(range(1000000))

    # テスト2: 複数の処理を計測
    print("\nテスト2: 複数の処理を計測")
    with timer("リスト作成"):
        data = [i ** 2 for i in range(100000)]

    with timer("データ処理"):
        result = sum(data)
        average = result / len(data)
        print(f"  平均値: {average:.2f}")

    # テスト3: ネストしたタイマー
    print("\nテスト3: ネストしたタイマー")
    with timer("全体の処理"):
        with timer("  サブ処理1"):
            time.sleep(0.2)

        with timer("  サブ処理2"):
            time.sleep(0.3)

    # テスト4: クラスベースのコンテキストマネージャー
    print("\nテスト4: クラスベースのコンテキストマネージャー")
    with Timer("クラスベース処理") as t:
        time.sleep(0.5)
        numbers = [x for x in range(500000) if x % 2 == 0]

    print(f"  実測時間: {t.get_elapsed_time():.2f}秒")

    # テスト5: 例外が発生した場合でも時間を計測
    print("\nテスト5: 例外発生時の計測")
    try:
        with timer("エラーが発生する処理"):
            time.sleep(0.3)
            raise ValueError("テスト用のエラー")
    except ValueError as e:
        print(f"  例外をキャッチ: {e}")

    print("\n全てのテストが成功しました！")
