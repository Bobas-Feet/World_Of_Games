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


def welcome_h():
    try:
        name = input('שלום, מה שמך? '
                     '[שם המשתמש מוכרך להיות באותיות בלבד, ללא רווחים וסימנים מיוחדים, ובין 2-15 תווים.]\n')

        if any([i > 'ת' or i < 'א' for i in name]):
            print('תקלה. מכיל סימנים לא חוקיים.\n')
            return welcome_h()
        if len(name) > 15 or len(name) < 2:
            print('תקלה. שם המשתמש ארוך או קצר מידי.\n')
            return welcome_h()
        elif name == '' or name == ' ':
            print('תקלה. לא ניתן להשאיר שדה זה ריק.\n')
            return welcome_h()
        else:
            print('ברוכים הבאים, ' + '[' + name + ']' + ' לעולם המשחקים (WoG).\n'
                                                        'כאן תוכל/י לשחק במשחקים נפלאים ומאתגרים.')

    except ValueError:
        print('הזנה לא חוקית.')


def load_game_h():
    game1 = 'משחק הזיכרון'
    game2 = 'משחק הניחושים'
    game3 = 'משחק רולטה מט"ח'

    while True:
        try:
            g = int(input(f'\nאנא בחר/י משחק:\n'
                          f'\n 1: משחק הזיכרון  \n2: משחק הניחושים  '
                          f'\n3: משחק רולטה מט"ח\n\nאו [0] ליציאה     \n'))

            if int(g) == 1:
                print(f'{game1}: רצף של מספרים רנדומליים יופיעו ל-1 שניות, והמשתמש/ת צריך להזין את הרצף כפי שהופיע.')
                difficulty = int(input('באיזה רמת קושי תרצי/ה לשחק? [1/2/3/4/5]\n'))
                if difficulty not in range(1, 6):
                    print('האפשרויות היחידות שלך הן [1/2/3/4/5]')
                elif bool(MemoryGame.play_h(difficulty)) is True:
                    add_score(difficulty=difficulty)
                    MainScores.app.run(difficulty=difficulty)

            if int(g) == 2:
                print(f'{game2}: משחק אשר צריך לנחש מספר רנדומלי שנוצר על ידי המחשב.')
                difficulty = int(input('באיזה רמת קושי תרצי/ה לשחק? [1/2/3/4/5]\n'))
                if difficulty not in range(1, 6):
                    print('האפשרויות היחידות שלך הן [1/2/3/4/5]')
                elif bool(GuessGame.play_h(difficulty)) is True:
                    add_score(difficulty=difficulty)
                    MainScores.app.run(difficulty=difficulty)

            if int(g) == 3:
                print(f'{game3}: נסי/ה לחשב את ערך ההמרה בין דולר לש"ח, '
                      f'כאשר המשתמש/ת מקבלים סכום רנדומלי שנוצר ע"י המחשב.')
                difficulty = int(input('באיזה רמת קושי תרצי/ה לשחק? [1/2/3/4/5]\n'))
                if difficulty not in range(1, 6):
                    print('האפשרויות היחידות שלך הן [1/2/3/4/5]')
                elif bool(CurrencyRouletteGame.play_h(difficulty)) is True:
                    add_score(difficulty=difficulty)
                    MainScores.app.run(difficulty=difficulty)

            while int(g) == 0:
                quit_game = input('האם אתה בטוח שאת/ה רוצה לצאת? [כ/ל]\n').lower()
                if quit_game == 'כ':
                    print('להתראות. נשמח לראותך שוב.')
                    quit()
                elif quit_game == 'ל':
                    load_game_h()
                else:
                    continue

        except ValueError:
            print('הנזה לא חוקית, ניתן להזין רק מספרים.')
        except KeyboardInterrupt:
            print('\n.להתראות. נשמח לראותך שוב.')
            quit()


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
                    add_score(difficulty=difficulty)
                    MainScores.app.run()

            if int(g) == 2:
                print(f'{game2}: A numbers guessing game in which you need to guess the number that'
                      f'\nwas generated randomly by the computer.')
                difficulty = int(input('What difficulty would you like to play? [1/2/3/4/5]\n'))
                if difficulty not in range(1, 6):
                    print('Your only options here are [1/2/3/4/5]')
                elif bool(GuessGame.play(difficulty)) is True:
                    add_score(difficulty=difficulty)
                    MainScores.app.run()

            if int(g) == 3:
                print(f'{game3}: Try and guess the value of a random'
                      f' amount of USD in ILS.')
                difficulty = int(input('What difficulty would you like to play? [1/2/3/4/5]\n'))
                if difficulty not in range(1, 6):
                    print('Your only options here are [1/2/3/4/5]')
                elif bool(CurrencyRouletteGame.play(difficulty)) is True:
                    add_score(difficulty=difficulty)
                    MainScores.app.run()

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


