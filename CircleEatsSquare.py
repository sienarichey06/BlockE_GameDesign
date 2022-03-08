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
while check:
    screen.fill(background)
    for case in pygame.event.get():
        if case.type==pygame.QUIT:
            check-False

    keys= pygame.key.get_pressed()#this returns a list
    if keys[pygame.K_a] and square.x >=move:
        square.x -= move
    if keys[pygame.K_d] and square.x:
        square.x += move
    if keys[pygame.K_w]:
        square.y -= move
    if keys[pygame.K_s]:
        square.y += move

    pygame.draw.rect(screen, sq_color, square)
    pygame.draw.circle(screen, cr_color, (xc, yc), rad)

    pygame.display.update()
    pygame.time.delay(10)

