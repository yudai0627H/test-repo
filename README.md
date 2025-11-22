# FastAPI 完全マスターコース

## 概要

このコースは、Pythonとバックエンド開発の経験が浅いジュニアエンジニアが、シニアエンジニアレベルのスキルを身につけることを目標としています。FastAPIフレームワークを中心に、モダンなWebアプリケーション開発の実践的なスキルを習得できます。

## 🎯 学習目標

- FastAPIを使った本格的なRESTful APIの開発
- 認証・認可の実装（JWT、OAuth2）
- データベース設計と連携（SQLAlchemy）
- テスト駆動開発（TDD）の実践
- 非同期プログラミングの理解と活用
- 本番環境を想定したセキュリティとパフォーマンス最適化

## 📚 コース構成

全11章、100問以上の演習問題で構成されています。

### 初級編

1. **[Python基礎復習](chapters/01-python-basics/README.md)** (演習10問)
   - Python基本文法の復習
   - オブジェクト指向プログラミング
   - 型ヒントとデータ構造

2. **[FastAPI入門](chapters/02-fastapi-intro/README.md)** (演習10問)
   - FastAPIの基本概念
   - 最初のAPIアプリケーション作成
   - ドキュメント自動生成

3. **[ルーティングとHTTPメソッド](chapters/03-routing/README.md)** (演習10問)
   - パスパラメータとクエリパラメータ
   - GET、POST、PUT、DELETE
   - ルーターの分割と管理

4. **[リクエストとレスポンス](chapters/04-request-response/README.md)** (演習10問)
   - リクエストボディの処理
   - レスポンスモデルの定義
   - ステータスコードとヘッダー

### 中級編

5. **[Pydanticとバリデーション](chapters/05-pydantic/README.md)** (演習10問)
   - Pydanticモデルの詳細
   - カスタムバリデーター
   - データのシリアライズ/デシリアライズ

6. **[データベース連携](chapters/06-database/README.md)** (演習10問)
   - SQLAlchemyの基礎
   - モデル定義とマイグレーション
   - CRUD操作の実装

7. **[依存性注入](chapters/07-dependency-injection/README.md)** (演習10問)
   - Depends()の活用
   - データベースセッション管理
   - カスタム依存関係の作成

### 上級編

8. **[認証認可](chapters/08-auth/README.md)** (演習15問)
   - JWTトークンの生成と検証
   - OAuth2フロー
   - ロールベースアクセス制御（RBAC）
   - パスワードのハッシュ化

9. **[テストコード](chapters/09-testing/README.md)** (演習10問)
   - pytestの基礎
   - テストクライアントの使用
   - モックとフィクスチャ
   - カバレッジの確認

10. **[非同期処理とバックグラウンドタスク](chapters/10-async/README.md)** (演習10問)
    - async/awaitの理解
    - 非同期データベース操作
    - バックグラウンドタスク
    - 並行処理とパフォーマンス

11. **[上級トピック](chapters/11-advanced/README.md)** (演習15問)
    - WebSocket通信
    - ミドルウェアの実装
    - CORS設定
    - ロギングとモニタリング
    - Dockerコンテナ化
    - 本番環境へのデプロイ

## 🚀 始め方

### 環境セットアップ

```bash
# リポジトリをクローン
git clone <repository-url>
cd test-repo

# 仮想環境を作成
python -m venv venv
source venv/bin/activate  # Windowsの場合: venv\Scripts\activate

# 依存パッケージをインストール
pip install -r requirements.txt
```

### 学習の進め方

1. 各章のREADMEを読んで概念を理解する
2. `examples/`ディレクトリのサンプルコードを実行して動作を確認
3. `exercises/`ディレクトリの演習問題に取り組む
4. 自力で解答を作成し、`solutions/`ディレクトリの模範解答と比較
5. 理解が深まったら次の章へ進む

## 📝 演習問題について

- **演習問題数**: 全120問
- **難易度**: 各章ごとに基礎→応用→実践の順で段階的に難易度が上がります
- **模範解答**: すべての問題に詳細な解説付きの模範解答があります
- **推奨時間**: 各章を完了するのに2〜4時間程度を想定

## 🎓 習得できるスキル

このコースを完了すると、以下のスキルが身につきます：

✅ FastAPIを使った高品質なAPIの設計と実装
✅ セキュアな認証認可システムの構築
✅ データベース設計とORMの効率的な使用
✅ テスト駆動開発による保守性の高いコード作成
✅ 非同期処理による高パフォーマンスアプリケーション開発
✅ 本番環境を想定したデプロイとモニタリング
✅ チーム開発で必要なベストプラクティス

## 📖 推奨リソース

- [FastAPI公式ドキュメント](https://fastapi.tiangolo.com/)
- [Pydantic公式ドキュメント](https://docs.pydantic.dev/)
- [SQLAlchemy公式ドキュメント](https://docs.sqlalchemy.org/)
- [pytest公式ドキュメント](https://docs.pytest.org/)

## 🤝 サポート

問題や質問があれば、Issueを作成してください。

## ライセンス

このコースはMITライセンスの下で公開されています。

---

**それでは、FastAPIマスターへの旅を始めましょう！** 🚀
