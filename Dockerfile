FROM python:3.9


RUN pip install flask \
    && pip3 install --upgrade pip

WORKDIR /app

COPY WoG-project/MainScores.py .

COPY WoG-project/Utils.py .

COPY /Scoreboard/name.txt .

COPY /Scoreboard/Scores.txt .

EXPOSE 5000

CMD ["python", "MainScores.py"]


