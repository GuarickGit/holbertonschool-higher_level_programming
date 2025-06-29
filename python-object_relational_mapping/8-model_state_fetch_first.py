#!/usr/bin/python3
"""
Ce script affiche le premier objet State de la base de données hbtn_0e_6_usa.
Si la table est vide, il affiche 'Nothing'.
"""

import sys
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
# Import des classes définies dans model_state.py
from model_state import Base, State

if __name__ == "__main__":
    # Récupération des arguments passés en ligne de commande
    username = sys.argv[1]
    password = sys.argv[2]
    db_name = sys.argv[3]

    # Création de la connexion à la base MySQL
    engine = create_engine(
        f"mysql+mysqldb://{username}:{password}@localhost:3306/{db_name}",
        pool_pre_ping=True
    )

    # Création d'une session pour interagir avec la base
    Session = sessionmaker(bind=engine)
    session = Session()

    # Requête pour récupérer le premier objet State (trié par id)
    first_state = session.query(State).order_by(State.id).first()

    # Affichage du résultat
    if first_state is None:
        print("Nothing")
    else:
        print(f"{first_state.id}: {first_state.name}")

    # Fermeture propre de la session
    session.close()
