'''''
numL=[]

#0에서부터 5까지 넣어보세요
#append
print(numL)
numL.append(0)
numL.append(1)
numL.append(2)
numL.append(3)
numL.append(4)
numL.append(5)
print(numL)
# for 문을 사용하여 0-5까지 숫자 넣기
#[0,  1,  2,  3,  4,  5]
# 0   1   2   3  4    5
#num=[4]
num= []
for i in range(6):  # i는 0에서부터 6 미만까지 1씩 증가
    num.append(i)
    
print('num[] =', num)

aa=[1,2,3,4]
#index를 사용해서 값 읽기
for i in aa:
    print(i)
    
for i in range(0,4):
    print(aa[i])
    
f= ['사과','복숭아','딸기','포도', '자몽']
for i in f:
    print(i)
for i in range(len(f)):  # 리스트의 길이 len함수는 반복문에서 많이 사용
    print(f[i])

c= ['미국','영국','호주','캐나다','일본','중국']
#for문을 사용해서 출력해보기 2가지 방법으로 다 해보기
for i in c:
    print(i)
for i in range(len(c)):
    print(c[i])
    
#1에서 100까지 들어가는 numL=[] 를 만들고 출력해보기
numL=[]
#numL.append(1)~append(100)
for i in range(1,100):
    numL.append(i+1)
#     #print(i+1, end=' ') #출력확인
print(numL)
for i in range(100):
    print(numL[i])
  '''''
#반복문 안에 if 문 사용
for i in range(10):
    # print(i) # 0~9까지 출력이 됨
    if i ==9 : 
        print('9입니다')   
lan = ['영어','스페인어','일본어','중국어'] 
for i in lan : 
    if i =='영어':
        print('영어입니다.')
    else:
        print('다른 언어입니다')   
        
# 2의 배수만 출력 (1-100 사이)
# 1)증감 사용
# 2)if 사용
for i in range(2,102,2):
    print(i, end= ' ')
    print()
for i in range(1,101):
    if i %2==0:
        print(i, end=',')
print()

# 7의 배수만 출력 (1-100 사이)
# 1)증감 사용
# 2)if 사용
for i in range(7,101,7):
    print(i, end=' ')
print()
for i in range(1,101):
    if (i+1) %7==0:
        print(i+1, end=',')
print()  
aa=[100,90, 86, 79, 72, 52, 98, 94]
# #80점 이상만 합격 출력: 합격이 5번 출력

for i in aa:
    if i>=80:
        print('합격')


f= ['사과','복숭아','딸기','포도', '자몽']

#딸기가 있으면 딸기, 다른 과일은 다른 과일 이라고 출력

for i in f:
    if i=='딸기':
        print("딸기")
    else:
        print("다른과일")    
        
num = [1,2,5,7,9,10, 23,43]
#짝수면 짝수 홀수면 홀수를 출력
# 1. for i in num:
for i in num:
    if i%2==0:
        print(i, "짝수")
    else:
        print(i, "홀수")

# 2. for i in range(len(num))
for i in range(len(num)): # range를 쓸 경우 0부터 1씩 증가
    #print(i)              # 0,1,2,3,....
      print(num[i])   # num[0], num[1], num[2] ....
      if num[i] %2==0:
          print(num[i], '짝수')
      else:
          print(num[i], '홀수')
          
   
for i in range(len(f)):  # 리스트의 길이 len함수는 반복문에서 많이 사용
    print(f[i])

b= [4,6,7,8,9,0 ]    
for i in range(len(b)):
    print(b[i])
    if b[i] %2 ==0:
        print(b[i], '짝수')
    else:
        print(b[i], '홀수')
