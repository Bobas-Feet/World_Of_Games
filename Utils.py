from os import system, name

Path = 'C:/DevOps/WoG (project)/'

# score_file_name = open(f'{Path}Scores.txt', 'w')

bad_return_code = int(401)


def screen_cleaner():
    if name == 'nt':
        _ = system('cls')

