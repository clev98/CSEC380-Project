FROM mariadb
COPY initialize_db.sql /docker-entrypoint-initdb.d/init.sql
EXPOSE 3306
CMD ["mysqld"]