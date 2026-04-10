import pytest
from src.carte import Carte

def test_creation_carte():
    carte = Carte(10, "Coeur")
    assert carte.valeur == 10
    assert carte.couleur == "Coeur"
    
def test_valeur_invalide():
    with pytest.raises(ValueError):
        Carte(14, "Coeur")
        
def test_couleur_invalide():
    with pytest.raises(ValueError):
        Carte(10, "Rouge")