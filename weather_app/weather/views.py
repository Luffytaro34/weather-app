import requests
from django.shortcuts import render

# Function to get weather data from the API
def get_weather_data(city_name):
    api_key = '4f2c4e79d2bf929213761aa087b7911f'
    url = f"https://api.openweathermap.org/data/2.5/weather?q={city_name}&appid={api_key}&units=metric"

    # Make the API request
    response = requests.get(url)
    data = response.json()

    # Check if the response is valid
    if response.status_code == 200:
        weather_data = {
            'city': city_name,
            'temperature': data['main']['temp'],
            'description': data['weather'][0]['description'],
            'icon': data['weather'][0]['icon'],
        }
        return weather_data
    else:
        return None  # If the city is not found or any other issue occurs

def index(request):
    # List of cities you want to get weather data for
    cities = ['Hyderabad', 'London', 'New York']

    # Create a list of weather data for each city
    weather_data = []
    for city in cities:
        data = get_weather_data(city)
        if data:
            weather_data.append(data)

    # Pass the weather data to the template
    context = {'weather_data': weather_data}
    return render(request, 'weather/weather.html', context)
