#!/usr/bin/python3
"""
Ce script affiche l'id d'un objet State dont le nom correspond
au nom donné en argument.
Si aucun objet ne correspond, il affiche 'Not found'.
"""

import sys
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from model_state import Base, State  # Import de la classe State (table states)

if __name__ == "__main__":
    # Récupération des arguments :
    # nom d'utilisateur, mot de passe, nom de la base, nom de l'état
    username = sys.argv[1]
    password = sys.argv[2]
    db_name = sys.argv[3]
    state_name = sys.argv[4]

    # Connexion à la base de données MySQL
    engine = create_engine(
        f"mysql+mysqldb://{username}:{password}@localhost:3306/{db_name}",
        pool_pre_ping=True
    )

    # Création de la session
    Session = sessionmaker(bind=engine)
    session = Session()

    # Requête pour trouver un seul State avec un nom exact
    # (sécurité : pas d'injection SQL)
    state = session.query(State).filter(State.name == state_name).first()

    # Affichage du résultat
    if state is None:
        print("Not found")
    else:
        print(state.id)

    # Fermeture de la session
    session.close()
