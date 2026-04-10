from src.blackjack import Blackjack

jeu = Blackjack()
jeu.distribuer_cartes()

print(" -- Blackjack -- ")

while True:
    print(f"Votre main: {jeu.joueur.main} (Score: {jeu.joueur.score()})")
    print(f"Main du croupier: [{jeu.croupier.main}, (Score: {jeu.croupier.score()})]")
    action = input("Voulez-vous piocher une carte ? (o/n) ")
    
    if action.lower() == 'o':
        jeu.joueur_pioche()
        print(f"Votre main: {jeu.joueur.main} (Score: {jeu.joueur.score()})")
        if jeu.joueur.est_busted():
            print("Vous avez dépassé 21 ! Croupier gagne.")
            break
    
    else:
        break
    
jeu.croupier_pioche()

print(f"Croupier : {jeu.croupier.main} (Score: {jeu.croupier.score()})")
print(jeu.resultat())