"""
問題6の模範解答: 継承とポリモーフィズム
"""

from abc import ABC, abstractmethod
import math


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

    def describe(self) -> str:
        """図形の説明を返す"""
        return f"{self.__class__.__name__}: 面積={self.area():.2f}, 周囲={self.perimeter():.2f}"


class Rectangle(Shape):
    """長方形クラス"""

    def __init__(self, width: float, height: float):
        """
        長方形を初期化

        Args:
            width: 幅
            height: 高さ
        """
        self.width = width
        self.height = height

    def area(self) -> float:
        """面積を計算"""
        return self.width * self.height

    def perimeter(self) -> float:
        """周囲の長さを計算"""
        return 2 * (self.width + self.height)

    def __str__(self) -> str:
        return f"Rectangle(width={self.width}, height={self.height})"


class Circle(Shape):
    """円クラス"""

    def __init__(self, radius: float):
        """
        円を初期化

        Args:
            radius: 半径
        """
        self.radius = radius

    def area(self) -> float:
        """面積を計算"""
        return math.pi * self.radius ** 2

    def perimeter(self) -> float:
        """周囲の長さ（円周）を計算"""
        return 2 * math.pi * self.radius

    def __str__(self) -> str:
        return f"Circle(radius={self.radius})"


class Triangle(Shape):
    """三角形クラス（追加実装）"""

    def __init__(self, base: float, height: float, side1: float, side2: float):
        """
        三角形を初期化

        Args:
            base: 底辺
            height: 高さ
            side1: 辺1の長さ
            side2: 辺2の長さ
        """
        self.base = base
        self.height = height
        self.side1 = side1
        self.side2 = side2

    def area(self) -> float:
        """面積を計算"""
        return 0.5 * self.base * self.height

    def perimeter(self) -> float:
        """周囲の長さを計算"""
        return self.base + self.side1 + self.side2

    def __str__(self) -> str:
        return f"Triangle(base={self.base}, height={self.height})"


def calculate_total_area(shapes: list[Shape]) -> float:
    """
    複数の図形の合計面積を計算（ポリモーフィズムの例）

    Args:
        shapes: 図形のリスト

    Returns:
        合計面積
    """
    return sum(shape.area() for shape in shapes)


# テストコード
if __name__ == "__main__":
    print("=== 図形クラスのテスト ===\n")

    # 長方形
    rectangle = Rectangle(width=5, height=3)
    print(rectangle)
    print(f"面積: {rectangle.area()}")
    print(f"周囲: {rectangle.perimeter()}")
    print(rectangle.describe())
    assert rectangle.area() == 15
    assert rectangle.perimeter() == 16

    # 円
    print()
    circle = Circle(radius=5)
    print(circle)
    print(f"面積: {circle.area():.2f}")
    print(f"周囲: {circle.perimeter():.2f}")
    print(circle.describe())
    assert abs(circle.area() - 78.54) < 0.01
    assert abs(circle.perimeter() - 31.42) < 0.01

    # 三角形
    print()
    triangle = Triangle(base=4, height=3, side1=3, side2=5)
    print(triangle)
    print(f"面積: {triangle.area()}")
    print(f"周囲: {triangle.perimeter()}")
    print(triangle.describe())
    assert triangle.area() == 6
    assert triangle.perimeter() == 12

    # ポリモーフィズム: 異なる図形をリストで扱う
    print("\n=== ポリモーフィズムのテスト ===")
    shapes = [rectangle, circle, triangle]

    print("全ての図形:")
    for shape in shapes:
        print(f"  - {shape.describe()}")

    total_area = calculate_total_area(shapes)
    print(f"\n合計面積: {total_area:.2f}")
    assert abs(total_area - 99.54) < 0.01

    print("\n全てのテストが成功しました！")
