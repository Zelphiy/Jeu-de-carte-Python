import pytest
from src.carte import Carte

def test_creation_carte():
    carte = Carte(10, "Coeur")
    assert carte.valeur == 10
    assert carte.couleur == "Coeur"