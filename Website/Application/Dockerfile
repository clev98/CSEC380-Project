FROM python:latest

COPY requirements.txt app.py /
COPY templates /templates
COPY /static/ /static/
COPY server.crt server.key /

RUN pip install -r requirements.txt

CMD sleep 30s; python app.py
