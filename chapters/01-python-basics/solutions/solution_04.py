"""
問題4の模範解答: デコレータの実装
"""

from functools import wraps


def count_calls(func):
    """関数の実行回数をカウントするデコレータ"""

    @wraps(func)
    def wrapper(*args, **kwargs):
        wrapper.call_count += 1
        return func(*args, **kwargs)

    wrapper.call_count = 0
    return wrapper


# テストコード
if __name__ == "__main__":

    @count_calls
    def say_hello():
        print("Hello!")

    @count_calls
    def greet(name: str) -> str:
        return f"こんにちは、{name}さん！"

    # テスト1: 実行回数のカウント
    print("=== テスト1: say_hello ===")
    assert say_hello.call_count == 0

    say_hello()
    assert say_hello.call_count == 1

    say_hello()
    say_hello()
    assert say_hello.call_count == 3
    print(f"say_hello の実行回数: {say_hello.call_count}")

    # テスト2: 引数を持つ関数
    print("\n=== テスト2: greet ===")
    assert greet.call_count == 0

    result1 = greet("太郎")
    print(result1)
    assert result1 == "こんにちは、太郎さん！"
    assert greet.call_count == 1

    result2 = greet("花子")
    print(result2)
    assert greet.call_count == 2
    print(f"greet の実行回数: {greet.call_count}")

    # テスト3: 複数の関数で独立してカウント
    print("\n=== テスト3: 独立したカウント ===")
    print(f"say_hello: {say_hello.call_count}回")
    print(f"greet: {greet.call_count}回")
    assert say_hello.call_count == 3
    assert greet.call_count == 2

    print("\n全てのテストが成功しました！")
