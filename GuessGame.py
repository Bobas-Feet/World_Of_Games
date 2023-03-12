import random
import time


def generate_number(difficulty):

    while True:
        if difficulty == 1:
            print('Very Easy')
            print('Generating...')
            time.sleep(2.5)
            return random.randint(1, (difficulty * 5))
        elif difficulty == 2:
            print('Easy')
            print('Generating...')
            time.sleep(2.5)
            return random.randint(1, (difficulty * 5))
        elif difficulty == 3:
            print('Medium')
            print('Generating...')
            time.sleep(2.5)
            return random.randint(1, (difficulty * 5))
        elif difficulty == 4:
            print('Hard')
            print('Generating...')
            time.sleep(2.5)
            return random.randint(1, (difficulty * 5))
        elif difficulty == 5:
            print('Very Hard')
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
        guess = int(input(f'The number the computer is thinking about is between 1 and {difficulty * 5}.'
                          f'\nCan you guess what it is? '))
        if int(count) > 3:
            print("Well, it seems you're out of attempts.")
            compare_results(guess, rng)
            return False

        if rng > guess:
            print('Nope. Maybe higher.')
        elif rng < guess:
            print('Nope. Maybe lower.')
        else:
            compare_results(guess, rng)
            return True
    # return play(difficulty) if input('Do you want to play again? [y/ Any key to exit] ').lower() == 'y' else 0


def compare_results(guess, rng):

    if guess == rng:
        print(f'You got it right. Good for you.\n')
        return True
    else:
        print('You got it wrong. You suck at this.\n')
        return False


def play(difficulty):
    if get_guess_from_user(difficulty):
        return True
    else:
        return False
