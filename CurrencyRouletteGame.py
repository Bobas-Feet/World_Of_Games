# from inputimeout import inputimeout
import requests
import datetime
import random
from credentials import api_key


def get_money_interval():

    today = datetime.date.today()

    amount = 1
    url = f'https://v6.exchangerate-api.com/v6/{api_key}/pair/USD/ILS/{amount}'
    response = requests.get(url)
    data = response.json()
    converted = data['conversion_rate']

    print(f'The exchange rate for today, {today}, is: \n1 USD = {converted} ILS')
    rng = int(random.uniform(1, 101))
    x = rng * converted
    # x = int(rng * converted)

    print(f'You get ${rng}, YAY. The converted amount is {x} ILS') # no need for this
    get_guess_from_user(rng, x)
    return rng


def get_guess_from_user(rng, x):

    try:
        guess = int(input(f'Can you calculate how much ${rng}'
                          f' is in ILS? \nYou have 10 seconds to answer: '))
        print(guess)

        if guess == x - 5 or guess == x + 5:
            # print('You got it right, you are a lean-mean-calculating machine.')
            return True
        else:
            # print('You suck')
            return False

    except ValueError:
        print("Error: You can only enter numbers.")
    except Exception:
        timed_out = 'Too slow. You timed out.'
        print(timed_out)


def play(difficulty):
    if get_money_interval() is True:
        print('you win')
        return True
    else:
        print('you lose')
        return False
