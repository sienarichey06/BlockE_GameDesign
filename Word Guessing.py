#SienaRichey
#02/08/2022
#Word Game with 3 levels: 
#       1. Fruits
#       2. Animals 
#       3. Computer Parts   
# Choice:

#Create word lists
from modulefinder import IMPORT_NAME
import os, random 
os.system('cls')

def menu():
    print('##########################################################')
    print('#            How Well Do You Know Your Words?            #')
    print('#                    Lets find out!!                     #')
    print('#                                                        #')
    print('#                   CHOICE OF LEVELS:                    #')
    print('#                       1. FRUITS                        #')
    print('#                      2. ANIMALS                        #')
    print('#                    3. COMPUTER PARTS                   #')
    print('#                                                        #')
    print('#       choose any category to recieve instructions!     #')
    print('##########################################################')

word=""
guess=""
def selectWord():
    global word
    fruits=["bananas", "grapes", "watermelon", "papaya", 'oranges', 'tomatoes','mangos', 'kiwis', 
    'strawberries' 'mangoes', 'blueberries', 'apples']
    animals=["horse", "snake", "dog", "cow", "hamster", "pig", "turtle", "frog", "wolf", "elephant", 
    "cheetah", "giraffe"]
    computerparts= ["mouse", "screen", "motherboard", "monitor", "keyboard"]
    # size=(len(fruits))
    # randy= random.randint(0,size)
    # print(randy)
    # word=fruits[randy]
    # print(word)
    word=random.choice(fruits)
def guessFunction():
    global guess
    check=True
    while check:
        try: 
            guess=input("\nenter a letter to guess the word ")
            if guess.isalpha() and len(guess)==1:
                check=False
            else:
                 print("only one letter please")
        except ValueError:
            print("only one letter please")
menu()
gameOn=True
tries=0
letterGuessed=""
selectWord()
while gameOn:
    
    guessFunction()
    letterGuessed += guess  #letterGuessed=letterGuessed + guess
    if guess not in word:   
        tries +=1
        print(tries)# for testing delete when game is ready
    countLetter=0
    for letter in word:
        if letter in letterGuessed: 
            print(letter, end=" ")
            countLetter +=1
        else: 
            print("_", end=" ")
    if tries>6:
        print("\n Sorry, ran out of chances")
        #playgame() ask user if they want to play again
    if countLetter == len(word):
        print("you guessed it!")
        #Calculate score
        #playGame()