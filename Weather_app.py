import requests

def get_weather(city_name, api_key):
    base_url = "http://api.openweathermap.org/data/2.5/weather"
    params = {
        'q': city_name,
        'appid': api_key,
        'units': 'metric'  # use 'imperial' for Fahrenheit
    }

    response = requests.get(base_url, params=params)

    if response.status_code == 200:
        data = response.json()
        city = data['name']
        country = data['sys']['country']
        temp = data['main']['temp']
        humidity = data['main']['humidity']
        description = data['weather'][0]['description']

        print(f"\n📍 Weather in {city}, {country}")
        print(f"🌡️ Temperature: {temp}°C")
        print(f"💧 Humidity: {humidity}%")
        print(f"☁️ Description: {description.capitalize()}")
    else:
        print("\n❌ City not found or invalid API key.")

if __name__ == "__main__":
    API_KEY = "1b8b611537b2750e1b9265b984845381d"  
    city = input("Enter city name: ")
    get_weather(city, API_KEY)
