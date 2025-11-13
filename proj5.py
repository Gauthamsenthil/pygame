import pygame, random, sys

# proj5.py - simple Pygame: player collects 7 moving enemies, score increases on collision

pygame.init()
W, H = 640, 480
screen = pygame.display.set_mode((W, H))
clock = pygame.time.Clock()
font = pygame.font.SysFont(None, 36)

# player
P = pygame.Rect(W // 2, H // 2, 30, 30)
SPEED = 5

# enemies: 7 random positions, avoid spawning on player, each has a velocity
ENEMIES = []
for _ in range(7):
    r = pygame.Rect(0, 0, 24, 24)
    while True:
        r.topleft = (random.randrange(0, W - r.w), random.randrange(0, H - r.h))
        if not r.colliderect(P):
            break
    # random velocity, avoid very slow velocities
    vx = random.choice([-1, 1]) * random.uniform(1.0, 3.0)
    vy = random.choice([-1, 1]) * random.uniform(1.0, 3.0)
    ENEMIES.append({'r': r, 'v': [vx, vy]})

score = 0

while True:
    for ev in pygame.event.get():
        if ev.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

    keys = pygame.key.get_pressed()
    if keys[pygame.K_LEFT]:
        P.x -= SPEED
    if keys[pygame.K_RIGHT]:
        P.x += SPEED
    if keys[pygame.K_UP]:
        P.y -= SPEED
    if keys[pygame.K_DOWN]:
        P.y += SPEED

    # keep on screen
    P.x = max(0, min(W - P.w, P.x))
    P.y = max(0, min(H - P.h, P.y))

    # update enemy positions and bounce off walls
    for e in ENEMIES:
        r = e['r']
        vx, vy = e['v']
        r.x += vx
        r.y += vy
        # bounce X
        if r.left < 0:
            r.left = 0
            e['v'][0] = -vx
        elif r.right > W:
            r.right = W
            e['v'][0] = -vx
        # bounce Y
        if r.top < 0:
            r.top = 0
            e['v'][1] = -vy
        elif r.bottom > H:
            r.bottom = H
            e['v'][1] = -vy

    # collisions: remove enemy and increase score (no regeneration)
    for e in ENEMIES[:]:
        if P.colliderect(e['r']):
            ENEMIES.remove(e)
            score += 1

    # draw
    screen.fill((30, 30, 30))
    pygame.draw.rect(screen, (50, 200, 50), P)  # player
    for e in ENEMIES:
        pygame.draw.rect(screen, (200, 50, 50), e['r'])  # enemies

    txt = font.render(f"Score: {score}", True, (240, 240, 240))
    screen.blit(txt, (10, 10))


    pygame.display.flip()
    clock.tick(60)