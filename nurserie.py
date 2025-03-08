import pygame
from random import randint
from chat_repro import Chat
from reproduction import ChatPrevision, affcihage_stat

class Nurserie:
    def __init__(self, screen, game):
        self.game = game
        self.screen = screen
        self.clock = pygame.time.Clock()
        self.running = True
        self.all_chat = pygame.sprite.Group()
        self.bg = pygame.image.load("asset/bg_3.png")
        self.return_home = pygame.image.load("asset/home.png")
        self.return_home_rect = pygame.Rect(1250, 20, 100, 100)
        self.case = 0
        self.y = 0
        self.suite_y = 0
        self.animation = 0
        self.nouveaux_ne = 0
        self.valider = pygame.image.load("asset/valider.png")
        self.valider = pygame.transform.scale(self.valider, (150, 150))
        self.valider_rect = self.valider.get_rect(center=(690, 500))
        self.repro = [0, 0]
        self.male = False
        self.femelle = False
    
                

    def handlings_events(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT or event.type == pygame.K_ESCAPE:
                for chat in self.all_chat:
                    if chat.rect.y == 5:
                        if self.femelle and chat.rect.x == 1050:
                            self.repro[1] = chat.ID
                        if self.male and chat.rect.x == 100:
                            self.repro[0] = chat.ID
                self.running = False
            elif event.type == pygame.MOUSEBUTTONDOWN:
                if event.button == 1:
                    if self.return_home_rect.collidepoint(event.pos):
                        for chat in self.all_chat:
                            if chat.rect.y == 5:
                                if self.male and chat.rect.x == 100:
                                    self.repro[0] = chat.ID
                                if self.femelle and chat.rect.x == 1050:
                                    self.repro[1] = chat.ID
                        self.running = False
                    elif self.valider_rect.collidepoint(event.pos):
                        self.nouveaux_ne.reproduction_lance = True
                    for chat in self.all_chat:
                        if chat.rect.collidepoint(event.pos) and chat.stat_durabilité != 0:
                            if chat.stat_genre == 'male':
                                if not self.male:
                                    chat.rect = chat.image.get_rect(x=100, y=5)
                                    self.male = True
                                    if self.femelle:
                                        self.nouveaux_ne = ChatPrevision(self.all_chat)
                                        self.game.new_born(self.nouveaux_ne)
                                elif chat.rect.y == 5:
                                    chat.rect = chat.image.get_rect(x=250 * (chat.suite + self.case), y=550 + self.suite_y)        
                                    self.male = False
                                    self.nouveaux_ne = 0
                            elif chat.stat_genre == 'femelle':
                                if not self.femelle:
                                    chat.rect = chat.image.get_rect(x=1050, y=5)
                                    self.femelle = True
                                    if self.male:
                                        self.nouveaux_ne = ChatPrevision(self.all_chat)
                                        self.game.new_born(self.nouveaux_ne)
                                elif chat.rect.y == 5:
                                    chat.rect = chat.image.get_rect(x=250 * (chat.suite + self.case), y=550 + self.suite_y)
                                    self.femelle = False
                                    self.nouveaux_ne = 0
            elif event.type == pygame.MOUSEWHEEL and self.suite_y == 0:
                if event.y > 0 and self.case >= -6.2:
                    self.case -= 0.2
                elif self.case <= -0.2 and event.y < 0:
                    self.case += 0.2
            elif event.type == pygame.MOUSEMOTION:
                _, self.y = pygame.mouse.get_pos()
            
    def update(self):
        if self.nouveaux_ne != 0:
            if self.nouveaux_ne.temps <= 0:
                self.nouveaux_ne = 0
                self.male = False
                self.femelle = False
                for chat in self.all_chat:
                    chat.rect = chat.image.get_rect(x=250 * (chat.suite + self.case), y=550 + self.suite_y)
        self.time += 5
        if self.animation == 1:
            self.suite_y -= 20
            if self.suite_y == 0:
                self.animation = 0
        elif self.animation == 2:
            self.suite_y += 20
            if self.suite_y == 260:
                self.animation = 0
        else:
            if self.y > 650 and self.suite_y > 0 and self.animation == 0:
                self.animation = 1
            if self.y < 500 and self.suite_y < 250:
                self.animation = 2
        
    def display(self):
        self.screen.blit(self.bg, (0, 0))
        self.screen.blit(self.return_home, self.return_home_rect)
        affcihage_stat(self.screen, False, 100, 5)
        affcihage_stat(self.screen, False, 1050, 5)
        if self.male and self.femelle and self.nouveaux_ne != 0:
            if not self.nouveaux_ne.reproduction_lance:
                self.screen.blit(self.valider, self.valider_rect)
        for chat in self.all_chat:
            if chat.rect.y != 5:
                chat.rect = chat.image.get_rect(x=240 * (chat.suite + self.case), y=550 + self.suite_y)
            else:
                if chat.rect.x == 100:
                    affcihage_stat(self.screen, chat, 100, 5)
                elif chat.rect.x == 1050:
                    affcihage_stat(self.screen, chat, 1050, 5)
            chat.draw(self.screen, self.case, self.suite_y)
        if self.nouveaux_ne != 0:
            self.nouveaux_ne.draw(self.screen)
        pygame.display.flip()

    def run(self, all_chat, time, liste, nouveau_ne):
        self.time = time
        a = 0
        for i in all_chat:
            self.all_chat.add(Chat(i.rank_nb, i.numero, i.iv, a, i.sexe, i.ID))
            a += 1
        self.male = False
        self.femelle = False
        for chat in self.all_chat:
            if chat.ID == liste[0]:
                self.male = True
                chat.rect = chat.image.get_rect(x=100, y=5)
            elif chat.ID == liste[1]:
                self.femelle = True
                chat.rect = chat.image.get_rect(x=1050, y=5)
        if self.male and self.femelle:
            self.nouveaux_ne = nouveau_ne
        
        while not a == 12:
            self.all_chat.add(Chat(-1, 0, 0, a, 0, 0))
            a += 1
        while self.running:
            self.handlings_events()
            self.update()
            self.display()
            self.clock.tick(100)
        time = self.time
