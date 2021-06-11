import json
import requests


currency = input()

exchange_rates = json.loads(requests.get(f'http://www.floatrates.com/daily/{currency.lower()}.json').content)
print(exchange_rates['usd'], exchange_rates['eur'], sep='\n')
