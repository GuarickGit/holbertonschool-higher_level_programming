#!/usr/bin/python3
"""
Module pour interagir avec l'API JSONPlaceholder.

Ce module contient deux fonctions principales :
- fetch_and_print_posts : récupère et affiche les titres de tous les posts.
- fetch_and_save_posts : récupère les posts et les enregistre dans un fichier
CSV.

Utilise la bibliothèque requests pour la communication HTTP,
et csv pour l'exportation des données.
"""

import requests
import csv


def fetch_and_print_posts():
    """
    Récupère tous les posts depuis JSONPlaceholder
    et affiche le code de réponse ainsi que les titres de chaque post.
    """
    try:
        # Envoi d'une requête GET à l'API
        response = requests.get("https://jsonplaceholder.typicode.com/posts")
    except requests.exceptions.RequestException as e:
        # En cas d'erreur réseau ou autre problème de requête
        print("Une erreur est survenue lors de la requête :", e)
        return

    # Affiche le code de statut de la réponse HTTP
    print("Status Code:", response.status_code)

    if response.status_code == 200:
        # Conversion du contenu JSON en liste de dictionnaires Python
        posts = response.json()

        # Affichage de chaque titre de post
        for post in posts:
            print(post["title"])
    else:
        print("Échec de la récup. des posts. Code :", response.status_code)


def fetch_and_save_posts():
    """
    Récupère tous les posts depuis JSONPlaceholder
    et enregistre leurs id, titre et contenu dans un fichier CSV.
    """
    try:
        # Requête GET à l'API
        response = requests.get("https://jsonplaceholder.typicode.com/posts")
    except requests.exceptions.RequestException as e:
        print("Une erreur est survenue lors de la requête :", e)
        return

    if response.status_code == 200:
        posts = response.json()

        # Liste pour stocker les posts filtrés (id, titre, contenu)
        csv_data = []

        for post in posts:
            # Construction d'un dictionnaire avec les champs souhaités
            filtered_post = {
                "id": post["id"],
                "title": post["title"],
                "body": post["body"]
            }

            # Ajout du dictionnaire à la liste
            csv_data.append(filtered_post)

        # Ouverture du fichier CSV en écriture
        # (en mode texte, sans ligne vide supplémentaire)
        with open("posts.csv", "w", newline="") as f:
            # Définition des noms de colonnes pour le CSV
            fieldnames = ["id", "title", "body"]

            # Création d’un objet DictWriter pour écrire les données
            writer = csv.DictWriter(f, fieldnames=fieldnames)

            # Écriture de la ligne d’en-tête dans le CSV
            writer.writeheader()

            # Écriture de toutes les lignes de données
            writer.writerows(csv_data)
    else:
        print("Impossible de save les posts. Code :", response.status_code)
