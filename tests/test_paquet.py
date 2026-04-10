from src.paquet import Paquet

def test_creation_paquet():
    paquet = Paquet()
    assert len(paquet.cartes) == 52
    
def test_melanger_paquet():
    paquet = Paquet()
    cartes_avant = paquet.cartes.copy()
    paquet.melanger()
    assert paquet.cartes != cartes_avant
    
def test_couper_paquet():
    paquet = Paquet()
    cartes_avant = paquet.cartes.copy()
    paquet.couper()
    assert paquet.cartes != cartes_avant
    
def test_piocher_paquet():
    paquet = Paquet()
    carte = paquet.piocher()
    assert carte is not None
    assert len(paquet.cartes) == 51