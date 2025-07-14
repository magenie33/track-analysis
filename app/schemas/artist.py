from pydantic import BaseModel
from typing import List, Optional
from datetime import datetime

class ArtistBase(BaseModel):
    name: str
    spotify_id: str
    popularity: Optional[int] = None
    followers_count: Optional[int] = None
    genres: Optional[List[str]] = None
    image_url: Optional[str] = None

class ArtistResponse(ArtistBase):
    id: str
    created_at: datetime
    updated_at: datetime
    
    class Config:
        from_attributes = True 