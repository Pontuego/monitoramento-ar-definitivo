from pydantic import BaseModel
from typing import Optional

class AirQualityResponse(BaseModel):
    location: str
    temperature: Optional[float]
    humidity: Optional[float]
    air_quality: Optional[int]
    status: str
    recommendation: str