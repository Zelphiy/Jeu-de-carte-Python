from src.joueur import Joueur
from src.carte import Carte

def test_creation_joueur():
    joueur = Joueur("Toto")
    assert joueur.nom == "Toto"
    assert joueur.main == []

def test_ajouter_carte():
    joueur = Joueur("Toto")
    joueur.ajouter_carte(Carte(6, "Pique"))
    assert len(joueur.main) == 1
    
    joueur = Joueur("Toto")
    joueur.ajouter_carte(Carte("Valet", "Pique"))
    assert len(joueur.main) == 1
    
def test_score_sans_as():
    joueur = Joueur("Toto")
    joueur.ajouter_carte(Carte(6, "Pique"))
    joueur.ajouter_carte(Carte(7, "Coeur"))
    assert joueur.score() == 13

def test_score_avec_as():
    joueur = Joueur("Toto")
    joueur.ajouter_carte(Carte(1, "Pique"))
    joueur.ajouter_carte(Carte(10, "Coeur"))
    assert joueur.score() == 21
    
def test_est_busted():
    joueur = Joueur("Toto")
    joueur.ajouter_carte(Carte(10, "Pique"))
    joueur.ajouter_carte(Carte(10, "Coeur"))
    joueur.ajouter_carte(Carte(2, "Trèfle"))
    assert joueur.est_busted() == True