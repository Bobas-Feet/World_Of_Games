import os

from flask import Flask, render_template
from App import AppScore
from Utils import bad_return_code, last_scores_flask, scores_file_flask
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


@app.route('/')
def score_server():

    with open('./name.txt', 'r+') as file:
        username = file.read()
    if os.path.exists(scores_file_flask):
        with open(scores_file_flask, 'r') as scores_file:
            score = scores_file.readline().strip()

        return "<html" \
               "><head><title>Scores Game</title>" \
               "<meta http-equiv='refresh' content='10'>" \
               "</head>" \
               "<h1>---Game Score---</h1>" \
               "<body>" \
               "<h2>Hello " + username + ", your score is:" \
                                         "<div id='score'>" + score + "</div>" \
                                                                      "</h2>" \
                                                                      "</body>" \
                                                                      "</html>"
    else:
        return "<html>" \
               "<head>" \
               "<title>Scores Game</title>" \
               "</head>" \
               "<body>" \
               "<h1>" \
               "<div id='score' style='color:red'>" \
            + str(bad_return_code) + "</div>" \
                                     "</h1>" \
                                     "</html>"


host = os.environ.get('FLASK_RUN_HOST', '0.0.0.0')
port = int(os.environ.get('FLASK_RUN_PORT', 5000))
debug = os.environ.get('FLASK_DEBUG', 'False').lower() == 'true'

if __name__ == '__main__':
    app.run(host=host, debug=debug, port=port)


@app.route('/last_score')
def old_score():
    with open('./name.txt', 'r+') as file:
        username = file.read()
    if os.path.exists(last_scores_flask):
        with open(last_scores_flask, 'r') as scores_file:
            last_s = scores_file.readline().strip()
        return "<html><head><title>Scores Game</title><meta http-equiv='refresh' content='30'></head><body>" \
               "<h1>Hello " + username + " your last score was:<div id='score'>" + last_s + "</div></h1></body></html>"
    else:
        return "<html><head><title>Last Scores Game</title></head><body><h1><div id='score' style='color:red'>" \
            + str(bad_return_code) + "</div></h1>"


host = os.environ.get('FLASK_RUN_HOST', '0.0.0.0')
port = int(os.environ.get('FLASK_RUN_PORT', 5000))
debug = os.environ.get('FLASK_DEBUG', 'False').lower() == 'true'

if __name__ == '__main__':
    app.run(host=host, debug=debug, port=port)




    # from Scores import add_score
    # add_score(difficulty)
    #
    # file_path = 'C:/DevOps/WoG-project/'
    # try:
    #     add_score.score_file = open(f'{file_path}Scores.txt', 'a')
    #     score = add_score.score_file.read()
    #     print(score)
    #     return render_template('index.html', games=games)
    # except FileNotFoundError or FileExistsError:
    #     return render_template('error.html', ERROR='Unknown Error')


# if __name__ == '__main__':
#     app.run()
