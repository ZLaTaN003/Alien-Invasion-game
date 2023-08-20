import pygame

class Settings:
   #Stores settings of game

   
   def __init__(self):
      #Screen settings
      self.screen=pygame.display.set_mode((1200,700))
     
      
      self.bg_color=(230,230,230)
      self.caption=pygame.display.set_caption("Alien_Invasion")

      #Ship settings
      self.shipspeed = 1.5

      #Bullet settings
      self.bulletspeed =  2
      self.bulletwidth =  3
      self.bulletheight = 15
      self.bulletcolor = (220,210,210)
      self.bulletallowed = 12

      #Alien
      self.alienspeed = 1.0
      self.fleetdropspeed = 10

      self.fleetdirection = 1