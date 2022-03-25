#SienaRichey
#Learning how to draw circles and rectangles
#Use keys to move objects
#Using dictionaries

#Objective of the game is for the rect to get away from the circle, if they collide the circle eats the square
#Circle will get larger and a new rect should appear somewhere on screen

import colorsys
from curses import mouseinterval
import os, random, time, pygame
from pickle import TRUE

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
background= colors.get('white')
randColor= ''
cr_color=colors.get('aqua')

WIDTH=700
HEIGHT=700
wb=30
hb=30
xs=50
ys=250
MAIN=TRUE
INST=False


#List for messages
MenuList=['Instructions', 'Level 1', 'Level 2', 'Level 3', 'Settings', 'Scoreboard', 'Exit Game']
SettingList=['Screen Size', 'Font Size', 'Background Color', 'jncej', 'dgwreer', 'dssefer', 'fgerwsf']
#Get colors
colors={'white':[255, 255, 255], 'red': [255, 0, 0], 'aqua':[51,153,255], 'orange': [255, 85, 0], 
'purple': [48, 25, 52], 'navy':[5, 31, 64], 'pink': [200, 3, 75]}
background= colors.get('white')
randColor= ''
sq_color=colors.get('aqua')

#SCREEN
screen=pygame.display.set_mode((WIDTH,HEIGHT))
pygame.display.set_caption("Circle Eats Square")
#create different type


TITLE_FNT=pygame.font.SysFont('comicsans', 80)
MENU_FNT=pygame.font.SysFont('comicsans', 50)
INST_FNT=pygame.font.SysFont('comicsans', 30)

#Create Title
def TitleMenu(Message):
    text=MENU_FNT.render('MENU', 1, (51, 153, 255))
    screen.fill((255, 255, 255))
    #get width of text 
    #x value = WIDTH/2 - Wtext/2
    xt=WIDTH/2-text.get_width()/2
    screen.blit(text, (xt,50))

#Create first button


#Create Square menu


square=pygame.Rect(xs, ys, wb, hb)
#this is a function uses a parameter

def MainMenu(Mlist):
    txty=243
    for i in range(len(Mlist)):
        message=Mlist[i]
        text=INST_FNT.render(message,1, (0, 0, 255))
        screen.blit(text, (90,txty))
        pygame.draw.rect(screen, sq_color, square)
        square.y+=50
        txty+=50
        
    pygame.display.update()
    pygame.time.delay(1000)



def changeColor():
    global randColor
    colorCheck=True
    while colorCheck:
        randColor=random.choice(list(colors))
        if colors.get(randColor)==background:
            print(randColor)
            print(background)   
            randColor=random.choice(list(colors))
        else:
            colorCheck=False

# sq_color=colors.get('navy')
#Making a rand c f the square
changeColor()
sq_color=colors.get(randColor)


MAX=10
jumpCount=MAX
JUMP=False

while check:
    screen.fill(background)
    TitleMenu("MENU")
    MainMenu(MenuList)
    for case in pygame.event.get():
        if case.type==pygame.QUIT:
            check=False

    keys= pygame.key.get_pressed()#this returns a list
    if case.type == pygame.MOUSEBUTTONDOWN:
        mouse_pos=pygame.mouse.get_pos()
        print(mouse_pos)
        if ((mouse_pos[0] >20 and mouse_pos[0]< 60) and (mouse_pos[1] >250 and mouse_pos[1]< 290))or INST:
            MAIN=False
            screen.fill(background)
            TitleMenu('INSTRUCTIONS')
            INST=True


    # if keys[pygame.K_a] and square.x >=move:
    #     square.x -= move
    # if keys[pygame.K_d] and square.x < WIDTH - (wbox):
    #     square.x += move
    # #jumping part
    # if not JUMP:

    #     if keys[pygame.K_w] and square.y >= move:
    #         square.y -= move
    #     if keys[pygame.K_s] and square.y < HEIGHT - (hbox):
    #         square.y += move
    #     if keys[pygame.K_SPACE]:
    #         JUMP=True
    # else: 
    #     if jumpCount>=- MAX:
    #         square.y-= jumpCount*abs(jumpCount)/2
    #         jumpCount-= 1
    #     else:
    #         jumpCount=MAX
    #         JUMP=False


    # if keys[pygame.K_LEFT] and xc >=rad + move:
    #        xc -= move
    # if keys[pygame.K_RIGHT] and xc < WIDTH - (rad+move):
    #        xc += move
    # if keys[pygame.K_UP] and yc >= (rad + move):
    #        yc -= move
    # if keys[pygame.K_DOWN] and yc < HEIGHT - (rad + move):
    #        yc += move

    # checkCollide=square.collidepoint(xc, yc)
    # if checkCollide:
    #     square.x=random.randint(wbox, WIDTH)
    #     square.y=random.randint(hbox, HEIGHT)
    #     changeColor()
    #     sq_color=colors.get(randColor)
    #     rad += move 
    # pygame.draw.rect(screen, sq_color, square)
    # pygame.draw.circle(screen, cr_color, (xc, yc), rad)

    # pygame.display.update()
    # pygame.time.delay(10)
