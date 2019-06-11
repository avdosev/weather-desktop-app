import requests as req

api_url = {
    'current_day': 'http://api.openweathermap.org/data/2.5/weather',
    'next_days': 'http://api.openweathermap.org/data/2.5/forecast/daily',
    'next_hours': 'http://api.openweathermap.org/data/2.5/forecast'
}

def getCurrentWeather(cityID, apikey, lang='ru'):
    res = req.get(api_url['current_day'], params={
            'id': cityID,
            'units': 'metric',
            'APPID': apikey,
            'lang': lang
        })
    return res.json()

def getForNextDays(cityID, apikey, count, lang='ru'):
    res = req.get(api_url['next_days'], params={
            'id': cityID,
            'units': 'metric',
            'APPID': apikey,
            'lang': lang,
            'cnt': count
        })
    return res.json()

def getHoursForecastData(cityID, apikey, lang='ru'):
    res = req.get(api_url['next_hours'], params={
            'id': cityID,
            'units': 'metric',
            'APPID': apikey,
            'lang': lang
        })
    return res.json()
