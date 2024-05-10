from random import *
lotto =[]  #1.변수선언1-10
mynum =[2,5,1,9,3,7] #2. 입력받은 숫자
#3. 로또번호 생성

# for i in range(6):
#     n=randint(1,10)
#     if n not in lotto:
#         lotto.append(n)
# print(lotto) 중복있을수 있음

num=[1,2,3,4,5,6,7,8,9,10]  #특징:중복이 없다, 1-10까지
#    0                 9


for i in range(10):   #10번 섞기 
    tmp = randint(0,9)  # 0-9 사이 랜덤한 숫자 생성
    print(tmp)
    num[0], num[tmp] = num[tmp], num[0]
    print(num)   #[ 7, 6,10, 4, 3, 8, 5, 9, 2, 1]

for i in range(6):
    lotto.append(num[i])
print(lotto) #[7,6,10,4,3,8]   #로또번호로 사용 가능.6자리 중복없는 랜덤숫자
ok=[]
for i in range(len(mynum)):
    # print(mynum[i])   #리스트에 있는 숫자 출력
    if mynum[i] in lotto:
        ok.append(mynum[i])
print(mynum[i])    #당첨번호 출력

    