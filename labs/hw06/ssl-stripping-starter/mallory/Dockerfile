FROM ubuntu:latest

RUN apt-get update && apt-get install dsniff iptables net-tools python python-twisted-web wget -y

WORKDIR /root

RUN wget https://moxie.org/software/sslstrip/sslstrip-0.9.tar.gz
RUN tar xvzf sslstrip-0.9.tar.gz
RUN rm -Rf sslstrip-0.9.tar.gz