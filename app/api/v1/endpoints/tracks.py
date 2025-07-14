from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from typing import List
from app.core.database import get_db
from app.models.track import Track
from app.schemas.track import TrackResponse

router = APIRouter()

@router.get("/", response_model=List[TrackResponse])
async def get_tracks(db: Session = Depends(get_db)):
    """获取所有歌曲列表"""
    tracks = db.query(Track).all()
    return tracks

@router.get("/{track_id}", response_model=TrackResponse)
async def get_track(track_id: str, db: Session = Depends(get_db)):
    """根据ID获取歌曲信息"""
    track = db.query(Track).filter(Track.spotify_id == track_id).first()
    if not track:
        raise HTTPException(status_code=404, detail="Track not found")
    return track

@router.get("/artist/{artist_id}", response_model=List[TrackResponse])
async def get_artist_tracks(artist_id: str, db: Session = Depends(get_db)):
    """获取指定歌手的所有歌曲"""
    tracks = db.query(Track).filter(Track.artist_id == artist_id).all()
    return tracks 