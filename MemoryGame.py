import random
import time


def generate_sequence(difficulty):

    try:
        if difficulty == '' or difficulty == ' ':
            print('Error. You must provide an answer.')
        difficulty = int(difficulty)

        rng = []
        for i in range(1, difficulty + 1):
            rng.append(random.randint(1, 101))
        print(rng)

        time.sleep(0.7)
        for b in range(0, 10000):
            print('')

        return rng

    except ValueError:
        print('Error')


def get_list_from_user(difficulty):

    n = []
    print(f"Let's begin the game. Insert {difficulty} numbers, one number at a time and press [ENTER]:")
    for i in range(difficulty):
        n.append(int(input('What numbers do you remember seeing in the sequence above? ')))

    return n


def is_list_equal(n, rng):

    n.sort()
    rng.sort()
    if rng == n:
        return True
    else:
        return False


def play(difficulty):

    rng = generate_sequence(difficulty)
    n = get_list_from_user(difficulty)

    if is_list_equal(n=n, rng=rng):
        print('Yay. You got all the answers right.\n')
        return True, play(difficulty) if input("Do you want to play again?"
                                               " [Enter 'Y' to play another round/"
                                               " Any other key to exit] ").lower() == 'y' else 0
    else:
        print('Well, Fuck. You lost.\n')
        return False, play(difficulty) if input("Do you want to play again?"
                                                " [Enter 'Y' to play another round/"
                                                " Any other key to exit] ").lower() == 'y' else 0


def generate_sequence_h(difficulty):

    try:
        if difficulty == '' or difficulty == ' ':
            print('תקלה. יש להזין בחירה.')
        difficulty = int(difficulty)

        rng = []
        for i in range(1, difficulty + 1):
            rng.append(random.randint(1, 101))
        print(rng)

        time.sleep(0.7)
        for b in range(0, 10000):
            print('')

        return rng

    except ValueError:
        print('תקלה.')


def get_list_from_user_h(difficulty):

    n = []
    print('הבה נתחיל. עליך להזין', difficulty, 'מספרים לפי הסדר שהופיעו.')
    for i in range(difficulty):
        n.append(int(input('האם את/ה זוכר/ת את כל המספרים שהופיעו?\n')))

    return n


def is_list_equal_h(n, rng):

    n.sort()
    rng.sort()
    if rng == n:
        return True
    else:
        return False


def play_h(difficulty):

    rng = generate_sequence_h(difficulty)
    n = get_list_from_user_h(difficulty)

    if is_list_equal_h(n=n, rng=rng):
        print('כל הכבוד, כל התשובות היו נכונות וניצחת במשחק.\n')
        return True, play_h(difficulty) if input('האם תרצי/ה לשחק בשנית? [כ/ כל מקש אחר ליציאה]\n') == 'כ' else 0
    else:
        print('ובכן, הפסדת.\n')
        return False, play_h(difficulty) if input('האם תרצי/ה לשחק בשנית? [כ/ כל מקש אחר ליציאה]\n') == 'כ' else 0

