from pydantic import BaseModel

class AirQualityResponse(BaseModel):
    location: str
    temperature: float
    humidity: float
    air_quality: int
    status: str
    recommendation: str