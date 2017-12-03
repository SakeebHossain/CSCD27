FROM ubuntu:trusty

ENV DEBIAN_FRONTEND noninteractive

RUN echo "mysql-server mysql-server/root_password password pass4root" | debconf-set-selections
RUN echo "mysql-server mysql-server/root_password_again password pass4root" | debconf-set-selections
RUN apt-get update && apt-get install curl apache2 mysql-server php5-mysql php5 libapache2-mod-php5 php5-mcrypt python python-pip -yq 

RUN dpkg-reconfigure mysql-server

RUN pip install requests

RUN rm -Rf file /var/www/html/*
COPY ./microblogging /var/www/html/
RUN chown -R www-data:www-data /var/www/

RUN echo "ServerName localhost" >> /etc/apache2/apache2.conf

# ####### enable SQLi remote code execution  ########
RUN sed  '/\[mysqld\]/a secure-file-priv = \"\"' /etc/mysql/my.cnf
RUN usermod -a -G www-data  mysql
RUN chmod g+w /var/www/html/media/uploads/
######################################

EXPOSE 80

CMD /usr/bin/mysqld_safe --skip-grant-tables & /usr/sbin/apache2ctl -D FOREGROUND 

