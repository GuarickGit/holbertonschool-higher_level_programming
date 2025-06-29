#!/usr/bin/python3
"""
Ce script affiche tous les objets State dont le nom contient la lettre 'a',
triés par id croissant.
"""

import sys
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from model_state import Base, State  # Import du modèle ORM

if __name__ == "__main__":
    # Récupération des arguments de connexion
    username = sys.argv[1]
    password = sys.argv[2]
    db_name = sys.argv[3]

    # Connexion à la base de données MySQL avec SQLAlchemy
    engine = create_engine(
        f"mysql+mysqldb://{username}:{password}@localhost:3306/{db_name}",
        pool_pre_ping=True
    )

    # Création de la session
    Session = sessionmaker(bind=engine)
    session = Session()

    # Requête : récupérer tous les State où name contient 'a', triés par id
    states = (
        session.query(State)
        .filter(State.name.like('%a%'))
        .order_by(State.id)
        .all()
    )

    # Affichage des résultats
    for state in states:
        print(f"{state.id}: {state.name}")

    # Fermeture propre de la session
    session.close()
