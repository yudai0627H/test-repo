# 第5章: Pydanticとバリデーション

## 学習目標

- Pydanticモデルの詳細な使い方
- カスタムバリデーターの実装
- フィールドの制約と設定
- データのシリアライズとデシリアライズ

## Pydanticモデルの基本

```python
from pydantic import BaseModel, Field, EmailStr
from typing import Optional

class User(BaseModel):
    id: int
    name: str = Field(..., min_length=1, max_length=50)
    email: EmailStr
    age: Optional[int] = Field(None, ge=0, le=150)
    is_active: bool = True
```

## カスタムバリデーター

```python
from pydantic import BaseModel, validator

class User(BaseModel):
    name: str
    email: str
    password: str

    @validator('email')
    def validate_email(cls, v):
        if '@' not in v:
            raise ValueError('有効なメールアドレスではありません')
        return v

    @validator('password')
    def validate_password(cls, v):
        if len(v) < 8:
            raise ValueError('パスワードは8文字以上必要です')
        return v
```

## フィールド制約

```python
from pydantic import BaseModel, Field

class Product(BaseModel):
    name: str = Field(..., min_length=3, max_length=100)
    price: float = Field(..., gt=0, le=1000000)
    quantity: int = Field(0, ge=0)
```
