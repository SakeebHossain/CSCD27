#!/usr/bin/env bash

iptables -F
iptables -F -t nat
iptables -F -t mangle

if [ `cat /proc/sys/net/ipv4/ip_forward` -eq 1 ]
then
    echo "Welcome to POOPLab" > index.html
    chmod 777 index.html
    iptables -t nat -A POSTROUTING -o eth0 -j MASQUERADE
    iptables -A FORWARD -i eth0 -o eth1 -m state --state RELATED,ESTABLISHED -j ACCEPT
    iptables -A FORWARD -i eth1 -o eth0 -j ACCEPT
    iptables -t nat -A PREROUTING -p tcp -i eth1 -d 142.1.97.172 --dport 80 -j DNAT --to-destination 10.0.0.3:8080
    python -m SimpleHTTPServer 8080
fi
