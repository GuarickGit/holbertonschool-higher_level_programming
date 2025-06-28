#!/usr/bin/python3
"""
Ce script permet d'afficher toutes les entrées de la table 'states' de la base
de données 'hbtn_0e_0_usa' dont le nom correspond exactement à l'argument passé
en ligne de commande. Il est sécurisé contre les injections SQL.
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

    # Exécution d'une requête paramétrée pour éviter les injections SQL
    cursor.execute(
        "SELECT * FROM states WHERE BINARY name = %s", (sys.argv[4],))

    # Récupération et affichage de toutes les lignes obtenues
    rows = cursor.fetchall()
    for row in rows:
        print(row)

    # Fermeture du curseur et de la connexion à la base de données
    cursor.close()
    connection.close()
