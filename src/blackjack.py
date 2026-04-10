from src.paquet import Paquet
from src.joueur import Joueur

class Blackjack:
    def __init__(self):
        self.paquet = Paquet()
        self.paquet.melanger()
        self.joueur = Joueur("Joueur")
        self.croupier = Joueur("Croupier")