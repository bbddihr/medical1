'''
주석 여러줄 쓸때
한줄 주석 #주석 써도 되고 ctrl +/
tab: 들여쓰기
shift+tab (들여쓰기 삭제)
alt + shift + 위아래방향키(커서있는 문장 복사)

num = [100,200,300,400]
# for 문을 사용해서 하나씩 출력    
for n in num:
    print(n, end='\t')
    
for i in range(len(num)):
    print(num[i], end='\t')

numlist= [[1,2],[3,4],[5,6,]]   # 변수 in 리스트이름
#      num[0][0],num[0][1], num[1][0], num[1][1], num[2][0], num[2][1]

for n in numlist:
    print(n, end='\t')
    for a in n:
        print(a, end=' ')
    print()
    #print(n,end='\t')
'''
# in range
for i in range(len(numlist)) : # for i in range(3)
    #print(i)
    #print(numlist[i])    
    for j in range(len(numlist[i])):
        print(numlist[i][j], end= ' ')
print()

f = [['딸기', 100,1000],['수박',100, 500],['사과',100, 1200], ['귤', 100,300]] 
#요소 한개한개를 출력해보세요
for i in f:
    for s in i:
        print(s)
    
#과일 이름만 출력
print(f[0][0],f[1][0],)
for i in range(len(f)):
    print(f[i][0])
    
for i in range(len(f)): 
    for j in range(len(f[i])):
        print(f[i][j], end= '  ')

score= [90,80,70,100,95,85,100] 
#점수의 총합을 구하세요
#그 점수를 total 리스트에 넣어주세요 
t=0
total=[]
for i in score:
    t+=i
    print(t)

sum = 0
for s in score:
    sum = sum +s
print(sum)
print()

sum1=0

for i in range(len(score)):
    print(score[i])
    sum1 += score[i]
print(sum1)
total.append(sum)
print(total)
