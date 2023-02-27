import requests
from settings import api_config
import json
geo_key = 'bdb0d875-cf0f-4e00-ad4a-d7a8f53c36c9'
weather_key = {'X-Yandex-API-Key': 'b7c057d1-075a-47c8-b407-cebb77207ad4'}

def get_city_coord(city):
    payload = {'geocode' : city, 'apikey' : geo_key, 'format' : 'json'}
    r = requests.get('https://geocode-maps.yandex.ru/1.x', params=payload)
    geo = json.loads(r.text)
    try:
        res = geo['response']['GeoObjectCollection']['featureMember'][0]['GeoObject']['Point']['pos']
        return res
    except IndexError as exp:
        return None

def get_weather(city):
    try:
        coordinates = get_city_coord(city).split()
        payload = {'lat' : coordinates[1], 'lon' : coordinates[0], 'lang' : 'ru_RU'}
        r = requests.get('https://api.weather.yandex.ru/v2/informers', params=payload, headers=weather_key)
        weather_data = json.loads(r.text)
        return weather_data['fact']
    except:
        return None


print(get_city_coord('орорро'))