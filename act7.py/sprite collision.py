import pygame
import random

#constants for easier adjustments
SCREEN_WIDTH, SCREEN_HEIGHT = 500,400
MOVEMENT_SPEED = 5
FONT_SIZE = 72

#initialize pygame
pygame.init()

#load and transform the background image
background_image = pygame.transform.scale(pygame.image.load("image.png"),(SCREEN_WIDTH, SCREEN_HEIGHT))

#load font once at the beginning
font = pygame.font.SysFont("Times New Roman", FONT_SIZE)

class sprite(pygame.sprite.sprite):

    def __init__(self,color,height,width):
        super().__init__()
        self.image = pygame.surface([width,height])
        self.image.fill(pygame.Color('dodgerblue'))#background color of sprite
        pygame.draw.rect(self.image,color,pygame.Rect(0,0,width,height))
        self.rect = self.image.get_rect()

    def move(self, X_change, Y_change):
        self.rect.x = max(
            min(self.rect.x + X_change,SCREEN_WIDTH - self.rect.width),0)
        self.rect.y = max(
            min(self.rect.y + Y_change,SCREEN_HEIGHT - self.rect.height),0)
        

#setup
screen = pygame.display.set_mode((SCREEN_WIDTH,SCREEN_HEIGHT))
pygame.display.set_caption("Sprite Collision")
all_sprites = pygame.sprite.Group()

#Create sprites
sprite1 = sprite(pygame.Color('black'),20,30)
sprite1.rect.x,sprite1.rect.y = random.randint(
    0,SCREEN_WIDTH - sprite1.rect.width),random.randint(
        0,SCREEN_HEIGHT - sprite1.rect.height)
all_sprites.add(sprite1)

sprite2 = sprite(pygame.Color('black'),20,30)
sprite2.rect.x,sprite1.rect.y = random.randint(
    0,SCREEN_WIDTH - sprite2.rect.width),random.randint(
        0,SCREEN_HEIGHT - sprite2.rect.height)
all_sprites.add(sprite2)

