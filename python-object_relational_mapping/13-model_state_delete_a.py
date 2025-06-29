#!/usr/bin/python3
"""
Ce script supprime tous les objets State dont le nom contient la lettre 'a'.
"""

import sys
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from model_state import Base, State  # Import du modèle ORM

if __name__ == "__main__":
    # Récupération des arguments passés en ligne de commande
    username = sys.argv[1]
    password = sys.argv[2]
    db_name = sys.argv[3]

    # Connexion à la base de données MySQL avec SQLAlchemy
    engine = create_engine(
        f"mysql+mysqldb://{username}:{password}@localhost:3306/{db_name}",
        pool_pre_ping=True
    )

    # Création de la session ORM
    Session = sessionmaker(bind=engine)
    session = Session()

    # Récupération de tous les objets State dont le nom contient 'a'
    states_to_delet = session.query(State).filter(State.name.like('%a%')).all()

    # Suppression de chaque objet individuellement
    for state in states_to_delet:
        session.delete(state)

    # Envoi des suppressions à la base
    session.commit()

    # Fermeture propre de la session
    session.close()
