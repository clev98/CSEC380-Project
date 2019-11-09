FROM mariadb
COPY initialize_db.sql /docker-entrypoint-initdb.d/init.sql
CMD ["mysqld"]
