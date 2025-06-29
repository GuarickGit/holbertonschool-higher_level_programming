#!/usr/bin/python3
"""
Ce module définit la classe City, liée à la table 'cities' dans la
base de données.
"""

from sqlalchemy import Column, Integer, String, ForeignKey
# On importe Base depuis model_state, comme demandé
from model_state import Base


class City(Base):
    """
    Classe City représentant la table 'cities' avec une relation vers la
    table 'states'.
    """
    __tablename__ = 'cities'

    id = Column(Integer, primary_key=True, autoincrement=True, nullable=False)
    name = Column(String(128), nullable=False)
    state_id = Column(Integer, ForeignKey("states.id"), nullable=False)
