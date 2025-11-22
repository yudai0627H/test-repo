"""
問題3の模範解答: 辞書操作
"""


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
    return [
        product for product in products
        if min_price <= product["price"] <= max_price
    ]


# テストコード
if __name__ == "__main__":
    # テストデータ
    products = [
        {"name": "ノートPC", "price": 89800, "stock": 5},
        {"name": "マウス", "price": 1980, "stock": 50},
        {"name": "キーボード", "price": 8900, "stock": 30},
        {"name": "モニター", "price": 29800, "stock": 15},
        {"name": "USBケーブル", "price": 680, "stock": 100},
        {"name": "外付けHDD", "price": 12800, "stock": 20},
    ]

    # テストケース1: 1000円から30000円の商品
    result1 = filter_products(products, 1000, 30000)
    print("テスト1 (1000-30000円):")
    for p in result1:
        print(f"  - {p['name']}: ¥{p['price']:,}")
    assert len(result1) == 4
    assert any(p["name"] == "マウス" for p in result1)
    assert any(p["name"] == "モニター" for p in result1)
    assert not any(p["name"] == "ノートPC" for p in result1)  # 高すぎる
    assert not any(p["name"] == "USBケーブル" for p in result1)  # 安すぎる

    # テストケース2: 10000円以上
    result2 = filter_products(products, 10000, 100000)
    print("\nテスト2 (10000円以上):")
    for p in result2:
        print(f"  - {p['name']}: ¥{p['price']:,}")
    assert len(result2) == 3

    # テストケース3: 該当なし
    result3 = filter_products(products, 100000, 200000)
    print("\nテスト3 (100000-200000円):")
    print(f"  結果: {result3}")
    assert len(result3) == 0

    print("\n全てのテストが成功しました！")
