FROM python:3.13.0b4-slim

WORKDIR /app

copy requirements.txt /app/

RUN pip install  -r requirements.txt

COPY . /app

EXPOSE 80

ENV NAME world

CMD ["uvicorn","main:app"]