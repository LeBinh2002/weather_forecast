import requests
from django.shortcuts import render

def get_weather_data(city):
    api_key = 'baee47d89c934056302c0989441611e8'
    url = f'http://api.openweathermap.org/data/2.5/weather?q={city}&appid={api_key}&units=metric'
    response = requests.get(url)
    return response.json()

def index(request):
    city = 'Hanoi'
    if request.method == 'POST':
        city = request.POST.get('city')
    weather_data = get_weather_data(city)
    context = {
        'city': city,
        'weather_data': weather_data
    }
    return render(request, 'weather/index.html', context)
