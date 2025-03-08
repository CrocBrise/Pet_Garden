import pygame
from math import floor
from random import randint
pygame.init()

class Chat(pygame.sprite.Sprite):
    def __init__(self, rank, numero, iv, suite : int, sexe, ID):
        super().__init__()
        """
        rank : int
        Son rank donc 0 = A ; 1 = B
        numero : int
        Son numéro pour retrouver le fichier
        attack, defens, pv, durabilité : float
        Ses stats
        Time : temps général pour la repro
        """
        self.font = pygame.font.SysFont('Arial', 30)
        self.ID = ID
        self.rank = rank
        self.rarety = ['A', 'B', 'C', 'D', 'E']
        self.rarety = self.rarety[self.rank]
        self.numero = numero
        self.suite = suite
        if rank != -1:
            self.position = 'observe'
            self.stat_attack = iv['attack']
            self.stat_defens = iv["defens"]
            self.stat_pv = iv["pv"]
            self.stat_vitesse = iv["vitesse"]
            self.stat_durabilité = iv["durabilité"]
            self.image = pygame.image.load("asset/chat/chat_{0}/{0}{1}_{2}.png".format(self.rarety, self.numero, self.position))
            self.image = pygame.transform.scale(self.image, (250, 250))
            self.sexe = sexe
            self.sexe_image = pygame.image.load("asset/{0}.png".format(self.sexe))
            self.sexe_image = pygame.transform.scale(self.sexe_image, (50, 50))
            self.stat_genre = 'male' if 'masculin' == self.sexe else 'femelle'
        else:
            self.image = pygame.image.load("asset/absence.png")
        self.rect = self.image.get_rect(x=240 * self.suite, y=800)

    def draw(self, screen, suite, suite2):
        self.rect_rectangle = pygame.Rect(240 * (self.suite + suite), 525 + suite2, 250, 250)
        pygame.draw.rect(screen, (150, 150, 150), self.rect_rectangle)
        pygame.draw.rect(screen, (0, 0, 0), self.rect_rectangle, 10)
        screen.blit(self.image, self.rect)
        if self.rank != -1:
            screen.blit(self.sexe_image, (190 + 240 * (self.suite + suite), 550 + suite2))
        
        

    

    
