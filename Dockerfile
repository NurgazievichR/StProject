FROM python:3.9

ENV PYTHONUNBUFFERED 1

WORKDIR /StProject

COPY requirements.txt /StProject/

RUN pip install -r requirements.txt

COPY . /code/
