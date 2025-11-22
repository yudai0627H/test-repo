# 第2章 演習問題 - FastAPI入門

## 問題1: Hello World API
シンプルな"Hello World" APIを作成してください。

```python
# main.py を作成し、以下の要件を満たすAPIを実装
# - GET / でHello Worldメッセージを返す
# - GET /health でシステムステータスを返す
```

## 問題2: パスパラメータの基本
ユーザーIDを受け取るエンドポイントを作成してください。

```python
# GET /users/{user_id} でユーザー情報を返す
# user_idは整数型で受け取る
```

## 問題3: クエリパラメータの基本
商品検索APIを作成してください。

```python
# GET /products でクエリパラメータを使って検索
# パラメータ: name (オプション), min_price (デフォルト0), max_price (デフォルト10000)
```

## 問題4: 複数のエンドポイント
ブログ記事APIを作成してください。

```python
# GET /posts - 全記事のリストを返す
# GET /posts/{post_id} - 特定の記事を返す
# GET /posts/{post_id}/comments - 記事のコメントを返す
```

## 問題5: レスポンスのカスタマイズ
HTTPステータスコードを使い分けるAPIを作成してください。

```python
# POST /items - 201 Createdを返す
# GET /items/{item_id} - 存在しない場合404を返す
# DELETE /items/{item_id} - 204 No Contentを返す
```

## 問題6: アプリケーション設定
カスタムメタデータを持つFastAPIアプリケーションを作成してください。

```python
# title, description, versionを設定
# カスタムドキュメントURLを設定
```

## 問題7: パスパラメータのバリデーション
パスパラメータに制約を加えてください。

```python
# GET /items/{item_id}
# item_idは1以上100以下の整数のみ受け付ける
```

## 問題8: 列挙型を使ったパラメータ
選択肢が決まっているパラメータを実装してください。

```python
# GET /models/{model_name}
# model_nameは "alexnet", "resnet", "lenet" のいずれか
```

## 問題9: 複雑なクエリパラメータ
ページネーションとソート機能を持つAPIを作成してください。

```python
# GET /users
# パラメータ: page (デフォルト1), per_page (デフォルト10), sort_by (デフォルト"id")
```

## 問題10: ライフサイクルイベント
起動時と終了時にメッセージを表示するAPIを作成してください。

```python
# startup イベントで初期化処理
# shutdown イベントでクリーンアップ処理
```

---

模範解答は `solutions/` ディレクトリにあります。
