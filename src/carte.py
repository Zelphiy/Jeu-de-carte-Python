class Carte:
    VALEURS = list(range(1, 11)) + ["Valet", "Dame", "Roi"]
    COULEURS = ["Coeur", "Carreau", "Trèfle", "Pique"]
    
    def __init__(self, valeur, couleur):
        self._valeur = None
        self._couleur = None
        
        self.valeur = valeur
        self.couleur = couleur
        
    @property
    def valeur(self):
        return self._valeur
    
    @valeur.setter
    def valeur(self, valeur):
        if valeur not in self.VALEURS:
            raise ValueError(f"Valeur invalide")
        self._valeur = valeur

    @property
    def couleur(self):
        return self._couleur

    @couleur.setter
    def couleur(self, couleur):
        if couleur not in self.COULEURS:
            raise ValueError(f"Couleur invalide")
        self._couleur = couleur

    def points(self):
        if isinstance(self.valeur, int):
            return self.valeur
        
        mappign = {
            "Valet": 11,
            "Dame": 12,
            "Roi": 13
        }
        return mappign[self.valeur]

    def __repr__(self):
        return f"Carte {self.valeur} de {self.couleur}"