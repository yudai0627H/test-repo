"""
問題1の模範解答: 基本的なデータ型の操作
"""


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
    return {
        "name": name.upper(),
        "age": age,
        "is_adult": age >= 18,
        "hobby_count": len(hobbies),
        "primary_hobby": hobbies[0] if hobbies else "なし"
    }


# テストコード
if __name__ == "__main__":
    # テストケース1: 通常のケース
    result1 = process_user_data("太郎", 25, ["読書", "ゲーム", "料理"])
    print("テスト1:", result1)
    assert result1 == {
        "name": "太郎",
        "age": 25,
        "is_adult": True,
        "hobby_count": 3,
        "primary_hobby": "読書"
    }

    # テストケース2: 未成年
    result2 = process_user_data("花子", 15, ["音楽"])
    print("テスト2:", result2)
    assert result2 == {
        "name": "花子",
        "age": 15,
        "is_adult": False,
        "hobby_count": 1,
        "primary_hobby": "音楽"
    }

    # テストケース3: 趣味なし
    result3 = process_user_data("次郎", 20, [])
    print("テスト3:", result3)
    assert result3 == {
        "name": "次郎",
        "age": 20,
        "is_adult": True,
        "hobby_count": 0,
        "primary_hobby": "なし"
    }

    print("\n全てのテストが成功しました！")
