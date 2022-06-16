# argument is a list of lists

# columns are :
#  0    1   2     3    4     5      6 
# name qty set isFoil art isProxy deck

def needToBuy(cards):
    proxies = []
    owned = []
    for card in cards:
        if card[5] == 'TRUE':
            proxies.append(card)
        else:
            owned.append(card)   
    
    ownedNames = []
    for card in owned:
        ownedNames.append(card[0])
    
    
    print("=========================\nYou need to buy:\n=========================")

    for card in proxies:
        if card[0] not in ownedNames:
            print(card[0])