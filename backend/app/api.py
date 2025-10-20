from fastapi import APIRouter, Query
from app.service import get_air_quality
from app.schemas import AirQualityResponse

router = APIRouter()

@router.get("/qualidade-ar", response_model=AirQualityResponse)
async def qualidade_ar(
    lat: float = Query(..., description="Latitude do usuário"),
    lon: float = Query(..., description="Longitude do usuário")
):
    """
    Endpoint principal: recebe latitude e longitude e retorna
    a qualidade do ar processada.
    """
    data = await get_air_quality(lat, lon)
    return data