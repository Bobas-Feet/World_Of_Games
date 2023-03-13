import time
import requests
from datetime import datetime
import random
from credentials import api_key


def get_money_interval(difficulty):

    now = datetime.now()
    today = now.strftime("%a, %B %d %Y")

    amount = 1
    url = f'https://v6.exchangerate-api.com/v6/{api_key}/pair/USD/ILS/{amount}'
    response = requests.get(url)
    data = response.json()
    converted = data['conversion_rate']

    print(f'The exchange rate for today - {today} - is: \n1 USD = {converted} ILS')
    rng = int(random.uniform(1, 101))
    x = rng * converted

    print(f'You now have ${rng}.')
    get_guess_from_user(difficulty, rng, x, converted)
    return True


def get_guess_from_user(difficulty, rng, x, converted):

    try:
        while True:
            help1 = input('Do you want help? [y/n]\n').lower()
            if help1 == 'y':
                print(f"Here's a little help to get you going:")
                calc1 = int(input(f'How much money did you get?\n'))
                print('OK. Thinking...')
                time.sleep(1.5)
                print(f'The exchange rate for today is {converted}'
                      f'And that means you have', + int(calc1 * converted), 'ILS')
                break
            else:
                break

        guess = int(input(f"So, how much is ${rng} in ILS? "
                          f"\n(Hint: You don't need to be super accurate down to the decimal point)\n"))
        if int(guess) == (int(x) + (5 - difficulty)) or int(guess) == (int(x) - (5 - difficulty)):
            print('You got it right! You are a lean-mean-calculating machine!\n')
            return True
        else:
            print('Nope. You missed the mark. Maybe if you play again you will have better luck')
            return False

    except ValueError:
        print("Error: You can only enter numbers.")


def play(difficulty):
    if get_money_interval(difficulty):
        return True
    else:
        return False
