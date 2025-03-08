import pygame
from random import randint
from chat_interieur import Chat

class Capture:
    def __init__(self, screen):
        self.screen = screen
        self.clock = pygame.time.Clock()
        self.running = True
        self.all_chat = pygame.sprite.Group()
        self.bg = pygame.image.load("asset/bg_2.png")
        self.return_home = pygame.image.load("asset/home.png")
        self.return_home_rect = pygame.Rect(1250, 20, 100, 100)
        self.time = 0
        self.next_time = 0
        self.compteur = 0
        self.viseur = pygame.image.load("asset/viseur.png")
        self.viseur_rect = pygame.Rect(500, 500, 300, 300)
        self.viseur_capture_rect = pygame.Rect(0, 0, 18, 18)
        self.info = []

    def handlings_events(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT or event.type == pygame.K_ESCAPE:
                self.running = False
            if event.type == pygame.MOUSEBUTTONDOWN:
                
                if self.return_home_rect.collidepoint(event.pos):
                    self.running = False
                for chat in self.all_chat:
                    if chat.rect.collidepoint(event.pos):
                        self.info = [chat.rarety, chat.numero]
                        chat.kill()
                        self.compteur -= 1
                        for chat in self.all_chat:
                            chat.kill()
                        bg = pygame.image.load("asset/congrulation.png")
                        self.screen.blit(bg, (0, 0))
                        chat = pygame.image.load("asset/chat/chat_{0}/{0}{1}_observe.png".format(self.info[0], self.info[1]))
                        chat = pygame.transform.scale(chat, (400, 400))
                        self.screen.blit(chat, (500, 230))
                        pygame.display.update()
                        pygame.event.clear()
                        running = True
                        while running:
                            for event_deux in pygame.event.get():
                                if event_deux.type == pygame.MOUSEBUTTONDOWN:
                                    running = False
                        self.running = False

    def update(self):
        x, y = pygame.mouse.get_pos()
        if self.time >= self.next_time:
            self.next_time = self.time + randint(100, 500)
            if self.compteur < 10:
                self.all_chat.add(Chat())
                self.compteur += 1
        for chat in self.all_chat:
            chat.move(self.all_chat, self.compteur)
        self.viseur_rect = pygame.Rect(x - 150, y - 150, 300, 300)
        self.viseur_capture_rect = pygame.Rect(x - 9, y - 9, 18, 18)

    def display(self):
        self.screen.blit(self.bg, (0, 0))
        self.screen.blit(self.return_home, self.return_home_rect)
        for chat in self.all_chat:
            chat.draw(self.screen)
        self.screen.blit(self.viseur, self.viseur_rect)
        pygame.display.flip()

    def run(self):
        while self.running:
            self.handlings_events()
            self.update()
            self.display()
            self.clock.tick(100)
            self.time += 1
