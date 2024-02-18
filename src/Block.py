import pygame


class Block(pygame.sprite.Sprite):
    
    def __init__(self, color, width, height, xCordinate, yCordinate):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.Surface([width, height])
        self.image.fill(color)
        self.rect = self.image.get_rect()
        self.rect.x = xCordinate
        self.rect.y = yCordinate
        self.state = False

    def changeStateOnClick(self):
        if not pygame.mouse.get_pressed()[0]: return
        
        if self.rect.x >= pygame.mouse.get_pos()[0] or pygame.mouse.get_pos()[0] >= self.rect.x + self.rect.width: return
        if self.rect.y >= pygame.mouse.get_pos()[1] or pygame.mouse.get_pos()[1] >= self.rect.y + self.rect.height: return

        self.state = True
            
    def changeColour(self):
        if self.state:
            self.image.fill('black')        
            return
        
        self.image.fill('white')

    def draw(self, screen):
        screen.blit(self.image, self.rect)     

    def update(self):
        self.changeStateOnClick()
        self.changeColour()
        
    
