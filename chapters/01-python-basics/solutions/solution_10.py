"""
問題10の模範解答: 総合問題 - タスク管理システム
"""

from enum import Enum
from typing import List, Optional
from datetime import datetime


class Priority(Enum):
    """タスクの優先度"""
    LOW = 1
    MEDIUM = 2
    HIGH = 3


class Task:
    """
    タスククラス

    属性:
    - id: タスクID（自動採番）
    - title: タイトル
    - description: 説明
    - priority: 優先度
    - completed: 完了フラグ
    - created_at: 作成日時
    - completed_at: 完了日時
    """

    _id_counter = 0  # クラス変数でIDを管理

    def __init__(self, title: str, description: str = "", priority: Priority = Priority.MEDIUM):
        """
        タスクを初期化

        Args:
            title: タイトル
            description: 説明
            priority: 優先度
        """
        Task._id_counter += 1
        self.id = Task._id_counter
        self.title = title
        self.description = description
        self.priority = priority
        self.completed = False
        self.created_at = datetime.now()
        self.completed_at: Optional[datetime] = None

    def complete(self) -> None:
        """タスクを完了にする"""
        if not self.completed:
            self.completed = True
            self.completed_at = datetime.now()

    def uncomplete(self) -> None:
        """タスクを未完了に戻す"""
        self.completed = False
        self.completed_at = None

    def __str__(self) -> str:
        status = "✓" if self.completed else "□"
        priority_str = self.priority.name
        return f"[{status}] ({priority_str}) {self.title}"

    def __repr__(self) -> str:
        return f"Task(id={self.id}, title='{self.title}', priority={self.priority.name}, completed={self.completed})"


class TaskManager:
    """
    タスク管理クラス

    機能:
    - タスクの追加（add_task）
    - タスクの削除（remove_task）
    - タスクの完了（complete_task）
    - 未完了タスクの取得（get_pending_tasks）
    - 優先度別タスクの取得（get_tasks_by_priority）
    - タスクの検索（search_tasks）- タイトルまたは説明で検索
    """

    def __init__(self):
        """タスクマネージャーを初期化"""
        self.tasks: List[Task] = []

    def add_task(self, title: str, description: str = "", priority: Priority = Priority.MEDIUM) -> Task:
        """
        タスクを追加

        Args:
            title: タイトル
            description: 説明
            priority: 優先度

        Returns:
            作成されたタスク
        """
        task = Task(title, description, priority)
        self.tasks.append(task)
        print(f"タスクを追加しました: {task}")
        return task

    def remove_task(self, task_id: int) -> bool:
        """
        タスクを削除

        Args:
            task_id: タスクID

        Returns:
            削除成功の場合True
        """
        for task in self.tasks:
            if task.id == task_id:
                self.tasks.remove(task)
                print(f"タスクを削除しました: {task.title}")
                return True
        print(f"タスクID {task_id} が見つかりませんでした")
        return False

    def complete_task(self, task_id: int) -> bool:
        """
        タスクを完了にする

        Args:
            task_id: タスクID

        Returns:
            完了成功の場合True
        """
        task = self._find_task_by_id(task_id)
        if task:
            task.complete()
            print(f"タスクを完了しました: {task.title}")
            return True
        print(f"タスクID {task_id} が見つかりませんでした")
        return False

    def get_pending_tasks(self) -> List[Task]:
        """
        未完了タスクを取得

        Returns:
            未完了タスクのリスト
        """
        return [task for task in self.tasks if not task.completed]

    def get_completed_tasks(self) -> List[Task]:
        """
        完了済みタスクを取得

        Returns:
            完了済みタスクのリスト
        """
        return [task for task in self.tasks if task.completed]

    def get_tasks_by_priority(self, priority: Priority) -> List[Task]:
        """
        優先度別にタスクを取得

        Args:
            priority: 優先度

        Returns:
            指定された優先度のタスクリスト
        """
        return [task for task in self.tasks if task.priority == priority]

    def search_tasks(self, keyword: str) -> List[Task]:
        """
        タスクを検索（タイトルまたは説明で検索）

        Args:
            keyword: 検索キーワード

        Returns:
            検索結果のタスクリスト
        """
        keyword_lower = keyword.lower()
        return [
            task for task in self.tasks
            if keyword_lower in task.title.lower() or keyword_lower in task.description.lower()
        ]

    def list_tasks(self) -> None:
        """全タスクを表示"""
        if not self.tasks:
            print("タスクはありません")
            return

        print(f"\n=== タスク一覧（全{len(self.tasks)}件） ===")
        for task in self.tasks:
            print(f"  {task}")

    def _find_task_by_id(self, task_id: int) -> Optional[Task]:
        """
        IDでタスクを検索（内部メソッド）

        Args:
            task_id: タスクID

        Returns:
            タスクまたはNone
        """
        for task in self.tasks:
            if task.id == task_id:
                return task
        return None


# テストコード
if __name__ == "__main__":
    print("=== タスク管理システムのテスト ===\n")

    # タスクマネージャーの作成
    manager = TaskManager()

    # タスクの追加
    print("--- タスクの追加 ---")
    task1 = manager.add_task("FastAPI学習", "FastAPIの基本を学ぶ", Priority.HIGH)
    task2 = manager.add_task("データベース設計", "ER図を作成する", Priority.MEDIUM)
    task3 = manager.add_task("コードレビュー", "プルリクエストをレビュー", Priority.HIGH)
    task4 = manager.add_task("ドキュメント作成", "API仕様書を書く", Priority.LOW)
    task5 = manager.add_task("テスト作成", "ユニットテストを追加", Priority.MEDIUM)

    # タスク一覧表示
    manager.list_tasks()

    # タスクの完了
    print("\n--- タスクの完了 ---")
    manager.complete_task(task1.id)
    manager.complete_task(task3.id)

    # 未完了タスクの取得
    print("\n--- 未完了タスク ---")
    pending = manager.get_pending_tasks()
    print(f"未完了タスク数: {len(pending)}")
    for task in pending:
        print(f"  {task}")

    # 完了済みタスクの取得
    print("\n--- 完了済みタスク ---")
    completed = manager.get_completed_tasks()
    print(f"完了済みタスク数: {len(completed)}")
    for task in completed:
        print(f"  {task}")

    # 優先度別タスクの取得
    print("\n--- 優先度別タスク ---")
    high_priority = manager.get_tasks_by_priority(Priority.HIGH)
    print(f"HIGH優先度のタスク:")
    for task in high_priority:
        print(f"  {task}")

    # タスクの検索
    print("\n--- タスクの検索 ---")
    search_results = manager.search_tasks("テスト")
    print(f"「テスト」を含むタスク:")
    for task in search_results:
        print(f"  {task}")

    # タスクの削除
    print("\n--- タスクの削除 ---")
    manager.remove_task(task4.id)

    # 最終的なタスク一覧
    manager.list_tasks()

    # アサーション
    assert len(manager.get_pending_tasks()) == 2
    assert len(manager.get_completed_tasks()) == 2
    assert len(manager.tasks) == 4  # 1つ削除したので4つ

    print("\n全てのテストが成功しました！")
