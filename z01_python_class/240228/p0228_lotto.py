from random import *

'''
#1 - 45까지의 숫자를 넣어서 

n= []
for i in range(10):
    n.append(i+1)
l=[1,2,3,4,5,6,7,8,9,10]
#l=[1,2,3...,45]
mynum=[]   #입력을 1-45 사이의 숫자를 입력받음 (6개)
lotto=[]    #1-45사이의 랜덤한 숫자 6자리 저장
#4. 입력숫자와 랜덤숫자 비교 같은거 출력
#5. 출력
#3. 로또 번호 생성하기
for i in range(46):
    tmp=randint(0,44)
    lotto.append(tmp)
print(lotto)
for i in range(6):
    lotto.append(n[i])
'''
# n[0],n[tmp]=n[tmp],n[0]
#2. 입력받은 숫자 6개:
#mynum=[] input()을 통해서 숫자 6개를 넣을 예정
#n=int(input('{}번째 숫자를 입력하세요(총6개) >>'.format(i)))
#로또번호 생성하기:

a,b=10,9
a,b=b,a#a=9, b=10
num=[0,1,2]
num[0],num[2]=num[2],num[0]
   
mynum = []
for i in range(6):
    b= int(input('숫자입력>>'))
    mynum.append(b)
print(mynum)

#1 리스트에 1-45 중복이 없는 1-45까지의 숫자가 들어있음.
# [1,2,3,..................,45]
#  0번방                     44번방

l=[]
for i in range(1,46):
    l.append(i)
print('로또숫자:{}'.format(l))  # l 리스트에 1-45 중복이 없는 1-45까지의 숫자가 들어있음.    
for i in range(200):
    tmp=randint(0,44)
    l[0],l[tmp]=l[tmp],l[0]
print('로또숫자:{}'.format(l)) 
# 잘 섞여 있고, 중복없음
for i in range(6):
    lotto.append(l[i])

print('로또숫자:{}'.format(l))    
# lotto[1,2,3,4,5,6]
# mynum[7,8,9,10,5,7]

ok=[]
m=[1,2,3]

for 1 in range(6):
    if mynum[i] in lotto:
        ok.append(mynum[i])
print('당첨된 숫자: {}'.format(ok))

