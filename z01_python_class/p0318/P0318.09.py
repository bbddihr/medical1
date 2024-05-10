class Card: #4개의 변수:kind,width,height
    width =0
    height =0
    kind=""
    member=""

    def __init__(self,kind,number):
        self.kind=kind 
        self.number=number
        Card.width=100
        Card.width=200
     
    def Card_print(self):
        print(f"Card:{self.kind},{self.number}")
        
# c1=Card("spade",1)
# c1.Card_print()        
# c2=Card("spade",2)           
# c2.Card_print()        
# c3=Card("spade",3)           
# c3.Card_print()        
# c4=Card("spade",4)           
# c4.Card_print()        
# c5=Card("spade",5)  
# c5.Card_print()   
card_list =[] 


for i in range(13):    
    card_list.append(Card("spade",i+1))
    
    
# card_list.append(Card("spade","2"))
# card_list.append(Card("spade","3"))
# card_list.append(Card("spade","4"))
# card_list.append(Card("spade","5"))
# card_list.append(Card("spade","6"))
# card_list.append(Card("spade","7"))
# card_list.append(Card("spade","8"))
# card_list.append(Card("spade","9"))
# card_list.append(Card("spade","10"))
# card_list.append(Card("spade","J"))
# card_list.append(Card("spade","Q"))
# card_list.append(Card("spade","K"))

print("리스트개수: ",len(card_list))
for i in range(13):
    print("리스트 출력: ",card_list[i].kind, card_list[i].number)
    
# print("리스트 출력: ",card_list[1].kind, card_list[1].number)
# print("리스트 출력: ",card_list[2].kind, card_list[2].number)
# print("리스트 출력: ",card_list[3].kind, card_list[3].number)
# print("리스트 출력: ",card_list[12].kind, card_list[12].number)