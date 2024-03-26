import random
#클라스선언-설계도

class Card:
    
    def __init__(self,kind,number):
        self.kind=kind
        self.number=number
        
#52장의 카드
#spade,diamond,heart,clover
#1,2,3,4,5,6,7,8,9,10,11,12,13
kind_list=["spade","diamond","heart","clover"]
number_list=[1,2,3,4,5,6,7,8,9,10,11,12,13]
card_list=[]

def random_one():
    num=random.randint(0,51)
    print("랜덤카드1장: ",num, card_list[num].kind, card_list[num].number)

#52장 카드생성
for i in range(4):
    for j in range(13):
        card_list.append(Card(kind_list[i],number_list[j]))

#52장 카드 출력
for i in range(52):
    print("카드 :  ",card_list[i].kind,card_list[i].number)
        
        
#랜덤으로 1장 뽑기 출력      
# random_one()

#중복을 하지 않고, 랜덤카드 5장을 뽑으시오.
#1. 0-51 순차적인 것을 랜덤 섞기 후 순차적으로 뽑으면 됨.
#2. 5장을 랜덤으로 뽑으면 됨.
#3. 1장 뽑고 기존에 있는 카드와 비교해서 다시뽑음

#1. card_list shuffle
random.shuffle(card_list)
for i in range(5):
    print("랜덤 카드: ",card_list[i].kind,card_list[i].number)
print()
#2. card_list sample 5
ran_list = random.sample(card_list,5)
for i in ran_list:
    print("랜덤섞기 카드: ",i.kind,i.number)

#3. temp_list 저장장소를 1개만들고, 랜덤뽑기 1장의 카드를 저장장소의 리스트와 비교
# temp_list = []
# print("개수:  ",len(temp_list))
# cnt=0
# while True:
    
#     if cnt == 5: break  #랜덤뽑기 카드가 5장일경우 종료
#     c= random_one()
#     for i in temp_list:
#       if c.kind == i.kind and c.num == i.number: #같은 카드가 있으면 다음으로 
#         continue
# temp_list.append(c)     
# cnt+=1
    
# #
# for i in temp_list:
#     print("랜덤1장 뽑기 카드: ",i.kind, i.number)

Card("kind","number")   
#3.
for i in range(5):
    c=random_one()
    print("랜덤1장뽑기 카드 : ",c.kind,c.number) #중복카드뽑기될수있다