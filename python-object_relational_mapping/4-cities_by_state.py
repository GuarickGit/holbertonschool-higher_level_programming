#!/usr/bin/python3
"""
Ce script liste toutes les villes de la base de données hbtn_0e_4_usa,
avec le nom de leur État associé, en les triant par id croissant.
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

    # Requête SQL pour récupérer l'identifiant et le nom de chaque ville,
    # ainsi que le nom de son État, triés par identifiant de la ville
    query = ("SELECT cities.id, cities.name, states.name "
             "FROM cities JOIN states ON cities.state_id = states.id "
             "ORDER BY cities.id ASC")

    # Exécution de la requête SQL
    cursor.execute(query)

    # Récupération et affichage de toutes les lignes obtenues
    rows = cursor.fetchall()
    for row in rows:
        print(row)

    # Fermeture du curseur et de la connexion à la base de données
    cursor.close()
    connection.close()
