FROM python:latest

WORKDIR /usr/src/garden

ADD ./requirements.txt /usr/src/garden/requirements.txt
RUN pip install -r /usr/src/garden/requirements.txt