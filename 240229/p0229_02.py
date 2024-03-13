#리스트변수명 = [요소1, 요소2,,, 요소n]
#요소가 될 수 있는 타입이:bool, int, float, string, list
'''
fruits=['딸기','사과','배','수박','귤']
#귤 출력
print(fruits[4])
print(fruits[-1])
print(fruits[len(fruits)-1])
#리스트에 요소 추가
fruits.append('포도')
print(fruits)
fruits.remove('딸기')
print(fruits)
#리스트에서 3번째 삭제
del(fruits[3])
print(fruits)

if '한라봉' in fruits:
    print('있음')

for f in fruits:  #in 리스트명
    print(f)
    
for i in range(len(fruits)):
    print(fruits[i])
    
num=[[10,20,30],[100,200,300],[1,2,3]]  #list 안에 list
for n in num:
    print(n)
for n in num:
    for a in n:
        print(a) 
print()
for i in range(len(num)):
    print(num[i])
    for j in range(len(num)):
        print(num[i][j])
print()        
#리스트에 숫자 넣을 때 한줄로 표현하기, 방법1
aa=[]
for i in range(1,11):
    aa.append(i)
print(aa)
#방법2####
a= [i for i in range(1,11)]

print(a)  

a= [0 for _ in range(10)]
print(a)
 
a=[ [] for i in range(10)]
print(a) 
print()

#표현식 for 항목 in 리스트 if조건문
# for j 리스트 추가가능 

a=[i*j for i in range(1,3) for j in range(1,3)]
print(a)
# [1,2,2,4]
print()
a=[ i for i in range(100) if i%2 == 0]
print(a)
print()
b= [i for i in range(1,11)]
print(b)
print()
c=[i+1 for i in b]
print(c)
'''
names=['홍길동','유관순','이순신','강감찬','김구']
#출력
#1.홍길동 2. 유관순 3. 이순신

for i in range(len(names)):
    print('{}.{}'.format(i+1,names[i]),end=' ')
print()
    
#변수 1개 더 필요
i= 0
for name in names:
    i += 1
    print('{}.{}'.format(i,name))
print()  

  
##### enumerate 함수
# index를 넣고 싶을때 사용   # index:0부터 시작
for i , name in enumerate(names):
    print('{}.{}'.format(i,name))
    
#start를 넣으면 시작인덱스를 지정할수 있다    
for i , name in enumerate(names, start=1):  ## index:1부터 시작
    print('{}.{}'.format(i,name))
    
names=['홍길동','유관순','이순신','강감찬','김구']
#         0       1        2        3       4
for i , name in enumerate(names):
    print('{}는 {}번째에 있습니다'.format(name,i))
    
