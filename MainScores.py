import os
from flask import Flask, render_template, redirect, url_for, request
from Utils import bad_return_code, last_scores_flask, scores_file_flask, scores_file_flask_lose


WoG = Flask(__name__)


@WoG.route('/')
def score_server():

    file_path = 'C:/DevOps/WoG-project/Scoreboard/'
    with open(f'{file_path}name.txt', 'r+') as file:
        username = file.read()

    if os.path.exists(scores_file_flask):
        with open(scores_file_flask, 'r') as scores_file:
            score = scores_file.readline().strip()
            return render_template('WoG-Scores.html', score=score, username=username)

    else:
        return render_template('errors.html')


host = os.environ.get('FLASK_RUN_HOST', '0.0.0.0')
port = int(os.environ.get('FLASK_RUN_PORT', 5000))
debug = os.environ.get('FLASK_DEBUG', 'False').lower() == 'true'

if __name__ == '__main__':
    WoG.run(host='0.0.0.0', debug=True, port=int('5000'))


WoG2 = Flask(__name__)


@WoG2.route('/')
def score_server_lose():

    file_path = 'C:/DevOps/WoG-project/Scoreboard/'
    with open(f'{file_path}name.txt', 'r+') as file:
        username = file.read()

    if os.path.exists(scores_file_flask_lose):
        with open(scores_file_flask_lose, 'r') as scores_file_lose:
            losing_score = scores_file_lose.readline().strip()
        return render_template('WoG-Scores-lose.html', score=losing_score, username=username)

    else:
        return render_template('error.html')


host = os.environ.get('FLASK_RUN_HOST', '0.0.0.0')
port = int(os.environ.get('FLASK_RUN_PORT', 5000))
debug = os.environ.get('FLASK_DEBUG', 'False').lower() == 'true'

if __name__ == '__main__':
    WoG.run(host='0.0.0.0', debug=True, port=int('5000'))


