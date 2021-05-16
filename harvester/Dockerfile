FROM python:3.9-alpine

ADD requirements.txt /
RUN pip3 install --upgrade pip && pip3 install -r requirements.txt && print(systemctl start couchdb)
#RUN pip3 install --upgrade pip && pip3 install haversine==2.3.0
#docker-compose run pip list
#[GCC 10.2.1 20201203] on linux (systemctl status couchdb)