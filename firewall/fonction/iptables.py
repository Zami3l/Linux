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

    #Déclaration des paramètres acceptés par la fonction Commande Globale
    Parametres_Commande = {'Filter': None, 'In_Interface': None, 'Out_Interface': None, 'Protocole': None, 'Destination': None,
                    'Destination_Protocole': None, 'Table': None, 'Action': None}

    #Declaration d'une liste pour la sauvegarde des paramètres trouvés
    Save_Parametres = [0] * len(Parametres_Commande.keys())

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

            result = "iptables -t {} -X".format(Table)

        print(result)

        return result

    #Fonction Test Argument : Permet de vérifier et de sauvegarder les paramètres passés dans la fonction Commande Globale
    def Test_Argument(self, Argument):

        for Index in range(0, len(self.Parametres_Commande.keys())):

            if Argument == list(self.Parametres_Commande.keys())[Index]:
                
                #Si un argument est trouvé dans la liste, on sauvegarde le paramètre et on sort de la boucle FOR
                self.Save_Parametres[Index] = True
                break

    # Fonction Commande Globale : Permet d'ajouter des règles dans le Firewall
    def commande_globale(self, **Parametres):

        #On reset la liste de sauvegarde des paramètres
        self.Save_Parametres = [0] * len(self.Parametres_Commande.keys())

        result = "iptables "

        # On lance la fonction Test Argument
        for Index in range(0, len(Parametres.keys())):

            self.Test_Argument(list(Parametres.keys())[Index])

        # On affecte le paramètre Filter
        if self.Save_Parametres[0] == True:

            result += "-A {} ".format(Parametres.get('Filter'))

        # On affecte le paramètre In Interface
        if self.Save_Parametres[1] == True:

            result += "-i {} ".format(Parametres.get('In_Interface'))

        # On affecte le paramètre Out Interface
        if self.Save_Parametres[2] == True:

            result += "-o {} ".format(Parametres.get('Out_Interface'))

        # On affecte le paramètre Protocole
        if self.Save_Parametres[3] == True:

            result += "-p {} ".format(Parametres.get('Protocole'))

        # On affecte le paramètre Destination
        if self.Save_Parametres[4] == True:

            result += "-d {} ".format(Parametres.get('Destination'))

        # On affecte le paramètre Destionation Protocole
        if self.Save_Parametres[5] == True:

            result += "--dport {} ".format(Parametres.get('Destination_Protocole'))

        # On affecte le paramètre Table
        if self.Save_Parametres[6] == True:

            result += "-n {} ".format(Parametres.get('Table'))

        # On affecte le paramètre Action
        if self.Save_Parametres[7] == True:

            result += "-j {} ".format(Parametres.get('Action'))

        print(result)

        return result