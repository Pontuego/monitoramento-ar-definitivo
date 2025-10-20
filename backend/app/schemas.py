from pydantic import BaseModel

class AirQualityResponse(BaseModel):
    location: str
    aqi: int
    status: str
    recommendation: str