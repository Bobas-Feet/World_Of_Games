from flask import Flask, render_template
from Scores import *

app = Flask(__name__)


@app.route("/")
def score_server():
    file_path = 'C:/DevOps/WoG (project)/'
    try:
        score_file = open(f'{file_path}Scores.txt', 'r')
        score = score_file.read()
        return render_template('score.html', SCORE=score)
    except FileNotFoundError or FileExistsError:
        return render_template('error.html', ERROR='Unknown Error')


app.run()

