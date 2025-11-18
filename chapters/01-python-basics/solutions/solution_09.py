"""
問題9の模範解答: 型ヒントを使った関数
"""

from typing import Optional, List, Dict, Any


def find_user_by_id(users: List[Dict[str, Any]], user_id: int) -> Optional[Dict[str, Any]]:
    """
    IDでユーザーを検索（見つからない場合はNone）

    Args:
        users: ユーザーリスト
        user_id: 検索するユーザーID

    Returns:
        ユーザー辞書またはNone
    """
    for user in users:
        if user.get("id") == user_id:
            return user
    return None


def get_active_users(users: List[Dict[str, Any]]) -> List[Dict[str, Any]]:
    """
    アクティブなユーザーのみを返す

    Args:
        users: ユーザーリスト

    Returns:
        アクティブなユーザーのリスト
    """
    return [user for user in users if user.get("active", False)]


def merge_user_data(user: Dict[str, Any], updates: Dict[str, Any]) -> Dict[str, Any]:
    """
    ユーザーデータを更新して新しい辞書を返す（元のデータは変更しない）

    Args:
        user: 元のユーザーデータ
        updates: 更新データ

    Returns:
        マージされた新しいユーザーデータ
    """
    # 元のデータをコピーして更新
    merged = user.copy()
    merged.update(updates)
    return merged


def filter_users_by_age(
    users: List[Dict[str, Any]],
    min_age: Optional[int] = None,
    max_age: Optional[int] = None
) -> List[Dict[str, Any]]:
    """
    年齢範囲でユーザーをフィルタリング

    Args:
        users: ユーザーリスト
        min_age: 最小年齢（指定しない場合は制限なし）
        max_age: 最大年齢（指定しない場合は制限なし）

    Returns:
        フィルタリングされたユーザーリスト
    """
    result = users.copy()

    if min_age is not None:
        result = [u for u in result if u.get("age", 0) >= min_age]

    if max_age is not None:
        result = [u for u in result if u.get("age", 0) <= max_age]

    return result


def get_user_names(users: List[Dict[str, Any]]) -> List[str]:
    """
    ユーザー名のリストを取得

    Args:
        users: ユーザーリスト

    Returns:
        ユーザー名のリスト
    """
    return [user.get("name", "Unknown") for user in users]


# テストコード
if __name__ == "__main__":
    # テストデータ
    users: List[Dict[str, Any]] = [
        {"id": 1, "name": "太郎", "age": 25, "active": True},
        {"id": 2, "name": "花子", "age": 30, "active": True},
        {"id": 3, "name": "次郎", "age": 20, "active": False},
        {"id": 4, "name": "美咲", "age": 35, "active": True},
        {"id": 5, "name": "健太", "age": 28, "active": False},
    ]

    print("=== 型ヒント付き関数のテスト ===\n")

    # テスト1: find_user_by_id
    print("テスト1: find_user_by_id")
    user = find_user_by_id(users, 2)
    print(f"ID=2のユーザー: {user}")
    assert user is not None
    assert user["name"] == "花子"

    not_found = find_user_by_id(users, 999)
    print(f"ID=999のユーザー: {not_found}")
    assert not_found is None

    # テスト2: get_active_users
    print("\nテスト2: get_active_users")
    active_users = get_active_users(users)
    print(f"アクティブユーザー数: {len(active_users)}")
    for u in active_users:
        print(f"  - {u['name']}")
    assert len(active_users) == 3
    assert all(u["active"] for u in active_users)

    # テスト3: merge_user_data
    print("\nテスト3: merge_user_data")
    original_user = {"id": 1, "name": "太郎", "age": 25}
    updates = {"age": 26, "email": "taro@example.com"}
    merged = merge_user_data(original_user, updates)
    print(f"元データ: {original_user}")
    print(f"更新データ: {updates}")
    print(f"マージ結果: {merged}")
    assert merged["age"] == 26
    assert merged["email"] == "taro@example.com"
    assert original_user["age"] == 25  # 元のデータは変更されていない

    # テスト4: filter_users_by_age
    print("\nテスト4: filter_users_by_age")
    filtered1 = filter_users_by_age(users, min_age=25, max_age=30)
    print(f"25-30歳のユーザー:")
    for u in filtered1:
        print(f"  - {u['name']}: {u['age']}歳")
    assert len(filtered1) == 3

    filtered2 = filter_users_by_age(users, min_age=30)
    print(f"\n30歳以上のユーザー:")
    for u in filtered2:
        print(f"  - {u['name']}: {u['age']}歳")
    assert len(filtered2) == 2

    # テスト5: get_user_names
    print("\nテスト5: get_user_names")
    names = get_user_names(users)
    print(f"全ユーザー名: {names}")
    assert len(names) == 5
    assert "太郎" in names
    assert "花子" in names

    print("\n全てのテストが成功しました！")
