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