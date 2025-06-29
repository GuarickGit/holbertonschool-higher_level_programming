#!/usr/bin/python3
"""
Ce script affiche toutes les villes de la base, avec leur état associé,
triées par id croissant.
"""

import sys
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from model_state import Base, State
from model_city import City

if __name__ == "__main__":
    # Récupération des identifiants MySQL
    username = sys.argv[1]
    password = sys.argv[2]
    db_name = sys.argv[3]

    # Connexion à la base de données
    engine = create_engine(
        f"mysql+mysqldb://{username}:{password}@localhost:3306/{db_name}",
        pool_pre_ping=True
    )

    # Création d'une session ORM
    Session = sessionmaker(bind=engine)
    session = Session()

    # Requête avec jointure entre City et State
    results = (
        session.query(City, State)
        .join(State, City.state_id == State.id)
        .order_by(City.id)
        .all()
    )

    # Affichage
    for city, state in results:
        print(f"{state.name}: ({city.id}) {city.name}")

    # Fermeture de la session
    session.close()
