FROM python:latest

ENV PYTHONONBUFFERED 1

WORKDIR /app

COPY requirements.txt requirements.txt

RUN sudo pip install -r requirements.txt

VOLUME . .

CMD ["python","main.py"]