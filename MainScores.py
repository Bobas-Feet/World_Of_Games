from flask import Flask, render_template


class AppScore:
    count = 1

    def __init__(self, name):
        self.name = name
        self.id = AppScore.count
        AppScore.count += 1


app = Flask(__name__)

game1 = AppScore(name='The Memory Game')
game2 = AppScore(name='The Guessing Game')
game3 = AppScore(name='The Currency Roulette Game')

games = [game1, game2, game3]


@app.route('/games')
def score_server(difficulty):
    from Scores import add_score
    # return render_template('index.html', games=games)

    file_path = 'C:/DevOps/WoG-project/'
    try:
        add_score.score_file = open(f'{file_path}Scores.txt', 'a')
        score = add_score.score_file.read()
        return render_template('Score.html', SCORE=score)
    except FileNotFoundError or FileExistsError:
        return render_template('error.html', ERROR='Unknown Error')


if __name__ == '__main__':
    app.run()
