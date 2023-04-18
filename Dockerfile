FROM python:latest
LABEL Maintainer="Boba's Feet"

WORKDIR /DevOps/WoG-project
RUN pip install flask

COPY Scores/MainScores.py .

COPY Utils.py .

COPY ../name.txt .

COPY Scores/Scores.txt

EXPOSE 5000

CMD ["python", "MainScores.py"]


