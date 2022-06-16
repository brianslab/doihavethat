# argument is a list of lists

# columns are :
#  0    1   2     3    4     5      6 
# name qty set isFoil art isProxy deck

def needToBuy(cards):
    proxies = []
    owned = []
    
    for card in cards:
        if card[5] == 'TRUE':
            proxies += card
        else:
            owned += card   
