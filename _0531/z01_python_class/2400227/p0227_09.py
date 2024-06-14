print('2단 출력')
for i in range(1,10): #i = 1,2,3,4,5,...9
    print('2*{}={}'.format(i,2*i))
    
for i in range(1,10): #i = 1,2,3,4,5,...9
    print('{}*{}={}'.format(2,i, 2*i))
    
    
#원하는 단을 입력받아서 구구단을 입력하세요
#3을 입력받으면 3단 출력.
n=3   
for i in range(1,10):
    print('{}*{}={}'.format(3,i,3*i))



#5번 반복
for _ in range(5):    # 이중 for 문 쓸때 변수 다르게 지정  
    num=int(input('숫자를 입력하세요>>'))
    for i in range(1,10):
        print('{}*{}={}'.format(num,i,num*i))

        

     