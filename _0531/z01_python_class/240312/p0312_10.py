import random
#카드 종류: SPADE, DIAMOND, HEART, CLOVER 
#카드 숫자: A,2,3,4,5,6,7,8,9,10,J,Q,K   13장
#카드 총수 : 52장

# def card_creat():
#     pass

# def card_shuffle():
#     pass

# def card_share():
#     pass
# def card_print():
#     pass
# while True:
#     print("[카드 프로그램]")
#     print("1.카드생성")
#     print("1.카드섞기")
#     print("1.카드5장 나눠주기")
#     print("1.카드5장 확인하기")
#     print("-"*40)
#     choice = int(input("원하는 번호를 입력하세요.>>"))

#     if choice ==1 :
#         card_creat()
#     elif choice ==2:
#         card_shuffle()
#     elif choice ==3:
#         card_share()
#     elif choice ==4:
#         card_print()
#     else:
#         print("프로그램을 종료합니다.")
#         break
    
card_list=[]
shape_list=["SPADE", "DIAMOND", "HEART", "CLOVER"]

num_list=[i for i in range(1,14)]
num_list[0]="A"
num_list[-1]="K"
num_list[-2]="Q"
num_list[-3]="J"
print(num_list)

card_list=[[0]*2 for i in range(52)]
cnt=0

for i in shape_list:
    for j in range(13):
        card_list[cnt] = {shape_list[i],num_list[j]}
        cnt+=1
print(card_list)



random.shuffle(card_list)

print(card_list)
