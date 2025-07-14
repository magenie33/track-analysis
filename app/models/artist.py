from sqlalchemy import Column, String, Integer, ARRAY, DateTime
from sqlalchemy.sql import func
from app.core.database import Base
import uuid

class Artist(Base):
    __tablename__ = "artists"
    
    id = Column(String, primary_key=True, default=lambda: str(uuid.uuid4()))
    spotify_id = Column(String, unique=True, nullable=False, index=True)
    name = Column(String, nullable=False)
    popularity = Column(Integer)
    followers_count = Column(Integer)
    genres = Column(ARRAY(String))
    image_url = Column(String)
    created_at = Column(DateTime(timezone=True), server_default=func.now())
    updated_at = Column(DateTime(timezone=True), server_default=func.now(), onupdate=func.now())
    
    def __repr__(self):
        return f"<Artist(name='{self.name}', spotify_id='{self.spotify_id}')>" 