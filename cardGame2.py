#Make a lits like this(2,3,4,5,6,7,8,9,10,J,Q,K)
#Make a deck of cards adding each suit

#first let's import random since we will be shuffling
import random, os
os.system('cls')
deck=[]
#next, let's start building lists to build the deck
#NumberCards is the list to hold numbers plus face cards
numberCards = []
suits = ['h',"d", "c", "s"]
royals = ["J", "Q", "K", "A"]
tempplayer1 = []
tempplayer2 = []
halfdeck = 0
    


#using loops and append to add our content to numberCards :
def carddecks():
    for i in range(2,11):
        numberCards.append(str(i))

#this adds numbers 2-10 and converts them to string data

    for j in range(4):
        numberCards.append(royals[j])
        #this will add card faces to the base list
        #create full deck


    for j in range(4):
        numberCards.append(royals[j])
    #this will add the card faces to the base list
    #Create full deck

    for k in range(4):   # four suits
        for l in range(13): #13 cards per suit
            card = (numberCards[l] + " " + suits[k])
            #this makes each card, cycling through suits, but first through faces
            deck.append(card)
            #this adds the information to the "full deck" we want to make
#you can print the deck here, if you want to see how it looks
#print(deck)
#now let's see the deck!

def printdecks():
    global row, col
    counter=0
    for row in range(4):
        for col in range(13):
          print(deck[counter], end=" ")
    counter +=1
    print()

def realShuffle():
    global player1
    global player2
#now let's shuffle our deck!    
#Shuffle the deck cards
    random.shuffle(deck)
    player1=[]
    player2=[]
    # you could print it again here just to see how it shuffle
    #loop to devide the cards to each player

    for l in range(52):
            if l%2==0:
                player1.append(deck[l])
            else:
                player2.append(deck[l])

   
def splitdeck():
    global halfDeck
    halfDeck = int(len(deck)/2)


#print("player1 ",player1)
#print()
#print("player2 ",player2)
# halfDeck=int(len(deck)/2)
# plyr1=0
# plyr2=0

    #ask user to hit a key to release cards
halfDeck=int(len(deck)/2)
GameOn=True
while GameOn:
    carddecks()
    splitdeck()
    realShuffle()
    numberofcards=0
    for i in range (0,halfDeck):
        click=input("Press a any key to get cards")
        print("Player 1     Player 2")
        print("     "+player1[i]+"      "+player2[i])
        if player1[i]>player2[i]:
            tempplayer1.append(player1[i])
            tempplayer1.append(player2[i])
        elif player1[i]<player2[i]:
            tempplayer2.append(player1[i])
            tempplayer2.append(player2[i])
        elif player1 [i] == player2:
            tempplayer1.append(player1[i])
            tempplayer2.append(player2[i])

    if (len(tempplayer2)) == 0:
        print("player 1 won the game!")
        GameOn= False
    elif (len(tempplayer1)) == 0:
        print("player 2 won the game!")
    else: 
        print ("in", halfdeck)
        print("length=", len(player1))
        for j in range (0, int(halfDeck/2)):
            player1.pop(j)
            player2.pop(j)
        player1.extend(tempplayer1)
        player2.extend(tempplayer2)
        if len(player1)<len(player2):
            halfDeck = len(player2)
        else:
            halfDeck = len(player2)
        
        
    #     print("Player I: "+str(plyr1)+"     Player II: "+ str(plyr2))
    # if plyr1>plyr2:
    #     print("Player one won the game "+str(plyr1)+" to "+str(plyr2))
    # else:
    #     print("Player two won the game "+str(plyr2)+" to "+str(plyr1))


#after a round, the user who wins gets all of the cards from the rounds that they won
