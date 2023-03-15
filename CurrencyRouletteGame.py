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

    print(f'The exchange rate for today - {today} - is: \n1 USD = {converted} ILS.')
    rng = int(random.uniform(1, 101))
    x = rng * converted

    print(f'You now have ${rng}.')
    get_guess_from_user(difficulty, rng, x, converted)
    return True


def get_guess_from_user(difficulty, rng, x, converted):

    try:
        while True:
            help1 = input('If you need help with calculations, just say the word. [y/n]\n').lower()
            if help1 == 'y':
                print(f"Alright, here's how it goes:")
                calc1 = int(input(f'How much money did you get?\n'))
                if calc1 == rng:
                    pass
                else:
                    print("No, that's wrong. Let's try this again.\n")
                    continue
                print('OK. Calculating...')
                time.sleep(1.5)
                print(f'The exchange rate for today is {converted}.\n'
                      f'So that means you have', + int(calc1 * converted - (5 - difficulty)), 'ILS.')
                break
            elif help1 == 'n':
                break
            else:
                input('Tell me what you want. [y/n]').lower()
                break

        guess = int(input(f"So, how much is ${rng} in ILS? "
                          f"\n(Hint: You don't need to be super accurate down to the decimal point)\n"))
        if int(guess) == (int(x) + (5 - difficulty)):
            print('You got it right! You are a lean-mean-calculating machine!\n')
            return True
        elif int(guess) == (int(x) - (5 - difficulty)):
            print('You got it right! You are a lean-mean-calculating machine!\n')
            return True
        else:
            print('Nope. You missed the mark. Maybe if you play again you will have better luck.')
            return False

    except ValueError:
        print("Error: You can only enter numbers.")

    return


def play(difficulty):
    if get_money_interval(difficulty):
        return True, play(difficulty) if input("Do you want to play again?"
                                               " [Enter 'Y' to play another round/"
                                               " Any other key to exit] ").lower() == 'y' else 0
    else:
        return False, play(difficulty) if input("Do you want to play again?"
                                                " [Enter 'Y' to play another round/"
                                                " Any other key to exit] ").lower() == 'y' else 0


def get_money_interval_h(difficulty):

    now = datetime.now()
    today = now.strftime("%d/%m/%Y")

    amount = 1
    url = f'https://v6.exchangerate-api.com/v6/{api_key}/pair/USD/ILS/{amount}'
    response = requests.get(url)
    data = response.json()
    converted = data['conversion_rate']

    print(f'שער החליפין להיום - {today} - הוא:\n 1$ = {converted} ש"ח')
    rng = int(random.uniform(1, 101))
    x = rng * converted

    print(f'קיבלת ${rng}')
    get_guess_from_user_h(difficulty, rng, x, converted)
    return True


def get_guess_from_user_h(difficulty, rng, x, converted):

    try:
        while True:
            help1 = input('אם את/ה זקוק/ה לעזרה בחישובים, רק תגיד. [כ/ל]\n')
            if help1 == 'כ':
                print(f"אוקי, ככה זה עובד:")
                calc1 = int(input(f'כמה כסף קיבלת?\n'))
                if calc1 == rng:
                    pass
                else:
                    print('משהו לא הסתדר, אולי הסכום שהזנת לא נכון?\n')
                    continue
                print('אוקי, מחשב...')
                time.sleep(1.5)
                print(f'שער החליפין להיום הוא {converted}.\n'
                      f'וזה אומר שיש לך', + int(calc1 * converted - (5 - difficulty)), 'ש"ח.')
                break
            elif help1 == 'ל':
                break

        guess = int(input(f'אז כמה זה ${rng} בש"ח?'
                          f'\n(רמז: לא צריך להיות מדויקים עד לרמת הנקודה העשרונית)\n'))
        if int(guess) == (int(x) + (5 - difficulty)):
            print('כל הכבוד לך! את/ה מכונת חישובים משומנת ומיומנת!\n')
            return True
        elif int(guess) == (int(x) - (5 - difficulty)):
            print('כל הכבוד לך! את/ה מכונת חישובים משומנת ומיומנת!\n')
            return True
        else:
            print('לא, פספסת את המטרה. אולי יהיה לך מזל אם צנסה בשנית.')
            return False

    except ValueError:
        print('תקלה. ניתן להזין רק מספרים.')

    return


def play_h(difficulty):
    if get_money_interval_h(difficulty):
        return True, play_h(difficulty) if input('האם תרצי/ה לשחק בשנית? [כ/ כל מקש אחר ליציאה]\n') == 'כ' else 0
    else:
        return False, play_h(difficulty) if input('האם תרצי/ה לשחק בשנית? [כ/ כל מקש אחר ליציאה]\n') == 'כ' else 0
