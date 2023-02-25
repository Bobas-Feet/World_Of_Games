# 24/2/2023

import GuessGame
import MemoryGame
import CurrencyRouletteGame


def welcome():
    name = input('What is your name? [You may use only letters,'
                 '\n no numbers or special symbols (!@#$%^) and no spaces] ')

    try:
        if any([i > 'z' or i < 'a' for i in name]):
            print("Error. Contains illegal characters")
            welcome()
        elif name == '' or name == ' ':
            print('Error. No blanks')
            welcome()
        elif 3 >= len(name) >= 15:
            print('Error. Username either too long or too short')
            welcome()
        else:
            print(f'Welcome {name}, to the World of Games (WoG).'
                  f' Here you can play many cool games')
            pass

    except ValueError:
        print('invalid')


def load_game():
    game1 = 'The Memory Game'
    game2 = 'The Guessing Game'
    game3 = 'The Currency Roulette Game'

    while True:
        try:
            g = int(input('What game would you like to play? [1/2/3] '))

            if int(g) == 1:
                print(f'{game1}: A sequence of numbers will appear for 1 second, and you have'
                      f' to guess it back.')
                difficulty = int(input('What difficulty would you like to play? [1/2/3/4/5] '))
                MemoryGame.play(difficulty)

            if int(g) == 2:
                print(f'{game2}: Guess a number and see if you chose'
                      f' like the computer.')
                difficulty = int(input('What difficulty would you like to play? [1/2/3/4/5] '))
                GuessGame.play(difficulty)

            if int(g) == 3:
                print(f'{game3}: Try and guess the value of a random'
                      f' amount of USD in ILS.')
                difficulty = int(input('What difficulty would you like to play? [1/2/3/4/5] '))
                CurrencyRouletteGame.play(difficulty)

        except ValueError:
            print('Invalid input. You can only enter numbers')
