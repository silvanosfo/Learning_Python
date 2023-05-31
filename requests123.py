import requests as req
import json

cotacoes = req.get('https://economia.awesomeapi.com.br/json/last/EUR-USD,EUR-BRL,BTC-USD')

# transforma em json dicionario
cotacoes = cotacoes.json()

# faz idendentacao do json
#cotacoes = json.dumps( cotacoes, indent=True)
#
#print(cotacoes)

print(f'\nEURUSD: {cotacoes["EURUSD"]["bid"]}$\nBTCUSD: {cotacoes["BTCUSD"]["bid"]}$\n')
