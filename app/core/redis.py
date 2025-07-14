import redis
from app.core.config import settings

# 创建Redis连接池
redis_client = redis.Redis.from_url(
    settings.REDIS_URL,
    decode_responses=True,  # 自动解码响应
    socket_connect_timeout=5,  # 连接超时
    socket_timeout=5,  # 读写超时
    retry_on_timeout=True,  # 超时重试
    health_check_interval=30  # 健康检查间隔
)

def get_redis():
    """获取Redis客户端的依赖函数"""
    return redis_client 