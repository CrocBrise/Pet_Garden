import pygame
from math import floor
from random import randint
pygame.init()
id = 0
class Chat(pygame.sprite.Sprite):
    def __init__(self, case, rarety, numero, repro):
        global id
        super().__init__()
        """
        Une case qui sera definit par deux formules pour obtenir sa loc de 1 à 12
        """
        self.font = pygame.font.SysFont('Arial', 30)
        id += 1
        self.ID = id
        self.case = case
        self.x = 325 + 184 * (self.case % 4)
        self.y = 195 + 177 * floor(self.case / 4)
        self.rank_let = rarety                          #Lettre
        self.rank_nb = ['A', 'B', 'C', 'D', 'E']        #Nombre
        self.rank_nb = self.rank_nb.index(self.rank_let)
        self.numero = numero
        aléatoire = randint(1, 3)
        if aléatoire == 1:
            self.position = 'allongé'
        elif aléatoire == 2:
            self.position = 'observe'
        else:
            self.position = 'debout'
        self.image = pygame.image.load("asset/chat/chat_{0}/{0}{1}_{2}.png".format(self.rank_let, self.numero, self.position))
        self.image_profil = pygame.image.load("asset/chat/chat_{0}/profil_{0}{1}_{2}.png".format(self.rank_let, self.numero, self.position))
        self.carte = pygame.image.load("asset/carte_{0}.png".format(self.rank_let))
        self.rect = self.image.get_rect(x=self.x, y=self.y)
        self.area = pygame.Rect(self.rect.x, self.rect.y, 150, 115)
        self.interface = False
        self.interface_rect = pygame.Rect(433, 84, 500, 600)
        self.delete_rect = pygame.Rect(840, 124, 50, 50)
        self.delete = pygame.image.load("asset/delete.png")
        self.sexe = 'masculin' if randint(1, 2) == 1 else 'feminin'
        self.sexe_image = pygame.image.load("asset/{0}.png".format(self.sexe))
        #Définition des statistiques
        self.stats = ['attack', 'defens', 'pv', 'vitesse', 'durabilité', 'age']
        if repro == 0:
            self.iv = {
                'attack' : randint(1, 5),
                'defens' : randint(1, 5),
                'pv' : randint(1, 5),
                'durabilité' : randint(1, 5),
                'vitesse' : randint(1, 5)
                }
        else:
            self.iv = {
                'attack' : repro.stat_attack,
                'defens' : repro.stat_defens,
                'pv' : repro.stat_pv,
                'durabilité' : repro.stat_durabilité,
                'vitesse' : repro.stat_vitesse
                }
        rank = abs(self.rank_nb - 5)
        self.stat_attack = self.iv['attack'] * rank
        self.stat_attack_text = self.font.render('Attaque : {}'.format(self.stat_attack), True , (0, 0, 0))
        self.stat_defens = round(self.iv['defens'] * rank / 3, 1)
        self.stat_defens_text = self.font.render('Défense : {}'.format(self.stat_defens), True , (0, 0, 0))
        self.stat_pv = self.iv['pv'] * rank * 3
        self.stat_pv_text = self.font.render('Point de vie : {}'.format(self.stat_pv), True , (0, 0, 0))
        self.stat_vitesse = self.iv['vitesse'] * rank * 1.5
        self.stat_vitesse_text = self.font.render('Vitesse : {}'.format(self.stat_vitesse), True, (0, 0, 0))
        self.stat_durabilité = self.iv['durabilité'] * rank * 10
        self.stat_durabilité_text = self.font.render('Durabilité : {}'.format(self.stat_durabilité), True, (0, 0, 0))
        self.stats_iv = {
            'attack' : self.stat_attack,
            'defens' : self.stat_defens,
            'pv' : self.stat_pv,
            'vitesse' : self.stat_vitesse
        }
        self.time = 0
        self.stat_age = 0
        self.stat_age_text = self.font.render('Age :  {}'.format(self.stat_age), True, (0, 0, 0))

    
    def interface_draw(self, screen, group, liste):
        self.time += 1
        self.stat_age = self.time // 100
        if self.stat_age > self.stat_durabilité:
            liste[self.case] = False
            self.kill()
            group.remove(self)
        if self.interface:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    self.interface = False
                if event.type == pygame.MOUSEBUTTONDOWN:
                    if not self.interface_rect.collidepoint(event.pos):
                        self.interface = False
                    elif self.delete_rect.collidepoint(event.pos):
                        liste[self.case] = False
                        self.kill()
                        group.remove(self)

            screen.blit(self.carte, (433, 84))
            screen.blit(self.sexe_image, (500, 320))
            self.stat_age_text = self.font.render('Age :  {}'.format(self.stat_age), True, (0, 0, 0))
            y = 140
            for stat in self.stats:
                text = getattr(self, f'stat_{stat}_text')
                screen.blit(text, (670, y))
                y += 50
            screen.blit(self.image_profil, (473, 134))
            screen.blit(self.delete, (840, 124))
            pygame.display.flip()
        
    def draw(self, screen):
        screen.blit(self.image, self.rect)

    

    
