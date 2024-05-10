import random
# card_list=[{"shape":"spade", "num":"A"},
#            {"shape":"spade", "num":2},
#            {"shape":"spade", "num":3},
#            {"shape":"spade", "num":4},
#            ]
           
# card_list=[{"spade":"A"},
#            {"spade", 2},
#            {"spade", 3},
#            {"spade", 4},
#            ]           


shape_list = ["spade", "diamond", "heart","clover"]
card_list=[]

num_list = [0]*13
for i in range(1,14):
    num_list[i-1]=i
num_list[0] = "A"
num_list[10] = "J"
num_list[11] = "Q"
num_list[12] = "K"

# print(shape_list)
# print(num_list)
# print()

#카드 1세트를 구현 : 52장
card_list =[[0]*2 for i in range(52)]
cnt=0
for i in shape_list:     #"spade","diamond"...
    for j in range(13):
        card_list[cnt] = [i,num_list[j]]
        # print(card_list[cnt][0])
        # print(card_list[cnt][1])
        cnt+= 1
# print(card_list)        
# 카드를 랜덤섞기
random.shuffle(card_list)
arr_num = 0
while True:
    print("1.카드 1장 뽑기")
    print("2.카드 5장 뽑기")
    print("0.종료")
    c_num = int(input("번호를 선택해주세요>"))
    print("현재 남은 카드: ",len(card_list)-arr_num) # len(card_list) 빼기 arrr_num
    if c_num == 1:
        print(card_list[arr_num])   #0
        arr_num+=1
    elif c_num ==2:
        for i in range(5):
            print(card_list[arr_num])  #1,2,3,
            arr_num += 1 
    print(card_list)