FROM mariadb:latest as builder
COPY initialize_db.sql /docker-entrypoint-initdb.d/init.sql
EXPOSE 3306

RUN ["sed", "-i", "s/exec \"$@\"/echo \"not running $@\"/", "/usr/local/bin/docker-entrypoint.sh"]
ENV MYSQL_ROOT_PASSWORD=absolutely_totally_secure
RUN ["/usr/local/bin/docker-entrypoint.sh", "mysqld", "--datadir", "/initialized-db", "--aria-log-dir-path", "/initialized-db"]

FROM mariadb:latest
COPY --from=builder /initialized-db /var/lib/mysql
CMD ["mysqld"]