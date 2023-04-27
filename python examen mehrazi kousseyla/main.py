from client import Client, GestionClients

# Création d'une instance de gestion des clients
gestion_clients = GestionClients()

# Exemple d'ajout de clients
client1 = Client(1, "Mehrazi", "Kousseyla", 1990, "123456789", "1, rue du Paris")
client2 = Client(2, "Zinedine", "Zidane", 1975, "987650000", "2, avenue des Champs-Élysées")
client3 = Client(3, "Jean", "Marc", 1988, "70145201", "152, avenue de la Chine")
client4 = Client(4, "Yan", "Lu", 2002, "14587255", "587, avenue des pins")
client5 = Client(5, "Messi", "Lionel", 1987, "91552321", "202, avenue Argentine")
gestion_clients.ajouter_client(client1)
gestion_clients.ajouter_client(client2)
gestion_clients.ajouter_client(client3)
gestion_clients.ajouter_client(client4)
gestion_clients.ajouter_client(client5)
# Chercher un client avec son nom
nom_recherche = "Jean"
client_recherche = gestion_clients.chercher_client(nom_recherche)
if client_recherche:
    print("Le client "+str(nom_recherche)+" est trouvé :")
else:
    print("Aucun client trouvé avec le nom :", nom_recherche)

# Affichage du nombre total de clients
nombre_total_clients = gestion_clients.afficher_nombre_total_clients()
print("Nombre total de clients:", nombre_total_clients)

# Affichage de l'âge moyen des clients
age_moyen_clients = gestion_clients.afficher_age_moyen_clients()
print("Âge moyen des clients:", age_moyen_clients)

# Exemple de suppression d'un client
gestion_clients.supprimer_client(2)

# Exemple de modification des informations d'un client
gestion_clients.modifier_client(4, "999999999", "3, boulevard Marsaille")

# Affichage du nombre total de clients après suppression et modification
nombre_total_clients = gestion_clients.afficher_nombre_total_clients()
print("Nombre total de clients après suppression et modification:", nombre_total_clients)