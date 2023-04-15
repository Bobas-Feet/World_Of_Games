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
    updated_score = current_score + points_for_winning
    with open(scores_file_name, 'w+') as scores:
        scores.write(str(f'{updated_score}'))
        scores.write(f'\n')
    return updated_score


def no_score(difficulty):
    now = datetime.now()
    today = now.strftime("%a, %B %d %Y, %H:%M")

    points_for_losing = (difficulty * 3) - 3
    # file_path = 'C:/DevOps/WoG-project/txt-files/Scores.txt'
    if os.path.exists(points_for_losing):
        with open(points_for_losing, 'w+') as scores:
            scores_list = scores.readlines()
        scores_list = [int(x.strip()) for x in scores_list]
        current_score = sum(scores_list)

    else:
        current_score = 0
    updated_score = current_score + points_for_losing
    with open(scores_file_name, 'w+') as scores:
        scores.write(str(f'{updated_score}'))
        scores.write(f'\n')
    return updated_score

    # try:
    #     score_file = open('Scores.txt', 'w+')
    #     score_file.write(f'{points_for_losing}')
    #     score_file.write(f'\n')
    #
    # except FileNotFoundError:
    #     score = open(f'Scores.txt', 'x')
    #     score.write(f'{points_for_losing}')
