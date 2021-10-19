'''
Class for Space Invaders Game Definitions
'''

import pygame as pg
from pygame.constants import QUIT

player_speed = 20

class SpaceInvaders:

    def __init__(self):
        
        pg.init()
        self.is_running = True
        self.screen = pg.display.set_mode((1200,700))
        pg.display.set_caption("Space Invaders")
        icon = pg.image.load("images/player.png")
        pg.display.set_icon(icon)
        self.player = None
        self.player_x = 600
        self.player_y = 600

    def start(self):
        self.mainloop()

    def set_image(self, imagename="", pos = set((0, 0))):
        image = pg.image.load(f'images/{imagename}')
        self.screen.blit(image, pos)

    def mainloop(self):

        while self.is_running:

            # Set BG Image
            self.set_image("bg.jpg", (0, 0))

            # Listen for key events
            for event in pg.event.get():
                if event.type == pg.QUIT:
                    pg.display.quit()

            pressed = pg.key.get_pressed()
                
            if pressed[pg.K_LEFT]:
                self.player_x -= player_speed

                if self.player_x <= 0:
                    self.player_x = 0
    
            if pressed[pg.K_RIGHT]:
                self.player_x += player_speed

                if self.player_x >= 1140:
                    self.player_x = 1140

            if pressed[pg.K_SPACE]:
                print("shoot")
                
            
            # Set player image 
            self.set_image("player.png", (self.player_x, self.player_y))
            pg.display.update()
            

    
