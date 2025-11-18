import pygame
import random

# Constants for snake adjustments
SCREEN_WIDTH, SCREEN_HEIGHT = 500, 400
MOVEMENT_SPEED = 5
FONT_SIZE = 20

# Initialize Pygame
pygame.init()

# Load and transform the background image
background_image = pygame.transform.scale(
    pygame.image.load("bg.jpg"),
    (SCREEN_WIDTH, SCREEN_HEIGHT)
)

# Load font once at the beginning
font = pygame.font.SysFont("Times New Roman", FONT_SIZE)

class Sprite(pygame.sprite.Sprite):
    def __init__(self, color, width, height):
        super().__init__()
        self.image = pygame.Surface((width, height))
        self.image.fill(color)  # Background color of sprite
        pygame.draw.rect(self.image, color, pygame.Rect(0, 0, width, height))
        self.rect = self.image.get_rect()

    def move(self, x_change, y_change):
        self.rect.x += x_change
        self.rect.y += y_change

        # Keep sprite within screen
        self.rect.x = max(0, min(self.rect.x, SCREEN_WIDTH - self.rect.width))
        self.rect.y = max(0, min(self.rect.y, SCREEN_HEIGHT - self.rect.height))

# Setup
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption("Sprite Collision")
all_sprites = pygame.sprite.Group()

# Create sprites
sprite1 = Sprite(pygame.Color("black"), 20, 30)
sprite1.rect.x = random.randint(0, SCREEN_WIDTH - sprite1.rect.width)
sprite1.rect.y = random.randint(0, SCREEN_HEIGHT - sprite1.rect.height)

sprite2 = Sprite(pygame.Color("red"), 20, 30)
sprite2.rect.x = random.randint(0, SCREEN_WIDTH - sprite2.rect.width)
sprite2.rect.y = random.randint(0, SCREEN_HEIGHT - sprite2.rect.height)

all_sprites.add(sprite1)
all_sprites.add(sprite2)

# Game loop control variables
running = True
won = False
clock = pygame.time.Clock()

# Main game loop
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

        # Key press movement
        if event.type == pygame.KEYDOWN:
            keys = pygame.key.get_pressed()
            x_change = y_change = 0

            if keys[pygame.K_LEFT]:
                x_change = -MOVEMENT_SPEED
            if keys[pygame.K_RIGHT]:
                x_change = MOVEMENT_SPEED
            if keys[pygame.K_UP]:
                y_change = -MOVEMENT_SPEED
            if keys[pygame.K_DOWN]:
                y_change = MOVEMENT_SPEED

            sprite1.move(x_change, y_change)

            # Collision check
            if pygame.sprite.collide_rect(sprite1, sprite2):
                all_sprites.remove(sprite2)
                won = True

    # Drawing
    screen.blit(background_image, (0, 0))
    all_sprites.draw(screen)

    # Winning message
    if won:
        win_text = font.render(
            "You win!", True, pygame.Color("black")
        )
        screen.blit(
            win_text,
            (SCREEN_WIDTH // 2 - win_text.get_width() // 2,
             SCREEN_HEIGHT // 2 - win_text.get_height() // 2)
        )

    pygame.display.flip()
    clock.tick(60)

pygame.quit()
