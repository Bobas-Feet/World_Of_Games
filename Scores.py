from pathlib import Path


def add_score(difficulty):

    points_for_winning = str((difficulty * 3) + 5)
    file_path = 'C:/DevOps/WoG (project)/'
    print(file_path)

    try:
        score_file = open('C:/DevOps/WoG (project)/Scores.txt', 'w')
        # score = open(Path('Scores.txt'), 'a')
        score_file.write(f'{points_for_winning}')
        # if score_file.read() == 'r':
        #     contents = score_file.read()
        #     print(contents)

    except FileNotFoundError:
        score = open(f'{file_path}/Scores.txt', 'x')
        score.write(points_for_winning)

