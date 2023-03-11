from pathlib import Path


def add_score(difficulty):

    points_for_winning = str((difficulty * 3) + 5)
    file_path = 'C:/DevOps/WoG (project)/'

    try:
        score_file = open(f'{file_path}Scores.txt', 'a')

        score_file.write(f'Your Score for playing on difficulty {difficulty} is {points_for_winning}')
        score_file.write(f'\n')

    except FileNotFoundError:
        score = open(f'{file_path}/Scores.txt', 'x')
        score.write(f'{points_for_winning}')

