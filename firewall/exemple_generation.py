# -*-coding:utf-8 -*-

import os
from fonction.iptables import Iptables

#Déclaration des interfaces présentes
Interface_Local = 'lo'
Interface_LAN = 'LAN'
Interface_WAN = 'WAN'
Interface_DMZ = 'DMZ'
Interface_VM = 'VM'

#Affectation de la classe Iptables
Cmd_Iptables = Iptables()

#On crée notre fichier sh
Cmd_Iptables.create_file()

#On ouvre le fichier sh
Cmd_Iptables.open_file()

#On initialise iptables
Cmd_Iptables.initialisation()

#On change les politiques par défaut
Cmd_Iptables.commande('filter', 'INPUT', 'DROP', 'Politique_Simple')
Cmd_Iptables.commande('filter', 'FORWARD', 'DROP', 'Politique_Simple')
Cmd_Iptables.commande('filter', 'OUTPUT', 'ACCEPT', 'Politique_Simple')

#On autorise le trafic sur la machine locale
Cmd_Iptables.commande_globale(Filter='INPUT', In_Interface=Interface_Local, Action='ACCEPT')

## Interface WAN

#Création du NAT
Cmd_Iptables.commande_globale(Table='nat', Filter='POSTROUTING', Out_Interface='WAN', Action='MASQUERADE')

#On autorise le trafic du WAN vers le Firewall
Cmd_Iptables.commande_globale(Filter='INPUT', In_Interface=Interface_WAN, Action='ACCEPT')

#On ferme le fichier sh
Cmd_Iptables.close_file()