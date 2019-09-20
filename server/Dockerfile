FROM debian
EXPOSE 8080

RUN apt-get update && apt-get install -y \
	apache2 \
	htop \
	curl
RUN sed -i "s/Listen 80/Listen 8080/" /etc/apache2/ports.conf
RUN sed -i "s/*:80/*:8080/" /etc/apache2/sites-available/000-default.conf
COPY src/index.html /var/www/html/
STOPSIGNAL WINCH
CMD	["/usr/sbin/apache2ctl",  "-D", "FOREGROUND"]
