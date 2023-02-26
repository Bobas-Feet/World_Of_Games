
def add_score(difficulty):
    # """
    # Adds a score to the Scores.txt file.
    # :param difficulty: The difficulty of the game.
    # """
    points_for_winning = str((difficulty * 3) + 5)
    file_path = 'C:/DevOps/WoG (project)'

    try:

        # score = open('C:/DevOps/WoG (project)/Scores.txt', 'w')
        score_file = open("Scores.txt", "w+")
        score_file.write(f"{points_for_winning}")
        score_file.read()
        score_file.close()

    except FileNotFoundError:
        score_file = open(f"{file_path}/Scores.txt", "x")
        score_file.write(points_for_winning)
