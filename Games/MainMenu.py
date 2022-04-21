#Siena Richey
#3/23/22

import pygame, time
pygame.init()
#variables

WIDTH=700
HEIGHT=700
wb=30
hb=30
xs=50
ys=250

#List for messages
MenuList=['Instructions', 'Screen Size', 'fhfnjre', 'fnvfj', 'hjfjer', 'djnvfj', 'dnfejkn']

#Get colors
colors={'white':[255, 255, 255], 'red': [255, 0, 0], 'aqua':[51,153,255], 'orange': [255, 85, 0], 
'purple': [48, 25, 52], 'navy':[5, 31, 64], 'pink': [200, 3, 75]}
background= colors.get('pink')
randColor= ''
sq_color=colors.get('pink')

#SCREEN
wind=pygame.display.set_mode((WIDTH,HEIGHT))
pygame.display.set_caption("Circle Eats Square")
#create different type


TITLE_FNT=pygame.font.SysFont('comicsans', 80)
MENU_FNT=pygame.font.SysFont('comicsans', 50)
INST_FNT=pygame.font.SysFont('comicsans', 30)

#Create Title
text=MENU_FNT.render('MENU', 1, (51, 153, 255))
wind.fill((255, 255, 255))
#get width of text 
#x value = WIDTH/2 - Wtext/2
xt=WIDTH/2-text.get_width()/2
wind.blit(text, (xt,50))

#Create first button


#Create Square menu


square=pygame.Rect(xs, ys, wb, hb)
txty=243
for i in range(7):
    message=MenuList[i]
    text=INST_FNT.render(message,1, (0, 0, 255))
    wind.blit(text, (90,txty))
    pygame.draw.rect(wind, sq_color, square)
    square.y+=50
    txty+=50
    
pygame.display.update()
pygame.time.delay(1000)
