# from pathlib import Path


def user_score(points_for_winning):
    scores_file_name = open('Scores.txt', 'w+')
    scores_file_name.write(points_for_winning)
    scores_file_name.close()

    scores_file_name = open('Scores.txt', 'r+')
    scores = scores_file_name.read()
    scores_file_name.close()
    return scores


bad_return_code = int(401)


def screen_cleaner():
    import os
    os.system('cls' if os.name == 'nt' else 'clear')

