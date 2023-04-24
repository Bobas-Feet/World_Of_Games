FROM python:3.9

WORKDIR /WoGApp

RUN pip install flask \
    && pip3 install --upgrade pip

COPY WoG-project/MainScores.py .

COPY WoG-project/Utils.py .

COPY /Scoreboard/name.txt .

COPY /Scoreboard/Scores.txt .

EXPOSE 5000

CMD ["python", "MainScores.py"]


