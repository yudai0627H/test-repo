"""
問題1の模範解答: Hello World API
"""

from fastapi import FastAPI

app = FastAPI()


@app.get("/")
def read_root():
    """ルートエンドポイント"""
    return {"message": "Hello World"}


@app.get("/health")
def health_check():
    """ヘルスチェックエンドポイント"""
    return {
        "status": "healthy",
        "service": "FastAPI Learning Course",
        "version": "1.0.0"
    }


# 実行方法:
# uvicorn solution_01:app --reload
#
# テスト:
# curl http://localhost:8000/
# curl http://localhost:8000/health
#
# ドキュメント:
# http://localhost:8000/docs

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)
