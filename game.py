import pygame
from chat import Chat
from capture import Capture
from nurserie import Nurserie
pygame.init()

class Game:
    def __init__(self, screen):
        self.font = pygame.font.SysFont('Arial', 30)
        self.repro = [0, 0]
        self.time = 0
        self.screen = screen
        self.running = True
        self.all_chat = pygame.sprite.Group()
        self.next_case = [
            False, False, False, False, 
            False, False, False, False, 
            False, False, False, False
            ]
        self.clock = pygame.time.Clock()
        self.bg = pygame.image.load("asset/bg_1.png")
        self.capture = pygame.image.load("asset/capture.png")
        self.capture_rect = self.capture.get_rect(center=(75, 200))
        self.nurserie = pygame.image.load("asset/nurserie.png")
        self.nurserie = pygame.transform.scale(self.nurserie, (95, 95))
        self.nurserie_rect = self.capture.get_rect(center=(75, 350))
        self.nurserie_fenetre = 0
        self.nouveau_ne = 0

    def handlings_events(self):
        for event in pygame.event.get():
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    self.running = False
                elif event.key == pygame.K_c:
                    for i in range(12):
                                if not self.next_case[i]:
                                    self.all_chat.add(Chat(i, 'A', 1, 0))
                                    self.next_case[i] = True
                                    break
            elif event.type == pygame.QUIT:
                self.running = False
            elif event.type == pygame.MOUSEBUTTONDOWN:
                if self.capture_rect.collidepoint(event.pos):
                    if False in self.next_case:
                        capture = Capture(self.screen)
                        capture.run()
                        if capture.info != []:
                            rarety = capture.info[0]
                            numero = capture.info[1]
                            for i in range(12):
                                if not self.next_case[i]:
                                    self.all_chat.add(Chat(i, rarety, numero, 0))
                                    self.next_case[i] = True
                                    break
                    else:
                        self.screen.blit(self.font.render('Vous possédez deja le nombre maxium de chat autorisé', True, (255, 0, 0)),(1366/ 2, 600) )
                        pygame.time.wait(2000)
                elif self.nurserie_rect.collidepoint(event.pos):
                    self.nurserie_fenetre = Nurserie(self.screen, self)
                    self.nurserie_fenetre.run(self.all_chat, self.time, self.repro, self.nouveau_ne)
                    self.repro = self.nurserie_fenetre.repro
                if all(chat.interface == False for chat in self.all_chat):
                    for chat in self.all_chat:
                        if chat.area.collidepoint(event.pos):
                                chat.interface = True
                    

    def update(self):
        self.time += 5
        if self.nouveau_ne != 0:
            self.nouveau_ne.temps -= 5
            if self.nouveau_ne.temps <= 0:
                for i in range(12):
                    if not self.next_case[i]:
                        self.all_chat.add(Chat(i, self.nouveau_ne.rank, self.nouveau_ne.numero, self.nouveau_ne))
                        self.next_case[i] = True
                        break
                self.nouveau_ne = 0
                self.repro = [0, 0]
                
    def display(self):
        self.screen.blit(self.bg, (0, 0)) 
        self.screen.blit(self.capture, self.capture_rect)
        self.screen.blit(self.nurserie, self.nurserie_rect)
        for chat in self.all_chat:
            chat.draw(self.screen)
        for chat in self.all_chat:
            chat.interface_draw(self.screen, self.all_chat, self.next_case)
        pygame.display.flip()

    def run(self):
        while self.running:
            self.handlings_events()
            self.update()
            self.display()
            self.clock.tick(100)
    
    def new_born(self, nouveau_ne):
        self.nouveau_ne = nouveau_ne

