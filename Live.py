import GuessGame
import MemoryGame
import CurrencyRouletteGame
from Scores import add_score


def welcome():
    name = input('What is your name? [You may use only letters,'
                 '\nno numbers or special symbols (!@#$%^) and no spaces] ').lower()

    try:
        if any([i > 'z' or i < 'a' for i in name]):
            print("Error. Contains illegal characters")
            return welcome()
        elif name == '' or name == ' ':
            print('Error. You cannot leave this field empty.')
            return welcome()
        elif 3 < len(name) > 15:
            print('Error. Username either too long or too short')
            return welcome()
        else:
            print(f'Welcome {name}, to the World of Games (WoG).'
                  f' Here you can play many cool games')

    except ValueError:
        print('invalid')


def load_game():
    game1 = 'The Memory Game'
    game2 = 'The Guessing Game'
    game3 = 'The Currency Roulette Game'

    while True:
        try:
            g = int(input('Choose a game to play'
                          '\n1: The Memory Game\n2: The Guessing Game\n3: The Currency Roulette Game \n'))

            if int(g) == 1:
                print(f'{game1}: A sequence of numbers will appear for 1 second, and you need'
                      f' to recall what the sequence of numbers was.')
                difficulty = int(input('What difficulty would you like to play? [1/2/3/4/5] '))
                if difficulty not in range(1, 6):
                    print('Your only options here are [1/2/3/4/5]')
                elif bool(MemoryGame.play(difficulty)) is True:
                    add_score(difficulty=difficulty)

            if int(g) == 2:
                print(f'{game2}: A numbers guessing game in which you need to guess the number that'
                      f'\nwas generated randomly by the computer.')
                difficulty = int(input('What difficulty would you like to play? [1/2/3/4/5] '))
                if difficulty not in range(1, 6):
                    print('Your only options here are [1/2/3/4/5]')
                elif bool(GuessGame.play(difficulty)) is True:
                    add_score(difficulty=difficulty)

            if int(g) == 3:
                print(f'{game3}: Try and guess the value of a random'
                      f' amount of USD in ILS.')
                difficulty = int(input('What difficulty would you like to play? [1/2/3/4/5] '))
                if difficulty not in range(1, 6):
                    print('Your only options here are [1/2/3/4/5]')
                elif bool(CurrencyRouletteGame.play(difficulty)) is True:
                    add_score(difficulty=difficulty)

        except ValueError:
            print('Invalid input. You can only enter numbers')
        except KeyboardInterrupt:
            print('\nGoodbye, we hope to see you again.')
            quit()
