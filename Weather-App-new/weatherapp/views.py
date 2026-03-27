from django.shortcuts import render
from django.contrib import messages
import requests
import datetime


def home(request):

    if 'city' in request.POST:
        city = request.POST['city']
    else:
        city = 'indore'

    # OpenWeatherMap API key
    WEATHER_API_KEY = 'cf6042d570c12c3cdf7ce7a141122f9d'
    url = f'https://api.openweathermap.org/data/2.5/weather?q={city}&appid={WEATHER_API_KEY}'
    PARAMS = {'units': 'metric'}

    # City background image: use Pexels landscape photos via a query-based redirect.
    # We encode the city name into a Picsum-backed URL for reliable free images.
    # Using Bing's image search redirect (no key, redirects to image directly):
    city_encoded = city.replace(' ', '+')
    image_url = f'https://loremflickr.com/1920/1080/{city_encoded},city,skyline'

    try:
        data = requests.get(url, params=PARAMS).json()
        description = data['weather'][0]['description']
        icon = data['weather'][0]['icon']
        temp = data['main']['temp']
        day = datetime.date.today()

        return render(request, 'weatherapp/index.html', {
            'description': description,
            'icon': icon,
            'temp': temp,
            'day': day,
            'city': city,
            'exception_occurred': False,
            'image_url': image_url,
        })

    except KeyError:
        exception_occurred = True
        messages.error(request, 'Entered city is not available in the Weather API')
        day = datetime.date.today()

        return render(request, 'weatherapp/index.html', {
            'description': 'clear sky',
            'icon': '01d',
            'temp': 25,
            'day': day,
            'city': 'indore',
            'exception_occurred': exception_occurred,
            'image_url': 'https://images.pexels.com/photos/3008509/pexels-photo-3008509.jpeg?auto=compress&cs=tinysrgb&w=1600',
        })