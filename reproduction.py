import pygame
from random import randint
pygame.init()


class ChatPrevision(pygame.sprite.Sprite):
    def __init__(self, all_chat):
        super().__init__()
        def calcul_iv(iv_A, iv_B):
            stat_return = 0
            while stat_return == 0:
                if randint(1, 3) == 1 and self.stat_give_A < 2:
                    self.stat_give_A += 1
                    stat_return = iv_A
                elif randint(1, 2) == 1 and self.stat_give_B < 2:
                    self.stat_give_B += 1
                    stat_return = iv_B
                elif self.stat_give_aléatoire == 0:
                    self.stat_give_aléatoire += 1
                    stat_return = randint(1, 5)
            return stat_return
        rank = ['A', 'B', 'C', 'D', 'E']
        numero_r = [1, 2, 2, 3, 4]
        self.stat_give_aléatoire = 0
        self.reproduction_lance = False
        self.temps = 6000
        self.font = pygame.font.Font(None, 40)
        for chat in all_chat:
            if chat.rect.y == 5:
                if chat.rect.x == 100:
                    stat_attack_A = chat.stat_attack
                    stat_defens_A = chat.stat_defens
                    stat_pv_A = chat.stat_pv
                    stat_durabilité_A = chat.stat_durabilité
                    self.rank_A = rank[chat.rank]
                    self.numero_A = chat.numero
                    stat_vitesse_A = chat.stat_vitesse
                    self.stat_give_A = 0
                if chat.rect.x == 1050:
                    stat_attack_B = chat.stat_attack
                    stat_defens_B = chat.stat_defens
                    stat_pv_B = chat.stat_pv
                    stat_durabilité_B = chat.stat_durabilité
                    self.rank_B = rank[chat.rank]
                    self.numero_B = chat.numero
                    stat_vitesse_B = chat.stat_vitesse
                    self.stat_give_B = 0
        self.rank = self.rank_A if randint(1, 2) == 1 else self.rank_B
        if self.numero_A == self.numero_B:
            self.numero = self.numero_B
        else:
            self.numero = randint(1, numero_r[rank.index(self.rank)])
        self.stat_attack = calcul_iv(stat_attack_A, stat_attack_B)
        self.stat_defens = calcul_iv(stat_defens_A, stat_defens_B)
        self.stat_pv = calcul_iv(stat_pv_A, stat_pv_B)
        self.stat_durabilité = calcul_iv(stat_durabilité_A, stat_durabilité_B)
        self.stat_vitesse = calcul_iv(stat_vitesse_A, stat_vitesse_B)
        self.stat_genre = 'male' if randint(1, 2) == 1 else 'femelle'
        self.image = pygame.image.load("asset/chat/chat_{0}/{0}{1}_observe.png".format(self.rank, self.numero))
        self.rect = self.image.get_rect(x=625, y=150)

    def draw(self, screen):
        screen.blit(self.image, self.rect)
        if self.reproduction_lance:
            screen.blit(self.font.render(f'{self.temps / 100}s', True, (0, 0, 0)), (self.rect.x + 10, self.rect.y + 250))
            self.temps -= 5

def affcihage_stat(screen, chat, x_chat, y_chat):
    x = x_chat
    y = y_chat
    y += 250
    x -= 50
    images = {
        'attack': pygame.transform.scale(pygame.image.load("asset/stat/attack.png"), (40, 40)),
        'defens': pygame.transform.scale(pygame.image.load("asset/stat/defens.png"), (40, 40)),
        'pv': pygame.transform.scale(pygame.image.load("asset/stat/pv.png"), (40, 40)),
        'durabilité': pygame.transform.scale(pygame.image.load("asset/stat/age.png"), (40, 40)),
        'vitesse' : pygame.transform.scale(pygame.image.load("asset/stat/vitesse.png"), (40, 40)),
        'genre': pygame.transform.scale(pygame.image.load("asset/stat/genre.png"), (40, 40))
    }

    stats = ['attack', 'defens', 'pv', 'durabilité', 'vitesse', 'genre']
    font = pygame.font.Font(None, 40)
    for stat in stats:
        image = images[stat]
        screen.blit(image, (x, y))
        x += 50
        y += 5
        if chat != False:
            valeur_stat = getattr(chat, f'stat_{stat}')
            screen.blit(font.render(str(valeur_stat), True, (0, 0, 0)), (x, y))
        x -= 50
        y += 45