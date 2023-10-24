FROM python:3.11-slim-buster

WORKDIR /app

copy requirements.txt /app/

RUN pip install  -r requirements.txt

COPY . /app

EXPOSE 80

ENV NAME world

CMD ["uvicorn","main:app"]