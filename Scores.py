
def add_score(difficulty):

    # Adds a score to the Scores.txt file.
    # :param difficulty: The difficulty of the game.

    points_for_winning = str((difficulty * 3) + 5)
    file_path = 'C:/DevOps/WoG (project)/'

    try:

        # score = open('C:/DevOps/WoG (project)/Scores.txt', 'w')
        score_file = open("Scores.txt", "x")
        # score_file = open("Scores.txt", "w+")
        score_file.write(points_for_winning)

        score_file = open("Scores.txt", "r")
        if score_file.read() == "r":
            contents = score_file.read()
            print(contents)

    except FileNotFoundError:
        score_file = open(f"{file_path}/Scores.txt", "x")
        score_file.write(points_for_winning)

    if __name__ == "__main__":
        score_file.close()
        print(f"Score: {points_for_winning}")
