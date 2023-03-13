import GuessGame
import MemoryGame
import CurrencyRouletteGame
from Scores import add_score
# from Utils import screen_cleaner
import MainScores


def welcome():
    try:
        name = input('Greetings Newcomer, what is your name? '
                     '[Username must be 3-15 characters, only letters allowed.]\n')

        if any([i > 'z' or i < 'a' for i in name]):
            print('Error. Contains illegal characters.\n')
            return welcome()
        elif len(name) > 15 or len(name) < 3:
            print('Error. Username either too long or too short.\n')
            return welcome()
        elif name == '' or name == ' ':
            print('Error. You cannot leave this field empty.\n')
            return welcome()
        else:
            print(f'Welcome [{name}], to the World of Games-(WoG).'
                  f' Here you can play many cool games.')

    except ValueError:
        print('invalid input.')


def load_game():
    game1 = 'The Memory Game'
    game2 = 'The Guessing Game'
    game3 = 'The Currency Roulette Game'

    while True:
        try:
            g = int(input(f'\nChoose a game to play:\n'
                          f'\n1: The Memory Game\n2: The Guessing Game'
                          f'\n3: The Currency Roulette Game \n\nOr [0] to exit\n'))

            if int(g) == 1:
                print(f'{game1}: A sequence of numbers will appear for 1 second, and you need'
                      f' to recall what the sequence of numbers was.')
                difficulty = int(input('What difficulty would you like to play? [1/2/3/4/5]\n'))
                if difficulty not in range(1, 6):
                    print('Your only options here are [1/2/3/4/5]')
                elif bool(MemoryGame.play(difficulty)) is True:
                    # add_score(difficulty=difficulty)
                    MainScores.app.run(difficulty=difficulty)

            if int(g) == 2:
                print(f'{game2}: A numbers guessing game in which you need to guess the number that'
                      f'\nwas generated randomly by the computer.')
                difficulty = int(input('What difficulty would you like to play? [1/2/3/4/5]\n'))
                if difficulty not in range(1, 6):
                    print('Your only options here are [1/2/3/4/5]')
                elif bool(GuessGame.play(difficulty)) is True:
                    # add_score(difficulty=difficulty)
                    MainScores.score_server(difficulty=difficulty)

            if int(g) == 3:
                print(f'{game3}: Try and guess the value of a random'
                      f' amount of USD in ILS.')
                difficulty = int(input('What difficulty would you like to play? [1/2/3/4/5]\n'))
                if difficulty not in range(1, 6):
                    print('Your only options here are [1/2/3/4/5]')
                elif bool(CurrencyRouletteGame.play(difficulty)) is True:
                    # add_score(difficulty=difficulty)
                    MainScores.score_server(difficulty=difficulty)

            while int(g) == 0:
                quit_game = input('Are you sure you want to quit? [y/n]\n').lower()
                if quit_game == 'y':
                    print('Goodbye, we hope to see you again.')
                    quit()
                elif quit_game == 'n':
                    load_game()
                else:
                    continue

        except ValueError:
            print('Invalid input. You can only enter numbers')
        except KeyboardInterrupt:
            print('\nGoodbye, we hope to see you again.')
            quit()
