#!/usr/bin/python3
"""
Ce script modifie le nom de l'objet State ayant l'id 2 pour 'New Mexico'.
"""

import sys
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from model_state import Base, State  # Import du modèle State et de la base

if __name__ == "__main__":
    # Récupération des arguments de connexion
    username = sys.argv[1]
    password = sys.argv[2]
    db_name = sys.argv[3]

    # Connexion à la base MySQL avec SQLAlchemy
    engine = create_engine(
        f"mysql+mysqldb://{username}:{password}@localhost:3306/{db_name}",
        pool_pre_ping=True
    )

    # Création d'une session ORM
    Session = sessionmaker(bind=engine)
    session = Session()

    # Recherche de l'objet State avec id = 2
    # .get(2) est une méthode pratique et optimisée de SQLAlchemy pour
    # chercher un objet directement via sa clé primaire (ici id = 2).
    # C’est plus clair et plus rapide que :
    # session.query(State).filter(State.id == 2).first()
    state = session.query(State).get(2)

    # Si l'objet existe, on modifie son nom
    if state:
        state.name = "New Mexico"
        session.commit()

    # Fermeture de la session proprement
    session.close()
