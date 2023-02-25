from pathlib import Path


def add_score(difficulty):
    points_for_winning = str((difficulty * 3) + 5)
    file_path = 'C:/DevOps/WoG (project)/'
    try:
        # score_file = open('C:/DevOps/WoG (project)/Scores.txt', 'w')
        score_file = open(f"{file_path} Scores.txt", "a")
        score_file.write(f" ,{points_for_winning}")
        score_file.read()
        score_file.close()
    except FileNotFoundError:
        score_file = open("C:/DevOps/WoG (project)/Scores.txt", "x")
        score_file.write(points_for_winning)
