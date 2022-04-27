#Pseudo code



#define variables

#define images, make image lists and randomize them

#make scores files manually(not in code)

#function for menu with instructions, five choices(easy, medium, hard, scores, exit) that go to where user pressed/chose

#function for scores screen (score=how many turns before wining), with best score for each level

#function that draws screen with cards (number of cards is based on what user pressed in menu) that knows when not to show cards and always shows user's score

#main function: tracks click, flips over to back side if no match, keeps cards up if they do match, calculates turns/score, adds scores to file and prints user's score at the end, and goes to menu when done

#run game

import pygame, time, random, math



#setup

WIDTH=800

HEIGHT=800

pygame.init()

screen=pygame.display.set_mode((WIDTH,HEIGHT))

pygame.display.set_caption("Memory Game!")



#variables

size=100

margin=size+12

RADIUS = 20

infoy=90

infox=20

left=200

down=400

x=12

y=12



#defining images

square=pygame.image.load("images\\backofCard.jpg")

square=pygame.transform.scale(square,(size,size))

panda=pygame.image.load("images\\panda.jpg")

bat=pygame.image.load("images\\bat.jpg")

elephant=pygame.image.load("images\\elephant.jpg")

giraffe=pygame.image.load("images\\giraffe.jpg")

hippo=pygame.image.load("images\\hippo.jpg")

lion=pygame.image.load("images\\lion.jpg")

monkey=pygame.image.load("images\\monkey.jpg")

snake=pygame.image.load("images\\snake.jpg")

turtle=pygame.image.load("images\\turtle.jpg")

zebra=pygame.image.load("images\\zebra.jpg")

bee=pygame.image.load("images\\bee.jpg")

ladybug=pygame.image.load("images\\ladybug.jpg")

crab=pygame.image.load("images\\crab.jpg")

starfish=pygame.image.load("images\\starfish.jpg")

fireworks=pygame.image.load("images\\Fireworks.jpg")

fireworks=pygame.transform.scale(fireworks,(WIDTH,HEIGHT))

forest=pygame.image.load("images\\forest.jpg")

forest=pygame.transform.scale(forest,(WIDTH, HEIGHT))



#colors

white=(255,255,255)

black=(0,0,0)

blue = (196, 224, 255)

green = (74, 189, 41)

yellow = (231, 195, 0)

red = (196, 52, 41)

purple = (158, 98, 170)



#fonts

SCORE_FONT = pygame.font.SysFont('comicsans', 60)

INFO_FONT = pygame.font.SysFont('comicsansms', 21)

WIN_FONT = pygame.font.SysFont('comicsansms', 45)

STAR_FONT = pygame.font.SysFont('comicsansms', 18)

MENU_FONT = pygame.font.SysFont('comicsans', 45)

CHOICE_FONT = pygame.font.SysFont('comicsans', 45)

TITLE_FONT = pygame.font.SysFont('comicsans', 70)

BESTSCORES_FONT = pygame.font.SysFont('comicsansms', 60)



#image lists

#easy

matches1=[panda,panda,bat,bat,elephant,elephant,giraffe,giraffe,hippo,hippo,lion,lion]



#medium

matches2=[panda,panda,bat,bat,elephant,elephant,giraffe,giraffe,hippo,hippo,lion,lion,monkey,monkey,snake,snake,turtle,turtle,zebra,zebra]



#hard

matches3=[panda,panda,bat,bat,elephant,elephant,giraffe,giraffe,hippo,hippo,lion,lion,monkey,monkey,snake,snake,turtle,turtle,zebra,zebra,bee,bee,ladybug,ladybug,crab,crab,starfish,starfish]



#best scores

def best_scores():

    global define1, define2, define3

    runBest=True

    #screen continues showing while true

    while runBest:

        pressed=pygame.key.get_pressed()

        screen.fill(blue)

        text = TITLE_FONT.render("BEST SCORES FOR:", 1, black)

        screen.blit(text, (WIDTH/2 - text.get_width()/2, 20))

        #easy scores

        file1=open("memoryEasy.txt","r")

        score1=file1.read()

        easy = BESTSCORES_FONT.render("Easy:  "+score1,1,green)

        file1.close()

        screen.blit(easy,(WIDTH/2 - easy.get_width()/2, 200))

        #medium scores

        file2=open("memoryMedium.txt","r")

        score2=file2.read()

        medium = BESTSCORES_FONT.render("Medium:  "+score2,1,yellow)

        file2.close()

        screen.blit(medium,(WIDTH/2 - medium.get_width()/2, 350))

        #hard scores

        file3=open("memoryHard.txt","r")

        score3=file3.read()

        hard = BESTSCORES_FONT.render("Hard:  "+score3,1,red)

        file3.close()

        screen.blit(hard,(WIDTH/2 - hard.get_width()/2, 500))

        #press anywhere

        text=STAR_FONT.render("Press anywhere to go back to menu.",1,black)

        screen.blit(text,(250,700))

        pygame.display.update()

        for event in pygame.event.get():

            if event.type == pygame.QUIT:

                runBest=False #window closes if "x" button is pressed

            if event.type == pygame.MOUSEBUTTONDOWN:

                runBest=False #if user pressed the mouse anywhere, screen goes to menu

                menu()



#draw screen/grid

def draw(dict):

    global score, card_statis, square

    screen.blit(forest,(0,0)) #background for all levels

    #cards to print based on difficulty

    #only if hard

    if dict==define3:

        if card_statis[0][0]==0:

            screen.blit(square,(x,y))

        else:

            pic20=pygame.transform.scale(dict["b20"],(size,size))

            screen.blit(pic20,(x,y))

        if card_statis[0][1]==0:

            screen.blit(square,(x+margin,y))

        else:

            pic21=pygame.transform.scale(dict["b21"],(size,size))

            screen.blit(pic21,(x+margin,y))

        if card_statis[0][2]==0:

            screen.blit(square,(x+margin*2,y))

        else:

            pic22=pygame.transform.scale(dict["b22"],(size,size))

            screen.blit(pic22,(x+margin*2,y))

        if card_statis[0][3]==0:

            screen.blit(square,(x+margin*3,y))

        else:

            pic23=pygame.transform.scale(dict["b23"],(size,size))

            screen.blit(pic23,(x+margin*3,y))



        if card_statis[6][0]==0:

            screen.blit(square,(x,y+margin*6))

        else:

            pic24=pygame.transform.scale(dict["b24"],(size,size))

            screen.blit(pic24,(x,y+margin*6))

        if card_statis[6][1]==0:

            screen.blit(square,(x+margin,y+margin*6))

        else:

            pic25=pygame.transform.scale(dict["b25"],(size,size))

            screen.blit(pic25,(x+margin,y+margin*6))

        if card_statis[6][2]==0:

            screen.blit(square,(x+margin*2,y+margin*6))

        else:

            pic26=pygame.transform.scale(dict["b26"],(size,size))

            screen.blit(pic26,(x+margin*2,y+margin*6))

        if card_statis[6][3]==0:

            screen.blit(square,(x+margin*3,y+margin*6))

        else:

            pic27=pygame.transform.scale(dict["b27"],(size,size))

            screen.blit(pic27,(x+margin*3,y+margin*6))

    #if hard or medium

    if dict==define2 or dict==define3:

        if card_statis[1][0]==0:

            screen.blit(square,(x,y+margin))

        else:

            pic12=pygame.transform.scale(dict["b12"],(size,size))

            screen.blit(pic12,(x,y+margin))

        if card_statis[1][1]==0:

            screen.blit(square,(x+margin,y+margin))

        else:

            pic13=pygame.transform.scale(dict["b13"],(size,size))

            screen.blit(pic13,(x+margin,y+margin))

        if card_statis[1][2]==0:

            screen.blit(square,(x+margin*2,y+margin))

        else:

            pic14=pygame.transform.scale(dict["b14"],(size,size))

            screen.blit(pic14,(x+margin*2,y+margin))

        if card_statis[1][3]==0:

            screen.blit(square,(x+margin*3,y+margin))

        else:

            pic15=pygame.transform.scale(dict["b15"],(size,size))

            screen.blit(pic15,(x+margin*3,y+margin))



        if card_statis[5][0]==0:

            screen.blit(square,(x,y+margin*5))

        else:

            pic16=pygame.transform.scale(dict["b16"],(size,size))

            screen.blit(pic16,(x,y+margin*5))

        if card_statis[5][1]==0:

            screen.blit(square,(x+margin,y+margin*5))

        else:

            pic17=pygame.transform.scale(dict["b17"],(size,size))

            screen.blit(pic17,(x+margin,y+margin*5))

        if card_statis[5][2]==0:

            screen.blit(square,(x+margin*2,y+margin*5))

        else:

            pic18=pygame.transform.scale(dict["b18"],(size,size))

            screen.blit(pic18,(x+margin*2,y+margin*5))

        if card_statis[5][3]==0:

            screen.blit(square,(x+margin*3,y+margin*5))

        else:

            pic19=pygame.transform.scale(dict["b19"],(size,size))

            screen.blit(pic19,(x+margin*3,y+margin*5))

    #always print no matter what level

    if card_statis[2][0]==0:

        screen.blit(square,(x,y+margin*2))

    else:

        pic0=pygame.transform.scale(dict["b0"],(size,size))

        screen.blit(pic0,(x,y+margin*2))

    if card_statis[2][1]==0:

        screen.blit(square,(x+margin,y+margin*2))

    else:

        pic1=pygame.transform.scale(dict["b1"],(size,size))

        screen.blit(pic1,(x+margin,y+margin*2))

    if card_statis[2][2]==0:

        screen.blit(square,(x+margin*2,y+margin*2))

    else:

        pic2=pygame.transform.scale(dict["b2"],(size,size))

        screen.blit(pic2,(x+margin*2,y+margin*2))

    if card_statis[2][3]==0:

        screen.blit(square,(x+margin*3,y+margin*2))

    else:

        pic3=pygame.transform.scale(dict["b3"],(size,size))

        screen.blit(pic3,(x+margin*3,y+margin*2))



    if card_statis[3][0]==0:

        screen.blit(square,(x,y+margin*3))

    else:

        pic4=pygame.transform.scale(dict["b4"],(size,size))

        screen.blit(pic4,(x,y+margin*3))

    if card_statis[3][1]==0:

        screen.blit(square,(x+margin,y+margin*3))

    else:

        pic5=pygame.transform.scale(dict["b5"],(size,size))

        screen.blit(pic5,(x+margin,y+margin*3))

    if card_statis[3][2]==0:

        screen.blit(square,(x+margin*2,y+margin*3))

    else:

        pic6=pygame.transform.scale(dict["b6"],(size,size))

        screen.blit(pic6,(x+margin*2,y+margin*3))

    if card_statis[3][3]==0:

        screen.blit(square,(x+margin*3,y+margin*3))

    else:

        pic7=pygame.transform.scale(dict["b7"],(size,size))

        screen.blit(pic7,(x+margin*3,y+margin*3))



    if card_statis[4][0]==0:

        screen.blit(square,(x,y+margin*4))

    else:

        pic8=pygame.transform.scale(dict["b8"],(size,size))

        screen.blit(pic8,(x,y+margin*4))

    if card_statis[4][1]==0:

        screen.blit(square,(x+margin,y+margin*4))

    else:

        pic9=pygame.transform.scale(dict["b9"],(size,size))

        screen.blit(pic9,(x+margin,y+margin*4))

    if card_statis[4][2]==0:

        screen.blit(square,(x+margin*2,y+margin*4))

    else:

        pic10=pygame.transform.scale(dict["b10"],(size,size))

        screen.blit(pic10,(x+margin*2,y+margin*4))

    if card_statis[4][3]==0:

        screen.blit(square,(x+margin*3,y+margin*4))

    else:

        pic11=pygame.transform.scale(dict["b11"],(size,size))

        screen.blit(pic11,(x+margin*3,y+margin*4))



    #title and score

    text=SCORE_FONT.render("Score: "+str(score),1,black)

    screen.blit(text,(570,400))

    game=BESTSCORES_FONT.render("Animal",1,black)

    screen.blit(game,(565,80))

    game=BESTSCORES_FONT.render("Memory",1,black)

    screen.blit(game,(540,150))

    game=BESTSCORES_FONT.render("Game!",1,black)

    screen.blit(game,(570,220))

    pygame.display.update()



#main code

def main(dict):

    global score, card_statis, square, run, runMenu, define1, define2, define3

    clicked=[] #list for images(to know if they are the same)

    tracking=[] #list for tracking place in card_statis, so if not match, cards = 0 and go to back of card

    card_statis=[[0,0,0,0],

                [0,0,0,0],

                [0,0,0,0],

                [0,0,0,0],

                [0,0,0,0],

                [0,0,0,0],

                [0,0,0,0]]



    score=0

    run=True

    draw(dict)

    count=0

    while run:

        for event in pygame.event.get():

            if event.type == pygame.QUIT:

                run = False

                runMenu=False

            if event.type == pygame.MOUSEBUTTONDOWN:

                if pygame.mouse.get_pressed() and count<2:

                    pos=pygame.mouse.get_pos()

                    pos=pos[0]//(size+x),pos[1]//(size+y)

                    #additional rows only for hard

                    if dict==define3: #following descriptions apply to all position/image statements

                        if pos[0]==0 and pos[1]==0 and card_statis[0][0]==0: #finds osition of card and can't click same card if up

                            clicked.append(dict["b20"]) #add card to list to check if two are the same

                            count+=1 #add a count to know how many cards are up

                            card_statis[0][0]=1 #makes card flip over

                            tracking.append(0) #adds place in card_statis to list, so if not a match, if will be 0 again and go to back of card

                            tracking.append(0)

                        if pos[0]==1 and pos[1]==0 and card_statis[0][1]==0:

                            clicked.append(dict["b21"])

                            count+=1

                            card_statis[0][1]=1

                            tracking.append(0)

                            tracking.append(1)

                        if pos[0]==2 and pos[1]==0 and card_statis[0][2]==0:

                            clicked.append(dict["b22"])

                            count+=1

                            card_statis[0][2]=1

                            tracking.append(0)

                            tracking.append(2)

                        if pos[0]==3 and pos[1]==0 and card_statis[0][3]==0:

                            clicked.append(dict["b23"])

                            count+=1

                            card_statis[0][3]=1

                            tracking.append(0)

                            tracking.append(3)



                        if pos[0]==0 and pos[1]==6 and card_statis[6][0]==0:

                            clicked.append(dict["b24"])

                            count+=1

                            card_statis[6][0]=1

                            tracking.append(6)

                            tracking.append(0)

                        if pos[0]==1 and pos[1]==6 and card_statis[6][1]==0:

                            clicked.append(dict["b25"])

                            count+=1

                            card_statis[6][1]=1

                            tracking.append(6)

                            tracking.append(1)

                        if pos[0]==2 and pos[1]==6 and card_statis[6][2]==0:

                            clicked.append(dict["b26"])

                            count+=1

                            card_statis[6][2]=1

                            tracking.append(6)

                            tracking.append(2)

                        if pos[0]==3 and pos[1]==6 and card_statis[6][3]==0:

                            clicked.append(dict["b27"])

                            count+=1

                            card_statis[6][3]=1

                            tracking.append(6)

                            tracking.append(3)

                    #additional rows for medium or hard

                    if dict==define2 or dict==define3:

                        if pos[0]==0 and pos[1]==1 and card_statis[1][0]==0:

                            clicked.append(dict["b12"])

                            count+=1

                            card_statis[1][0]=1

                            tracking.append(1)

                            tracking.append(0)

                        if pos[0]==1 and pos[1]==1 and card_statis[1][1]==0:

                            clicked.append(dict["b13"])

                            count+=1

                            card_statis[1][1]=1

                            tracking.append(1)

                            tracking.append(1)

                        if pos[0]==2 and pos[1]==1 and card_statis[1][2]==0:

                            clicked.append(dict["b14"])

                            count+=1

                            card_statis[1][2]=1

                            tracking.append(1)

                            tracking.append(2)

                        if pos[0]==3 and pos[1]==1 and card_statis[1][3]==0:

                            clicked.append(dict["b15"])

                            count+=1

                            card_statis[1][3]=1

                            tracking.append(1)

                            tracking.append(3)



                        if pos[0]==0 and pos[1]==5 and card_statis[5][0]==0:

                            clicked.append(dict["b16"])

                            count+=1

                            card_statis[5][0]=1

                            tracking.append(5)

                            tracking.append(0)

                        if pos[0]==1 and pos[1]==5 and card_statis[5][1]==0:

                            clicked.append(dict["b17"])

                            count+=1

                            card_statis[5][1]=1

                            tracking.append(5)

                            tracking.append(1)

                        if pos[0]==2 and pos[1]==5 and card_statis[5][2]==0:

                            clicked.append(dict["b18"])

                            count+=1

                            card_statis[5][2]=1

                            tracking.append(5)

                            tracking.append(2)

                        if pos[0]==3 and pos[1]==5 and card_statis[5][3]==0:

                            clicked.append(dict["b19"])

                            count+=1

                            card_statis[5][3]=1

                            tracking.append(5)

                            tracking.append(3)

                    #cards to always print

                    if pos[0]==0 and pos[1]==2 and card_statis[2][0]==0:

                        clicked.append(dict["b0"])

                        count+=1

                        card_statis[2][0]=1

                        tracking.append(2)

                        tracking.append(0)

                    if pos[0]==1 and pos[1]==2 and card_statis[2][1]==0:

                        clicked.append(dict["b1"])

                        count+=1

                        card_statis[2][1]=1

                        tracking.append(2)

                        tracking.append(1)

                    if pos[0]==2 and pos[1]==2 and card_statis[2][2]==0:

                        clicked.append(dict["b2"])

                        count+=1

                        card_statis[2][2]=1

                        tracking.append(2)

                        tracking.append(2)

                    if pos[0]==3 and pos[1]==2 and card_statis[2][3]==0:

                        clicked.append(dict["b3"])

                        count+=1

                        card_statis[2][3]=1

                        tracking.append(2)

                        tracking.append(3)



                    if pos[0]==0 and pos[1]==3 and card_statis[3][0]==0:

                        clicked.append(dict["b4"])

                        count+=1

                        card_statis[3][0]=1

                        tracking.append(3)

                        tracking.append(0)

                    if pos[0]==1 and pos[1]==3 and card_statis[3][1]==0:

                        clicked.append(dict["b5"])

                        count+=1

                        card_statis[3][1]=1

                        tracking.append(3)

                        tracking.append(1)

                    if pos[0]==2 and pos[1]==3 and card_statis[3][2]==0:

                        clicked.append(dict["b6"])

                        count+=1

                        card_statis[3][2]=1

                        tracking.append(3)

                        tracking.append(2)

                    if pos[0]==3 and pos[1]==3 and card_statis[3][3]==0:

                        clicked.append(dict["b7"])

                        count+=1

                        card_statis[3][3]=1

                        tracking.append(3)

                        tracking.append(3)



                    if pos[0]==0 and pos[1]==4 and card_statis[4][0]==0:

                        clicked.append(dict["b8"])

                        count+=1

                        card_statis[4][0]=1

                        tracking.append(4)

                        tracking.append(0)

                    if pos[0]==1 and pos[1]==4 and card_statis[4][1]==0:

                        clicked.append(dict["b9"])

                        count+=1

                        card_statis[4][1]=1

                        tracking.append(4)

                        tracking.append(1)

                    if pos[0]==2 and pos[1]==4 and card_statis[4][2]==0:

                        clicked.append(dict["b10"])

                        count+=1

                        card_statis[4][2]=1

                        tracking.append(4)

                        tracking.append(2)

                    if pos[0]==3 and pos[1]==4 and card_statis[4][3]==0:

                        clicked.append(dict["b11"])

                        count+=1

                        card_statis[4][3]=1

                        tracking.append(4)

                        tracking.append(3)

                    draw(dict)



                    if count==2:

                        score+=1

                        if clicked[0]==clicked[1]:

                            clicked=[]

                            count=0

                            tracking=[]

                        else:

                            clicked=[]

                            count=0

                            pygame.time.delay(900)

                            track1=tracking[0]

                            track2=tracking[1]

                            track3=tracking[2]

                            track4=tracking[3]

                            card_statis[track1][track2]=0

                            card_statis[track3][track4]=0

                            tracking=[]

                    draw(dict)

                    #how to know if user won

                    if dict==define1 and card_statis==[[0,0,0,0],[0,0,0,0],[1,1,1,1],[1,1,1,1],[1,1,1,1],[0,0,0,0],[0,0,0,0]]:

                        pygame.time.delay(700)

                        screen.blit(fireworks,(0,0)) #new background

                        win=WIN_FONT.render("Good job! Your score was "+str(score)+"!",1,white) #tels user their score

                        screen.blit(win,(100,350))

                        file1 = open("memoryEasy.txt", "r")

                        if int(file1.read())>score:#checks if score is better than best

                            file1.close()

                            best=TITLE_FONT.render("NEW BEST SCORE!!!",1,white) #lets user know they beat score

                            screen.blit(best,(150,450))

                            file1=open("memoryEasy.txt","w") #replaces old best score with new one

                            file1.write(str(score))

                        file1.close()

                        pygame.display.update()

                        pygame.time.delay(3000)

                        menu()

                    if dict==define2 and card_statis==[[0,0,0,0],[1,1,1,1],[1,1,1,1],[1,1,1,1],[1,1,1,1],[1,1,1,1],[0,0,0,0]]:

                        pygame.time.delay(700)

                        screen.blit(fireworks,(0,0))

                        win=WIN_FONT.render("Good job! Your score was "+str(score)+"!",1,white)

                        screen.blit(win,(100,350))

                        file2 = open("memoryMedium.txt", "r")

                        if int(file2.read())>score:

                            file2.close()

                            best=TITLE_FONT.render("NEW BEST SCORE!!!",1,white)

                            screen.blit(best,(150,450))

                            file2=open("memoryMedium.txt","w")

                            file2.write(str(score))

                        file2.close()

                        pygame.display.update()

                        pygame.time.delay(3000)

                        menu()

                    if dict==define3 and card_statis==[[1,1,1,1],[1,1,1,1],[1,1,1,1],[1,1,1,1],[1,1,1,1],[1,1,1,1],[1,1,1,1]]:

                        pygame.time.delay(700)

                        screen.blit(fireworks,(0,0))

                        win=WIN_FONT.render("Good job! Your score was "+str(score)+"!",1,white)

                        screen.blit(win,(100,350))

                        file3 = open("memoryHard.txt", "r")

                        if int(file3.read())>score:

                            file3.close()

                            best=TITLE_FONT.render("NEW BEST SCORE!!!",1,white)

                            screen.blit(best,(150,450))

                            file3=open("memoryHard.txt","w")

                            file3.write(str(score))

                        file3.close()

                        pygame.display.update()

                        pygame.time.delay(3000)

                        menu() #goes ack to menu and cycle starts again



                    pygame.display.update()



#menu

def menu():

    global run, runMenu, define1, define2, define3, matches1, matches2, matches3

    runMenu=True

    while runMenu:

        screen.fill(blue)

        text = TITLE_FONT.render("LET'S PLAY A MEMORY GAME!", 1, black)

        screen.blit(text, (40, 20))



        #instructions

        text = INFO_FONT.render("Once you choose your level, that number of cards will appear face down. You", 1, black)

        text2 = INFO_FONT.render("will click on two cards at a time, and those cards will flip over showing an image.", 1, black)

        text3 = INFO_FONT.render("If the two images match, they will stay face up. If they do not, they will flip", 1, black)

        text4 = INFO_FONT.render("back over and you will choose two more. This cycle will continue until all the", 1, black)

        text5 = INFO_FONT.render("cards are face up. Good luck!",1,black)

        screen.blit(text, (infox, infoy))

        screen.blit(text2, (infox, infoy+5+text.get_height()))

        screen.blit(text3, (infox, infoy+10+text.get_height()*2))

        screen.blit(text4, (infox, infoy+15+text.get_height()*3))

        screen.blit(text5, (infox, infoy+20+text.get_height()*4))



        choice = CHOICE_FONT.render("CHOICES:",1,black)

        screen.blit(choice,(infox+50, infoy+70+text.get_height()*5))

        #3 circles

        pygame.draw.circle(screen, black, (left, down), RADIUS, 3)

        pygame.draw.circle(screen, black, (left, down+RADIUS*2+20), RADIUS, 3)

        pygame.draw.circle(screen, black, (left, down+RADIUS*4+40), RADIUS, 3)

        pygame.draw.circle(screen, black, (left, down+RADIUS*6+60), RADIUS, 3)

        pygame.draw.circle(screen, black, (left, down+RADIUS*8+80), RADIUS, 3)



        #easy

        one=MENU_FONT.render("1",1,green)

        screen.blit(one,(left-8,down-12))

        choice1=MENU_FONT.render("Easy (12)",1,green)

        screen.blit(choice1,(235,down-15))



        #medium

        two=MENU_FONT.render("2",1,yellow)

        screen.blit(two,(left-8,down+RADIUS*2+6))

        choice2=MENU_FONT.render("Meduim (20)",1,yellow)

        screen.blit(choice2,(235,down+45))



        #hard

        three=MENU_FONT.render("3",1,red)

        screen.blit(three,(left-8,down+RADIUS*4+25))

        choice3=MENU_FONT.render("Hard (28)",1,red)

        screen.blit(choice3,(235,down+105))



        #scores

        four=MENU_FONT.render("4",1,purple)

        screen.blit(four,(left-8,down+RADIUS*6+45))

        choice4=MENU_FONT.render("Best Scores*",1,purple)

        screen.blit(choice4,(235,down+165))



        #exit

        five=MENU_FONT.render("5",1,black)

        screen.blit(five,(left-8,down+RADIUS*8+65))

        choice5=MENU_FONT.render("EXIT",1,black)

        screen.blit(choice5,(235,down+225))



        #how to calculate scores

        star=STAR_FONT.render("*Your score is the number of turns it takes you to guess all the matches, so the lower the", 1, purple)

        star2=STAR_FONT.render("score the better.*",1,purple)

        screen.blit(star,(20,700))

        screen.blit(star2,(20,star.get_height()+705))



        #shuffle easy

        random.shuffle(matches1)

        define1={}

        for number in range(12):

            define1["b{0}".format(number)]=matches1[number]

        #shuffle medium

        random.shuffle(matches2)

        define2={}

        for number in range(20):

            define2["b{0}".format(number)]=matches2[number]

        #shuffle hard

        random.shuffle(matches3)

        define3={}

        for number in range(28):

            define3["b{0}".format(number)]=matches3[number]



        for event in pygame.event.get():

            if event.type == pygame.QUIT:

                runMenu=False

                run=False

            #depending on where user clicked, the screen will change

            if event.type == pygame.MOUSEBUTTONDOWN:

                m_x, m_y = pygame.mouse.get_pos()

                dis = math.sqrt((left - m_x)**2 + (down - m_y)**2)

                if dis<RADIUS:

                    main(define1) #easy pic list

                    runMenu=False

                else:

                    dis = math.sqrt((left - m_x)**2 + ((down+RADIUS*2+20) - m_y)**2)

                    if dis<RADIUS:

                        main(define2) #medium pic list

                        runMenu=False

                    else:

                        dis = math.sqrt((left - m_x)**2 + ((down+RADIUS*4+40) - m_y)**2)

                        if dis<RADIUS:

                            main(define3) #hard pic list

                            runMenu=False

                        else:

                            dis = math.sqrt((left - m_x)**2 + ((down+RADIUS*6+60) - m_y)**2)

                            if dis<RADIUS:

                                best_scores()

                                runMenu=False

                            else:

                                dis = math.sqrt((left - m_x)**2 + ((down+RADIUS*8+80) - m_y)**2)

                                if dis<RADIUS:

                                    runMenu=False

                                    run=False





        pygame.display.update()



menu() #runs menu, and therefore, everything els