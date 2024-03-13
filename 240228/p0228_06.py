from random import *

n1 =randrange(1,11)  #1-10까지의 정수
n2 =randint(1,10)    #1-10까지의 정수

#랜덤한 숫자 6개 lotto 리스트에 넣고
#내가 입력한 숫자 6개는 mynum리스트에 넣어주세요

lotto =[]


for i in range(6):
    n=randint(1,10) 
    if n not in lotto: #만약에 랜덤숫자(n)가 lotto 리스트에 없다면
        lotto.append(n)
print(lotto)

mynum =[]
for i in range(6):
    m=int(input('{}번째 숫자를 입력하세요>>'.format(i+1)))
    
    mynum.append(m)

print('lotto 숫자는 {}입니다.'format(lotto))
print('입력하신 숫자는 {}입니다.'format(mynum))

f= ['딸기', '포도']