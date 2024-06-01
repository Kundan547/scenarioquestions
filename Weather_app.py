"""You have written a new Python script, weather_app.py,
    that fetches the current weather data for a given city using an API. 
     You want to start tracking this script using Git."""

import requests

def fetch_weather(city):
    WeatherAppKey = 'a26d861e4d62d8944250eb1ddd94008b'
    base_url = f'http://api.openweathermap.org/data/2.5/weather?q={city}&appid={WeatherAppKey}&units=metric'
    response = requests.get(base_url)

    # Debug print to check the status code and response content
    print(f"Status code: {response.status_code}")
    print(f"Response content: {response.text}")

    if response.status_code == 200:
        data = response.json()
        main = data['main']
        wind = data['wind']
        weather_desc = data['weather'][0]['description']
        temperature = main['temp']
        humidity = main['humidity']
        wind_speed = wind['speed']
        return (f'Temperature: {temperature}°C\n'
                f'Humidity: {humidity}%\n'
                f'Weather Description: {weather_desc}\n'
                f'Wind Speed: {wind_speed} m/s')
    else:
        return "City not found"

if __name__ == '__main__':
    city = input("Enter city name: ")
    print(fetch_weather(city))


