#!/usr/bin/python3
"""
Ce script se connecte à une base de données MySQL et affiche toutes les
entrées de la table 'states' dont le nom correspond exactement à l'argument
fourni (sensible à la casse). Les résultats sont triés par identifiant
croissant.
"""

import MySQLdb
import sys

if __name__ == "__main__":
    # Connexion à la base de données MySQL en utilisant les arguments passés
    # en ligne de commande
    connection = MySQLdb.connect(
        host="localhost",
        user=sys.argv[1],  # Nom d'utilisateur MySQL
        passwd=sys.argv[2],  # Mot de passe MySQL
        db=sys.argv[3],  # Nom de la base de données
        port=3306  # Port par défaut de MySQL
    )

    # Création d'un curseur pour exécuter des requêtes SQL
    cursor = connection.cursor()

    # Construction de la requête SQL avec filtrage exact (sensible à la casse)
    query = ("SELECT * FROM states "
             "WHERE BINARY name = '{}'").format(sys.argv[4])

    # Exécution de la requête SQL
    cursor.execute(query)

    # Récupération et affichage de toutes les lignes obtenues
    rows = cursor.fetchall()
    for row in rows:
        print(row)

    # Fermeture du curseur et de la connexion à la base de données
    cursor.close()
    connection.close()
