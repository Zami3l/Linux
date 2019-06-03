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
    Parametres_Commande = { 'Filter': None,
                            'In_Interface': None, 'Out_Interface': None,
                            'Protocole': None,
                            'In_Destination': None, 'Out_Destination': None,
                            'In_Destination_Protocole': None, 'Out_Destination_Protocole': None,
                            'Table': None, 
                            'Action': None}

    #Declaration d'une liste pour la sauvegarde des paramètres trouvés
    Save_Parametres = [0] * len(Parametres_Commande.keys())

    #Nom du fichier à créer
    Name_File = 'iptables.sh'

    #Fonction Création fichier sh : Création/Test du fichier iptables
    def create_file(self):

        if (os.path.exists(self.Name_File) == True):
            os.remove(self.Name_File)
        
        os.system("echo -e '#!/bin/bash\n' >> {}".format(self.Name_File))

    def open_file(self):
        self.File = open(self.Name_File, "a")

    def close_file(self):
        self.File.close()        

    def ecrire_file(self, valeur):
        self.File.write("\n" + valeur)

    #Fonction Initialisation : Permet d'initialiser iptables
    def initialisation(self):

        #Accepter tout
        for Index_Table in range(0,3):

            for Index_Chaine in range(0,len(self.Liste[list(self.Liste.keys())[Index_Table]])):

                self.ecrire_file(self.commande(list(self.Liste.keys())[Index_Table], self.Liste[list(self.Liste.keys())[Index_Table]][Index_Chaine], self.Liste['Action'][0], 'Politique_Avancee'))

        #Remttre les compteurs à zéro
        for Index_Table in range(0,3):

            self.ecrire_file(self.commande(Table=(list(self.Liste.keys())[Index_Table]), Mode='Reset'))

        #Supprimer les règles actives et les chaines personnalisées
        for Index_Table in range(0,3):

            self.ecrire_file(self.commande(Table=(list(self.Liste.keys())[Index_Table]), Mode='Del_Regle'))
            self.ecrire_file(self.commande(Table=(list(self.Liste.keys())[Index_Table]), Mode='Del_Chaine'))

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

        self.ecrire_file(result)

        return result

    #Fonction Test Argument : Permet de vérifier et de sauvegarder les paramètres passés dans la fonction Commande Globale
    def test_argument(self, Argument):

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

            self.test_argument(list(Parametres.keys())[Index])

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

        # On affecte le paramètre In Destination
        if self.Save_Parametres[4] == True:

            result += "-d {} ".format(Parametres.get('In_Destination'))

        # On affecte le paramètre Out Destination
        if self.Save_Parametres[5] == True:

            result += "-s {} ".format(Parametres.get('Out_Destination'))

        # On affecte le paramètre In Destionation Protocole
        if self.Save_Parametres[6] == True:

            result += "--dport {} ".format(Parametres.get('In_Destination_Protocole'))

        # On affecte le paramètre Out Destionation Protocole
        if self.Save_Parametres[7] == True:

            result += "--sport {} ".format(Parametres.get('Out_Destination_Protocole'))

        # On affecte le paramètre Table
        if self.Save_Parametres[8] == True:

            result += "-n {} ".format(Parametres.get('Table'))

        # On affecte le paramètre Action
        if self.Save_Parametres[9] == True:

            result += "-j {} ".format(Parametres.get('Action'))

        self.ecrire_file(result)

        return result