import pygame
pygame.init()

class Start:
    def __init__(self, screen):
        self.screen = screen
        self.running = True
        self.clock = pygame.time.Clock()
        self.bg = pygame.image.load("asset/bg.jpg")
        self.button = pygame.image.load("asset/play.png")
        self.button_rect = self.button.get_rect(center=(670, 400))
    
    def handlings_events(self):
        for event in pygame.event.get():
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    self.running = False
            elif event.type == pygame.QUIT:
                self.running = False
            if event.type == pygame.MOUSEBUTTONDOWN:
                if self.button_rect.collidepoint(event.pos):
                    self.running = False
                
    def update(self):
        pass
        
    def display(self):
        self.screen.blit(self.bg, (0, 0))  
        self.screen.blit(self.button, self.button_rect)    
        pygame.display.flip()

    def run(self):
        while self.running:
            self.handlings_events()
            self.update()
            self.display()
            self.clock.tick(60)

