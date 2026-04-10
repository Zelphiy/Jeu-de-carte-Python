from src.blackjack import Blackjack

def test_initialisation_blackjack():
    jeu = Blackjack()
    assert jeu.joueur is not None
    assert jeu.croupier is not None
    assert len(jeu.paquet.cartes) == 52
    
def test_distribuer_cartes():
    jeu = Blackjack()
    jeu.distribuer_cartes()
    assert len(jeu.joueur.main) == 2
    assert len(jeu.croupier.main) == 2
    assert len(jeu.paquet.cartes) == 48 

def test_joueur_pioche():
    jeu = Blackjack()
    jeu.distribuer_cartes()
    jeu.joueur_pioche()
    assert len(jeu.joueur.main) == 3
    assert len(jeu.paquet.cartes) == 47