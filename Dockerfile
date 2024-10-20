
FROM python:3.10-bullseye

ENV DEBIAN_FRONTEND=noninteractive
RUN apt-get update && apt-get install -y tzdata

COPY requirements.txt /opt/requirements.txt

RUN pip install -U pip
RUN pip install -r /opt/requirements.txt

ENV TZ="UTC"

WORKDIR /opt/app
COPY . /opt/app
