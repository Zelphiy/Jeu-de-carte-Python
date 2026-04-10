class Joueur:
    def __init__(self, nom):
        self.nom = nom
        self.main = []
        
    def ajouter_carte(self, carte):
        self.main.append(carte)