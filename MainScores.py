from flask import Flask, render_template
from App import AppScore
# from Scores import add_score


app = Flask(__name__)

game1 = AppScore(name='The Memory Game')
game2 = AppScore(name='The Guessing Game')
game3 = AppScore(name='The Currency Roulette Game')

games = [game1, game2, game3]


# @app.route('/games')
# def index():
#
#     return render_template('index.html', games=games)


@app.route('/games')
def score_server(difficulty):

    from Scores import add_score
    add_score(difficulty)

    file_path = 'C:/DevOps/WoG-project/'
    try:
        add_score.score_file = open(f'{file_path}Scores.txt', 'a')
        score = add_score.score_file.read()
        print(score)
        return render_template('index.html', games=games)
    except FileNotFoundError or FileExistsError:
        return render_template('error.html', ERROR='Unknown Error')


# if __name__ == '__main__':
#     app.run()
