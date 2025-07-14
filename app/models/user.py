from sqlalchemy import Column, String, DateTime
from sqlalchemy.sql import func
from app.core.database import Base

class User(Base):
    __tablename__ = "users"
    
    spotify_id = Column(String, primary_key=True)
    display_name = Column(String)
    email = Column(String)
    access_token = Column(String)
    refresh_token = Column(String)
    created_at = Column(DateTime(timezone=True), server_default=func.now())
    updated_at = Column(DateTime(timezone=True), server_default=func.now(), onupdate=func.now())
    
    def __repr__(self):
        return f"<User(spotify_id='{self.spotify_id}', display_name='{self.display_name}')>" 