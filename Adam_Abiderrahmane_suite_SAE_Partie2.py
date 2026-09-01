import random
import pygame

pygame.init()
#Au lieu de créer une fenêtre on crée juste une surface 4000x4000
surface = pygame.Surface((4000, 4000))
grand_carre = 100
#Je fais la liste des couleurs présente sur l'oeuvre
couleur_du_tableau = ['yellow','red','orange','brown','blue','green','purple','pink','black','white']
surface.fill('white')
#Je parcours en tout 40 lignes et colonne car 4000/100 = 40
for ligne in range(4000//grand_carre):
    for colonne in range(4000//grand_carre):
        if colonne % 2 == 0 and ligne % 2 == 0:
            #J'ai choisi 10 couleurs que j'ai placé on en prend au hasard
            couleur = random.choice(couleur_du_tableau)
            #je prends la taille au hasard qui varie entre 25 et 90 pixels
            taille = random.randint(25,90)
            #Je les place bien dans ma fenêtre donc 100/2 = 50
            x = colonne*grand_carre + grand_carre//2
            y = ligne*grand_carre + grand_carre//2
            #Je mets un choix entre le premier paramètre donc soit avoir un carré soit avoir un cercle
            forme = random.randint(1, 2)
            if forme == 1:
                pygame.draw.rect(surface, couleur, (x - taille//2, y-taille//2, taille, taille))
            if forme == 2:
                pygame.draw.circle(surface, couleur, (x, y), taille//2)

#Je charge mon image clown (elle doit être dans le même dossier que mon code)
clown = pygame.image.load("tete_clown.png")
#Je redimensionne le clown pour qu'il fasse 2000x2000 pixels
clown = pygame.transform.scale(clown, (2000, 2000))
#Je place le clown au centre 1000 = 4000//2-2000//2 (2000 c'est le centre de la surface) et (1000 c'est la surface du clown)
surface.blit(clown, (1000, 1000))
#Je sauvegarde directement sans afficher de fenêtre
pygame.image.save(surface, "reponse.png")
pygame.quit()