import sys
import pygame

from scripts.entities import PhysicsEntity
from scripts.utils import load_image, load_images
from scripts.tilemap import Tilemap

class Game:
    def __init__(self):
        pygame.init()

        pygame.display.set_caption('platformer') #set name of display

        self.screen = pygame.display.set_mode((640,480)) #creates window, 640, 480 is resolution

        self.display = pygame.Surface((320, 240)) # second surface for rendering. render onto this then scale up


        self.clock = pygame.time.Clock() # set time interval of 60fps for game loop

        self.movement = [False, False]

        self.assets = {
            'decor' : load_images('tiles/decor'),
            'grass' : load_images('tiles/grass'),
            'large_decor' : load_images('tiles/large_decor'),
            'stone' : load_images('tiles/stone'),
            'player': load_image('entities/player.png')
        }
        
        self.player = PhysicsEntity(self, 'player', (50,50), (8, 15))

        self.tilemap = Tilemap(self, tile_size=16)
    
    def run(self):
        while True:
            self.display.fill((14, 219, 248)) #takes rgb value and fill screen with that color, essentially a reset
            self.tilemap.render(self.display)
            self.player.update(self.tilemap, (self.movement[1] - self.movement[0], 0))
            self.player.render(self.display)

            for event in pygame.event.get(): #event is equivalent to user input
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()
                
                if event.type == pygame.KEYDOWN: #only tracks whether key is pressed down, not held down
                    if event.key == pygame.K_LEFT:
                        self.movement[0] = True
                    if event.key == pygame.K_RIGHT:
                        self.movement[1] = True
                    if event.key == pygame.K_UP:
                        self.player.velocity[1] = -3

                if event.type == pygame.KEYUP: #only tracks whether key is released, not held down
                    if event.key == pygame.K_LEFT:
                        self.movement[0] = False
                    if event.key == pygame.K_RIGHT:
                        self.movement[1] = False
            
            self.screen.blit(pygame.transform.scale(self.display, self.screen.get_size()), (0,0)) # scale up display to size of screen then lay it on top of screen
            pygame.display.update() #draw onto screen
            self.clock.tick(60) # set time interval of 60fps

Game().run()