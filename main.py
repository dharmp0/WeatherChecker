import requests
from dotenv import load_dotenv
import os


load_dotenv() # loads variables from .env
API_KEY = os.getenv("API_KEY") # reads API_KEY variable and assigns to local API_KEY 

def get_coords():
    city = input("Enter city name: ").lower()

    location_api = requests.get(f"http://api.openweathermap.org/geo/1.0/direct?q={city}&limit=1&appid={API_KEY}")

    if not location_api.json():
        print("City not found, please try again!")
        return get_coords()
    
    elif location_api.status_code == 200:
        cord_data = location_api.json()
        latitude = cord_data[0]["lat"]
        longitude = cord_data[0]["lon"]

    return latitude, longitude, city

def get_weather(latitude, longitude):
    weather_api = requests.get(f"https://api.openweathermap.org/data/2.5/weather?lat={latitude}&lon={longitude}&appid={API_KEY}&units=metric")

    if weather_api.status_code == 200:
        weather_data = weather_api.json()
        weather = weather_data["weather"][0]["main"]
        temp= weather_data["main"]["temp"]
    
    return weather, temp

def main():
    lat, lon,city = get_coords()
    weather, temp = get_weather(lat,lon)
    print("Weather in", city.title() + ":", weather, temp, "°C.")

if __name__ == "__main__":
    main()
