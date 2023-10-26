FROM python

ENV PYTHONONBUFFERED 1

WORKDIR /app

COPY . .

RUN pip install -r requirements.txt

VOLUME . .

CMD ["python", "main.py"]