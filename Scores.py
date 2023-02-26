from pathlib import Path


def add_score(difficulty):

    points_for_winning = str((difficulty * 3) + 5)
    file_path = 'C:/DevOps/WoG (project)/'
    try:
        score_file = open(Path('Scores.txt'), 'r')
        score = open(Path('Scores.txt'), 'a')
        score.write(points_for_winning)
        if score_file.read() == 'r':
            contents = score_file.read()
            print(contents)

    except FileNotFoundError:
        scores_file_name = open(f'{file_path}/Scores.txt', 'x')
        scores_file_name.write(points_for_winning)

    if __name__ == '__main__':
        print(f'Score: {points_for_winning}')
