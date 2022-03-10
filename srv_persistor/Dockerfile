FROM python:3.8-slim

COPY ./srv_persistor /home/app

WORKDIR /home/app

RUN pip3.8 install --upgrade pip
RUN pip3.8 install -r requirements.txt

CMD [ "python3.8", "-u", "main.py" ]