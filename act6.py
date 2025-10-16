import pygame
import random
#initialize pygame
pygame.init()
#custom events IDs for color change events
SPRITE_COLOR_CHANGE_EVENT = pygame.USEREVENT + 1
BACKGROUND_COLOR_CHANGE_EVENT = pygame.USEREVENT + 2

#define basic colors using pygame.color
#background color
BLUE = pygame.Color('blue')
LIGHTBLUE = pygame.Color('lightblue')
DARKBLUE = pygame.Color('darkblue')

#sprite colors
YELLOW = pygame.Color('yellow')
MAGENTA = pygame.Color('magenta')
ORANGE = pygame.Color('orange')
WHITE = pygame.Color('white')

#sprite class representing the moving object
class sprite(pygame.sprite.spite):

    #constructor method
    def __init__(self,color,height,width):
        #call to the parent class (sprite) constructor
        super().__init__()

        #create the sprite's surface with dimensions and color
        self.image = pygame.Surface([width,height])
        self.image.fill(color)

        #get the sprite's image rect defining its position and size
        self.rect = self.image.get_rect()

        #set initial velocity with random direction
        self.velocity = [random.choice([-1,1]), random.choice([-1,1])]

    #method to update the sprite's position
    def update(self):
        #move the sprite by its velocity
        self.rect.move_ip(self.velocity)

        #flag to track if the sprite hits a boundary
        boundary_hit = False

        #check for collision with left or right boundaries and reverse direction
        if self.rect.left <= 0 or self.rect.right >= 500:
            self.velocity[0] =  -self.velocity[0]
            boundary_hit = True

        #check for collision with top or bottom boundaries and reverse direction
        if self.rect.top <= 0 or self.rect.bottom >= 400:
            self.velocity[1] =  -self.velocity[1]
            boundary_hit = True

        #if a boundary was hit, post events