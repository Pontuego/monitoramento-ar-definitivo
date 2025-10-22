from fastapi import APIRouter, Query
from app.service import get_air_quality

router = APIRouter()

@router.get("/sensor_data")
async def sensor_data(lat: float = Query(...), lon: float = Query(...)):
    return await get_air_quality(lat, lon)