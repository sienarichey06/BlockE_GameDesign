#Card War Game

numberCards=[]
for i in range(2,11):
    numberCards.append(i)
    numberCards[i]=str(numberCards[i-2])
print(numberCards)
suits=['s', 'c', 'h', 'd']
royals=['J','Q', 'K','A']

#Make a lits like this(2,3,4,5,6,7,8,9,10,J,Q,K)
#Make a deck of cards adding each suit