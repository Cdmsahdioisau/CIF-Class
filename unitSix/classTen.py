import pygame
import random

pygame.init()
sc = pygame.display.set_mode((500, 500))
pygame.display.set_caption("Game")

x = 50
y = 300
width = 30
height = 40
velx = 5
vely = 0
accel = 0
gravity = 1
jump_power = -15
moveSpeed = 2
touchingGround = False
movedLeft = False
movedRight = False
gameState = "live"
deathCause = ""
font25 = pygame.font.Font(None, 25)
font50 = pygame.font.Font(None, 50)
font75 = pygame.font.Font(None, 75)

part = [
    [pygame.Rect(100, 25, 25, 75), (50, 50, 50)], # Pipe Mouth
    [pygame.Rect(0, 37.5, 100, 50), (50, 50, 50)], # Pipe Body
    [pygame.Rect(400, 200, 50, 200), (50, 50, 50)], # Wall
    [pygame.Rect(0, 450, 300, 50), (100, 30, 30)], # Floor
    [pygame.Rect(150, 300, 100, 75), (50, 50, 50)], # Slip Part Base
    [pygame.Rect(125, 350, 125, 25), (50, 50, 50)], # Tunnel Roof
]

movePart = [
    {"shape": pygame.Rect(350, 350, 50, 25), "color": (120, 50, 50), "stopLeft": 250, "stopRight": 400, "speed": 3}, # Plat
]

coins = [
    [pygame.Rect(187.5, 200, 25, 25), (255, 255, 0)], # Ice Coin
    [pygame.Rect(412.5, 150, 25, 25), (255, 255, 0)], # Wall Coin
    [pygame.Rect(412.5, 0, 25, 25), (255, 255, 0)], # Air Coin
]

slipPart = [
    [pygame.Rect(150, 275, 100, 25), (0, 255, 0)], # Slip Part
]

lavaPart = [
    [pygame.Rect(300, 460, 200, 40), (255, 0, 0)], # Floor lavaPart
    [pygame.Rect(125, 50, 25, 300), (255, 0, 0)] # Pipe lavaPart
]

pusherPart = [
    {"shape": pygame.Rect(500, 150, 25, 50), "color": (120, 50, 50), "stopLeft": 400, "stopRight": 500, "speed": 3, "leftSpeed": -11, "rightSpeed": 1}, # Plat
]

backgroundPart = [
    [pygame.Rect(350, 300, 25, 160), (100, 0, 0)], # Background Lava
    [pygame.Rect(125, 350, 25, 100), (100, 0, 0)], # Pipe Lava
    [pygame.Rect(150, 375, 100, 75), (25, 25, 25)], # Slip Part Tunnel
]

# Player Image :D
try:
    playerPNG = pygame.image.load("player.png").convert_alpha()
    playerPNG = pygame.transform.scale(playerPNG, (width, height))
except pygame.error:
    playerPNG = pygame.Surface((width, height))
    playerPNG.fill((255, 255, 255))

run = True
clock = pygame.time.Clock()

while run:
    clock.tick(30)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False

    keys = pygame.key.get_pressed()

    mousePos = pygame.mouse.get_pos()
    clicked = pygame.mouse.get_pressed()

    moveCollidable = movePart + pusherPart
    allObjects = backgroundPart + part + [
        [movingPart["shape"], movingPart["color"]] for movingPart in movePart
    ] + coins + slipPart + lavaPart + [
        [movingPart["shape"], movingPart["color"]] for movingPart in pusherPart
    ]
    collidable = part + [
        [movingPart["shape"], movingPart["color"]] for movingPart in movePart
    ] + slipPart + [
        [movingPart["shape"], movingPart["color"]] for movingPart in pusherPart
    ]
    killObjects = lavaPart
    collectable = coins

    if gameState == "live":
        if (keys[pygame.K_m]):
            print("M")
            gameState = "menu"
        # Gravity
        vely += gravity
        if (keys[pygame.K_UP] or keys[pygame.K_w]) and touchingGround:
            vely = jump_power
            touchingGround = False

        # Keys
        moveLeft = keys[pygame.K_LEFT] or keys[pygame.K_a]
        moveRight = keys[pygame.K_RIGHT] or keys[pygame.K_d]

        # Player Hitbox
        playerRect = pygame.Rect(x, y, width, height)

        # THIS TOOK WAY TOO LONG
        onIce = touchingGround and any(playerRect.bottom == shape.top for shape, color in slipPart)
        if onIce:
            velx = 3
        else:
            velx = 5
        if moveLeft and x > 0:
            playerRect.x -= velx + accel
        if moveRight and x < 500 - width:
            playerRect.x += velx + accel
        if (movedLeft == True and moveRight) or (movedRight == True and moveLeft) and onIce:
            accel = 0
        if onIce and (moveLeft or moveRight):
            accel = min(accel + 0.5, 8) 
        else:
            accel = max(accel - 0.25, 0)
        if moveLeft:
            movedLeft = True
            movedRight = False
        if moveRight:
            movedLeft = False
            movedRight = True
        if movedLeft and not movedRight:
            if x > 0:
                playerRect.x -= accel
        if movedRight and not movedLeft:
            if x < 500 - width:
                playerRect.x += accel

        # X Collision
        for shape, color in collidable:
            if playerRect.colliderect(shape):
                if (moveRight or accel > 0) and playerRect.right > shape.left and playerRect.right < shape.right:
                    playerRect.right = shape.left
                if (moveLeft or accel > 0) and playerRect.left < shape.right and playerRect.left > shape.left:
                    playerRect.left = shape.right

        x = playerRect.x # Save clean X coordinates

        # 2. Move and Resolve Y-Axis
        prevTop = playerRect.top
        prevBottom = playerRect.bottom
        playerRect.y += vely
        touchingGround = False

        # Y Collision 
        for shape, color in collidable:
            if playerRect.left < shape.right and playerRect.right > shape.left:
                if vely > 0 and prevBottom <= shape.top and playerRect.bottom >= shape.top:
                    playerRect.bottom = shape.top
                    vely = 0
                    touchingGround = True
                elif vely < 0 and prevTop >= shape.bottom and playerRect.top <= shape.bottom:
                    playerRect.top = shape.bottom
                    vely = 0

        # Screen stuff
        if playerRect.bottom > 500:
            playerRect.bottom = 500
            vely = 0
            touchingGround = True

        y = playerRect.y # Save Y coordinates

        # Move Platforms
        for movingPart in movePart:
            shape = movingPart["shape"]
            stopLeft = movingPart["stopLeft"]
            stopRight = movingPart["stopRight"]
            speed = movingPart["speed"]
            previousX = shape.x
            shape.x += speed
            if shape.right > stopRight or shape.left < stopLeft:
                movingPart["speed"] *= -1
            movement = shape.x - previousX
            if movement != 0 and playerRect.colliderect(shape):
                if movement > 0:
                    playerRect.left = shape.right
                else:
                    playerRect.right = shape.left
                playerRect.clamp_ip(sc.get_rect())
                x = playerRect.x

        # Pusher Platforms
        for movingPart in pusherPart:
            shape = movingPart["shape"]
            stopLeft = movingPart["stopLeft"]
            stopRight = movingPart["stopRight"]
            speed = movingPart["speed"]
            previousX = shape.x
            shape.x += speed
            if shape.right > stopRight:
                shape.right = stopRight
                movingPart["speed"] = movingPart["leftSpeed"]
            elif shape.left < stopLeft:
                shape.left = stopLeft
                movingPart["speed"] = movingPart["rightSpeed"]

            movement = shape.x - previousX
            if movement != 0 and playerRect.colliderect(shape):
                if movement > 0:
                    playerRect.left = shape.right
                    movedRight = True
                    movedLeft = False
                else:
                    playerRect.right = shape.left
                    movedLeft = True
                    movedRight = False
                    accel += 10
                playerRect.clamp_ip(sc.get_rect())
                x = playerRect.x


        # Lave
        for shape, color in lavaPart:
            if playerRect.colliderect(shape):
                gameState = "dead"
                deathCause = "Lava"

        # Coinzzz
        for shape, color in coins:
            if playerRect.colliderect(shape):
                coins.remove([shape, color])
                print("Coin collected!")

        if len(coins) == 0:
            print("All coins collected! You win!")
            gameState = "win"

        # --- RENDER DISPLAY ---
        if gameState == "live":
            sc.fill((50, 0, 0)) # Live Screen
        elif gameState == "dead":
            sc.fill((150, 0, 0)) # Dead Screen
        elif gameState == "win":
            sc.fill((0, 150, 0)) # Win Screen
        elif gameState == "menu":
            sc.fill((200, 200, 200)) # Menu Screen

        # Draw all objects
        for shape, color in allObjects:
            pygame.draw.rect(sc, color, shape)
    elif gameState == "dead":
        deathText = font50.render("You Died To: ", True, (255, 255, 255))
        deathCauseText = font75.render(deathCause, True, (255, 255, 255))
        
        respawnBtn = pygame.Rect(150, 350, 200, 50)
        respawnText = font50.render("Respawn", True, (0, 0, 0))

        quitBtn = pygame.Rect(150, 425, 200, 50)
        quitText = font50.render("Quit", True, (0, 0, 0))

        pygame.draw.rect(sc, (0, 200, 0), respawnBtn)
        pygame.draw.rect(sc, (200, 0, 0), quitBtn)

        sc.blit(deathText, (25, 25))
        sc.blit(deathCauseText, (25, 75))
        sc.blit(respawnText, (160, 360))  
        sc.blit(quitText, (160, 435))

        if respawnBtn.collidepoint(mousePos):
            pygame.draw.rect(sc, (0, 225, 0), respawnBtn)
            sc.blit(respawnText, (160, 360))

        if quitBtn.collidepoint(mousePos):
            pygame.draw.rect(sc, (225, 0, 0), quitBtn)
            sc.blit(quitText, (160, 435))

        if respawnBtn.collidepoint(mousePos) and clicked[0]:
            gameState = "live"
            x = 50
            y = 300
            vely = 0
            accel = 0
            touchingGround = False
            movedLeft = False
            movedRight = False
            deathCause = ""
            coins = [
                [pygame.Rect(187.5, 200, 25, 25), (255, 255, 0)], # Ice Coin
                [pygame.Rect(412.5, 150, 25, 25), (255, 255, 0)], # Wall Coin
                [pygame.Rect(412.5, 0, 25, 25), (255, 255, 0)], # Air Coin
            ]

        if quitBtn.collidepoint(mousePos) and clicked[0]:
            run = False

    elif gameState == "win":
        winText = font75.render("You Win!", True, (255, 255, 255))

        playBtn = pygame.Rect(150, 350, 200, 50)
        playText = font50.render("Play Again", True, (0, 0, 0))

        quitBtn = pygame.Rect(150, 425, 200, 50)
        quitText = font50.render("Quit", True, (0, 0, 0))

        pygame.draw.rect(sc, (0, 200, 0), playBtn)
        pygame.draw.rect(sc, (200, 0, 0), quitBtn)

        sc.blit(winText, (25, 25))
        sc.blit(playText, (160, 360))
        sc.blit(quitText, (160, 435))

        if playBtn.collidepoint(mousePos):
            pygame.draw.rect(sc, (0, 225, 0), playBtn)
            sc.blit(playText, (160, 360))

        if quitBtn.collidepoint(mousePos):
            pygame.draw.rect(sc, (225, 0, 0), quitBtn)
            sc.blit(quitText, (160, 435))

        if playBtn.collidepoint(mousePos) and clicked[0]:
            gameState = "live"
            x = 50
            y = 300
            vely = 0
            accel = 0
            touchingGround = False
            movedLeft = False
            movedRight = False
            deathCause = ""
            coins = [
                [pygame.Rect(187.5, 200, 25, 25), (255, 255, 0)], # Ice Coin
                [pygame.Rect(412.5, 150, 25, 25), (255, 255, 0)], # Wall Coin
                [pygame.Rect(412.5, 0, 25, 25), (255, 255, 0)], # Air Coin
            ]

        if quitBtn.collidepoint(mousePos) and clicked[0]:
            run = False
    if gameState == "menu":
        menuText = font25.render("WASD to move, M to open and close menu", True, (255, 255, 255))

        continueBtn = pygame.Rect(150, 350, 200, 50)
        continueText = font50.render("Play", True, (0, 0, 0))

        quitBtn = pygame.Rect(150, 425, 200, 50)
        quitText = font50.render("Quit", True, (0, 0, 0))
                
        pygame.draw.rect(sc, (0, 200, 0), continueBtn)
        pygame.draw.rect(sc, (200, 0, 0), quitBtn)

        sc.blit(menuText, (25, 25))
        sc.blit(continueText, (160, 360))
        sc.blit(quitText, (160, 435))

        if continueBtn.collidepoint(mousePos):
            pygame.draw.rect(sc, (0, 225, 0), continueBtn)
            sc.blit(continueText, (160, 360))

        if continueBtn.collidepoint(mousePos) and clicked[0]:
            gameState = "live"

        if quitBtn.collidepoint(mousePos):
            pygame.draw.rect(sc, (225, 0, 0), quitBtn)
            sc.blit(quitText, (160, 435))

        if quitBtn.collidepoint(mousePos) and clicked[0]:
            run = False


    # Player Picture
    sc.blit(playerPNG, (x, y))
    

    pygame.display.update()

pygame.quit()
