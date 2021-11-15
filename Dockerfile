FROM python:3.8-alpine

ENV PYTHONDONTWRITEBITECODE 1
ENV PYTHONUNBUFFERED 1

WORKDIR /usr/src/fake_csv_app

RUN pip install --upgrade pip
COPY ./requirements.txt /usr/src/fake_csv_app/requirements.txt
RUN pip install --no-cache-dir -r requirements.txt


COPY . /usr/src/fake_csv_app
