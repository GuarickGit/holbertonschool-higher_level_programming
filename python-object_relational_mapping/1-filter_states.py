#!/usr/bin/python3
"""
Ce script affiche tous les États dont le nom commence par 'N'
depuis la base de données hbtn_0e_0_usa. Les résultats sont
triés par identifiant croissant.
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

    # Exécution de la requête pour récupérer les states commençant par 'N'
    cursor.execute(
        "SELECT * FROM states WHERE name LIKE 'N%' ORDER BY states.id ASC")

    # Récupération et affichage de toutes les lignes obtenues
    rows = cursor.fetchall()
    for row in rows:
        print(row)

    # Fermeture du curseur et de la connexion à la base de données
    cursor.close()
    connection.close()
