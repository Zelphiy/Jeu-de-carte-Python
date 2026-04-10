class Joueur:
    def __init__(self, nom):
        self.nom = nom
        self.main = []
        
    def ajouter_carte(self, carte):
        self.main.append(carte)
        
    def score(self):
        total = 0
        as_count = 0
        
        for carte in self.main:
            points = carte.points()
            
            if points > 10:
                points = 10
            elif points == 1:
                as_count += 1
                points = 11
                
            total += points
            
        while total > 21 and as_count > 0:
            total -= 10
            as_count -= 1
            
        return total
    
    def est_busted(self):
        return self.score() > 21