#Mon ancienne version (avec le clown) n'étais pas assez abstraite de ce fait j'ai réfléchis différement en supprimant certain aspect de 
#la figure de monsieur François Morellet tel que la grille donc je choisi de faire sortir les couleurs n'importe ou sur la page des 4000*4000 !
import pygame
import random

pygame.init()

#Je garde l'idée des 4000*4000 donc la taille de la figure en entier
surface = pygame.Surface((4000, 4000))
surface.fill('white')

#Je prend 9 couleurs qui seront choisi aléatoirement j'ai enlevé le blanc parce que des fois l'mage apparait en blanc même si c'est quand même intéressant
couleurs = ['yellow','red','orange','brown','blue','green','purple','pink','black']

#Je choisi le nombre de forme que je veux dans l'image ça sera chosi entre cercle et carré
nombre_de_formes = 500

#Au début j'avais gardé la grille comme dans mes autres codes (colonne%2==0) mais cétait trop régulier donc j'ai fais en sorte d'avoir plus de liberté et d'aléatoire
#au lieu de "diriger l'aléatoire" voilà le changement
for i in range(nombre_de_formes):
    #Je tire une couleur au hasard dans ma liste
    couleur = random.choice(couleurs)

    #Je tire une position complètement au hasard sur toute l'image
    x = random.randint(0, 4000)
    y = random.randint(0, 4000)

    #Je tire une taille au hasard pour la forme dans une intervalle de 25 à 90 pixel
    taille = random.randint(25, 90)

    #Je tire au hasard si je dessine un carré ou un cercle
    forme = random.randint(1, 2)

    if forme == 1:
        pygame.draw.rect(surface, couleur, (x, y, taille, taille))
    else:
        pygame.draw.circle(surface, couleur, (x, y), taille)

#Je sauvegarde le résultat dans un fichier image "reponse.png"
pygame.image.save(surface, "reponse.png")

pygame.quit()