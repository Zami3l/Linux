# -*-coding:Utf-8 -*

import os

class Iptables:

    #Déclaration d'un dictionnaire d'items pour l'initialisation
    Liste = {}
    Liste['Filter'] = 'INPUT', 'FORWARD', 'OUTPUT'
    Liste['Nat'] = 'PREROUTING', 'INPUT', 'OUTPUT', 'POSTROUTING'
    Liste['Mangle'] = 'PREROUTING', 'INPUT', 'FORWARD', 'OUTPUT', 'POSTROUTING'
    Liste['Chaine'] = 'INPUT', 'FORWARD', 'PREROUTING', 'POSTROUTING', 'OUTPUT'
    Liste['Action'] = 'ACCEPT', 'DENY', 'REJECT', 'DROP'

    #Fonction Initialisation : Permet d'initialiser iptables
    def initialisation(self):

        #Accepter tout
        for Index_Table in range(0,3):

            for Index_Chaine in range(0,len(self.Liste[list(self.Liste.keys())[Index_Table]])):

                print(self.commande(list(self.Liste.keys())[Index_Table], self.Liste[list(self.Liste.keys())[Index_Table]][Index_Chaine], self.Liste['Action'][0], 'Politique_Avancee'))

        #Remttre les compteurs à zéro
        for Index_Table in range(0,3):

            print(self.commande(Table=(list(self.Liste.keys())[Index_Table]), Mode='Reset'))

        #Supprimer les règles actives et les chaines personnalisées
        for Index_Table in range(0,3):

            print(self.commande(Table=(list(self.Liste.keys())[Index_Table]), Mode='Del_Regle'))
            print(self.commande(Table=(list(self.Liste.keys())[Index_Table]), Mode='Del_Chaine'))

    #Fonction Commande : Permet de générer les commandes iptables
    def commande(self, Table='filter', Chaine='INPUT', Action='DENY', Mode='Defaut'):

        #Paramétrage des politiques générales
        if Mode == 'Politique_Simple':
            result = "iptables -P {} {}".format(Chaine, Action)

        #Paramétrage des politiques d'une table
        elif Mode == 'Politique_Avancee':
            result = "iptables -t {} -P {} {}".format(Table, Chaine, Action)

        #Reset des compteurs d'une table
        elif Mode == 'Reset':
            result = "iptables -t {} -Z".format(Table)
        
        #Supprimer toutes les règles actives d'une table
        elif Mode == 'Del_Regle':
            result = "iptables -t {} -F".format(Table)

        #Supprimer toutes les chaines personnalisées d'une table
        elif Mode == 'Del_Chaine':
            result = "ptables -t {} -X".format(Table)

        print(result)

        return result
