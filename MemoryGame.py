# 24/2/23

import random
import time


def generate_sequence(difficulty):

    try:
        if difficulty == '' or difficulty == ' ':
            print('Error. You must provide an answer.')
        difficulty = int(difficulty)

        rng = []
        for i in range(difficulty):
            rng.append(random.randint(1, 101))
        print(rng)

        time.sleep(0.7)
        for b in range(0, 5):
            print('')

        return rng

    except ValueError:
        print('Error')


def get_list_from_user(difficulty):

    n = []
    print(f"Let's begin the game. Insert {difficulty} numbers, one number at a time and press [ENTER]:")
    for i in range(difficulty):
        n.append(int(input('What numbers do you remember seeing in the sequence above? ')))

    return n


def is_list_equal(n, rng):

    n.sort()
    rng.sort()
    if rng == n:
        return True
    else:
        return False


def play(difficulty):

    rng = generate_sequence(difficulty)
    n = get_list_from_user(difficulty)
    is_list_equal(n, rng)
    if is_list_equal(n=n, rng=rng):
        print('Yay. You got all the answers right.')
        quit()
    else:
        print('Well, Fuck. You lost.')
        quit()
