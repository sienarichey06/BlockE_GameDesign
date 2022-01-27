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
    print('#       Can you guess the number I am thinking of?          #')
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
        check=False
    except ValueError:
        print("Rough start for you! Please enter a number 1 to 3 only")


if choice == 1:
    myNumber= random.randint(1,10)
elif choice == 2:
    myNumber= random.randint(1,50)
elif choice == 3:
    myNumber = random.randint(1,100)
print(choice)

GameOn=True
while(GameOn):
    userGuess=int(input("Give me a number"))
    if myNumber ==userGuess:
        print("You guessed it!")
        GameOn=False
    else:
        print("Better luck next time", myNumber)
print("The number to guess was " + str(myNumber))
os.system('cls')
menu()