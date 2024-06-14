#1-100 까지 더하는데
#총 합이 100이 넘었을 때 수를 출력하세요
#1+2+....
# 1-10 까지 더하는데 총합이 4가 넘는 순간의 수를 출력
#1+2+3 총합 :6  수 3: 

sum=0
for i in range(1,101):
    sum+=i
    if sum >100:
        break
print('수: ',i)    
print('총합: ',sum)

    
sum=0
for i in range(1,11):
    sum += i
    if sum>4:
        break
    
print('수: ', i)
print('총합: ',sum)

print()
#while
total=0
i=1
while i <= 100:
    total += i
    break
print('수: ',i)    
print('총합: ',sum)