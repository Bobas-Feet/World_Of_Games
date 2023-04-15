from Live import load_game, welcome, welcome_h, load_game_h

while True:

    try:
        lang = int(input('Choose your language:\n1: English\n2: Hebrew\n'))

        if int(lang) == 1:
            username = welcome()
            load_game(username)

        elif lang == 2:
            username2 = welcome_h()
            load_game_h(username2)

        else:
            print('You can only choose one or the other.\n')
            continue

    except ValueError:
        print('You can only choose one or the other.\n')
    except KeyboardInterrupt:
        print('\nGoodbye, we hope to see you again.')
