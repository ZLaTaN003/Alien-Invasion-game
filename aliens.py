import pygame
from pygame.sprite import Sprite


class Alien(Sprite):

    def __init__(self,aliengame):
        super().__init__()
        self.screen = aliengame.screen
        self.settings = aliengame.settings


        
        self.image = pygame.image.load('images/alien3.bmp')
        self.rect = self.image.get_rect()


        self.rect.x = self.rect.width
        self.rect.y = self.rect.height


        self.x = float(self.rect.x)


    def checkedge(self):
        screen_rect = self.screen.get_rect()
        return (self.rect.right >= screen_rect.right) or (self.rect.left <=0)

    def update(self):
        #Move alien to Right
        self.x += self.settings.alienspeed * self.settings.fleetdirection
        self.rect.x = self.x

  