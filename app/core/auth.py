import spotipy
from spotipy.oauth2 import SpotifyOAuth
from jose import JWTError, jwt
from datetime import datetime, timedelta
from typing import Optional
from app.core.config import settings

class SpotifyAuth:
    """Spotify OAuth认证管理"""
    
    def __init__(self):
        self.scope = "user-read-private user-read-email playlist-modify-public"
        self.sp_oauth = SpotifyOAuth(
            client_id=settings.SPOTIFY_CLIENT_ID,
            client_secret=settings.SPOTIFY_CLIENT_SECRET,
            redirect_uri=settings.SPOTIFY_REDIRECT_URI,
            scope=self.scope
        )
    
    def get_auth_url(self) -> str:
        """获取Spotify授权URL"""
        return self.sp_oauth.get_authorize_url()
    
    def get_user_info(self, code: str):
        """通过授权码获取用户信息"""
        try:
            token_info = self.sp_oauth.get_access_token(code)
            sp = spotipy.Spotify(auth=token_info['access_token'])
            user = sp.current_user()
            return user, token_info
        except Exception as e:
            raise Exception(f"Spotify认证失败: {str(e)}")
    
    def refresh_token(self, refresh_token: str):
        """刷新访问令牌"""
        try:
            token_info = self.sp_oauth.refresh_access_token(refresh_token)
            return token_info
        except Exception as e:
            raise Exception(f"令牌刷新失败: {str(e)}")

class JWTAuth:
    """JWT令牌管理"""
    
    def create_access_token(self, data: dict, expires_delta: Optional[timedelta] = None):
        """创建访问令牌"""
        to_encode = data.copy()
        if expires_delta:
            expire = datetime.utcnow() + expires_delta
        else:
            expire = datetime.utcnow() + timedelta(minutes=settings.ACCESS_TOKEN_EXPIRE_MINUTES)
        
        to_encode.update({"exp": expire})
        encoded_jwt = jwt.encode(to_encode, settings.SECRET_KEY, algorithm="HS256")
        return encoded_jwt
    
    def verify_token(self, token: str):
        """验证令牌"""
        try:
            payload = jwt.decode(token, settings.SECRET_KEY, algorithms=["HS256"])
            return payload
        except JWTError:
            return None

# 创建全局实例
spotify_auth = SpotifyAuth()
jwt_auth = JWTAuth() 