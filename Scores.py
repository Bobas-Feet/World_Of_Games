from datetime import datetime


def add_score(difficulty):

    now = datetime.now()
    today = now.strftime("%a, %B %d %Y, %H:%M")

    points_for_winning = str((difficulty * 3) + 5)
    file_path = 'C:/DevOps/WoG-project/'

    try:
        score_file = open(f'{file_path}Scores.txt', 'a+')
        score_file.write(f'{today} - Your Score for winning on difficulty {difficulty} is - {points_for_winning}')
        score_file.write(f'\n')

    except FileNotFoundError:
        score = open(f'{file_path}/Scores.txt', 'x')
        score.write(f'{points_for_winning}')


def no_score(difficulty):
    now = datetime.now()
    today = now.strftime("%a, %B %d %Y, %H:%M")

    points_for_losing = str((difficulty * 3) - 3)
    file_path = 'C:/DevOps/WoG-project/'

    try:
        score_file = open(f'{file_path}Scores.txt', 'a+')
        score_file.write(f'{today} -\nYour Score after fucking up on difficulty {difficulty} is {points_for_losing}')
        score_file.write(f'\n')

    except FileNotFoundError:
        score = open(f'{file_path}/Scores.txt', 'x')
        score.write(f'{points_for_losing}')
