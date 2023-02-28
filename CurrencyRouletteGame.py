# 24/2/2023

from forex_python.converter import CurrencyRates
# import json
import os
# import urllib.request as r
import random
# from credentials import api_key


def get_money_interval(difficulty):

    # url = f'https://v6.exchangerate-api.com/v6/{api_key}/pair/USD/ILS'
    # response = r.urlopen(url)
    # data = json.load(response)
    # ex = int(data["USD_ILS"])

    cr = CurrencyRates()
    cr.get_rates('USD')

    rng = int(random.uniform(1, 100))
    from_currency = 'EUR'
    to_currency = 'USD'
    ex = cr.convert(from_currency, to_currency, 1)
    print(f'The Exchange rate for today is {ex}')
    t = rng * ex
    low = int(t - (5 - difficulty))
    high = int(t + (5 - difficulty))
    print(f'To play this game you are given ${rng}, YAY.')
    return rng, t, low, high


def get_guess_from_user(rng):

    while True:
        try:
            guess = int(input(f"Guess the value of ${rng} in ILS: "))
        except ValueError:
            print("Error: You can only enter numbers.")
            continue
        return guess


def play(difficulty):
    rng, t, low, high = get_money_interval(difficulty)
    guess = get_guess_from_user(rng)
    os.system('cls' if os.name == 'nt' else 'clear')
    if high >= guess >= low:
        return True
    else:
        return False
