import os
from flask import Flask, render_template, redirect, url_for, request
from App import AppScore
from Utils import bad_return_code, last_scores_flask, scores_file_flask
from e2e import main_function

app = Flask(__name__)


@app.route('/')
def score_server():

    with open('C:/DevOps/WoG-project/txt-files/name.txt', 'r+') as file:
        username = file.read()
    if os.path.exists(scores_file_flask):
        with open(scores_file_flask, 'r') as scores_file:
            score = scores_file.readline().strip()
        return render_template('WoW-Scores.html', score=score, username=username)

    else:
        return render_template('error.html')


host = os.environ.get('FLASK_RUN_HOST', '0.0.0.0')
port = int(os.environ.get('FLASK_RUN_PORT', 5000))
debug = os.environ.get('FLASK_DEBUG', 'False').lower() == 'true'

if __name__ == '__main__':
    app.run(host=host, debug=debug, port=port)
