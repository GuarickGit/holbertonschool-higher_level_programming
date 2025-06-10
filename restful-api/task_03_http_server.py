#!/usr/bin/python3
"""
Ce module implémente un serveur web HTTP simple utilisant le module http.server
de la bibliothèque standard de Python.

Il est conçu pour démontrer la mise en place d'un serveur basique, la gestion
des requêtes GET pour différentes routes (endpoints) et le service de données
textuelles et JSON.
"""

import http.server  # Fournit les classes pour créer des serveurs HTTP
import socketserver  # Module de bas niveau pour la gestion des sockets réseau
import json  # Utilisé pour encoder et décoder les données JSON

# Définition du port sur lequel le serveur va écouter
PORT = 8000


class New_server(http.server.BaseHTTPRequestHandler):
    """
    Gère les requêtes HTTP (GET) pour un serveur web simple.

    Cette classe hérite de BaseHTTPRequestHandler et implémente les méthodes
    nécessaires pour répondre à différentes routes URL.
    """

    def do_GET(self):
        """
        Gère les requêtes HTTP GET.

        Cette méthode est appelée automatiquement par le serveur quand une
        requête GET est reçue.
        Elle route les requêtes vers des logiques spécifiques en fonction de
        l'URL demandée (self.path).
        """
        # Vérifie si le chemin de la requête est "/data"
        if self.path == "/data":
            # Données à envoyer au format dictionnaire Python
            datas = {"name": "John", "age": 30, "city": "New York"}
            # Convertit le dictionnaire Python en une chaîne de caractères JSON
            json_string = json.dumps(datas)
            # Envoie le code de statut HTTP 200 (OK) pour indiquer le succès
            self.send_response(200)
            # Définit l'en-tête "Content-type" pour indiquer que la réponse
            # est au format JSON
            self.send_header("Content-type", "application/json")
            # Termine l'envoi des en-têtes HTTP
            self.end_headers()
            # Écrit la chaîne JSON encodée en UTF-8 dans le corps de la réponse
            self.wfile.write(json_string.encode("utf-8"))

        # Vérifie si le chemin de la requête est "/status"
        elif self.path == "/status":
            # Envoie le code de statut HTTP 200 (OK)
            self.send_response(200)
            # Définit l'en-tête "Content-type" pour indiquer que la réponse
            # est du texte brut
            self.send_header("content-type", "text/plain")
            # Termine l'envoi des en-têtes
            self.end_headers()
            # Écrit la chaîne "OK" encodée en UTF-8 dans le corps de la réponse
            self.wfile.write("OK".encode("utf-8"))

        # Vérifie si le chemin de la requête est "/info"
        elif self.path == "/info":
            # Données d'informations sur l'API au format dictionnaire Python
            infos_data = {
                "version": "1.0", "description":
                "A simple API built with http.server"}
            # Convertit le dictionnaire Python en une chaîne de caractères JSON
            infos_json_string = json.dumps(infos_data)
            # Envoie le code de statut HTTP 200 (OK)
            self.send_response(200)
            # Définit l'en-tête "Content-type" à "application/json" car le
            # contenu est du JSON
            self.send_header("content-type", "text/plain")
            # Termine l'envoi des en-têtes
            self.end_headers()
            # Écrit la chaîne JSON encodée en UTF-8 dans le corps de la réponse
            self.wfile.write(infos_json_string.encode("utf-8"))

        # Vérifie si le chemin de la requête est la racine "/"
        elif self.path == "/":
            # Envoie le code de statut HTTP 200 (OK)
            self.send_response(200)
            # Définit l'en-tête "Content-type" à "text/plain" pour un
            # message textuel
            self.send_header("Content-type", "text/plain")
            # Termine l'envoi des en-têtes
            self.end_headers()
            # Écrit le message de bienvenue encodé en UTF-8
            self.wfile.write("Hello, this is a simple API!".encode("utf-8"))

        # Si aucun des chemins ci-dessus ne correspond, gère l'erreur 404
        # (non trouvé)
        else:
            # Envoie le code de statut HTTP 404 (Not Found)
            self.send_response(404)
            # Définit l'en-tête "Content-type" à "text/plain"
            self.send_header("Content-type", "text/plain")
            # Termine l'envoi des en-têtes
            self.end_headers()
            # Écrit un message d'erreur clair encodé en UTF-8
            self.wfile.write("Endpoint not found".encode("utf-8"))


# Bloc principal d'exécution du script
if __name__ == "__main__":
    # Crée une instance de TCPServer qui écoute sur toutes les interfaces ("")
    # et utilise notre classe New_server pour gérer les requêtes HTTP.
    with socketserver.TCPServer(("", PORT), New_server) as httpd:
        # Affiche un message indiquant que le serveur est démarré et
        # sur quel port
        print(f"Serving on port {PORT}")
        # Lance le serveur en mode "serve_forever", ce qui le maintient
        # en attente de requêtes entrantes indéfiniment.
        httpd.serve_forever()
