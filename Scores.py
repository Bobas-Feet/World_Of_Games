from datetime import datetime
import os
from Utils import scores_file_name


def add_score(difficulty):

    now = datetime.now()
    today = now.strftime("%a, %B %d %Y, %H:%M")

    points_for_winning = (difficulty * 3) + 5

    if os.path.exists(points_for_winning):

        with open(points_for_winning, 'w+') as scores:
            scores_list = scores.readlines()
        scores_list = [int(x.strip()) for x in scores_list]
        current_score = sum(scores_list)

    else:
        current_score = 0
    update_score = current_score + points_for_winning
    with open(scores_file_name, 'w+') as scores:
        scores.write(str(f'{today} - Your score for winning on difficulty'
                         f' {difficulty} is - {update_score + points_for_winning}'))
        scores.write(f'\n')
    return update_score


        # try:
        #     score_file = open(f'{scores_file_name}Scores.txt', 'a+')
        #     score_file.write(f'{today} - Your Score for winning on difficulty {difficulty} is - {points_for_winning}')
        #     score_file.write(f'\n')
        #
        # except FileNotFoundError:
        #     score = open(f'{scores_file_name}/Scores.txt', 'x')
        #     score.write(f'{points_for_winning}')


def no_score(difficulty):
    now = datetime.now()
    today = now.strftime("%a, %B %d %Y, %H:%M")

    points_for_losing = (difficulty * 3) - 3
    file_path = 'C:/DevOps/WoG-project/'

    try:
        score_file = open(f'{file_path}Scores.txt', 'a+')
        score_file.write(f'{today} -\nYour Score after fucking up on difficulty {difficulty} is {points_for_losing}')
        score_file.write(f'\n')

    except FileNotFoundError:
        score = open(f'{file_path}/Scores.txt', 'x')
        score.write(f'{points_for_losing}')
