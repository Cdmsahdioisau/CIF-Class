import pygame
import sys
import keyboard

pygame.init()

sc = pygame.display.set_mode((400,400))

clock = pygame.time.Clock()

FPS = 30

white = (255,255,255)
black = (0,0,0)

speed = 30

moveRect = pygame.draw.rect(sc, white,(0, 0, 100, 100))

print("past while loop")
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

    sc.fill(black)

    if keyboard.is_pressed("d"):
        moveRect.x += speed
    elif keyboard.is_pressed("a"):
        moveRect.x -= speed
    elif keyboard.is_pressed("w"):
        moveRect.y -= speed
    elif keyboard.is_pressed("s"):
        moveRect.y += speed

    moveRect.clamp_ip(sc.get_rect())

    pygame.draw.rect(sc, white, moveRect)

    pygame.display.flip()

    clock.tick(FPS)

