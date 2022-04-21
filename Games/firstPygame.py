import os, time
import pygame as p

#initialize pygame
p.init()
#define colors
white=[225,255,255]
red=[255,0,0]
mag=[255,0,255]
aqua=[51,153,255]
blue=[47,59,198]
#create your own wndow/screen

#create your window/screen
WIDTH=600
HEIGHT=700
screen=p.display.set_mode((WIDTH,HEIGHT))
p.display.set_caption("My window)")
# screen.fill(m)
# p.display.update()
# p.time.delay(500)
# screen.fill(white)
# p.display.update()
# p.time.delay(500)
# screen.fill(red)
# p.display.update()
# p.time.delay(500)
# screen.fill(aqua) 
# define a rectangle
# position
x=20
y=30
#w and h of rectangle 
wbox=50
hbox=50
square=p.Rect(x,y,wbox,hbox)
square2=p.Rect(x+200, y+200, wbox, hbox)
p.display.update

run=True
while run:
    screen.fill(mag)

    for event in p.event.get():
        if event.type== p.QUIT:
            run = False
    square.x +=5
    square.y +=5
    p.draw.rect(screen,(white), square)
    p.draw.rect(screen,(red), square2)


    p.display.update()
    p.time.delay(100)
