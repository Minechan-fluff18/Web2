FROM python:3

ENV PYTHONUNBUFFERED=1
RUN mkdir /code
WORKDIR /code

COPY req.txt /code/
RUN pip3 install -r req.txt
COPY . /code/
