from Games import GuessGame, MemoryGame, CurrencyRouletteGame
# from Scores import add_score
from Utils import screen_cleaner
import MainScores
# from e2e import main_function


def welcome():
    try:
        username = input('Greetings Newcomer, what is your name? '
                         '[Username must be 3-15 characters, only letters allowed.]\n')

        with open('C:/DevOps/WoG-project/txt-files/name.txt', 'w+') as user_name_file:
            user_name_file.write(f'{username}')

        if any([i > 'z' or i < 'a' for i in username]):
            print('Error. Contains illegal characters.\n')
            return welcome()
        elif len(username) > 15 or len(username) < 3:
            print('Error. Username either too long or too short.\n')
            return welcome()
        elif username == '' or username == ' ':
            print('Error. You cannot leave this field empty.\n')
            return welcome()
        else:
            print(f'Welcome [{username}], to the World of Games-(WoG).'
                  f' Here you can play many cool games.')

    except ValueError:
        print('invalid input.')


def welcome_h():

    try:
        username2 = input('שלום, מה שמך? '
                          '[שם המשתמש מוכרך להיות באותיות בלבד, ללא רווחים וסימנים מיוחדים, ובין 2-15 תווים.]\n')

        if any([i > 'ת' or i < 'א' for i in username2]):
            print('שגיאה. מכיל סימנים לא חוקיים.\n')
            return welcome_h()
        if len(username2) > 15 or len(username2) < 2:
            print('שגיאה. שם המשתמש ארוך או קצר מידי.\n')
            return welcome_h()
        elif username2 == '' or username2 == ' ':
            print('שגיאה. לא ניתן להשאיר שדה זה ריק.\n')
            return welcome_h()

        else:
            print('ברוכים הבאים, ' + '[' + username2 + ']' + ' לעולם המשחקים (WoG).\n'
                                                             'כאן תוכל/י לשחק במשחקים נפלאים ומאתגרים.')
        # with open('C:/DevOps/WoG-project/txt-files/name.txt', 'w+') as user_name_file:
        #     user_name_file.write(f'{username2}')

    except ValueError:
        print('שגיאה. משהו פה לא בסדר...')


def load_game_h():
    game1 = 'משחק הזיכרון'
    game2 = 'משחק הניחושים'
    game3 = 'משחק רולטה מט"ח'

    while True:
        try:
            g = int(input(f'\nאנא בחר/י משחק:   \n'
                          f'\n 1: משחק הזיכרון  \n2: משחק הניחושים  '
                          f'\n3: משחק רולטה מט"ח\n\nאו [0] ליציאה     \n'))

            if int(g) == 1:
                print('================================================================'
                      '=================================')
                print(f'{game1}: רצף של מספרים רנדומליים יופיעו ל-1 שניות, והמשתמש/ת צריך להזין את הרצף כפי שהופיע.')
                print('================================================================'
                      '=================================')
                difficulty = int(input('באיזה רמת קושי תרצי/ה לשחק? [1/2/3/4/5]\n'))
                if difficulty not in range(1, 6):
                    print('האפשרויות היחידות שלך הן [1/2/3/4/5]')
                    continue
                else:
                    MemoryGame.play_h(difficulty)
                    MainScores.app.run(host=MainScores.host, debug=MainScores.debug, port=MainScores.port)
                    # main_function()

            if int(g) == 2:
                print('==================================================='
                      '===============')
                print(f'{game2}: משחק אשר צריך לנחש מספר רנדומלי שנוצר על ידי המחשב.')
                print('==================================================='
                      '===============')
                difficulty = int(input('באיזה רמת קושי תרצי/ה לשחק? [1/2/3/4/5]\n'))
                if difficulty not in range(1, 6):
                    print('האפשרויות היחידות שלך הן [1/2/3/4/5]')
                    continue
                else:
                    GuessGame.play_h(difficulty)
                    MainScores.app.run(host=MainScores.host, debug=MainScores.debug, port=MainScores.port)
                    # main_function()

            if int(g) == 3:
                print(f'===================================================================='
                      f'\n{game3}: נסי/ה לחשב את ערך ההמרה לפי שער החליפין העדכני,\nבין דולר לש"ח, '
                      f'כאשר המשתמש/ת מקבל/ת סכום רנדומלי שנוצר ע"י המחשב.')
                print('====================================================================')
                difficulty = int(input('באיזה רמת קושי תרצי/ה לשחק? [1/2/3/4/5]\n'))
                if difficulty not in range(1, 6):
                    print('האפשרויות היחידות שלך הן [1/2/3/4/5]')
                    continue
                else:
                    CurrencyRouletteGame.play_h(difficulty)
                    MainScores.app.run(host=MainScores.host, debug=MainScores.debug, port=MainScores.port)
                    # main_function()

            while int(g) == 0:
                quit_game = input('האם אתה בטוח שאת/ה רוצה לצאת? [כ/ל]\n').lower()
                if quit_game == 'כ':
                    print('להתראות. נשמח לראותך שוב.')
                    screen_cleaner()
                    quit()
                elif quit_game == 'ל':
                    load_game_h()
                else:
                    continue

        except ValueError:
            print('שגיאה, ניתן להזין רק מספרים.')
        except KeyboardInterrupt:
            print('\nלהתראות. נשמח לראותך שוב.')
            screen_cleaner()
            quit()


def load_game():

    game1 = 'The Memory Game'
    game2 = 'The Guessing Game'
    game3 = 'The Currency Roulette Game'

    while True:
        try:
            g = int(input(f'===============================\nChoose a game to play:\n-------------------------------'
                          f'\n1: The Memory Game\n-------------------------------\n2: The Guessing Game'
                          f'\n-------------------------------\n3: The Currency Roulette Game\n'
                          f'-------------------------------\nOr [0] to exit\n===============================\n'
                          f'Please enter your decision here: '))

            if int(g) == 1:
                print(f'================================================================'
                      f'\n{game1}: A sequence of numbers will appear for 1 second, \nand you need'
                      f' to recall what the sequence of numbers was.\n'
                      f'================================================================')
                difficulty = int(input('What difficulty would you like to play? [1/2/3/4/5]\n'))
                if difficulty not in range(1, 6):
                    print('Your only options here are [1/2/3/4/5]')
                else:
                    MemoryGame.play(difficulty)
                    MainScores.app.run(host=MainScores.host, debug=MainScores.debug, port=MainScores.port)
                    # main_function()

            if int(g) == 2:
                print(f'===================================='
                      f'=================================================='
                      f'\n{game2}: A numbers guessing game in which you need to guess the number that'
                      f'\nwas generated randomly by the computer.\n'
                      f'===================================='
                      f'==================================================')
                difficulty = int(input('What difficulty would you like to play? [1/2/3/4/5]\n'))
                if difficulty not in range(1, 6):
                    print('Your only options here are [1/2/3/4/5]')
                else:
                    GuessGame.play(difficulty)
                    MainScores.app.run(host=MainScores.host, debug=MainScores.debug, port=MainScores.port)
                    # main_function()

            if int(g) == 3:
                print(f'====================================================================================='
                      f'\n{game3}: Try and guess the value of a random'
                      f' amount of USD in ILS.\n'
                      f'=====================================================================================')
                difficulty = int(input('What difficulty would you like to play? [1/2/3/4/5]\n'))
                if difficulty not in range(1, 6):
                    print('Your only options here are [1/2/3/4/5]')
                else:
                    CurrencyRouletteGame.play(difficulty)
                    MainScores.app.run(host=MainScores.host, debug=MainScores.debug, port=MainScores.port)
                    # main_function()

            while int(g) == 0:
                quit_game = input('Are you sure you want to quit? [y/n]\n').lower()
                if quit_game == 'y':
                    print('Goodbye, we hope to see you again.')
                    screen_cleaner()
                    quit()
                elif quit_game == 'n':
                    load_game()
                else:
                    continue

        except ValueError:
            print('Invalid input. You can only enter numbers')
        except KeyboardInterrupt:
            print('\nGoodbye, we hope to see you again.')
            screen_cleaner()
            quit()
