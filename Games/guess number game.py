#Siena Richey
#01/21/22
#We are going to learn the input function, # type casting, branching, looping
import os, random
os.system('cls')
#declare variable for user input
# print("enter a number from 1-10: ", end="")
# userInfo=int(input()) #input returns a string we must type cast if we need a number
# print("The number is %.2f " %(userInfo/3))
# #input is a string, so it wont multiply an integer -  must convert to integer - must type cast if we need integer
# #If you want just a digit, use %d but for decimals you need %.2f (float)
# guess=int(input("Please give a number"))


#guess a number
# myNumber = 9 instead of using fized number we will use random

myNumber=random.randint(1,10)

import random, os
os.system('cls')
#Today we are learning try and except, functions, elif

#Let's make menu a function key word def
def menu():
    print('#############################################################')
    print('#         Can you guess the number I am thinking of?        #')
    print('#                                                           #')
    print('#                     PICK YOUR LEVEL                       #')
    print('#              BEGINNER: Choices 1-10 (type 1)              #')
    print('#            INTERMEDIATE: Choices 1-50 (type 2)            #')
    print('#             ADVANCED: Choices 1-100 (type 3)              #')
    print('#                                                           #')
    print('#         10 attemps to test your master abilities          #')
    print('#############################################################')
#Checking for correct user input

menu()  #calling the function menu
check=True
while check:
    try:
        choice=int(input("Choice: "))
        if choice>0 and choice<4: 
            check=False
        else: 
            print("Rough start for you! Please enter a number 1,2, or 3 only.")
    except ValueError:
        print("Rough start for you! Please enter a number 1, 2, or 3 only")


if choice == 1:
    myNumber= random.randint(1,10)
    Gamelevel = 10
    attempts = 11
elif choice == 2:
    myNumber= random.randint(1,50)
    Gamelevel = 50
    attempts = 10
elif choice == 3:
    myNumber = random.randint(1,100)
    Gamelevel = 100
    attempts = 15
print(choice)
print (myNumber)

GameOn=True
while(GameOn):
    if attempts ==1:
        GameOn = False
    else:
        GameOn = True
    print ('You have', attempts, 'chances remaining to guess')
    userGuess=(input("Guess a number wisely from 1 to " +str(Gamelevel))) 
    if myNumber ==userGuess:
        print("You guessed the correct number! Maybe it was luck.")
        GameOn=False
    else:
        print("You haven't found the number yet! Take another guess.", myNumber)
        attempts = attempts - 1
print("The number I was thinking of is " + str(myNumber))
os.system('cls')
menu()
