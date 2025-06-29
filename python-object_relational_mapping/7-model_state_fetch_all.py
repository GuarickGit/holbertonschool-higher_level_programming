#!/usr/bin/python3
"""
Ce script liste tous les objets State de la base de données fournie
en argument.
Les résultats sont affichés dans l'ordre croissant de l'id sous la forme :
id: name
"""

import sys
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
# Import des classes définies dans model_state.py.
from model_state import Base, State

if __name__ == "__main__":
    # Vérifie que les arguments sont bien passés
    # (nom d'utilisateur, mot de passe, nom de la base)
    # Sinon useless de faire le test.
    if len(sys.argv) != 4:
        print("Usage: ./0-select_states.py <username> <password> <database>")
        sys.exit(1)

    # Récupération des arguments en ligne de commande.
    username = sys.argv[1]
    password = sys.argv[2]
    db_name = sys.argv[3]

    # Création de l'engine pour se connecter à MySQL via SQLAlchemy
    # Format de l'URL :
    # mysql+mysqldb://<username>:<password>@localhost:3306/<database>
    engine = create_engine(
        f"mysql+mysqldb://{username}:{password}@localhost:3306/{db_name}",
        pool_pre_ping=True)

    # Création d'une session pour interagir avec la base de données
    Session = sessionmaker(bind=engine)
    session = Session()

    # Requête pour récupérer tous les objets State, triés par id croissant
    states = session.query(State).order_by(State.id).all()

    # Affichage des résultats sous forme "id: name"
    for state in states:
        print(f"{state.id}: {state.name}")

    # Fermeture de la session proprement
    session.close()
