import os, random, time, pygame, math, datetime
os.system('cls')
name=input("What is your name?")
#initialize pygame
pygame.init()

#Declare constants, variables, list, dictionaries, any objects
#screen size
WIDTH=700
HEIGHT=700
screen=pygame.sisplay.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption('LEVEL II')
bg=pygame.image.load('PUT IMAGE IN')
character=pygame.image.load("CHARACTER")
screen.blit(bg,(0,0))
screen.blit(chart, (200,200))
pygame.display.update()
pygame.time.delay(3000)

move=5
check=True
while check:
    screen.blit(bg,(0,0)

    for event in pygame.event.get():
        if event.type==pygame.QUIT
    


   
   
    if keys[pygame.K_LEFT] and xc >=rad + move:
           xc -= move
    if keys[pygame.K_RIGHT] and xc < WIDTH - (rad+move):
           xc += move
    if keys[pygame.K_UP] and yc >= (rad + move):
           yc -= move
    if keys[pygame.K_DOWN] and yc < HEIGHT - (rad + move):
           yc += move
