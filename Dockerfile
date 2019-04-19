FROM ubuntu:16.04

RUN apt-get update -y
RUN apt-get install -y python3-pip python-dev build-essential
RUN apt-get install -y software-properties-common
RUN apt-get install -y python3-software-properties
RUN add-apt-repository -y ppa:jonathonf/ffmpeg-3
RUN apt-get install -y ffmpeg

ENV PYTHONUNBUFFERED 1
COPY . /usr/src/app/
WORKDIR /usr/src/app

RUN python3 setup.py install
