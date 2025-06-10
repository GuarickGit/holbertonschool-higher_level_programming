#!/usr/bin/python3
"""
Ce module implémente un serveur web HTTP simple utilisant le module http.server
de la bibliothèque standard de Python.

Il est conçu pour démontrer la mise en place d'un serveur basique, la gestion
des requêtes GET pour différentes routes (endpoints) et le service de données
textuelles et JSON.
"""

import http.server
import socketserver
import json

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
        if self.path == "/data":
            datas = {"name": "John", "age": 30, "city": "New York"}
            json_string = json.dumps(datas)
            self.send_response(200)
            self.send_header("Content-type", "application/json")
            self.end_headers()
            self.wfile.write(json_string.encode("utf-8"))

        elif self.path == "/status":
            self.send_response(200)
            self.send_header("content-type", "text/plain")
            self.end_headers()
            self.wfile.write("OK".encode("utf-8"))

        elif self.path == "/info":
            infos_data = {
                "version": "1.0", "description":
                "A simple API built with http.server"}
            infos_json_string = json.dumps(infos_data)
            self.send_response(200)
            self.send_header("content-type", "text/plain")
            self.end_headers()
            self.wfile.write(infos_json_string.encode("utf-8"))

        elif self.path == "/":
            self.send_response(200)
            self.send_header("Content-type", "text/plain")
            self.end_headers()
            self.wfile.write("Hello, this is a simple API!".encode("utf-8"))

        else:
            self.send_response(404)
            self.send_header("Content-type", "text/plain")
            self.end_headers()
            self.wfile.write("Endpoint not found".encode("utf-8"))


with socketserver.TCPServer(("", PORT), New_server) as httpd:
    print(f"Serving on port {PORT}")
    httpd.serve_forever()
