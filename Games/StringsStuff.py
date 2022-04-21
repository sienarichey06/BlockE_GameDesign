#SienaRichey
#01/31/2022
#Strings array of characters
#Has Many Functions
import os, random
os.system('cls')
myName= "Siena Richey"
myStatement= """ My name is so nice because 
blah blah blah what ever"""
for elem in myName:
    print(elem, end=" ")
guess=random.choice(myName)
print(guess)
words=["Radio", "Clues", "Suite", "Peter", "Robot"]
word=random.choice(words)
print(word)

print ("My last name begins with "  +myName[6])
print(myStatement)
if 'blah' in myStatement:
    print('true')
print('expert' not in myStatement)
# find () will return the index of the character you are looking for(first instance)
INDEX= myName.find("e")
print(INDEX)
wordLen=len(myName)
print(wordLen) #your last index is len-1
# for loop in range 0 to limit
print(myName[11])
for i in range(wordLen-1):
    if "a" in myName[i]:
        print(i, end=", ")
print("")
print("done")
myStatement=myStatement.upper() #makes all letters upper case
print(myStatement)

check=True
while check: 
    letter=input("Dear user, please give us a nice letter ")
#alpha is a function that makes sure that the input is only letters
    if len(letter)>1 or letter.isalpha():
        print("BAD")
    else:
        check=False
print("ready to play the game.")

for elem in myName:
    print(elem, end=" ")
guess=random.choice(myName)
print(guess)
words=["Radio", "Clues", "Suite", "Peter", "Robot"]
word=random.choice(words)
print(word)