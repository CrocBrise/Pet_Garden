import pygame
from game import Game
from start import Start
pygame.init()
screen = pygame.display.set_mode()
pygame.display.set_caption("Eleve tes propres animaux")  # Titre de la fenêtre
#pygame.display.set_icon(pygame.image.load("asset/icone.png")) #Icone de la fenetre
start = Start(screen) #Ecran de debut avec le bouton start
start.run() #Lancement de l'ecran
game = Game(screen)#Boucle du jeu
game.run() #Lancement du jeu
pygame.quit()
