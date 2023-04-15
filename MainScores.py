import os
from flask import Flask, render_template, redirect, url_for, request
from App import AppScore
from Utils import bad_return_code, last_scores_flask, scores_file_flask


app = Flask(__name__)


@app.route('/')
def score_server():

    with open('./name.txt', 'r+') as file:
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


# @app.route('/last_score')
# def old_score():
#     with open('./name.txt', 'r+') as file:
#         username = file.read()
#     if os.path.exists(last_scores_flask):
#         with open(last_scores_flask, 'r') as scores_file:
#             last_s = scores_file.readline().strip()
#         return "<html>" \
#                "<head>" \
#                "<title>WoW - Scores</title>" \
#                "<meta http-equiv='refresh' content='30'>" \
#                "</head>" \
#                "<h1> ---Game Score--- </h1>" \
#                "<body>" \
#                "<p>Hello " + username + " your last score was: " \
#                                         "<div id='score'>" + last_s + "</div>" \
#                                         "</p>" \
#                                         "</body>" \
#                                         "</html>"
#     else:
#         return "<html>" \
#                "<head>" \
#                "<title>Last Scores Game</title>" \
#                "</head>" \
#                "<body>" \
#                "<h1>" \
#                "<div id='score' style='color:red'>" \
#             + str(bad_return_code) + "</div>" \
#                                      "</h1>" \
#                                      "</body>"
#
#
# host = os.environ.get('FLASK_RUN_HOST', '0.0.0.0')
# port = int(os.environ.get('FLASK_RUN_PORT', 5000))
# debug = os.environ.get('FLASK_DEBUG', 'False').lower() == 'false'
#
# if __name__ == '__main__':
#     app.run(host=host, debug=debug, port=port)
