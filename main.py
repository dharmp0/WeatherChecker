import requests
from dotenv import load_dotenv
import os


load_dotenv() # loads variables from .env
API_KEY = os.getenv("API_KEY") # reads API_KEY variable and assigns to local API_KEY 

city_name = input("Enter city name: ")

location_api = requests.get(f"http://api.openweathermap.org/geo/1.0/direct?q={city_name}&limit=1&appid={API_KEY}")

if location_api.status_code == 200:
    cord_data = location_api.json()
    latitude = cord_data[0]["lat"]
    longitude = cord_data[0]["lon"]

weather_api = requests.get(f"https://api.openweathermap.org/data/2.5/weather?lat={latitude}&lon={longitude}&appid={API_KEY}")

if weather_api.status_code == 200:
    weather_data = weather_api.json()
    weather = weather_data["weather"][0]["main"]

print(weather)

