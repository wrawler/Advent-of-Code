ans = 0
matchPerCard = {}
cardCopies = []

file = open("input.txt","r")
cards = file.readlines()

cardNumber = 1

for card in cards:
    card = card.replace('\n','')
    parts = card.split("|")

    winningNumbers = list(filter(bool,((parts[0].split(":"))[1]).split(" ")))
    myNumbers = list(filter(bool,parts[1].split(" ")))

    numberOfMatches = 0
    for winningNumber in winningNumbers:
        for myNumber in myNumbers:
            if myNumber == winningNumber:
                numberOfMatches += 1
    
    matchPerCard[cardNumber] = numberOfMatches
    cardCopies.append(cardNumber)
    
    cardNumber += 1
file.close()

cardIndex = 0
for cardNumber in cardCopies:
    for numberOfCopies in range(1,matchPerCard[cardNumber] + 1):
        cardCopies.insert(cardIndex + numberOfCopies , cardNumber + numberOfCopies)
    cardIndex += 1

ans = len(cardCopies)
print(ans)

"""_summary_

key = 1  ( value = 4 ) -> 2,3,4,5
=> 4 means 1+1,1+2,1+3,1+4

for i in range value:
    newCopies.append(key + i)
dictionary = {1:[2,3,4,5]}


A list of cards
[1,2,3,4,5]

first element 1 expands and list becomes
[1,2,3,4,5,2,3,4,5]

Then next element 2 expands
[1,2,3,4,3,4,5,2,3,4,5]

So on ....
[1,2,3,4,5]
"""