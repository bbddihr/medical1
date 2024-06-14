import random

[['spade', 2], ['diamond', 5], ['heart', 8], ['diamond', 'A'], ['spade', 10], ['diamond', 'K'], ['clover', 4], ['spade', 5], ['heart', 'Q'], ['diamond', 2], ['diamond', 4], ['heart', 7], ['clover', 'A'], ['diamond', 7], ['heart', 'A'], ['spade', 6], ['diamond', 6], ['clover', 8], ['spade', 8], ['heart', 'J'], ['diamond', 'J'], ['diamond', 'Q'], ['clover', 7], ['spade', 9], ['spade', 3], ['heart', 4], ['clover',
10], ['clover', 5], ['spade', 7], ['spade', 'J'], ['spade', 'A'], ['heart', 6], ['diamond', 8], ['heart', 2], ['heart', 5], ['diamond', 9], ['diamond', 3], ['heart',
3], ['clover', 9], ['clover', 'Q'], ['clover', 2], ['heart', 'K'], ['diamond', 10], ['spade', 'K'], ['spade', 'Q'], ['clover', 3], ['spade', 4], ['heart', 9], ['clover', 'K'], ['clover', 6], ['heart', 10], ['clover', 'J']]

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
        card_list[cnt] = {"shape":i, "num":num_list[j]}
        cnt+= 1
# print(card_list)        
# 카드를 랜덤섞기
random.shuffle(card_list)
arr_num = 0
while True:
    print("[카드게임]")
    print("-" *30)
    print("1.카드 1장 뽑기")
    print("2.카드 5장 뽑기")
    print("0.종료")
    c_num = int(input("번호를 선택해주세요>"))
    print("현재 남은 카드: ",len(card_list)-arr_num) # len(card_list) 빼기 arrr_num
    if c_num == 1:
        print("모양:{},번호:{}".format(card_list[arr_num]["shape"],card_list[arr_num]["num"]))   #0
        arr_num+=1
    elif c_num ==2:
        for i in range(5):
            print(card_list[arr_num])  #1,2,3,
            arr_num += 1 
    print(card_list)
    print(card_list[cnt][0])

