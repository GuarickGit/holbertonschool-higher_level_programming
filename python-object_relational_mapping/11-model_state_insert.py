#!/usr/bin/python3
"""
Ce script ajoute l'objet State 'Louisiana' à la base de données.
Après l'ajout, il affiche l'id de l'objet nouvellement créé.
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

    # Création d'une instance de State avec le nom 'Louisiana'
    new_state = State(name="Louisiana")

    # Ajout de l'objet à la session
    session.add(new_state)

    # Envoi de la transaction dans la base (c'est là que l'id est généré)
    session.commit()

    # Affichage de l'id généré automatiquement par MySQL
    print(new_state.id)

    # Fermeture de la session
    session.close()
