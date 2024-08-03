import sys
import pygame

class Game:
    def __init__(self):
        pygame.init()

        pygame.display.set_caption('platformer') #set name of display

        self.screen = pygame.display.set_mode((640,480)) #creates window, 640, 480 is resolution


        self.clock = pygame.time.Clock() # set time interval of 60fps for game loop

        self.img = pygame.image.load("data/images/clouds/cloud_1.png")
        self.img.set_colorkey((0,0,0)) #color to be replaced with transparency on render

        self.img_pos = [160,260]
        self.movement = [False, False]

        self.collision_area = pygame.Rect(50,50, 300, 50)
    
    def run(self):
        while True:
            self.screen.fill((14, 219, 248)) #takes rgb value and fill screen with that color, essentially a reset
             #first two args are top left position, next 2 are width and height of rectangle
            img_r = pygame.Rect(self.img_pos[0], self.img_pos[1], self.img.get_width(), self.img.get_height())
            if img_r.colliderect(self.collision_area):
                pygame.draw.rect(self.screen, (0,100,255), self.collision_area)
            else:
                pygame.draw.rect(self.screen, (0,50,155), self.collision_area)
            self.img_pos[1] += (self.movement[1] - self.movement[0]) * 5
            self.screen.blit(self.img, self.img_pos) #draw cloud at position img_pos, (0,0) starts at the top left corner, layering surfaces on top of each other
            

            for event in pygame.event.get(): #event is equivalent to user input
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()
                
                if event.type == pygame.KEYDOWN: #only tracks whether key is pressed down, not held down
                    if event.key == pygame.K_UP:
                        self.movement[0] = True
                    if event.key == pygame.K_DOWN:
                        self.movement[1] = True

                if event.type == pygame.KEYUP: #only tracks whether key is released, not held down
                    if event.key == pygame.K_UP:
                        self.movement[0] = False
                    if event.key == pygame.K_DOWN:
                        self.movement[1] = False
                

            pygame.display.update() #draw onto screen
            self.clock.tick(60) # set time interval of 60fps

Game().run()