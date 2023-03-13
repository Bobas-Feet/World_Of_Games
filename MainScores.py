from flask import Flask, render_template

app = Flask(__name__)


@app.route('/')
def score_server():
    from Scores import add_score
    file_path = 'C:/DevOps/WoG (project)/'
    try:
        score_file = open(f'{file_path}Scores.txt', 'a')
        score = score_file.read()
        return render_template('Score.html', SCORE=score)
    except FileNotFoundError or FileExistsError:
        return render_template('error.html', ERROR='Unknown Error')


if __name__ == '__main__':
    app.run()
