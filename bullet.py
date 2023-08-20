import pygame
from pygame.sprite import Sprite

class Bullet(Sprite):
    def __init__(self,aliengame):
        super().__init__()
        self.screen = aliengame.screen
        self.settings = aliengame.settings
        self.color = self.settings.bulletcolor


        self.rect= pygame.Rect(0,0,self.settings.bulletwidth,self.settings.bulletheight)

        self.rect.midtop = aliengame.ship.rect.midtop

        self.y= float(self.rect.y)
    def moveupdate(self):
        self.y -= self.settings.bulletspeed
        self.rect.y = self.y
    def drawbullet(self):
        pygame.draw.rect(self.screen,self.color,self.rect)

