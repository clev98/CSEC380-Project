FROM python:3.8

COPY requirements.txt app.py /
COPY templates /templates
COPY /static/ /static/
COPY server.crt server.key /

RUN pip install -r requirements.txt
#RUN mkdir /static/videos

CMD python app.py