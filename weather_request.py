import requests as req

api_url = {
    'current_day': 'http://api.openweathermap.org/data/2.5/weather',
    'next_days': ''
}

def getCurrentWeather(cityID, apikey, lang='ru'):
    res = req.get(api_url['current_day'], params={
            'id': cityID,
            'units': 'metric',
            'APPID': apikey,
            'lang': lang
        })
    return res.json()