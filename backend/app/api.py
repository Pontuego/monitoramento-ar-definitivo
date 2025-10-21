from fastapi import APIRouter, Query
from app.service import get_air_quality
from app.schemas import AirQualityResponse

router = APIRouter()

@router.get("/sensor_data", response_model=AirQualityResponse)
async def sensor_data(
    lat: float = Query(..., description="Latitude do usuário"),
    lon: float = Query(..., description="Longitude do usuário")
):
    """
    Endpoint principal: recebe latitude e longitude e retorna
    temperatura, umidade e qualidade do ar.
    """
    data = await get_air_quality(lat, lon)
    return data