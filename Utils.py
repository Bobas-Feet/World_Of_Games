from pathlib import Path

score_file_name = open(Path('score.txt'), 'x')

bad_return_code = int(401)


def screen_cleaner():
    import os
    os.system('cls' if os.name == 'nt' else 'clear')

