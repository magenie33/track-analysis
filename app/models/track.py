from sqlalchemy import Column, String, Integer, Boolean, Numeric, DateTime, ForeignKey
from sqlalchemy.sql import func
from app.core.database import Base
import uuid

class Track(Base):
    __tablename__ = "tracks"
    
    id = Column(String, primary_key=True, default=lambda: str(uuid.uuid4()))
    spotify_id = Column(String, unique=True, nullable=False, index=True)
    artist_id = Column(String, ForeignKey("artists.id"), nullable=False, index=True)
    album_id = Column(String, ForeignKey("albums.id"), nullable=True)
    name = Column(String, nullable=False)
    duration_ms = Column(Integer)
    popularity = Column(Integer)
    explicit = Column(Boolean)
    track_number = Column(Integer)
    disc_number = Column(Integer)
    
    # 音频特征
    acousticness = Column(Numeric(5, 4))
    danceability = Column(Numeric(5, 4))
    energy = Column(Numeric(5, 4))
    instrumentalness = Column(Numeric(5, 4))
    key = Column(Integer)
    loudness = Column(Numeric(5, 2))
    mode = Column(Integer)
    speechiness = Column(Numeric(5, 4))
    tempo = Column(Numeric(6, 2))
    time_signature = Column(Integer)
    valence = Column(Numeric(5, 4))
    
    created_at = Column(DateTime(timezone=True), server_default=func.now())
    updated_at = Column(DateTime(timezone=True), server_default=func.now(), onupdate=func.now())
    
    def __repr__(self):
        return f"<Track(name='{self.name}', spotify_id='{self.spotify_id}')>" 