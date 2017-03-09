FROM mongo:latest
FROM python:3.5
RUN pip install bottle
RUN pip install pymongo
RUN useradd -ms /bin/bash admin
USER admin
COPY . /usr/bin/dockermongo
WORKDIR /usr/bin/dockermongo
