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

user= 'paper'
computer = 1

if 'p' in user:
    user =int(1)
    print("paper"+str(user))
elif 'ro' in user:
    user=int(2)
elif 's' in user:
    user=int(3)
#