from pathlib import Path


def add_score(difficulty):
    points_for_winning = str((difficulty * 3) + 5)
    try:
        score_file = open(Path("Scores.txt"), "r")
        score = open(Path("Scores.txt"), "a")
        score.write(f" ,{points_for_winning}")
    except FileNotFoundError:
        score = open(Path("Scores.txt"), "x")
        score.write(points_for_winning)

