import pygame

class Ino(pygame.sprite.Sprite):
    #class for inos

    def __init__(self, screen):
        #creating inos and puting them on their position
        super(Ino, self).__init__()
        self.screen = screen
        self.image = pygame.image.load('/Users/vladberezhnyi/Desktop/programming/space defenders/images/ino.png')
        self.rect = self.image.get_rect()
        self.rect.x = self.rect.width
        self.rect.y = self.rect.height
        self.x = float(self.rect.x)
        self.y = float(self.rect.y)

    def draw(self):
        #inputing inos to screen
        self.screen.blit(self.image, self.rect)

    def update(self):
        #inos moves
        self.y += 0.1
        self.rect.y = self.y
