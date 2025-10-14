import pygame
pygame.init()
screen = pygame.display.set_mode((400,500))
done = False
while not done:
    for event in pygame.event.get():
        if event.type == pygame.quit:
            done = True
        pygame.draw.rect(screen,(0,128,0),pygame.Rect(50,50,50,50))
        
    pygame.display.flip()