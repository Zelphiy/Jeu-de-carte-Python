from src.paquet import Paquet

def test_creation_paquet():
    paquet = Paquet()
    assert len(paquet.cartes) == 52