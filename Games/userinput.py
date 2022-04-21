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
print('######################################')
print('#        Guess A Number Menu         #')
print('#            ADD a Menu              #')
print('#           Choices 1-10             #')
print('#           Choices 1-50             #')
print('#           Choices 1-100            #')
print('#         Select your choice         #')
print('######################################')
GameOn=True
while(GameOn):
    userGuess=int(input("      Guess a number from 1-10 "))
    if myNumber ==userGuess:
        print("You guessed it!")
        GameOn=False
    else:
        print("good luck next time")
print("The number to guess was " + str(myNumber))