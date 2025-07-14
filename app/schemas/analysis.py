from pydantic import BaseModel
from typing import Optional, Dict, Any
from datetime import datetime
from decimal import Decimal

class AnalysisResponse(BaseModel):
    id: str
    track_id: str
    hot_score: Decimal
    ranking_position: int
    analysis_date: datetime
    factors: Optional[Dict[str, Any]] = None
    created_at: datetime
    
    class Config:
        from_attributes = True 