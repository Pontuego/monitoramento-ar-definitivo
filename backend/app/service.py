import httpx
from app.schemas import AirQualityResponse

BASE_URL = "https://air-quality-api.open-meteo.com/v1/air-quality"

async def get_air_quality(lat: float, lon: float) -> AirQualityResponse:
    async with httpx.AsyncClient() as client:
        response = await client.get(
            BASE_URL,
            params={
                "latitude": lat,
                "longitude": lon,
                "hourly": "pm2_5,pm10,carbon_monoxide,nitrogen_dioxide,ozone",
                "timezone": "auto"
            }
        )
        data = response.json()

    pm2_5 = data["hourly"]["pm2_5"][-1]
    pm10 = data["hourly"]["pm10"][-1]

    if pm2_5 <= 12:
        aqi = 1
        status = "Bom"
        recommendation = "Excelente para atividades ao ar livre!"
    elif pm2_5 <= 35:
        aqi = 2
        status = "Moderado"
        recommendation = "Seguro, mas evite esforço físico intenso."
    elif pm2_5 <= 55:
        aqi = 3
        status = "Ruim"
        recommendation = "Pessoas sensíveis devem evitar sair."
    elif pm2_5 <= 150:
        aqi = 4
        status = "Muito Ruim"
        recommendation = "Evite sair de casa, o ar está poluído."
    else:
        aqi = 5
        status = "Perigoso"
        recommendation = "Permaneça em casa — risco grave à saúde."

    location = f"Lat {lat}, Lon {lon}"

    return AirQualityResponse(
        location=location,
        aqi=aqi,
        status=status,
        recommendation=recommendation
    )