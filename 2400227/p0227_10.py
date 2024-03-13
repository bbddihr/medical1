num = []
# for문을 사용해서 1-10까지 숫자를 num에 채우세요

#print(num)   #[1,2,3,4,5,6,7,8,9,10]


for i in range(1,11):
    num.append(i)
print(num)


#한줄로 표현할 수도 있다.    
#num1 = [i for i in range(1,11)]   
 
 # 1-10까지 짝수를 num2 리스트에 넣으세요 

num2=[]

#print(num2)  # [2,4,6,8,10]
for i in range(1,11):
    if i % 2 ==0:
        num2.append(i)
print(num2)

#1~10까지의 합 for문을 사용해서 구할 수 있음.
num=[1,2,3,4,5,6,7,8,9,10]
#num 리스트를 사용해서 1-10까지의 합을 구해보세요
#num리스트내의 숫자들의 합 구하기
#num2리스트 내 숫자들의 합을 구하세요 

t=0
for i in num:
    t=t+i
print(t)

s=0
for i in num2:
    s=s+i
print(s)


# for n in num:
#     print(n,end=' ')
# print()
# s1=0
# s1+=n
# for n in num:
# print(s1)
#
s3=0
for n in num2:
    s3 = s3+n
    #print(n, end='  ')
for i in range(len(num2)):
    s4 = s4 + num2[i]
print(s3,s4)



    

    
