# 第10章: 非同期処理とバックグラウンドタスク

## 学習目標

- async/awaitの理解と活用
- 非同期データベース操作
- バックグラウンドタスクの実装
- 並行処理とパフォーマンス最適化

## async/awaitの基本

```python
@app.get("/async-example")
async def async_example():
    result = await some_async_operation()
    return {"result": result}
```

## 非同期データベース操作

```python
from sqlalchemy.ext.asyncio import create_async_engine, AsyncSession

async_engine = create_async_engine("postgresql+asyncpg://...")

@app.get("/users")
async def get_users(db: AsyncSession = Depends(get_async_db)):
    result = await db.execute(select(User))
    users = result.scalars().all()
    return users
```

## バックグラウンドタスク

```python
from fastapi import BackgroundTasks

def send_email(email: str, message: str):
    # メール送信処理
    print(f"Sending email to {email}: {message}")

@app.post("/send-notification")
async def send_notification(
    email: str,
    background_tasks: BackgroundTasks
):
    background_tasks.add_task(send_email, email, "Welcome!")
    return {"message": "Notification will be sent in background"}
```

## 並行処理

```python
import asyncio

async def fetch_data_1():
    await asyncio.sleep(1)
    return {"data": 1}

async def fetch_data_2():
    await asyncio.sleep(1)
    return {"data": 2}

@app.get("/concurrent")
async def get_concurrent_data():
    results = await asyncio.gather(
        fetch_data_1(),
        fetch_data_2()
    )
    return results
```

## ストリーミングレスポンス

```python
from fastapi.responses import StreamingResponse

async def generate_data():
    for i in range(10):
        await asyncio.sleep(0.5)
        yield f"data: {i}\n\n"

@app.get("/stream")
async def stream_data():
    return StreamingResponse(generate_data(), media_type="text/event-stream")
```
