
# docker build -t wog:latest .

# This section imports the necessary modules and defines some constants
import os
import time

# some variables that I store my paths for the files in order to be used in the program in different modules
scores_file_name = './Scoreboard/Scores.txt'
scores_file_name_lose = './Scoreboard/Scores_lose.txt'
scores_file_flask = "./Scoreboard/Scores.txt"
scores_file_flask_lose = "./Scoreboard/Scores_lose.txt"
last_scores = "./Scoreboard/Last_scores.txt"
last_scores_flask = "./Scoreboard/Last_scores.txt"
bad_return_code = "ERROR CODE 214"


def screen_cleaner():

    time.sleep(0.85)
    if os.name == 'nt':          # Check if the OS is Windows
        os.system('cls')         # Clear the screen using "cls" command
    else:                        # if the if block its not returning True then it will use it for linux
        os.system('clear')       # Clear the screen using "clear" command


# This function reads the contents of a source file, writes them to a destination file, and then clears the source file
def transfer_and_clear_file(src_file, cp_file):
    with open(src_file, 'r') as scores:         # Open the source file
        current_score = scores.read().strip()   # Read the contents and remove any whitespace

    with open(cp_file, 'w') as scores:          # Open the destination file
        scores.write(current_score)             # Write the contents of the source file to the destination file

    with open(src_file, 'w') as scores:         # Open the source file again
        scores.write('')                        # Clear the contents of the source file
