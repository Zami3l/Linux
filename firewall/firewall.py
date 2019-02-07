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

#On initialise iptables
Cmd_Iptables.initialisation()

#On change les politiques par défaut
Cmd_Iptables.commande('filter', 'INPUT', 'DROP', 'Politique_Simple')
Cmd_Iptables.commande('filter', 'FORWARD', 'DROP', 'Politique_Simple')
Cmd_Iptables.commande('filter', 'OUTPUT', 'ACCEPT', 'Politique_Simple')
