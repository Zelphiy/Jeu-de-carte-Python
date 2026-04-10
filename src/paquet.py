from src.carte import Carte

class Paquet:
    def __init__(self):
        self.cartes = [
            Carte(valeur, couleur)
            for valeur in Carte.VALEURS
            for couleur in Carte.COULEURS
        ]