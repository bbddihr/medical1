#continue 예제
#1-100 합계를 구하는데 3의 배수는 제외하고 더하기 
#while or for 사용해서 

#1-100까지 출력, 3의 배수는 제외하고 출력
#[1 2 4 5 7 8 10 ...]


'''    
sum=0
for i in range(1,101):
    if i%3 ==0:
        i=i+1
        continue 
    sum += i
    
print(sum)
'''

for i in range(1,101):
    print(i,end= ' ')
print()

n=0
while n<100:
    if n%3 == 0:
         continue
    print(i,end=' ' )
print()

i=1
while i%3 == 0:
    i=i+1
    continue
    print(i)
    