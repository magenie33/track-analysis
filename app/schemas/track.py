from pydantic import BaseModel
from typing import Optional
from datetime import datetime
from decimal import Decimal

class TrackBase(BaseModel):
    name: str
    spotify_id: str
    artist_id: str
    album_id: Optional[str] = None
    duration_ms: Optional[int] = None
    popularity: Optional[int] = None
    explicit: Optional[bool] = None
    track_number: Optional[int] = None
    disc_number: Optional[int] = None
    
    # 音频特征
    acousticness: Optional[Decimal] = None
    danceability: Optional[Decimal] = None
    energy: Optional[Decimal] = None
    instrumentalness: Optional[Decimal] = None
    key: Optional[int] = None
    loudness: Optional[Decimal] = None
    mode: Optional[int] = None
    speechiness: Optional[Decimal] = None
    tempo: Optional[Decimal] = None
    time_signature: Optional[int] = None
    valence: Optional[Decimal] = None

class TrackResponse(TrackBase):
    id: str
    created_at: datetime
    updated_at: datetime
    
    class Config:
        from_attributes = True 