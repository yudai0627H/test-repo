"""
問題7の模範解答: 例外処理
"""


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

    Args:
        age: 検証する年齢

    Raises:
        AgeValidationError: 年齢が無効な場合
    """
    if age < 0:
        raise AgeValidationError("年齢は0以上である必要があります")
    if age > 150:
        raise AgeValidationError("年齢が異常に大きいです")


def process_user_age(name: str, age: int) -> str:
    """
    ユーザーの年齢を処理する

    Args:
        name: ユーザー名
        age: 年齢

    Returns:
        処理結果メッセージ
    """
    try:
        validate_age(age)
        return f"{name}さん（{age}歳）の年齢は有効です"
    except AgeValidationError as e:
        return f"エラー: {e}"


# テストコード
if __name__ == "__main__":
    print("=== 年齢検証のテスト ===\n")

    # テスト1: 正常なケース
    print("テスト1: 正常なケース")
    try:
        validate_age(25)
        print("✓ 25歳は有効です")
    except AgeValidationError:
        assert False, "エラーが発生すべきではない"

    try:
        validate_age(0)
        print("✓ 0歳は有効です")
    except AgeValidationError:
        assert False, "エラーが発生すべきではない"

    try:
        validate_age(150)
        print("✓ 150歳は有効です")
    except AgeValidationError:
        assert False, "エラーが発生すべきではない"

    # テスト2: 負の年齢
    print("\nテスト2: 負の年齢")
    try:
        validate_age(-5)
        assert False, "AgeValidationError が発生すべき"
    except AgeValidationError as e:
        print(f"✓ 期待通りのエラー: {e}")
        assert str(e) == "年齢は0以上である必要があります"

    # テスト3: 異常に大きい年齢
    print("\nテスト3: 異常に大きい年齢")
    try:
        validate_age(200)
        assert False, "AgeValidationError が発生すべき"
    except AgeValidationError as e:
        print(f"✓ 期待通りのエラー: {e}")
        assert str(e) == "年齢が異常に大きいです"

    # テスト4: process_user_age 関数のテスト
    print("\n=== process_user_age のテスト ===")

    result1 = process_user_age("太郎", 30)
    print(result1)
    assert "有効です" in result1

    result2 = process_user_age("花子", -10)
    print(result2)
    assert "エラー" in result2
    assert "0以上" in result2

    result3 = process_user_age("次郎", 999)
    print(result3)
    assert "エラー" in result3
    assert "異常に大きい" in result3

    print("\n全てのテストが成功しました！")
