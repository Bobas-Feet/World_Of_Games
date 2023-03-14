import random
import time


def generate_number(difficulty):
    while True:
        if difficulty == 1:
            print('The chosen difficulty is: Very Easy')
            print('Generating...')
            time.sleep(2.5)
            return random.randint(1, (difficulty * 5))
        elif difficulty == 2:
            print('The chosen difficulty is: Easy')
            print('Generating...')
            time.sleep(2.5)
            return random.randint(1, (difficulty * 5))
        elif difficulty == 3:
            print('The chosen difficulty is: Medium')
            print('Generating...')
            time.sleep(2.5)
            return random.randint(1, (difficulty * 5))
        elif difficulty == 4:
            print('The chosen difficulty is: Hard')
            print('Generating...')
            time.sleep(2.5)
            return random.randint(1, (difficulty * 5))
        elif difficulty == 5:
            print('The chosen difficulty is: Very Hard')
            print('Generating...')
            time.sleep(2.5)
            return random.randint(1, (difficulty * 5))
        else:
            print('Unknown difficulty')


def get_guess_from_user(difficulty):

    rng = generate_number(difficulty)
    count = 0
    while True:
        count += 1
        guess = int(input(f'The number the computer is thinking about is between 1 and {difficulty * 5}'
                          f'\nCan you guess what it is?\n'))
        if int(count) >= 3:
            # print("\nWell, it seems you're out of attempts.")
            compare_results(guess, rng)
            return False

        if rng > guess:
            print('Nope. Maybe higher.')
        elif rng < guess:
            print('Nope. Maybe lower.')
        else:
            compare_results(guess, rng)
            return True


def compare_results(guess, rng):

    if guess == rng:
        print(f'You got it right. Good for you.\n')
        return True
    else:
        print('You got it wrong. You suck at this.\n')
        return False


def play(difficulty):
    if get_guess_from_user(difficulty):
        return True, play(difficulty) if input("Do you want to play again?"
                                               " [Enter 'Y' to play another round/"
                                               " Any other key to exit] ").lower() == 'y' else 0
    else:
        return False, play(difficulty) if input("Do you want to play again?"
                                                " [Enter 'Y' to play another round/"
                                                " Any other key to exit] ").lower() == 'y' else 0


def generate_number_h(difficulty):
    while True:
        if difficulty == 1:
            print('רמת הקושי שנבחרה היא: קל מאוד')
            print('מייצר...')
            time.sleep(2.5)
            return random.randint(1, (difficulty * 5))
        elif difficulty == 2:
            print('רמת הקושי שנבחרה היא: קל')
            print('מייצר...')
            time.sleep(2.5)
            return random.randint(1, (difficulty * 5))
        elif difficulty == 3:
            print('רמת הקושי שנבחרה היא: בינוני')
            print('מייצר...')
            time.sleep(2.5)
            return random.randint(1, (difficulty * 5))
        elif difficulty == 4:
            print('רמת הקושי שנבחרה היא: קשה')
            print('מייצר...')
            time.sleep(2.5)
            return random.randint(1, (difficulty * 5))
        elif difficulty == 5:
            print('רמת הקושי שנבחרה היא: קשה מאוד')
            print('מייצר...')
            time.sleep(2.5)
            return random.randint(1, (difficulty * 5))
        else:
            print('תקלה. רמת קושי לא מוכרת')


def get_guess_from_user_h(difficulty):

    rng = generate_number_h(difficulty)
    count = 0
    while True:
        count += 1
        guess = int(input(f'המספר שהמחשב חושב עליו הוא בין 1-{difficulty * 5}'
                          f'\nהאם את/ה מסוגל/ת לנחש את המספר?\n'))
        if int(count) >= 3:
            # print("\nWell, it seems you're out of attempts.")
            compare_results_h(guess, rng)
            return False

        if rng > guess:
            print('לא, נסי/ה גבוה יותר.')
        elif rng < guess:
            print('לא, נסי/ה נמוך יותר.')
        else:
            compare_results_h(guess, rng)
            return True


def compare_results_h(guess, rng):

    if guess == rng:
        print(f'ניחשת נכון. כל הכבוד.\n')
        return True
    else:
        print('לא ניחשת נכון.\n')
        return False


def play_h(difficulty):
    if get_guess_from_user_h(difficulty):
        return True, play_h(difficulty) if input('האם תרצי/ה לשחק בשנית? [כ/ כל מקש אחר ליציאה]\n') == 'כ' else 0
    else:
        return False, play_h(difficulty) if input('האם תרצי/ה לשחק בשנית? [כ/ כל מקש אחר ליציאה]\n') == 'כ' else 0
