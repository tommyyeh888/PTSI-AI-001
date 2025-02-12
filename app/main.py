from fastapi import FastAPI
from app.routes import orders
from app.database import Base, engine

# 初始化資料庫
Base.metadata.create_all(bind=engine)

app = FastAPI()

# 註冊工單 API 路由
app.include_router(orders.router, prefix="/orders", tags=["工單管理"])

@app.get("/")
def root():
    return {"message": "完工回報系統 API 正常運行"}
