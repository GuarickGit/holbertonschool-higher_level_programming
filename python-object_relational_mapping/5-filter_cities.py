#!/usr/bin/python3
"""
Script Python qui affiche toutes les villes d’un État donné,
à partir d’une base de données MySQL (hbtn_0e_4_usa).
Le script prend 4 arguments :
  - nom d'utilisateur MySQL
  - mot de passe MySQL
  - nom de la base de données
  - nom de l'État
Les résultats sont affichés par ordre croissant des ID des villes.
"""

import MySQLdb
import sys

if __name__ == "__main__":
    # Connexion à la base de données
    connection = MySQLdb.connect(
        host="localhost",
        user=sys.argv[1],
        passwd=sys.argv[2],
        db=sys.argv[3],
        port=3306
    )

    # Création d’un curseur pour exécuter les requêtes
    cursor = connection.cursor()

    # Requête SQL pour récupérer les noms de villes liées à un État donné
    query = ("SELECT cities.name "
             "FROM cities "
             "JOIN states ON cities.state_id = states.id "
             "WHERE states.name = %s "
             "ORDER BY cities.id ASC")

    # Exécution sécurisée de la requête avec le nom de l'État
    cursor.execute(query, (sys.argv[4],))

    # Récupération et affichage des résultats, séparés par des virgules
    rows = cursor.fetchall()
    print(", ".join([row[0] for row in rows]))

    # Fermeture du curseur et de la connexion
    cursor.close()
    connection.close()
