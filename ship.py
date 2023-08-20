import pygame

#Make a Ship class
class Ship:

    def __init__(self,aliengame):
        #construct ship with self and a instance of aliengame which includes screen
        self.screen = aliengame.screen
        self.settings = aliengame.settings
        #Made scren rectangular
        self.screen_rect=aliengame.screen.get_rect()
        

        #making ship
        self.image=pygame.image.load("images/ship.bmp")
        #Made Ship rectangular
        self.rect = self.image.get_rect()
        
        #Made position of ship in mid bottom on screen
        self.rect.midbottom = self.screen_rect.midbottom
        self.x = float(self.rect.x)
        self.movingright = False
        self.movingleft = False
        
    def MoveUpdate(self):
        if self.movingright and self.rect.right<self.screen_rect.right:
           self.x += self.settings.shipspeed
        if self.movingleft and self.rect.left>0:
            self.x -= self.settings.shipspeed
          
        self.rect.x = self.x
    def blitme(self):
        #Drawing Ship at the Given Location
        self.screen.blit(self.image,self.rect)
