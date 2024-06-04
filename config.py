import os

from dotenv import load_dotenv


load_dotenv()

USE_ROUNDED_COORDINATES = True
OPENWEATHER_URL = (
    'https://api.openweathermap.org/data/2.5/weather?lat={latitude}&lon={longitude}&appid=' +
    str(os.getenv('OPENWEATHER_API_KEY')) + '&lang=ru&units=metric'
)
