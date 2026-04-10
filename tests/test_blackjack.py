from src.blackjack import Blackjack
from src.carte import Carte

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
    
def test_croupier_pioche():
    jeu = Blackjack()
    jeu.distribuer_cartes()
    jeu.croupier_pioche()
    assert len(jeu.croupier.main) >= 2
    assert len(jeu.paquet.cartes) >= 48
    
def test_resultat():
    jeu = Blackjack()
    jeu.joueur.ajouter_carte(Carte(3, "Pique"))
    jeu.joueur.ajouter_carte(Carte(1, "Coeur"))
    jeu.croupier.ajouter_carte(Carte(10, "Trèfle"))
    jeu.croupier.ajouter_carte(Carte(10, "Carreau"))
    assert jeu.resultat() == "Croupier gagne"
    
    jeu = Blackjack()
    jeu.joueur.ajouter_carte(Carte(10, "Pique"))
    jeu.joueur.ajouter_carte(Carte(10, "Coeur"))
    jeu.croupier.ajouter_carte(Carte(9, "Trèfle"))
    jeu.croupier.ajouter_carte(Carte(6, "Carreau"))
    assert jeu.resultat() == "Joueur gagne"
    
    jeu = Blackjack()
    jeu.joueur.ajouter_carte(Carte(10, "Pique"))
    jeu.joueur.ajouter_carte(Carte(10, "Coeur"))
    jeu.croupier.ajouter_carte(Carte(10, "Trèfle"))
    jeu.croupier.ajouter_carte(Carte(10, "Carreau"))
    assert jeu.resultat() == "Égalité"