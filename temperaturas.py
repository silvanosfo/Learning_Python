import requests as req
import json

# API key openweathermap
API_KEY =  '02ce3117223858290ecc99b227f0577d'

# Coordinates
LAT = '41.5387600'
LON = '-8.6150500'
LANG = 'pt'

while True:
    link = f"https://api.openweathermap.org/data/2.5/weather?lat={LAT}&lon={LON}&lang={LANG}&appid={API_KEY}&units=metric"

    temperaturas = req.get(link)
    temperaturas = temperaturas.json()

    local = temperaturas["name"]
    desc = temperaturas["weather"][0]["description"]
    temp = temperaturas["main"]["temp"]
    print(f'Local: {local}\nTempo: {desc}\nTemperatura: {temp}ºC\n')