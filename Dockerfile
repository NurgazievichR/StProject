FROM python:3.9

ENV PYTHONUNBUFFERED 1

WORKDIR /StProject

COPY req.txt /StProject/


RUN pip install -r req.txt

COPY . /StProject/
