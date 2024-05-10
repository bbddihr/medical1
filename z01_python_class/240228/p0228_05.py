'''

n1= 1 #input('첫번째 숫자를 입력해주세요>>')
n2=10 #input('두번째 숫자를 입력해주세요>>')
sum=0


for i in range(1,11):
    sum+=i
print(sum)

#n1 부터 n2까지의 합, n1,n2 비교해서 
#n1은 작은수를 n1 에 넣기
#만약에, n1이 n2보다 크다면 둘의 값을 바꿔라


a = 10
b = 8
a, b =b ,a  ###숫자바꾸기
print('a',a)
print('b',b)
'''
n1=int(input('첫번째 숫자를 입력해주세요>>'))
n2=int(input('두번째 숫자를 입력해주세요>>'))
sum=0

if n1>n2:
    n1, n2=n2 ,n1
    print('n1',n2)
    print('n2',n1)
for i in range(n1,n2+1):
    sum+=i
print(sum)

#print(odd_list)
odd_list = []  #n1-n2까지의 홀수값을 저장
for i in range(n1,n2+1):
    if i%2==1:
        odd_list.append(i)
print(odd_list)
    
