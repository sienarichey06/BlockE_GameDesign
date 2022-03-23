#Siena Richey
#3/23/22

import pygame, time
pygame.init()
#variables

WIDTH=700
HEIGHT=700
wb=30
hb=30

#Get colors
colors={'white':[255, 255, 255], 'red': [255, 0, 0], 'aqua':[51,153,255], 'orange': [255, 85, 0], 
'purple': [48, 25, 52], 'navy':[5, 31, 64], 'pink': [200, 3, 75]}
background= colors.get('pink')
randColor= ''
cr_color=colors.get('white')

#SCREEN
wind=pygame.display.set_mode((WIDTH,HEIGHT))
pygame.display.set_caption("Circle Eats Square")
#create different type



TITLE_FNT=pygame.font.SysFont('comicsans', 80)
MENU_FNT=pygame.font.SysFont('comicsans', 50)
INST_FNT=pygame.font.SysFont('comicsans', 20)

#Create Title

text=MENU_FNT.render('CIRCLE eats SQUARE', 1, (51, 153, 255))
wind.fill((255, 255, 255))
wind.blit(text, (90,10))
text=INST_FNT.render("2 player game. Circle uses keys up, down, side." , 1, (0, 0, 255))
wind.blit(text, (15, 150))
text=INST_FNT.render("Square uses keys w, a, s, d." , 1, (0, 0, 255))
wind.blit(text, (15, 190))
text=INST_FNT.render("Goal is for the circle to chase the square and eat it." , 1, (0, 0, 255))
wind.blit(text, (15, 230))
text=INST_FNT.render("Each time the circle eats the square, circle grows." , 1, (0, 0, 255))
wind.blit(text, (15, 270))
text=INST_FNT.render("Square will relocate and square player will try to escape the circle player again." , 1, (0, 0, 255))
wind.blit(text, (15, 310))
text=MENU_FNT.render("CLICK TO RETURN" , 1, (51, 153, 255))
wind.blit(text, (115, 400))
pygame.display.update()

pygame.time.delay(10000)