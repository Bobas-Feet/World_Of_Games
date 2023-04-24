import random
import time
from Scores import add_score, no_score


def generate_number(difficulty):

    while True:
        if difficulty == 1:
            print('The chosen difficulty is: Very Easy')
            print('Generating...')
            time.sleep(2.5)
            rng = random.randint(1, (difficulty * 5))
            return rng
        elif difficulty == 2:
            print('The chosen difficulty is: Easy')
            print('Generating...')
            time.sleep(2.5)
            rng = random.randint(1, (difficulty * 5))
            return rng
        elif difficulty == 3:
            print('The chosen difficulty is: Medium')
            print('Generating...')
            time.sleep(2.5)
            rng = random.randint(1, (difficulty * 5))
            return rng
        elif difficulty == 4:
            print('The chosen difficulty is: Hard')
            print('Generating...')
            time.sleep(2.5)
            rng = random.randint(1, (difficulty * 5))
            return rng
        elif difficulty == 5:
            print('The chosen difficulty is: Very Hard')
            print('Generating...')
            time.sleep(2.5)
            rng = random.randint(1, (difficulty * 5))
            return rng
        else:
            print('Unknown difficulty')


def get_guess_from_user(difficulty, rng):

    count = 0
    while True:
        count += 1
        guess = int(input(f'The number the computer is thinking about is between 1 and {difficulty * 5}'
                          f'\nCan you guess what it is?\n'))
        if int(count) >= 3:
            # print("\nWell, it seems you're out of attempts.")
            return False

        if rng > guess:
            print('Nope. Maybe higher.')
        elif rng < guess:
            print('Nope. Maybe lower.')
        else:
            return True


def compare_results(guess, rng):

    if guess != rng:
        return True
    else:
        return False


def play(difficulty):

    rng = generate_number(difficulty)
    guess = get_guess_from_user(difficulty, rng)
    result = compare_results(guess, rng)

    if result:
        print(f'You got it right. Good for you.\n')
        return True, play(difficulty) if input("\nDo you want to play again?"
                                               " [Enter 'Y' to play another round/"
                                               " Any other key to exit] ").lower().format(add_score(difficulty)) ==\
                                                'y' else 0
    else:
        print('You got it wrong. You suck at this.\nThe number that the computer was thinking of is [{}]'.format(rng))
        return False, play(difficulty) if input("\nDo you want to play again?"
                                                " [Enter 'Y' to play another round/"
                                                " Any other key to exit] ").lower().format(no_score(difficulty)) ==\
                                                'y' else 0


def generate_number_h(difficulty):

    while True:
        if difficulty == 1:
            print('רמת הקושי שנבחרה היא: קל מאוד')
            print('מייצר...')
            time.sleep(2)
            rng = random.randint(1, (difficulty * 5))
            return rng
        elif difficulty == 2:
            print('רמת הקושי שנבחרה היא: קל')
            print('מייצר...')
            time.sleep(2)
            rng = random.randint(1, (difficulty * 5))
            return rng
        elif difficulty == 3:
            print('רמת הקושי שנבחרה היא: בינוני')
            print('מייצר...')
            time.sleep(2)
            rng = random.randint(1, (difficulty * 5))
            return rng
        elif difficulty == 4:
            print('רמת הקושי שנבחרה היא: קשה')
            print('מייצר...')
            time.sleep(2)
            rng = random.randint(1, (difficulty * 5))
            return rng
        elif difficulty == 5:
            print('רמת הקושי שנבחרה היא: קשה מאוד')
            print('מייצר...')
            time.sleep(2)
            rng = random.randint(1, (difficulty * 5))
            return rng
        else:
            print('שגיאה. רמת קושי שהקשת לא מוכרת.')
            continue


def get_guess_from_user_h(difficulty, rng):

    count = 0
    while True:
        count += 1
        guess = int(input(f'המספר שהמחשב חושב עליו הוא בין 1-{difficulty * 5}'
                          f'\nהאם את/ה מסוגל/ת לנחש את המספר?\n'))
        if int(count) >= 3:
            # print("\nWell, it seems you're out of attempts.")
            return False

        if rng > guess:
            print('לא, אולי תנסי/ה מספר גבוה יותר.\n')
        elif rng < guess:
            print('לא, אולי תנסי/ה מספר נמוך יותר.\n')
        else:
            return True


def compare_results_h(guess, rng):

    if guess == rng:
        return True
    else:
        return False


def play_h(difficulty):

    rng = generate_number_h(difficulty)
    guess = get_guess_from_user_h(difficulty, rng)
    result = compare_results_h(guess, rng)

    if result:
        print(f'ניחשת נכון. כל הכבוד.\n')
        # add_score(difficulty)
        return True, play_h(difficulty) if input('האם תרצי/ה לשחק בשנית? [כ/ כל מקש אחר ליציאה]\n') == 'כ' else 0

    else:
        print('ניחשת לא נכון. המספר שהמחשב חיפש הוא [{}]\n'.format(rng))
        # no_score(difficulty)
        return False, play_h(difficulty) if input('האם תרצי/ה לשחק בשנית? [כ/ כל מקש אחר ליציאה]\n') == 'כ' else 0
