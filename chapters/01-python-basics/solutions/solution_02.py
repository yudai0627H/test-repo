"""
問題2の模範解答: リスト内包表記
"""


def get_divisible_numbers() -> list[int]:
    """3または5で割り切れる数値のリストを返す"""
    return [x for x in range(1, 101) if x % 3 == 0 or x % 5 == 0]


# テストコード
if __name__ == "__main__":
    result = get_divisible_numbers()
    print(f"3または5で割り切れる数値（1-100）: {result}")
    print(f"総数: {len(result)}")

    # 検証
    assert 3 in result
    assert 5 in result
    assert 15 in result  # 3と5の両方で割り切れる
    assert 100 in result  # 5で割り切れる
    assert 99 in result  # 3で割り切れる

    assert 1 not in result
    assert 2 not in result
    assert 7 not in result

    # 先頭の数値を確認
    print(f"最初の10個: {result[:10]}")
    assert result[:10] == [3, 5, 6, 9, 10, 12, 15, 18, 20, 21]

    print("\n全てのテストが成功しました！")
