FROM python:3.9


WORKDIR /DevOps/WoG-project
RUN pip install flask

COPY MainScores.py .

COPY Utils.py .

COPY Scoreboard/name.txt .

COPY Scoreboard/Scores.txt .

EXPOSE 5000

CMD ["python", "MainScores.py"]


