#Siena Richey
#1/27/2022
# Rock Paper and Scissors game

# Create Menu for rock paper scissor game

# Import random every time 

# Randomize imports 1-3

# Assign value to rock, paper, and scissors

# Ask user to guess 1-3 to attempt to match guess to code

# Computer will generate new option every time and if user guesses incorect value, they will be told to retry

# If and else statements for the guesses and if user wins or loses

# Complete game and ask to play again after one round of play

import os, random
os.system('cls')



myNumber=random.randint(1,10)

def menu():
    print('#############################################################')
    print('#         Can you beat me at ROCK PAPER SCISSORS?           #')
    print('#                                                           #')
    print('#   When instructed, pick either rock, paper, or scissors   #')
    print('#                                                           #')
    print('#                     WINNING VALUES:                       #')
    print('#                   Rock Beats Scissors                     #')
    print('#                   Scissors Beats Paper                    #')
    print('#                     Paper Beats Rock                      #')
    print('#                                                           #')
    print('#                        GOOD LUCK!                         #')
    print('#############################################################')

menu()  #calling the function menu

user= 'paper'
computer = 1

if '1' in user:
    user =int(1)
    print("paper"+str(user))
elif '2' in user:
    user=int(2)
elif '3' in user:
    user=int(3)

if choice == 1:
    myNumber= random.randint(1,3)

elif choice == 2:
    myNumber= random.randint(1,3)

elif choice == 3:
    myNumber = random.randint(1,3)


GameOn=True
while(GameOn):
    if attempts ==1:
        GameOn = False
    else:
        GameOn = True
    print ('You have', attempts, 'chances remaining to play')
    userGuess=(input("Guess a number wisely from 1 to " +str(Gamelevel))) 
    if myNumber ==userGuess:
        print("You won! Maybe it was luck.")
        GameOn=False
    else:
        print("You haven't won yet. Play again?", myNumber)
        attempts = attempts - 1
os.system('cls')
menu()