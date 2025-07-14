from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from typing import List
from app.core.database import get_db
from app.models.artist import Artist
from app.schemas.artist import ArtistResponse

router = APIRouter()

@router.get("/", response_model=List[ArtistResponse])
async def get_artists(db: Session = Depends(get_db)):
    """获取所有歌手列表"""
    artists = db.query(Artist).all()
    return artists

@router.get("/{artist_id}", response_model=ArtistResponse)
async def get_artist(artist_id: str, db: Session = Depends(get_db)):
    """根据ID获取歌手信息"""
    artist = db.query(Artist).filter(Artist.spotify_id == artist_id).first()
    if not artist:
        raise HTTPException(status_code=404, detail="Artist not found")
    return artist

@router.post("/sync")
async def sync_artist_data(db: Session = Depends(get_db)):
    """同步歌手数据（从Spotify API）"""
    # TODO: 实现Spotify API数据同步
    return {"message": "Artist data sync started"} 