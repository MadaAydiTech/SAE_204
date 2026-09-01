#Importer bibliothèque python : 
import pygame
import random

pygame.init()

#Au lieu de créer une fenêtre on crée juste une surface 4000x4000
surface = pygame.Surface((4000, 4000))

#Je définis la taille d'un grand carré = 100 pixels
grand_carre = 100

#Je fais la liste des couleurs présente sur l'oeuvre
couleur_du_tableau = ['yellow','red','orange',"brown"]
surface.fill((255,255,255))

#Je parcours en tout 40 lignes et colonne car 4000/100 = 40
for ligne in range(4000//grand_carre):
    for colonne in range(4000//grand_carre):
        if colonne % 2 == 0 and ligne % 2 == 0:
            couleur = random.choice(couleur_du_tableau)
            ordonnee = colonne * grand_carre
            abscisse = ligne * grand_carre
            pygame.draw.rect(surface, couleur, (ordonnee, abscisse, grand_carre, grand_carre))

#Je sauvegarde directement sans afficher de fenêtre
pygame.image.save(surface, "reponse.png")

pygame.quit()