from Live import load_game, welcome, welcome_h, load_game_h

while True:

    try:
        lang = int(input('Choose language to play:\n1: English\n2: Hebrew\n'))

        if int(lang) == 1:
            welcome()
            load_game()

        elif int(lang) == 2:
            welcome_h()
            load_game_h()

        else:
            print('You can only choose one or the other.\n')
            continue

    except ValueError:
        print('You can only choose one or the other.\n')
    except KeyboardInterrupt:
        print('\nGoodbye, we hope to see you again.')
