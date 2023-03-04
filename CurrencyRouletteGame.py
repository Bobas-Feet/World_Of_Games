import requests
import datetime
import random
from credentials import api_key


def get_money_interval(difficulty):

    now = datetime.datetime.now()
    amount = 1
    url = f'https://v6.exchangerate-api.com/v6/{api_key}/pair/USD/ILS/{amount}'

    response = requests.get(url)
    data = response.json()
    converted = data['conversion_rate']

    print(f'The exchange rate for today, {now}, is {converted}')
    rng = int(random.uniform(1, 101))
    print(f'You get ${rng}, YAY.')
    interval = (rng - (5 - difficulty), rng + (5 - difficulty))

    return interval


def get_guess_from_user(rng):

    while True:
        try:
            guess = int(input(f"Guess the value of ${rng} in ILS: "))
        except ValueError:
            print("Error: You can only enter numbers.")
            continue
        return guess


def play(difficulty):

    interval = get_money_interval(difficulty)
    get_guess_from_user(interval)



