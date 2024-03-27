class Card:
    kind=""
    number=""
    def __init__(self,kind,number):
        self.kind=kind
        self.number=number
card_list=[]

for i in range(13):
    card_list.append(Card("spade",i+1))
    
print(len(card_list)) 
for i in range(13):
    print(card_list[i].kind,card_list[i].number)
    