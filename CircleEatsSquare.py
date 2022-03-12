#SienaRichey
#Learning how to draw circles and rectangles
#Use keys to move objects
#Using dictionaries

#Objective of the game is for the rect to get away from the circle, if they collide the circle eats the square
#Circle will get larger and a new rect should appear somewhere on screen

import colorsys
import os, random, time, pygame

pygame.init()

#Declare constants, variables, list, dictionaries, any object

WIDTH=700
HEIGHT=700
check=True #for the while loop
move=5 #pixels
xs=20
ys=20
wbox=30
hbox=30
#circle variables 
rad=15
xc=random.randint(rad, WIDTH-rad)
yc=random.randint(rad, HEIGHT-rad)
#creating the rect object
square=pygame.Rect(xs, ys,wbox, hbox)

#create screen
screen=pygame.display.set_mode((WIDTH,HEIGHT))
pygame.display.set_caption('Circle eats Square')

#define colors
colors={'white':[255, 255, 255], 'red': [255, 0, 0], 'aqua':[51,153,255], 'orange': [255, 85, 0], 
'purple': [48, 25, 52], 'navy':[5, 31, 64], 'pink': [200, 3, 75]}

#Get colors
background= colors.get('pink')
sq_color=colors.get('navy')
cr_color=colors.get('white')

MAX=10
jumpCount=MAX
JUMP=False

while check:
    screen.fill(background)
    for case in pygame.event.get():
        if case.type==pygame.QUIT:
            check=False

    keys= pygame.key.get_pressed()#this returns a list
    if keys[pygame.K_a] and square.x >=move:
        square.x -= move
    if keys[pygame.K_d] and square.x < WIDTH - (wbox):
        square.x += move
    #jumping part
    if not JUMP:

        if keys[pygame.K_w] and square.y >= move:
            square.y -= move
        if keys[pygame.K_s] and square.y < HEIGHT - (hbox):
            square.y += move
        if keys[pygame.K_SPACE]:
            JUMP=True
    else: 
        if jumpCount>=- MAX:
            square.y-= jumpCount*abs(jumpCount)/2
            jumpCount-= 1
        else:
            jumpCount=MAX
            JUMP=False


    if keys[pygame.K_LEFT] and xc >=rad + move:
           xc -= move
    if keys[pygame.K_RIGHT] and xc < WIDTH - (rad+move):
           xc += move
    if keys[pygame.K_UP] and yc >= (rad + move):
           yc -= move
    if keys[pygame.K_DOWN] and yc < HEIGHT - (rad + move):
           yc += move

    checkCollide=square.collidepoint(xc, yc)
    if checkCollide:
        square.x=random.randint(wbox, WIDTH)
        square.y=random.randint(hbox, HEIGHT)
        rad += move 
    pygame.draw.rect(screen, sq_color, square)
    pygame.draw.circle(screen, cr_color, (xc, yc), rad)

    pygame.display.update()
    pygame.time.delay(10)

