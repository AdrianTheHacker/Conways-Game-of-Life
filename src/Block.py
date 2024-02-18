import pygame


class Block(pygame.sprite.Sprite):
    
    def __init__(self, color, width, height, xCordinate, yCordinate):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.Surface([width, height])
        self.image.fill(color)
        self.rect = self.image.get_rect()
        self.rect.x = xCordinate
        self.rect.y = yCordinate

    def update(self):
        pass
        
    def draw(self, screen):
        self.update()
        screen.blit(self.image, self.rect)      
