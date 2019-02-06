#!/bin/bash

# On reset iptables
iptables -F
iptables -t nat -F
iptables -X
iptables -t nat -X

# On bloque tout
iptables -P INPUT DROP
iptables -P OUTPUT DROP
iptables -P FORWARD DROP

# On autorise le trafic sur la machine locale
iptables -A INPUT -i lo -j ACCEPT
iptables -A OUTPUT -o lo -j ACCEPT

# -------------------- WAN --------------------

# NAT
iptables -t nat -A POSTROUTING -o WAN -j MASQUERADE

# On autorise le trafic du WAN sur le Firewall
iptables -A INPUT -i WAN -j ACCEPT
iptables -A OUTPUT -o WAN -j ACCEPT

#-------------------------------------------- 

# -------------------- LAN --------------------

# On autorise le ping du LAN sur le Firewall
iptables -A INPUT -i LAN -p icmp -j ACCEPT
iptables -A OUTPUT -o LAN -p icmp -j ACCEPT

# On autorise la connexion ssh du LAN sur le Firewall
iptables -A INPUT -i LAN -p tcp --dport ssh -j ACCEPT
iptables -A OUTPUT -o LAN -p tcp --sport ssh -j ACCEPT

# J'autorise la translation
iptables -A FORWARD -i LAN -o WAN -j ACCEPT
iptables -A FORWARD -o LAN -i WAN -j ACCEPT

# J'autorise l'accès au service WEB  du DMZ via le LAN
iptables -A FORWARD -i LAN -o DMZ -p tcp --destination-port 8080 -j ACCEPT
iptables -A FORWARD -o LAN -i DMZ -p tcp --source-port 8080 -j ACCEPT

#-------------------------------------------- 

# -------------------- DMZ --------------------

# Translation du WEB venant du WAN vers la DMZ
iptables -t nat -A PREROUTING -d 192.168.1.254 -p tcp --dport 80 -j DNAT --to-destination 10.10.10.10:8080

#-------------------------------------------- 
