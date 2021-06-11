import requests


# Exchange rates dictionary to cache data
exchange_rates = dict()

# Read origin currency
origin_currency = input().lower()

# Retrieve and cache 'USD' and 'EUR' exchange rates
exchange_rates_req_dict = requests.get(f'http://www.floatrates.com/daily/{origin_currency}.json').json()
if origin_currency != 'usd':
    exchange_rates['usd'] = exchange_rates_req_dict['usd']
if origin_currency != 'eur':
    exchange_rates['eur'] = exchange_rates_req_dict['eur']

while True:

    # Read target currency until empty input
    target_currency = input().lower()
    if not target_currency:
        break

    # Read amount of money to exchange
    origin_amount = float(input())

    # Check cache
    print('Checking the cache...')
    if target_currency in exchange_rates:
        print('Oh! It is in the cache!')
    else:
        print('Sorry, but it is not in the cache!')
        # Retrieve and cache target currency exchange rate
        exchange_rates_req_dict = requests.get(f'http://www.floatrates.com/daily/{origin_currency}.json').json()
        exchange_rates[target_currency] = exchange_rates_req_dict[target_currency]

    # Calculate amount in target currency
    target_amount = origin_amount * exchange_rates[target_currency]["rate"]
    print(f'You received {round(target_amount, 2)} {target_currency.upper()}.')
