FROM mysql:5.7

ENV MYSQL_USER root
ENV MYSQL_ROOT_PASSWORD absolutely_totally_secure
ENV MYSQL_DATABASE Application

RUN apt-get -q update && apt-get -qy install netcat

ADD initialize_db.sql /docker-entrypoint-initdb.d

EXPOSE 3306

CMD ["mysqld"]
