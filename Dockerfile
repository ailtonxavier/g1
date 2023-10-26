FROM python:3.12-slim

ENV PYTHONONBUFFERED 1

WORKDIR /app

COPY . .

RUN pip install --upgrade pip && pip install -r requirements.txt

CMD ["python", "main.py"]