#반복문
'''
for 변수 in range(시작값, 끝값+1, 증가값):
'''
for i in range(3):    #i= 0,1,2
    print('안녕')
    #i = 0일때
    #i=  1일때
    #i= 2 일때
for i in range(3):    #i=0,1,2
    print(i)
    
    
# i = 0,1,2,3,.. 개념외우기 i는 증가
# i = 1,2,3,4,5 ..
for i in range(100):
    print(i+1)
    
sum1=0
for i in range(1,6,1):
    sum1= sum1+i
    
#숫자 한개를 입력받아서 1부터 입력한 수 까지의 합을 구하세요

n1= 100 #1에서 100까지 (1+ ...+100)
#for i in range():
#    합계
# 합계 출력
t=0
for i in range(1,101):
    t+=i
print('1부터 100까지의 합은: {}입니다'.format(t))

sn=0 #총합을 넣을 변수 선언
for i in range(1,101):
    sn = sn+i
    #print(i, end= ' ')
print('{}부터 {}까지의 합은: {}입니다'.format(1,n1,sn))

s1= 0
#짝수의 합만 구함 (2+4+6+8+..+100)
for i in range(1,n1+1):
    if i %2 == 0:        #짝수
        print(i, end='  ')
        s1 = s1+i
print('{}부터 {}까지의 합은: {}입니다'.format(1,n1,s1))

# 1-10까지의 곱
s2 = 1
for i in range(1,11):
    s2= s2 *i 
    # i =1 > 1*1 ->1
    # i =2 > 1*2 ->2
    # i = 3> 2*3 ->6 
print(s2)


    
        
        


