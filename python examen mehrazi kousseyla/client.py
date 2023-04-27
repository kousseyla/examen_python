import random
import datetime


class Client:
    def __init__(self, id_client, nom, prenom, annee_naissance, telephone, adresse):
        self.id_client = id_client
        self.nom = nom
        self.prenom = prenom
        self.annee_naissance = annee_naissance
        self.telephone = telephone
        self.adresse = adresse

    def calculer_age(self):
        annee_actuelle = datetime.datetime.now().year
        return annee_actuelle - self.annee_naissance

    def generer_prix_achat_chaussure(self):
        return random.randint(50, 200)  # Génère un prix entre 50 et 200

    def generer_prix_achat_vetement(self):
        return random.randint(20, 100)  # Génère un prix entre 20 et 100

    def generer_prix_achat_accessoire(self):
        return random.randint(5, 50)  # Génère un prix entre 5 et 50

    def get_id_client(self):
        return self.id_client

    def get_nom(self):
        return self.nom

    def get_prenom(self):
        return self.prenom

    def get_telephone(self):
        return self.telephone

    def get_adresse(self):
        return self.adresse

    def set_telephone(self, telephone):
        self.telephone = telephone

    def set_adresse(self, adresse):
        self.adresse = adresse


class GestionClients:
    def __init__(self):
        self.clients = []

    def ajouter_client(self, client):
        with open("client.txt", "a") as f:
            f.write(f"{client.id_client},{client.nom},{client.prenom},{client.annee_naissance},{client.telephone},{client.adresse}\n")
        self.clients.append(client)

    def supprimer_client(self, id_client):
        self.clients = [client for client in self.clients if client.get_id_client() != id_client]
        with open("client.txt", "w") as f:
            for client in self.clients:
                f.write(f"{client.id_client},{client.nom},{client.prenom},{client.annee_naissance},{client.telephone},{client.adresse}\n")

    def modifier_client(self, id_client, nouveau_telephone, nouvelle_adresse):
        for client in self.clients:
            if client.get_id_client() == id_client:
                client.set_telephone(nouveau_telephone)
                client.set_adresse(nouvelle_adresse)
                break
        with open("client.txt", "w") as f:
            for client in self.clients:
                f.write(f"{client.id_client},{client.nom},{client.prenom},{client.annee_naissance},{client.telephone},{client.adresse}\n")


    def afficher_nombre_total_clients(self):
        with open("client.txt", "r") as f:
            return sum(1 for line in f)

    def afficher_age_moyen_clients(self):
        total_age = sum(client.calculer_age() for client in self.clients)
        return total_age / len(self.clients)

    def chercher_client(self, nom):
        trouve = 0
        with open("client.txt", "r") as f:
            txt = f.readline()
            while txt != "":
                txt = txt.strip().split(",")
                if nom in txt:
                    trouve += 1
                txt = f.readline()
        if trouve > 0:
            return True
        else:
            return False

