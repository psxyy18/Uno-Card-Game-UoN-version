class Card:
    def __init__(self) :
        pass

    def add_tuples(self,surface,color):
        self.att =  (surface,color)
        try:
            self.point = int(surface) 
        except:
            if surface != "Wild":
               self.point = 20
            else:
                self.point = 50

    
#card = Card()
# card.add_tuples('1','Red')
# print(card.att)
# print(card.point)

deck = []
colors = ['Blue','Red','Green','Yellow']
# print(colors[0])
for number in range(2):
    for i in range (1,10):
            
        for color in colors:
            card = Card()
            card.add_tuples(str(i),color)
            deck.append(card)

    for special in ['+2','Skip','Reverse']:
        for color in colors:
            card = Card()
            card.add_tuples(special,color)
            if card.point == 2:
                card.point = 20
            #print(card.point)
            deck.append(card)

for other in range(4):
    card_zero = Card()
    card_wild = Card()
    card_add4 =Card()
    card_zero.add_tuples('0', colors[0])
    card_wild.add_tuples('Wild', 'Black')
    card_add4.add_tuples('+4', 'Black')
    if card_add4.point == 4:
        card_add4.point == 50
    deck.append(card_zero)
    deck.append(card_wild)
    deck.append(card_add4)
    

print(len(deck))
for n in range(108):
    print(deck[n].att, str(deck[n].point))



