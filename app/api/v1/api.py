from fastapi import APIRouter
from app.api.v1.endpoints import artists, tracks, analysis

# 创建主API路由器
api_router = APIRouter()

# 包含各个模块的路由
api_router.include_router(artists.router, prefix="/artists", tags=["artists"])
api_router.include_router(tracks.router, prefix="/tracks", tags=["tracks"])
api_router.include_router(analysis.router, prefix="/analysis", tags=["analysis"]) 