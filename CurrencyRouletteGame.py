# from inputimeout import inputimeout
import requests
import datetime
import random
from credentials import api_key


def get_money_interval(difficulty):

    today = datetime.date.today()

    amount = 1
    url = f'https://v6.exchangerate-api.com/v6/{api_key}/pair/USD/ILS/{amount}'
    response = requests.get(url)
    data = response.json()
    converted = data['conversion_rate']

    print(f'The exchange rate for today, {today}, is: \n1 USD = {converted} ILS')
    rng = int(random.uniform(1, 101))
    print(f'You get ${rng}, YAY.')

    x = rng * converted
    print(f'the converted amount is {x} ILS')

    return rng


def get_guess_from_user(rng):

    try:
        guess = float(input(f'Can you calculate how much ${rng}'
                            f' is in ILS? \nYou have 10 seconds to answer: '))
        if (guess - rng + 5) or (guess - rng - 5):
            return True
    except ValueError:
        print("Error: You can only enter numbers.")
    except Exception:
        timed_out = 'Too slow. You timed out.'
        print(timed_out)
    return False


def play(difficulty):
    rng = get_money_interval(difficulty)
    if get_guess_from_user(rng):
        print('You got it right, you are a lean-mean-calculating machine.')
        return True
    else:
        print('Well, Fuck. You lost.')
        return False
