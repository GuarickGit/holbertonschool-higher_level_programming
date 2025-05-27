#!/usr/bin/python3

BaseGeometry = __import__('7-base_geometry').BaseGeometry


class Rectangle(BaseGeometry):
    """
    Classe représentant un rectangle, héritée de BaseGeometry.

    Valide les dimensions fournies lors de l’instanciation.
    """

    def __init__(self, width, height):
        """
        Initialise un nouveau rectangle après validation des dimensions.

        Args:
            width (int): La largeur du rectangle (doit être > 0).
            height (int): La hauteur du rectangle (doit être > 0).

        Raises:
            TypeError, ValueError: Si les valeurs sont invalides.
        """
        # Vérifie que width et height sont des entiers strictement positifs.
        # Utilise la méthode héritée de BaseGeometry pour centraliser
        # la logique de validation.
        # Les noms "width" et "height" sont passés pour apparaître clairement
        # dans les messages d'erreur si la validation échoue.
        self.integer_validator("width", width)
        self.integer_validator("height", height)
        self.__width = width
        self.__height = height
