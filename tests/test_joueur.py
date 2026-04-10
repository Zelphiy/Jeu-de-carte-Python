from src.joueur import Joueur

def test_creation_joueur():
    joueur = Joueur("Toto")
    assert joueur.nom == "Toto"
    assert joueur.main == []
