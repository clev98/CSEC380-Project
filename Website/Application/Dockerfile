FROM python:3.8

COPY requirements.txt app.py /
COPY templates /templates
COPY /static/ /static/

RUN pip install -r requirements.txt
EXPOSE 5001
CMD python app.py