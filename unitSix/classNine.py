import pygame
import random

pygame.init()

sc = pygame.display.set_mode((500, 500))

pygame.display.set_caption("Movement Boundaries Example")

x = 50
y = 50
width = 50
height = 50
vel = 5

obstacles = [
    [pygame.Rect(100,100,25,25),(100,100,100)], # Pole
    [pygame.Rect(400,200,50,200),(50,50,50)], # Wall
    [pygame.Rect(150,250,100,100),(0,255,0)] # Green thing you should not touch
]  
run = True
clock = pygame.time.Clock()

while run:

    clock.tick(30)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False

    keys = pygame.key.get_pressed()

    oldx = x
    oldy = y

    if keys[pygame.K_LEFT] or keys[pygame.K_a] and x > 0: 
        x -= vel
    if keys[pygame.K_RIGHT] or keys[pygame.K_d] and x < 500 - width:
        x += vel
    if keys[pygame.K_UP] or keys[pygame.K_w] and y > 0:
        y -= vel
    if keys[pygame.K_DOWN] or keys[pygame.K_s] and y < 500 - height:
        y += vel
    if keys[pygame.K_r]:
        x = random.randint(0,400)
        y = random.randint(0,400)

        pygame.time.wait(1000)

    sc.fill((0,0,0))

    playerRect = pygame.Rect(x, y, width, height)

    for shape, color in obstacles:
        pygame.draw.rect(sc,color,shape)

    for shape, color in obstacles:
        if playerRect.colliderect(shape):
            x = oldx
            y = oldy

            playerRect = pygame.Rect(x, y, width, height)

    pygame.draw.rect(sc, (255, 0, 0), playerRect)

    pygame.display.update()

pygame.quit()