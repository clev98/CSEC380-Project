FROM python:3.8

COPY requirements.txt app.py /
COPY templates /templates
COPY /static/images /static/images

RUN mkdir /static/videos/
RUN apt update; apt install -y ffmpeg
RUN pip install -r requirements.txt
EXPOSE 5001
CMD python app.py