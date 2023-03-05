import random


def generate_number(difficulty):
    secret_number = random.randint(1, int(difficulty) + 3)

    return secret_number


def get_guess_from_user(difficulty, secret_number):

    count = 0
    while difficulty != secret_number:
        count += 1
        guess = int(input('Now, try and guess the number that the computer is thinking about... '))

        if int(count) >= 3:
            print("Nope. You're out of attempts.")
            quit()
        else:
            pass

        if guess < secret_number:
            print('Nope. Maybe higher...?')
        elif guess > secret_number:
            print('Nope. Maybe lower...?')
        else:
            print(f'Congratulations, You got it right in attempt #{count}.')
            quit()


def compare_results(guess, secret_number):
    compare_guess = guess == secret_number
    if compare_guess is True:
        print('You win')
    else:
        print('You lose')
    quit()
    return guess == secret_number


def play(difficulty):
    secret = generate_number(difficulty)
    if compare_results(generate_number(difficulty), get_guess_from_user(difficulty, secret)):
        return True
    else:
        return False
