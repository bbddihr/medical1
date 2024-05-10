class Card:   #4개의 변수:kind,number,width,height
    width=0
    height = 0
         
    def __init__(self,kind,number):
        self.kind = kind
        self.number = number
        Card.width = 100
        Card.height=200

    
#52장 카드 생성
card_list=[]
shape=["SPADE","DIAMOND","HEART","CLOVER"]
number=["A","2","3","4","5","6","7","8","9","10","J","Q","K"]
for i in range(4):
    for j in range(13):
        c=Card(shape[i],number[j])  
        card_list.append(c)
    print(card_list)
