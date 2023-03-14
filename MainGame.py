from Live import load_game, welcome, welcome_h


lang = int(input('Choose your language:\n1: English\n2: Hebrew\n'))

if int(lang) == 1:
    welcome()

    load_game()

elif lang == 2:

    welcome_h()


