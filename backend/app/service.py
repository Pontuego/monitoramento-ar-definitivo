import httpx
from app.schemas import AirQualityResponse

BASE_URL = "https://air-quality-api.open-meteo.com/v1/air-quality"

async def get_air_quality(lat: float, lon: float) -> AirQualityResponse:
    try:
        async with httpx.AsyncClient() as client:
            response = await client.get(
                BASE_URL,
                params={
                    "latitude": lat,
                    "longitude": lon,
                    "hourly": "pm2_5,pm10",  # só os poluentes
                    "timezone": "auto"
                },
                timeout=10
            )
            data = response.json()

        hourly = data.get("hourly")
        if not hourly:
            raise ValueError("API não retornou dados 'hourly'.")

        # Pegar o último valor válido de PM2.5 e PM10
        pm2_5_list = [v for v in hourly.get("pm2_5", []) if v is not None]
        pm10_list = [v for v in hourly.get("pm10", []) if v is not None]

        pm2_5 = pm2_5_list[-1] if pm2_5_list else None
        pm10 = pm10_list[-1] if pm10_list else None

        if pm2_5 is None:
            aqi, status, recommendation = None, "Erro", "Não há dados de PM2.5 disponíveis."
        elif pm2_5 <= 12:
            aqi, status, recommendation = 1, "Bom", "Excelente para atividades ao ar livre!"
        elif pm2_5 <= 35:
            aqi, status, recommendation = 2, "Moderado", "Seguro, mas evite esforço físico intenso."
        elif pm2_5 <= 55:
            aqi, status, recommendation = 3, "Ruim", "Pessoas sensíveis devem evitar sair."
        elif pm2_5 <= 150:
            aqi, status, recommendation = 4, "Muito Ruim", "Evite sair de casa, o ar está poluído."
        else:
            aqi, status, recommendation = 5, "Perigoso", "Permaneça em casa — risco grave à saúde."

        location = f"Lat {lat}, Lon {lon}"

        return AirQualityResponse(
            location=location,
            temperature=None,  # não disponível nesse request
            humidity=None,     # não disponível nesse request
            air_quality=aqi,
            status=status,
            recommendation=recommendation
        )

    except Exception as e:
        print("❌ Erro ao obter dados do ar:", e)
        return AirQualityResponse(
            location=f"Lat {lat}, Lon {lon}",
            temperature=None,
            humidity=None,
            air_quality=None,
            status="Erro",
            recommendation="Não foi possível obter dados da qualidade do ar."
        )