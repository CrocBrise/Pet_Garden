import pygame
from random import randint
class Chat(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.x = 1300 if randint(1, 2) % 2 == 0 else -100
        self.y = 505
        aléatoire = randint(1, 100)
        if aléatoire <= 40:
            self.rarety = 'E'
            nb = 4
        elif aléatoire <= 65:
            self.rarety = 'D'
            nb = 3
        elif aléatoire <= 83:
            self.rarety = 'C'
            nb = 2
        elif aléatoire <= 95:
            self.rarety = 'B'
            nb = 2
        else:
            self.rarety = 'A'
            nb = 1
        self.numero = randint(1, nb)
        self.image = pygame.image.load("asset/chat/chat_{0}/{0}{1}_debout.png".format(self.rarety, self.numero))
        self.orignal = self.image
        self.image_profil = pygame.image.load("asset/chat/chat_{0}/profil_{0}{1}_debout.png".format(self.rarety, self.numero))
        self.carte = pygame.image.load("asset/carte_{0}.png".format(self.rarety))
        self.rect = self.image.get_rect(x=self.x, y=self.y)
        self.running = True
        self.point_x = randint(300, 1000)
        self.animation = False
        self.animation_pos = 0
        self.time = 0
        self.objectif_time = 0
        self.velocity = randint(1, 3)
    
    
    def move(self, group, nb):
        self.time += 1
        if not self.animation:
            if self.time % 2 == 0:
                if not abs(self.rect.x - self.point_x) <= 4:
                    if self.rect.x < -100 or self.rect.x > 1361:
                        self.kill()
                        nb -= 1
                        group.remove(self)
                    elif self.rect.x < self.point_x:
                        self.rect.move_ip(self.velocity, 0)
                        self.image = pygame.transform.flip(self.orignal, True, False)
                    else:
                        self.rect.move_ip(self.velocity * -1, 0)
                        self.image = pygame.transform.flip(self.orignal, False, False)
                else:
                    self.animation = True
                    self.animation_pos = 'allongé' if randint(1, 3) == 1 else 'observe'
                    self.objectif_time = randint(500, 1500)
                    self.time = 0
                    self.image = pygame.image.load("asset/chat/chat_{0}/{0}{1}_{2}.png".format(self.rarety, self.numero, self.animation_pos))
                
        else:
            if self.objectif_time <= self.time:
                self.animation = False
                self.image = pygame.image.load("asset/chat/chat_{0}/{0}{1}_debout.png".format(self.rarety, self.numero))
                if randint(1, 3) == 1:
                    self.point_x = 1361 if randint(1, 2) % 2 == 0 else -101
                else:
                    self.point_x = randint(100, 300)
                self.velocity = randint(1, 3)
                self.time = 0
                
        
    def draw(self, screen):
        screen.blit(self.image, self.rect)