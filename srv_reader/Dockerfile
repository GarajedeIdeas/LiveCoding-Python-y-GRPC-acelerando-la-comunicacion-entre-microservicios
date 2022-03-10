FROM python:3.8-slim

COPY ./srv_reader /home/app
COPY ./data/100_sr.csv /tmp/data/
COPY ./data/1000_sr.csv /tmp/data/
COPY ./data/10000_sr.csv /tmp/data/
COPY ./data/100000_sr.csv /tmp/data/

WORKDIR /home/app

RUN pip3.8 install --upgrade pip
RUN pip3.8 install -r requirements.txt

CMD [ "python3.8", "-u", "main.py" ]