#!/usr/bin/python3
"""
Ce module définit la classe State, qui représente une table 'states'
dans une base de données MySQL.
Il crée également une instance Base utilisée comme base pour toutes
les classes ORM avec SQLAlchemy.
"""

# On importe les objets nécessaires pour décrire les colonnes de la table.
from sqlalchemy import Column, Integer, String

# On importe la fonction qui permet de créer la classe de base de toutes les
# classes ORM.
from sqlalchemy.ext.declarative import declarative_base

# Création de la classe de base à partir de laquelle toutes les tables seront
# dérivées.
# Toutes les classes représentant des tables devront hériter de Base.
Base = declarative_base()


# Définition de la classe State, qui représentera la table 'states'
# dans la base de données.
class State(Base):
    """
    Classe State représentant la table 'states' dans la base de données.
    Chaque instance de cette classe correspondra à une ligne dans la table.
    """
    # Nom de la table dans la base de données MySQL
    __tablename__ = 'states'

    # Définition de la colonne 'id'
    # - Integer : type entier
    # - primary_key=True : clé primaire de la table
    # - autoincrement=True : auto-incrémentée automatiquement par MySQL
    # - nullable=False : cette colonne ne peut pas être NULL
    id = Column(Integer, primary_key=True, autoincrement=True, nullable=False)

    # Définition de la colonne 'name'
    # - String(128) : chaîne de caractères, max 128 caractères
    # - nullable=False : cette colonne ne peut pas être NULL
    name = Column(String(128), nullable=False)
