import random
from src.carte import Carte

class Paquet:
    def __init__(self):
        self.cartes = [
            Carte(valeur, couleur)
            for valeur in Carte.VALEURS
            for couleur in Carte.COULEURS
        ]
        
    def melanger(self):
        random.shuffle(self.cartes)
        
    def couper(self):
        index = random.randint(1, len(self.cartes) - 1)
        self.cartes = self.cartes[index:] + self.cartes[:index]
        
    def piocher(self):
        if not self.cartes:
            return None
        return self.cartes.pop(0)