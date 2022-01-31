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

GameOn=True

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


while (GameOn):

    if 'rock' in user:
        
        user =int(1)
        print("paper"+str(user))
    elif 'paper' in user:
        user=int(2)
    elif '' in user:
        user=int(3)

    choice=input("choice: ")

    if choice == rock: 
    elif choice == paper:
    elif choice == scissors:
    


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


 endchoice=input("Make Your Choice")
    if 'Y' in endchoice:
        computernum = random.randing(1,3)
