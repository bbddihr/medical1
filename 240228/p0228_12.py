
#1. 변수 선언
score = [[80,90,85], [70,80,90],[84,92,80],[72,81,76]]
name = ['홍길동','유관순','이순신','김구']
total = []
#2. 코딩
#2 -1)요소 하나하나 출력해보세요 80 90 85 70 80 90 ..
#2- 2)작은 요소의 합을 구해서 total 넣어주세요
#    total = [255, 240,256,229]
#3. 출력
'''
for i in range(len(score)):
    
    for j in range(len(score[i])):
        print(score[i][j])
print()
'''
t1=0
for a in score:
    print(a)
    t1=0
    for b in a:
        print(b)
        t1
    for b in 

for i in range(len(score)):
    
    #(i=0) score[0][0] +score[0][1] + score[0][2] =s
    #(i=1) score[0][0] +score[0][1] + score[0][2] =s
    #(i=2) score[0][0] +score[0][1] + score[0][2] =s
    s=0
    for j in range(len(score[i])):
        s=s+score[i][j] 
        print(score[i][j])
     
     #print(score[i])
    for j in range(len(score[i])): #j=0,1,2
        print(score[i][j])


'''
    for s in score:
        sum=sum+s
        print(sum)
    
 
sum = 0
for s in score

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
'''