FROM python:3.8
COPY requirements.txt app.py /
COPY templates /templates
COPY images /images
RUN mkdir /uploads/
RUN apt update; apt install -y ffmpeg
RUN pip install -r requirements.txt
EXPOSE 5001
CMD python app.py