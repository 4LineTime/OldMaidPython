#use library for shuffling deck at beginning and hand when choosing random card
import random

#build the deck at the beginning of the game
def buildDeck():
    #to set players and amount of the same card. IE Two eels, three eels, four eels, etc.
    playerAmount = 2

    #Fish List for Deck
    fishes = ['eel','pirahna','catfish','octopus','dolphin','manta ray','trout','salmon','pufferfish','seal','lionfish']
    
    #Old Maid List for Deck
    oldmaid = 'oil spill' # 'pollution','plastic','overfishing'
    
    #Build the deck using list comprehension, multiplying the fishes as necessary
    deck =[fish.title() for fish in fishes for __ in range(playerAmount)]

    #Add the Old Maid
    deck.append(oldmaid.title())
    return deck

#Deal the deck at the beginning of the game
def deal(deck):
    #empty hands
    artificialIntelligentPlayer = []
    humanPlayer = []

    #A boolean variable to alternate the dealing
    switchVar = True
    #Deal each card
    for card in range(len(deck)):
        #ai get a card
        if switchVar == False:
            artificialIntelligentPlayer.append(deck[card])
            switchVar = True
        #player gets a card
        elif switchVar == True:
            humanPlayer.append(deck[card])
            switchVar = False
    return (artificialIntelligentPlayer,humanPlayer)

#remove all pairs
def removePairs(hand):
    #list of pairs
    pairs = [card for card in hand if hand.count(card)>1]

    #list of singles
    hand = [card for card in hand if hand.count(card) <2]
    
    #remove duplicates from pair stack for viewing
    pairs = list(set(pairs))
    sorted(pairs)

    print('\nYou removed pairs of')
    print(*pairs, sep = ' | ')
    return hand

#For player to look at hand
def showHand(hand):
    
    print('\nYour cards are:')
    print(*hand, sep = ' | ')

#main function
def play():
    #build deck
    deck = buildDeck()

    #shuffle deck
    random.shuffle(deck)

    #each player gets a hand
    aiHand, humanHand = deal(deck)
    print ('Hi! Welcome to Fishy Old Maid!')

    #Make it personal
    humanName = input("What's your name? ").capitalize()
    print('\nHi '+ humanName + "! Let's play!")

    while len(aiHand) > 1 && len(humanHand) >1
        if len(humanHand) <1:
            print(humanName + 'Wins!')
        elif len(aiHand) <1:
            print('Computer Wins!')
        else:
            showHand(humanHand)
            humanHand = removePairs(humanHand)
            showHand(humanHand)




play()