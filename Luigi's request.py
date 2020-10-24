#Carlo, make me a moving Donut
import pygame

pygame.init()

screen = pygame.display.set_mode((800, 600))

pygame.display.set_caption("Moving Donut")

donutimg = pygame.image.load("donut.png") #https://tinyurl.com/yxla5dg7
donutX = 370
donutY = 480
donuty_change = 0
donutx_change = 0

score = 0

#function to show player icon
def donut(x,y): #we made a function because the Img coordinates are going to change
    screen.blit(donutimg, (x, y))


running = True
while running:

    screen.fill((192, 200, 192))
    #read keys
    for event in pygame.event.get():
        if event.type == pygame.QUIT: #remember event.type
            running=False

        if event.type == pygame.KEYDOWN: #If a keystroke is pressed, checks what arrow is
            if event.key == pygame.K_RIGHT: #Now it's event.key because we are going to see what key
                donutx_change += 0.5
            if event.key == pygame.K_LEFT:
                donutx_change -= 0.5
            if event.key == pygame.K_UP:
                donuty_change -= 0.5
            if event.key == pygame.K_DOWN:
                donuty_change += 0.5

        if event.type == pygame.KEYUP: #KEYUP is when a key is released. KEYDOWN is when pressed
            if event.key == pygame.K_RIGHT or event.key == pygame.K_LEFT or event.key == pygame.K_UP or event.key == pygame.K_DOWN:
                donutx_change = 0
                donuty_change = 0

    #change donut position
    donutX += donutx_change
    donutY += donuty_change

    #set borders
    if donutX <= -5: #-5 due to icon shape
        donutX = -5
    elif donutX >= 677:
        donutX = 677

    if donutY <= -5:
        donutY = -5
    elif donutY >= 477:
        donutY = 477


    donut(donutX, donutY)

    pygame.display.update()
