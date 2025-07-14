from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from app.core.config import settings
from app.api.v1.api import api_router

app = FastAPI(
    title="Track Analysis API",
    description="Spotify热门歌曲分析API",
    version="1.0.0",
    openapi_url=f"{settings.API_PREFIX}/openapi.json"
)

# CORS中间件
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # 生产环境中应该指定具体域名
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# 包含API路由
app.include_router(api_router, prefix=settings.API_PREFIX)

@app.get("/")
async def root():
    """健康检查端点"""
    return {"message": "Track Analysis API is running!", "version": "1.0.0"}

@app.get("/health")
async def health_check():
    """详细的健康检查"""
    return {
        "status": "healthy",
        "service": "track-analysis",
        "version": "1.0.0"
    } 