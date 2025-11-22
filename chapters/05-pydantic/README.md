# 第5章: Pydanticとバリデーション

## 学習目標

- Pydanticモデルの詳細な使い方
- カスタムバリデーターの実装
- フィールドの制約と設定
- データのシリアライズとデシリアライズ

## 重要: Pydantic v2 について

このコースでは **Pydantic v2** を使用します。v1からの主な変更点：
- `@validator` → `@field_validator`
- `orm_mode` → `from_attributes`
- `Config` クラス → `model_config`

## Pydanticモデルの基本

```python
from pydantic import BaseModel, Field, EmailStr, ConfigDict
from typing import Optional

class User(BaseModel):
    """ユーザーモデル"""
    model_config = ConfigDict(str_strip_whitespace=True)

    id: int
    name: str = Field(..., min_length=1, max_length=50)
    email: EmailStr
    age: Optional[int] = Field(default=None, ge=0, le=150)
    is_active: bool = True
```

## カスタムバリデーター（Pydantic v2）

```python
from pydantic import BaseModel, field_validator, model_validator

class User(BaseModel):
    name: str
    email: str
    password: str

    @field_validator('email')
    @classmethod
    def validate_email(cls, v: str) -> str:
        """メールアドレスを検証"""
        if '@' not in v:
            raise ValueError('有効なメールアドレスではありません')
        return v.lower()  # 小文字に正規化

    @field_validator('password')
    @classmethod
    def validate_password(cls, v: str) -> str:
        """パスワードの強度を検証"""
        if len(v) < 8:
            raise ValueError('パスワードは8文字以上必要です')
        if not any(c.isupper() for c in v):
            raise ValueError('パスワードには大文字を含める必要があります')
        if not any(c.isdigit() for c in v):
            raise ValueError('パスワードには数字を含める必要があります')
        return v

    @model_validator(mode='after')
    def validate_model(self) -> 'User':
        """モデル全体のバリデーション"""
        # 例: nameがemailに含まれていないことを確認
        if self.name.lower() in self.email.lower():
            raise ValueError('メールアドレスに名前を含めないでください')
        return self
```

## フィールド制約

```python
from pydantic import BaseModel, Field
from typing import Annotated

class Product(BaseModel):
    name: str = Field(..., min_length=3, max_length=100)
    price: float = Field(..., gt=0, le=1000000, description="価格（0より大きく100万以下）")
    quantity: int = Field(default=0, ge=0)

    # Annotatedを使った制約（推奨される新しい書き方）
    sku: Annotated[str, Field(pattern=r'^[A-Z]{3}-\d{4}$')] = Field(
        ...,
        description="商品コード（例: ABC-1234）"
    )
```

## ORMモデルとの連携（Pydantic v2）

```python
from pydantic import BaseModel, ConfigDict

class UserBase(BaseModel):
    name: str
    email: str

class UserCreate(UserBase):
    password: str

class UserResponse(UserBase):
    id: int
    is_active: bool

    # Pydantic v2でのORM設定
    model_config = ConfigDict(from_attributes=True)
```

## データのシリアライズ

```python
user = User(id=1, name="Alice", email="alice@example.com")

# 辞書に変換
user_dict = user.model_dump()  # v2では model_dump()
print(user_dict)

# JSON文字列に変換
user_json = user.model_dump_json()  # v2では model_dump_json()
print(user_json)

# 特定のフィールドを除外
user_dict_no_id = user.model_dump(exclude={'id'})

# 特定のフィールドのみ含める
user_dict_only_name = user.model_dump(include={'name', 'email'})
```

## 次のステップ

Pydanticの詳細を理解したら、[第6章: データベース連携](../06-database/README.md)に進みましょう。
