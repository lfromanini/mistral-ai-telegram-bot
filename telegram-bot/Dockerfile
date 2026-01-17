FROM python:3.14-alpine

ENV PYTHONOPTIMIZE=2

WORKDIR /app
COPY telegram-bot/ .

RUN pip install --no-cache-dir --requirement=requirements.txt

CMD python main.py
