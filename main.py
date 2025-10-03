import requests
from dotenv import load_dotenv
import os


load_dotenv() # loads variables from .env
API_KEY = os.getenv("API_KEY") # reads API_KEY variable and assigns to local API_KEY 

city_name = input("Enter city name: ")

location_api = f"http://api.openweathermap.org/geo/1.0/direct?q={city_name}&limit=1&appid={API_KEY}"

coordinates = requests.get(location_api)

if coordinates.status_code == 200:
    cord_data = coordinates.json()
    latitude = cord_data[0]["lat"]
    longitude = cord_data[0]["lon"]

print(latitude, longitude)

