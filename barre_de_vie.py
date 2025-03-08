import pygame
pygame.init()

class Health_bar(pygame.sprite.Sprite):
    def __init__(self, max_health):
        super().__init__()
        self.font = pygame.font.SysFont('Arial', 20)
        self.max_health = max_health
        

    def draw(self, screen, health, x, y, largeur, hauteur):
        rect = pygame.rect.Rect(x, y, largeur, hauteur)
        pygame.draw.rect(screen, 'red', rect)
        rect = pygame.rect.Rect(x, y, largeur * health / self.max_health, hauteur)
        pygame.draw.rect(screen, 'green', rect)
        pourcentage = f'{round(health / self.max_health * 100)}%'
        text = self.font.render(pourcentage, True, (0, 0, 0))
        screen.blit(text, (x + largeur - 40, y - 30))
