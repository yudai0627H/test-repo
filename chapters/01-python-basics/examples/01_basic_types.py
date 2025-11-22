"""
Python基本データ型のサンプルコード
"""

from typing import List, Dict, Set, Tuple


def demonstrate_basic_types() -> None:
    """基本的なデータ型のデモンストレーション"""

    # 文字列
    name: str = "FastAPI Developer"
    print(f"名前: {name}")
    print(f"大文字: {name.upper()}")
    print(f"文字数: {len(name)}")

    # 数値
    age: int = 25
    price: float = 1999.99
    print(f"\n年齢: {age}")
    print(f"価格: ¥{price:,.2f}")

    # ブール値
    is_active: bool = True
    is_admin: bool = False
    print(f"\nアクティブ: {is_active}")
    print(f"管理者: {is_admin}")

    # リスト
    numbers: List[int] = [1, 2, 3, 4, 5]
    print(f"\n数値リスト: {numbers}")
    numbers.append(6)
    print(f"追加後: {numbers}")
    print(f"合計: {sum(numbers)}")

    # 辞書
    user: Dict[str, any] = {
        "id": 1,
        "name": "Alice",
        "email": "alice@example.com",
        "active": True
    }
    print(f"\nユーザー情報: {user}")
    print(f"名前: {user['name']}")
    print(f"メールアドレス: {user.get('email')}")

    # セット
    unique_tags: Set[str] = {"python", "fastapi", "web", "python"}
    print(f"\nタグ: {unique_tags}")  # 重複は削除される

    # タプル
    coordinates: Tuple[float, float] = (35.6762, 139.6503)
    lat, lon = coordinates
    print(f"\n緯度: {lat}, 経度: {lon}")


def demonstrate_collections() -> None:
    """コレクション操作のデモンストレーション"""

    # リスト内包表記
    squares = [x ** 2 for x in range(10)]
    print(f"平方数: {squares}")

    # 条件付きリスト内包表記
    even_numbers = [x for x in range(20) if x % 2 == 0]
    print(f"偶数: {even_numbers}")

    # 辞書内包表記
    word_lengths = {word: len(word) for word in ["python", "fastapi", "web"]}
    print(f"単語の長さ: {word_lengths}")

    # セット内包表記
    unique_lengths = {len(word) for word in ["python", "fastapi", "web", "api"]}
    print(f"ユニークな文字数: {unique_lengths}")


if __name__ == "__main__":
    print("=== 基本データ型のデモンストレーション ===")
    demonstrate_basic_types()

    print("\n=== コレクション操作のデモンストレーション ===")
    demonstrate_collections()
