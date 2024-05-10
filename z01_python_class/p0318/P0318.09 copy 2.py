'''
class Card:
    kind=""
    number=""
    
c1=Card("spade",1)

#c1에 숫자를 5로 변경하시오.
#c1을 출력하시오



c1=Card("spade",1)
c1.number =5
print(c1.kind,c1.number)


#c2 "heart","A"
#모양을 diamond변경후 출력하시오.
c2=Card("heart","A")
c2.kind='diamond'
print(c2.kind,c2.number)
'''
#-------------------------------------
class Card:
    kind=""
    number=""

def __init__(self,kind,number):
    self.kind=kind
    self.number=number

#리스트를 이용해서 52장의 카드 생성    
    
c_list = []
kind=["spade","diamond","heart","clover"]
number=[1,2,3,4,5,6,7,8,9,10,11,12,13]
for i in range(4):
    for j in range(13):
        c=[kind[i],number[j]]
        c_list.append(c)
         
for i in range(4):
    for j in range(13):
        print("카드 출력 : ",kind[i],number[j])
    
        



# #리스트 선언
# c_list=[""]*52
# for i in range


# #1개 변수로 선언--------------
# kind="spade"
# number="1"

# kind2="heart"
# number2="5"

# kind3="diamond"
# number3="4"




'''
class Lotto:
    number= 0 
    shape ="circle"
    
    def __init__(self,number):
        self.number = number
        

#lotto 1-45까지의 숫자를 입력한 리스트를 생성한 후 , 출력하시오.
l_list=[]


for i in range(45):
    l=Lotto(i)
    l_list(l)
    
    
for i in range(45):
    l = l_list[i]
    print(l)



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

# print("리스트개수: ",len(card_list))
# for i in range(13):
#     print("리스트 출력: ",card_list[i].kind, card_list[i].number)
    
# print("리스트 출력: ",card_list[1].kind, card_list[1].number)
# print("리스트 출력: ",card_list[2].kind, card_list[2].number)
# print("리스트 출력: ",card_list[3].kind, card_list[3].number)
# print("리스트 출력: ",card_list[12].kind, card_list[12].number)
'''