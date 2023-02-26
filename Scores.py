from Utils import user_score


def add_score(difficulty):

    points_for_winning = str((difficulty * 3) + 5)
    user_score(points_for_winning)
    print(f"Score: {points_for_winning}")


    # file_path = 'C:/DevOps/WoG (project)/'
    # try:
    #     # score = open('C:/DevOps/WoG (project)/Scores.txt', 'w')
    #     # score_file = open("Scores.txt", "x")
    #     scores_file_name = open("Scores.txt", "w+")
    #     scores_file_name.write(points_for_winning)
    #
    #     scores_file_name = open("Scores.txt", "r")
    #     if scores_file_name.read() == "r":
    #         contents = scores_file_name.read()
    #         print(contents)
    #
    # except FileNotFoundError:
    #     scores_file_name = open(f"{file_path}/Scores.txt", "x")
    #     scores_file_name.write(points_for_winning)

    if __name__ == "__main__":
        print(f"Score: {points_for_winning}")
