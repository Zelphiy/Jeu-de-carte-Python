from src.paquet import Paquet
from src.joueur import Joueur

class Blackjack:
    def __init__(self):
        self.paquet = Paquet()
        self.paquet.melanger()
        self.joueur = Joueur("Joueur")
        self.croupier = Joueur("Croupier")
        
    def distribuer_cartes(self):
        for _ in range(2):
            self.joueur.ajouter_carte(self.paquet.piocher())
            self.croupier.ajouter_carte(self.paquet.piocher())
            
    def joueur_pioche(self):
        self.joueur.ajouter_carte(self.paquet.piocher())
        
    def croupier_pioche(self):
        while self.croupier.score() < 17:
            self.croupier.ajouter_carte(self.paquet.piocher())
    