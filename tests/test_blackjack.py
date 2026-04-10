from src.blackjack import Blackjack

def test_initialisation_blackjack():
    jeu = Blackjack()
    assert jeu.joueur is not None
    assert jeu.croupier is not None
    assert len(jeu.paquet.cartes) == 52
    