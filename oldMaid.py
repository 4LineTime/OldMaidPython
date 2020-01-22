import random
print("Welcome to Fishy Old Maid!")

#set cards
fishes = ['eel','pirahna','catfish','octopus','dolphin','manta ray','trout','salmon','pufferfish','seal']
oldmaid = "lionfish" #'pollution','plastic','overfishing',

#determine number of human and ai players
playerAmount = int(input("How many total players today?"))
#humanAmount = int(input("How many humans are playing?"))
#computerPlayers = playerAmount - humanAmount

#deck = fishes*playerAmount

#https://stackoverflow.com/questions/14878538/duplicate-elements-in-a-list from olivecoder's general example
deck =[fish for fish in fishes for __ in range(playerAmount)]

deck.append(oldmaid)
random.shuffle(deck)

print(deck)

hands = [deck[i::playerAmount]for i in range(0,playerAmount)]
print(hands)

#distribute hands to players



#def player
#def deck
#def hand
#def card
