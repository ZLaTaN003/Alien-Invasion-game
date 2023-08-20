import sys
from settings import Settings
from ship import Ship
from bullet import Bullet
from aliens import Alien
import pygame

class AlienGame:
   #Game BASIC NEED CLASS


    def __init__(self):

        pygame.init()
        
        self.clock=pygame.time.Clock()
        self.settings=Settings()
        self.background_image = pygame.image.load('images/space.jpg')
        #Called Settings Class which stores main game settings
        self.screen=(self.settings.screen)
        #screensize was set
        self.caption=(self.settings.caption)
        #Screen Caption was set
        self.ship = Ship(self)
        
        #Called Ship class 
        self.bullets = pygame.sprite.Group()
        self.aliens = pygame.sprite.Group()
        self._createfleet()
    def EventChecker(self):
              #Event for Quit
        for event in pygame.event.get():
            #If Event is X it Quits
          if event.type==pygame.QUIT:
                 sys.exit()
          elif event.type == pygame.KEYDOWN:
             self._checkkeydown(event)
                  
          elif event.type == pygame.KEYUP:
              self._checkkeyup(event)
    def _checkkeydown(self,event):
         if event.key == pygame.K_RIGHT:
                  self.ship.movingright = True
         elif event.key == pygame.K_LEFT:
                  self.ship.movingleft = True
         elif event.key == pygame.K_q:
              sys.exit()
         elif event.key == pygame.K_SPACE:
              self._firebullet()
              
    def _checkkeyup(self,event):
         if event.key == pygame.K_RIGHT:
             self.ship.movingright = False
         elif event.key == pygame.K_LEFT:
            self.ship.movingleft = False
         
    def update_screen(self):  
          self.screen.blit(self.background_image,(0,0)) 
          
          #Fills Background with color
          for bullet in self.bullets.sprites():
               bullet.drawbullet()
              
          self.ship.blitme()
          self.aliens.draw(self.screen) 
          pygame.display.flip()
          #Updates the sscreen 
          # 
          #  
    def _firebullet(self):
      if len(self.bullets)<self.settings.bulletallowed:
           newbullet = Bullet(self)
           self.bullets.add(newbullet) 


    def _updatebullets(self):
          self.bullets.update()
           #Bullet firing for all
          for bullet in self.bullets.sprites():
               bullet.moveupdate()
           #Delete Unwanted Bullets
          for bullet in self.bullets.copy():
               if bullet.rect.bottom <= 0:
                    self.bullets.remove(bullet)
          if not self.aliens:
               self._createfleet()
          collisions = pygame.sprite.groupcollide(self.bullets,self.aliens,True,True)
    def _updatealiens(self):
         self.aliens.update()
         self._checkfleetedges()
     #Fleet of Aliens
    def _createfleet(self):
          alien = Alien(self)
          self.aliens.add(alien)
          alienwidth,alienheight= alien.rect.size
          currentx,currenty = alienwidth,alienheight
          while currenty < (700-3*alienheight):
           self._createalien(currentx,currenty)
           while currentx <(1000-2*alienwidth):
            self._createalien(currentx,currenty)
            currentx += 2*alienwidth
           currentx = alienwidth
           currenty += 2*alienheight
           



      #Makes aliens
    def _createalien(self,currentx,currenty):
            newalien = Alien(self)
            newalien.x = currentx
            newalien.rect.x = currentx
            newalien.rect.y = currenty
            self.aliens.add(newalien)
            
             
    def _checkfleetedges(self):
         for a in self.aliens.sprites():
              if a.checkedge():
                   self._changefleetdirection() 

    def _changefleetdirection(self):
         for a in self.aliens.sprites():
              a.rect.y += self.settings.fleetdropspeed
         self.settings.fleetdirection *= -1
    def rungame(self):
        #MainGame 
        while True:
          self.EventChecker()
          self.ship.MoveUpdate()
          self._updatebullets()     
          self._updatealiens()
          self.update_screen()
          self.clock.tick(60)
          #Framerate of the Screen

aliengame = AlienGame()
aliengame.rungame()