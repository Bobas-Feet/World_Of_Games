from pathlib import Path

folder_Path = 'C:/DevOps/WoG (project)'
SCORES_FILE_NAME = open(f'{folder_Path}/Scores.txt', 'x')


BAD_RETURN_CODE = int(401)


def screen_cleaner():
    import os
    os.system('cls' if os.name == 'nt' else 'clear')

