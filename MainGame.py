from Live import load_game, welcome, welcome_h, load_game_h

while True:

    try:
        lang = int(input('Choose your language:\n1: English\n2: Hebrew\n'))

        if int(lang) == 1:
            welcome()
            load_game()

        elif lang == 2:
            welcome_h()
            load_game_h()

        else:
            print('You must choose correctly.\n')
            continue

    except ValueError:
        print('You must choose correctly.\n')
