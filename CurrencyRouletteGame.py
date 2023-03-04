from inputimeout import inputimeout
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
    # low = int(rng - (5 - difficulty))
    # high = int(rng + (5 - difficulty))
    # interval = (rng - (5 - difficulty), rng + (5 - difficulty))

    return rng


def get_guess_from_user(rng):

    while True:
        try:
            guess = int(inputimeout(prompt=f'Can you calculate how much ${rng}'
                                           f' is in ILS? \nYou have 10 seconds to answer: ', timeout=10))
            if guess > rng:
                print('Too high.')
            elif guess < rng:
                print('Too low.')
            else:
                print('Correct!')

        except ValueError:
            print("Error: You can only enter numbers.")
        except Exception:
            timed_out = 'Too slow. You timed out.'
            print(timed_out)
            quit()


def play(difficulty):

    rng = get_money_interval(difficulty)
    if get_guess_from_user(rng):
        print('You got it right, you are a lean-mean-calculating machine.')
        quit()
    else:
        print('Well, Fuck. You lost.')
        quit()



