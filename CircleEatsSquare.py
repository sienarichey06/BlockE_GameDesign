#Nikky Nandipati
#4/5/22
#Some help from
# https://www.youtube.com/watch?v=FfWpgLFMI7w&ab_channel=freeCodeCamp.org
# https://www.youtube.com/watch?v=wkrXbl1RlAg&ab_channel=FHCoding
# https://www.geeksforgeeks.org/decimal-functions-python-set-1/
# https://www.youtube.com/watch?v=g8-VJo9sXlU&ab_channel=MasterCodeOnline

import pygame as p
import os
import random
import math
import datetime
from decimal import ROUND_UP

os.system('cls')

enterName= input("Enter your name... ")

p.init()

WIDTH=700
HEIGHT=700
xs=50
ys=250
wb=30
hb=30

MAIN=True
INSTRUCTIONS=False
SETTINGS=False
BACK_COLOR=False
CIRCLE_COLOR=False
levelI=False
levelII=False
levelIII=False
MANGO=False
SCOREBOARD=False
EXIT=False

MenuList=['Instructions', 'Settings', 'Level 1', 'Level 2', "Level 3", "Scoreboard", "Exit"]
SettingList=[ 'Background Color', 'Circle Color']
BackColorList=['Aqua',"Purple", "Magenta", "Mystery Color!"]
CIRCLE_COLORList=['White', 'Lime Green', 'Navy', 'Mystery Color!']
screen=p.display.set_mode((WIDTH,HEIGHT))
p.display.set_caption("Circle Eats Square")

titleFont= p.font.SysFont("comicsans", 75)
subtitleFont= p.font.SysFont("comicsans", 40)
menuFont= p.font.SysFont("comicsans", 50)
instructionsFont= p.font.SysFont('comicsans', 30)

loop=True
seconds=0
wbox=30
hbox=30
rad=15
bigx=20
bigy=20
bigger=5
move=5
banana=0
xc=random.randint(rad, WIDTH-rad)
yc=random.randint(rad, HEIGHT-rad)
ibox=rad*math.sqrt(2)
xig= xc-(ibox/2)
yig= yc-(ibox/2)
inscribSq=p.Rect(xig,yig,ibox,ibox)
otherSquare=p.Rect(bigx, bigy, wbox, hbox)
square=p.Rect(xs,ys,wb,hb)

colors={'white': [255,255,255], 'red': [255,0,0], 'purple':[161, 0, 176], 'orange':[255, 85, 0], 'blue':[51, 0, 255], 'navy':[5, 1, 34], 'mystery color':[47,192,229], 'lime green':[50, 205, 50], 'magenta':[255, 0, 255], 'yellow':[240, 180, 14], 'aqua':[51, 153, 255], 'pink': [200,75,125], 'mystery color 2': [255, 184, 18]}

background=colors.get('aqua')
squareColor=colors.get('white')
circleColor=colors.get('white')
textColor=colors.get('white')
titleColor=colors.get('blue')
inscribsquareColor=colors.get('white')
sqM_color=colors.get('blue')
txt=''
txty=''
xt=''

def menuTitle(message):
    txt=titleFont.render(message, 1, (titleColor))
    screen.fill((background))
    xt= WIDTH/2-txt.get_width()/2
    screen.blit(txt,(xt,50))

def backButton(message):
    txt=menuFont.render(message, 1, (textColor))
    xt= WIDTH/2-txt.get_width()/2
    screen.blit(txt,(xt,550))
   
def mainmenu(Mlist):
    txty=245
    square.y=250
    for i in range(len(Mlist)):
        message=Mlist[i]
        txt=instructionsFont.render(message, 1, (255, 255, 255) )
        screen.blit(txt, (90,txty))
        txty+=50
        p.draw.rect(screen, sqM_color, square)
        square.y+=50
    p.display.update()

def instr():  
    print("in instr")
    myFile=open('CircleEatSquare\instructiones.txt', 'r')
    yi=150
    pineapple= myFile.readlines()
    print(pineapple)
    for line in pineapple:
        print(line)
        text=instructionsFont.render(line, 1, textColor)
        screen.blit(text, (40,yi))
        p.display.update()
        p.time.delay(50)
        yi+=50
    myFile.close()

def wScore():
    myFile=open('CircleEatSquare\scoreboard.txt', 'r')
    yi=150
    pineapple=myFile.readlines()
    pineapple.sort()
    print(len(pineapple))
    if len(pineapple)>5:
        n=5
    else:
        n=(len(pineapple))-1
    for i in range(n, -1, -1):
        txt=instructionsFont.render(pineapple[i], 1, (255, 255, 255))
        screen.blit(txt, (90,yi))
        yi+= 50
    myFile.close()

def scoreBoard(score):
    date=datetime.datetime.now()
    print(date.strftime('%m/%d/%Y'))
    scoreLine=str(score)+"\t"+enterName+"\t"+date.strftime('%m/%d/%Y'+'\n')
    print (scoreLine)
    myFile=open('CircleEatSquare\scoreboard.txt', 'a')
    myFile.write(scoreLine)
    myFile.close()

randColor=''
def changeClr():
    global randColor
    colorCheck=True
    while colorCheck:
        randColor=random.choice(list(colors))
        if colors.get(randColor) == background:
            randColor=random.choice(list(colors))
        else:
            colorCheck=False
changeClr()
squareColor=colors.get(randColor)    

def round_up(n, decimals=0):
    multiplier = 10 ** decimals
    return math.ceil(n * multiplier) / multiplier

MAX=10
jumpCount=10
JUMP=False
mouse_pos=(0,0)
while loop:
    keys=p.key.get_pressed()
    if MAIN:
        screen.fill(background)
        menuTitle("Circle Eats Square")
        mainmenu(MenuList)
    if INSTRUCTIONS:
        screen.fill(background)
        menuTitle("Instructions")
        backButton("BACK")
        instr()
    if SETTINGS:
        screen.fill(background)
        menuTitle("Settings")
        backButton("BACK")
        mainmenu(SettingList)  
    if BACK_COLOR:
        screen.fill(background)
        menuTitle("Background Color")
        backButton("Back")
        mainmenu(BackColorList)  
    if CIRCLE_COLOR:
        screen.fill(background)
        menuTitle("Circle Color")
        backButton("Back")
        mainmenu(CIRCLE_COLORList)
    if MANGO:
        timePlayed=((ticksEnd/1000)-(ticksStart/1000))
        timePlyR=round_up(timePlayed)
        screen.fill(background)
        menuTitle("Your Score")
        backButton("BACK")
        txt=instructionsFont.render("Your score is:", 1,(255, 255, 255))
        xt= WIDTH/2-txt.get_width()/2
        screen.blit(txt,(xt,200))
        score= ((banana)*5-2*(timePlyR))
        txt=subtitleFont.render(str(score), 1, (255, 255, 255))
        xt= WIDTH/2-txt.get_width()/2
        screen.blit(txt,(xt,250))      
    if SCOREBOARD:
        screen.fill(background)
        menuTitle("!Scoreboard!")
        backButton("BACK")
        wScore()    
       
    if EXIT:
        screen.fill(background)
        txt=instructionsFont.render("Good Riddance!", 1,(255, 255, 255))
        screen.blit(txt,(xt,200))
        p.time.delay(2000)
        screen.blit(txt,(xt,240))
        p.time.delay(5000)
        p.QUIT    

    for event in p.event.get():
        if event.type == p.QUIT:
            loop = False 

    if event.type ==p.MOUSEBUTTONDOWN:
        mouse_pos=p.mouse.get_pos()
        print(mouse_pos)
       
    if MAIN:
        banana=0
        rad=15
        if ((mouse_pos[0] >50 and mouse_pos[0] <80) and (mouse_pos[1] >250 and mouse_pos[1] <280))or INSTRUCTIONS:
            MAIN=False
            screen.fill(background)
            INSTR=True
        if((mouse_pos[0] >50 and mouse_pos[0] <80) and (mouse_pos[1] >300 and mouse_pos[1] <330))or SETTINGS:
            MAIN=False 
            SETTINGS=True
            p.time.delay(300)
            mouse_pos=(0,0)    
        if ((mouse_pos[0] >50 and mouse_pos[0] <80) and (mouse_pos[1] >350 and mouse_pos[1] <380))or levelI:
            MAIN=False
            levelI=True
            ticksStart=p.time.get_ticks()
        if ((mouse_pos[0] >50 and mouse_pos[0] <80) and (mouse_pos[1] >400 and mouse_pos[1] <430))or levelII:
            MAIN=False
            levelII=True
            ticksStart=p.time.get_ticks()
        if ((mouse_pos[0] >50 and mouse_pos[0] <80) and (mouse_pos[1] >450 and mouse_pos[1] <480))or levelIII:
            MAIN=False
            levelIII=True
            ticksStart=p.time.get_ticks()
        if ((mouse_pos[0] >50 and mouse_pos[0] <80) and (mouse_pos[1] >500 and mouse_pos[1] <530))or SCOREBOARD:
            MAIN=False
            SCOREBOARD=True
        if ((mouse_pos[0] >50 and mouse_pos[0] <80) and (mouse_pos[1] >550 and mouse_pos[1] <580))or EXIT:
            MAIN=False
            EXIT=True

    if SETTINGS:
        if ((mouse_pos[0] >50 and mouse_pos[0] <80) and (mouse_pos[1] >250 and mouse_pos[1] <290))or BACK_COLOR:
            SETTINGS=False
            screen.fill(background)
            BACK_COLOR=True
            p.time.delay(300)
            mouse_pos=(0,0)
        if((mouse_pos[0] >50 and mouse_pos[0] <80) and (mouse_pos[1] >300 and mouse_pos[1] <340))or CIRCLE_COLOR:
            SETTINGS=False
            CIRCLE_COLOR=True
            p.time.delay(300)
            mouse_pos=(0,0)

    if BACK_COLOR:
        if ((mouse_pos[0] >306 and mouse_pos[0] <393) and (mouse_pos[1] >560 and mouse_pos[1] <595)) or SETTINGS:
            BACK_COLOR=False
            SETTINGS=True
            p.time.delay(300)
            mouse_pos=(0,0)
        if ((mouse_pos[0] >50 and mouse_pos[0] <80) and (mouse_pos[1] >250 and mouse_pos[1] <290)):
            background=colors.get('aqua')  
        if ((mouse_pos[0] >50 and mouse_pos[0] <80) and (mouse_pos[1] >300 and mouse_pos[1] <340)):
            background=colors.get('purple')    
        if ((mouse_pos[0] >50 and mouse_pos[0] <80) and (mouse_pos[1] >350 and mouse_pos[1] <390)):
            background=colors.get('magenta')
        if ((mouse_pos[0] >50 and mouse_pos[0] <80) and (mouse_pos[1] >400 and mouse_pos[1] <440)):
            background=colors.get('mystery color')  
   
    if CIRCLE_COLOR:
        if ((mouse_pos[0] >50 and mouse_pos[0] <80) and (mouse_pos[1] >250 and mouse_pos[1] <290)):
            circleColor=colors.get('white')
            inscribsquareColor=colors.get('white')  
        if ((mouse_pos[0] >50 and mouse_pos[0] <80) and (mouse_pos[1] >300 and mouse_pos[1] <340)):
            circleColor=colors.get('lime green')
            inscribsquareColor=colors.get('lime green')  
        if ((mouse_pos[0] >50 and mouse_pos[0] <80) and (mouse_pos[1] >350 and mouse_pos[1] <390)):
            circleColor=colors.get('navy')  
            inscribsquareColor=colors.get('navy')  
        if ((mouse_pos[0] >50 and mouse_pos[0] <80) and (mouse_pos[1] >400 and mouse_pos[1] <440)):
            circleColor=colors.get('mystery color 2')  
            inscribsquareColor=colors.get('mystery color 2')  
        if ((mouse_pos[0] >306 and mouse_pos[0] <393) and (mouse_pos[1] >560 and mouse_pos[1] <595)) or SETTINGS:
            CIRCLE_COLOR=False
            SETTINGS=True
            p.time.delay(300)
            mouse_pos=(0,0)
             
    if not MAIN and not levelI:
        if ((mouse_pos[0] >210 and mouse_pos[0] <490) and (mouse_pos[1] >561 and mouse_pos[1] <595))or MAIN:
            if INSTRUCTIONS:
                INSTRUCTIONS=False
                MAIN=True
            if SETTINGS:
                SETTINGS=False
                MAIN=True
            if MANGO:
                MANGO=False
                MAIN=True
                scoreBoard(score)
            if SCOREBOARD:
                SCOREBOARD=False
                MAIN=True

    if levelI:
        screen.fill(background)
        if keys[p.K_a] and otherSquare.x>=move :
            otherSquare.x -= move
        if keys[p.K_d] and otherSquare.x <=WIDTH-(wbox+move):
            otherSquare.x += move
        if not JUMP:
            if keys[p.K_w] and otherSquare.y>=move:
                otherSquare.y -= move  
            if keys[p.K_s] and otherSquare.y<=HEIGHT-(hbox+move):
                otherSquare.y += move
            if keys[p.K_SPACE]:
                JUMP=True
        else:
            if jumpCount>=-MAX:
                otherSquare.y -= jumpCount*abs(jumpCount)/2
                jumpCount-=1
            else:
                jumpCount=MAX
                JUMP=False
        if keys[p.K_LEFT] and xc >=rad+move:
            xc -= move
        if keys[p.K_RIGHT] and xc<=WIDTH-(rad+move):
            xc += move
        if keys[p.K_UP] and yc>=rad+move:
            yc -= move
        if keys[p.K_DOWN] and yc<=HEIGHT-(rad+move):
            yc+= move
       
        choque=otherSquare.collidepoint((xc,yc))
        if choque:
            otherSquare.x=random.randint(wbox, WIDTH-wbox)
            otherSquare.y=random.randint(hbox, HEIGHT-hbox)
            rad+=bigger
        ibox=rad*math.sqrt(2)
        xig= xc-(ibox/2)
        yig= yc-(ibox/2)
        inscribSq=p.Rect(xig,yig,ibox,ibox)
        sqCollide=otherSquare.colliderect((inscribSq))
        if sqCollide:
            otherSquare.x=random.randint(wbox, WIDTH-wbox)
            otherSquare.y=random.randint(hbox, HEIGHT-hbox)
            changeClr()
            squareColor=colors.get(randColor)  
            rad+=bigger
            banana+=1
   
        p.draw.rect(screen,squareColor, otherSquare)    
        p.draw.circle(screen,circleColor, (xc,yc), rad)
        p.draw.rect(screen,inscribsquareColor, inscribSq)

        if banana>=5:
            levelI=False
            MANGO=True
            ticksEnd=p.time.get_ticks()
            print(ticksStart, ticksEnd)

    if levelII:        
        screen.fill(background)
        if keys[p.K_a] and otherSquare.x>=move :
            otherSquare.x -= move
        if keys[p.K_d] and otherSquare.x <=WIDTH-(wbox+move):
            otherSquare.x += move
        if not JUMP:
            if keys[p.K_w] and otherSquare.y>=move:
                otherSquare.y -= move  
            if keys[p.K_s] and otherSquare.y<=HEIGHT-(hbox+move):
                otherSquare.y += move
            if keys[p.K_SPACE]:
                JUMP=True
        else:
            if jumpCount>=-MAX:
                otherSquare.y -= jumpCount*abs(jumpCount)/2
                jumpCount-=1
            else:
                jumpCount=MAX
                JUMP=False
        if keys[p.K_LEFT] and xc >=rad+move:
            xc -= move
        if keys[p.K_RIGHT] and xc<=WIDTH-(rad+move):
            xc += move
        if keys[p.K_UP] and yc>=rad+move:
            yc -= move
        if keys[p.K_DOWN] and yc<=HEIGHT-(rad+move):
            yc+= move
       
        choque=otherSquare.collidepoint((xc,yc))
        if choque:
            otherSquare.x=random.randint(wbox, WIDTH-wbox)
            otherSquare.y=random.randint(hbox, HEIGHT-hbox)
            rad+=bigger
        ibox=rad*math.sqrt(2)
        xig= xc-(ibox/2)
        yig= yc-(ibox/2)
        inscribSq=p.Rect(xig,yig,ibox,ibox)
        sqCollide=otherSquare.colliderect((inscribSq))
        if sqCollide:
            otherSquare.x=random.randint(wbox, WIDTH-wbox)
            otherSquare.y=random.randint(hbox, HEIGHT-hbox)
            changeClr()
            squareColor=colors.get(randColor)  
            rad+=bigger
            banana+=1

        p.draw.rect(screen,squareColor, otherSquare)    
        p.draw.circle(screen,circleColor, (xc,yc), rad)
        p.draw.rect(screen,inscribsquareColor, inscribSq)

        if banana>=20:
            levelII=False
            MANGO=True
            ticksEnd=p.time.get_ticks()
            print(ticksStart, ticksEnd)
   
    if levelIII:        
        screen.fill(background)
        if keys[p.K_a] and otherSquare.x>=move :
            otherSquare.x -= move
        if keys[p.K_d] and otherSquare.x <=WIDTH-(wbox+move):
            otherSquare.x += move
        if not JUMP:
            if keys[p.K_w] and otherSquare.y>=move:
                otherSquare.y -= move  
            if keys[p.K_s] and otherSquare.y<=HEIGHT-(hbox+move):
                otherSquare.y += move
            if keys[p.K_SPACE]:
                JUMP=True
        else:
            if jumpCount>=-MAX:
                otherSquare.y -= jumpCount*abs(jumpCount)/2
                jumpCount-=1
            else:
                jumpCount=MAX
                JUMP=False
        if keys[p.K_LEFT] and xc >=rad+move:
            xc -= move
        if keys[p.K_RIGHT] and xc<=WIDTH-(rad+move):
            xc += move
        if keys[p.K_UP] and yc>=rad+move:
            yc -= move
        if keys[p.K_DOWN] and yc<=HEIGHT-(rad+move):
            yc+= move
       
        choque=otherSquare.collidepoint((xc,yc))
        if choque:
            otherSquare.x=random.randint(wbox, WIDTH-wbox)
            otherSquare.y=random.randint(hbox, HEIGHT-hbox)
            rad+=bigger
        ibox=rad*math.sqrt(2)
        xig= xc-(ibox/2)
        yig= yc-(ibox/2)
        inscribSq=p.Rect(xig,yig,ibox,ibox)
        sqCollide=otherSquare.colliderect((inscribSq))
        if sqCollide:
            otherSquare.x=random.randint(wbox, WIDTH-wbox)
            otherSquare.y=random.randint(hbox, HEIGHT-hbox)
            changeClr()
            squareColor=colors.get(randColor)  
            rad+=bigger
            banana+=1
     
        p.draw.rect(screen,squareColor, otherSquare)    
        p.draw.circle(screen,circleColor, (xc,yc), rad)
        p.draw.rect(screen,inscribsquareColor, inscribSq)

        if banana>=30:
            levelIII=False
            MANGO=True
            ticksEnd=p.time.get_ticks()
            print(ticksStart, ticksEnd)        
    p.display.update()
    p.time.delay(10)