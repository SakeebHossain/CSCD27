FROM ubuntu:latest

RUN apt-get update && apt-get install iptables python3 libdnet python3-pip git iptables -y

RUN pip3 install --upgrade pip
RUN pip3 install netifaces 
RUN pip3 install scapy-python3
RUN git clone https://github.com/invernizzi/scapy-http.git && \
    cd scapy-http && \
    python3 setup.py install && \ 
    apt-get remove -y git && \
    rm -rf /scapy-http