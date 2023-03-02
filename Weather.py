'''Using API to get weather information for any city specified by the user.'''

from pprint import pprint
import requests


API_KEY = 'insert your api key here'

city = input('Enter a city.')
BASE_URL = str('http://api.openweathermap.org/data/2.5/weather?appid=' + API_KEY + '&q=' + city)

weather_data = requests.get(BASE_URL, timeout=5).json()

pprint(weather_data)
