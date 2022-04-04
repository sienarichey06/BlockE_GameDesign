#Siena Richey
#Learning Files
# a) open/create a file
# b) write 'w'
# c) append 'a'
# d) read'r' e) close()


import pygame, os, datetime
os.system('cls')
date=datetime.datetime.now()
score=123
name= 'Jesse'
print(date.strftime('%m/%d/%Y'))
scoreLine=str(score)+" "+name+" "+date.strftime ('%m/%d/%Y'+'\n')
print(scoreLine )
#open a file and write in it
# when y write it erases the prev
myFile=open('sce.txt', 'w')
myFile.write(scoreLine)

myFile.close()
score=345
name='Jay'
print(date.strftime('%m/%d/%Y'))
scoreLine=str(score)+" "+name+" "+date.strftime ('%m/%d/%Y'+'\n')
myFile=open('sce.txt', 'a')
myFile.write(scoreLine)
myFile.close()
myFile=open('sce.txt', 'r')
lines=myFile.readline()
print(lines)
lines=myFile.readline()
print(lines)
myFile.close()

