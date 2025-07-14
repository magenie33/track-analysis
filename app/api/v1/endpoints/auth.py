from fastapi import APIRouter, Depends, HTTPException, Request
from fastapi.responses import RedirectResponse
from sqlalchemy.orm import Session
from app.core.database import get_db
from app.core.auth import spotify_auth, jwt_auth
from app.models.user import User
from app.schemas.auth import UserResponse

router = APIRouter()

@router.get("/spotify")
async def spotify_login():
    """Spotify登录入口"""
    auth_url = spotify_auth.get_auth_url()
    return RedirectResponse(url=auth_url)

@router.get("/callback")
async def spotify_callback(code: str, request: Request, db: Session = Depends(get_db)):
    """Spotify回调处理"""
    try:
        # 获取用户信息
        user_info, token_info = spotify_auth.get_user_info(code)
        
        # 查找或创建用户
        user = db.query(User).filter(User.spotify_id == user_info['id']).first()
        if not user:
            user = User(
                spotify_id=user_info['id'],
                display_name=user_info['display_name'],
                email=user_info.get('email'),
                access_token=token_info['access_token'],
                refresh_token=token_info.get('refresh_token')
            )
            db.add(user)
        else:
            # 更新令牌
            user.access_token = token_info['access_token']
            user.refresh_token = token_info.get('refresh_token')
        
        db.commit()
        
        # 创建JWT令牌
        access_token = jwt_auth.create_access_token(data={"sub": user.spotify_id})
        
        # 重定向到前端，携带令牌
        frontend_url = "http://localhost:8000"
        return RedirectResponse(url=f"{frontend_url}?token={access_token}")
        
    except Exception as e:
        raise HTTPException(status_code=400, detail=str(e))

@router.get("/me", response_model=UserResponse)
async def get_current_user(request: Request, db: Session = Depends(get_db)):
    """获取当前用户信息"""
    # 从请求头获取令牌
    auth_header = request.headers.get("Authorization")
    if not auth_header or not auth_header.startswith("Bearer "):
        raise HTTPException(status_code=401, detail="未提供认证令牌")
    
    token = auth_header.split(" ")[1]
    payload = jwt_auth.verify_token(token)
    if not payload:
        raise HTTPException(status_code=401, detail="无效的认证令牌")
    
    user_id = payload.get("sub")
    user = db.query(User).filter(User.spotify_id == user_id).first()
    if not user:
        raise HTTPException(status_code=404, detail="用户不存在")
    
    return user

@router.post("/logout")
async def logout():
    """用户登出"""
    # 在实际应用中，可以将令牌加入黑名单
    return {"message": "登出成功"} 