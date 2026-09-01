import os
#Je mets une sorte de sécurité qui m'oblige à faire marcher mon oreuvre 
os.environ["SDL_VIDEODRIVER"] = "dummy"

import random
import pygame

pygame.init()
surface = pygame.Surface((600, 600))

grand_carre = 15

#Je fais la liste des couleurs présente sur l'oeuvre
couleur_du_tableau = ['yellow', 'red', 'orange', 'brown','blue', 'green', 'purple', 'pink','black', 'white']

surface.fill('white')

for ligne in range(600 // grand_carre):
    for colonne in range(600 // grand_carre):
        if colonne % 2 == 0 and ligne % 2 == 0:

            #Sur les 10 couleurs que j'ai placé on en prend au hasard
            couleur = random.choice(couleur_du_tableau)

            #La taille on la prend au hasard entre 3 et 16 pixels
            taille = random.randint(4, 14)

            #Je les place bien dans ma fenêtre
            x = colonne*grand_carre + grand_carre// 2
            y = ligne*grand_carre + grand_carre// 2

            #Je mets un choix entre le premier paramètre donc soit avoir un carré soit avoir un cercle
            forme = random.randint(1, 2)

            if forme == 1:
                pygame.draw.rect(surface, couleur, (x - taille//2, y-taille//2, taille, taille))

            if forme == 2:
                pygame.draw.circle(surface, couleur, (x, y), taille//2)

#Je charge mon image clown (elle doit être dans le même dossier que mon code)
clown = pygame.image.load("tete_clown.png")

#Je redimensionne le clown pour qu'il fasse 300x300 pixels pour avoir pile la taille que je veux au milieu assez grand mais pas trop non plus
clown = pygame.transform.scale(clown, (300, 300))

#Je place le clown au centre de ma fenetre 600x600
# 150 c'est 600//2-300//2 = 150 pour le centrer donc je le dessine après la boucle pour le faire apparaitre au dessus de mes formes géométriques
surface.blit(clown, (150, 150))

#Je sauvegarde mon image en PNG pour l'afficher sur mon site web
pygame.image.save(surface, "reponse.png")

pygame.quit()