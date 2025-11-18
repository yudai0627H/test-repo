"""
オブジェクト指向プログラミングのサンプルコード
"""

from typing import List, Optional
from datetime import datetime


class User:
    """ユーザークラスの基本実装"""

    # クラス変数
    total_users: int = 0

    def __init__(self, name: str, email: str, age: int):
        self.name = name
        self.email = email
        self.age = age
        self._created_at = datetime.now()
        User.total_users += 1

    @property
    def created_at(self) -> datetime:
        """作成日時を取得"""
        return self._created_at

    def greet(self) -> str:
        """挨拶メッセージを返す"""
        return f"こんにちは、{self.name}さん！"

    def is_adult(self) -> bool:
        """成人かどうかを判定"""
        return self.age >= 18

    def __str__(self) -> str:
        """文字列表現"""
        return f"User(name={self.name}, email={self.email})"

    def __repr__(self) -> str:
        """デバッグ用の文字列表現"""
        return f"User(name='{self.name}', email='{self.email}', age={self.age})"

    @classmethod
    def get_total_users(cls) -> int:
        """総ユーザー数を取得"""
        return cls.total_users

    @staticmethod
    def validate_email(email: str) -> bool:
        """メールアドレスの簡易バリデーション"""
        return "@" in email and "." in email


class PremiumUser(User):
    """プレミアムユーザークラス（継承の例）"""

    def __init__(self, name: str, email: str, age: int, subscription_type: str = "monthly"):
        super().__init__(name, email, age)
        self.subscription_type = subscription_type
        self.features: List[str] = ["ad-free", "priority-support"]

    def greet(self) -> str:
        """オーバーライド: プレミアムユーザー向けの挨拶"""
        return f"こんにちは、{self.name}さん！プレミアム会員としてようこそ！"

    def add_feature(self, feature: str) -> None:
        """新しい機能を追加"""
        if feature not in self.features:
            self.features.append(feature)

    def __str__(self) -> str:
        return f"PremiumUser(name={self.name}, subscription={self.subscription_type})"


class AdminUser(User):
    """管理者ユーザークラス"""

    def __init__(self, name: str, email: str, age: int, permissions: Optional[List[str]] = None):
        super().__init__(name, email, age)
        self.permissions = permissions or ["read", "write"]

    def has_permission(self, permission: str) -> bool:
        """権限を持っているか確認"""
        return permission in self.permissions

    def grant_permission(self, permission: str) -> None:
        """権限を付与"""
        if permission not in self.permissions:
            self.permissions.append(permission)
            print(f"権限 '{permission}' を付与しました")

    def revoke_permission(self, permission: str) -> None:
        """権限を削除"""
        if permission in self.permissions:
            self.permissions.remove(permission)
            print(f"権限 '{permission}' を削除しました")


class Team:
    """チームクラス（集約の例）"""

    def __init__(self, name: str):
        self.name = name
        self.members: List[User] = []

    def add_member(self, user: User) -> None:
        """メンバーを追加"""
        self.members.append(user)
        print(f"{user.name}をチーム '{self.name}' に追加しました")

    def remove_member(self, user: User) -> None:
        """メンバーを削除"""
        if user in self.members:
            self.members.remove(user)
            print(f"{user.name}をチーム '{self.name}' から削除しました")

    def get_member_count(self) -> int:
        """メンバー数を取得"""
        return len(self.members)

    def list_members(self) -> None:
        """メンバー一覧を表示"""
        print(f"\nチーム '{self.name}' のメンバー:")
        for i, member in enumerate(self.members, 1):
            print(f"  {i}. {member.name} ({type(member).__name__})")


def main():
    """メイン関数"""

    # 通常ユーザーの作成
    user1 = User("太郎", "taro@example.com", 25)
    user2 = User("花子", "hanako@example.com", 30)

    print(user1.greet())
    print(f"{user1.name}は成人ですか？ {user1.is_adult()}")

    # プレミアムユーザーの作成
    premium_user = PremiumUser("次郎", "jiro@example.com", 28, "yearly")
    print(premium_user.greet())
    print(f"機能: {premium_user.features}")
    premium_user.add_feature("offline-mode")
    print(f"追加後の機能: {premium_user.features}")

    # 管理者ユーザーの作成
    admin = AdminUser("管理者", "admin@example.com", 35, ["read", "write", "delete"])
    print(f"\n{admin.name}の権限: {admin.permissions}")
    print(f"削除権限がありますか？ {admin.has_permission('delete')}")
    admin.grant_permission("manage_users")

    # チームの作成
    team = Team("開発チーム")
    team.add_member(user1)
    team.add_member(user2)
    team.add_member(premium_user)
    team.add_member(admin)
    team.list_members()

    # クラスメソッドとスタティックメソッドの使用
    print(f"\n総ユーザー数: {User.get_total_users()}")
    print(f"メールアドレスのバリデーション: {User.validate_email('test@example.com')}")


if __name__ == "__main__":
    main()
