#숫자를 입력받아서
#100보다 크거나 같으면 [100보다 크거나 같습니다]
#아니면 [100보다 작습니다]
#를 출력해보세요

n=int(input("숫자를 입력하세요>>"))
if n>= 100:
    print("100보다 크거나 같습니다")
else:
    print("100보다 작습니다")
    

#입력받은 숫자로
#짝수면 짝수입니다. 홀수면 홀수입니다를 출력
# 힌트: 짝수는 2로 나눈 나머지값이 0


if n % 2 == 0:
    print("짝수입니다")
    
else:
    print("홀수입니다")
    
#60점 이상이면 합격 아니면 불합격을 출력해보세요

n1=int(input("점수를 입력하세요>>"))
if n1 >=60:
    print("합격입니다")
else:
    print("불합격입니다") 
   
# 5보다 크고 10보다 작은 수 비교
# n이 [5보다 크고 10보다 작은수 입니다] 

n=int(input("숫자를 입력하세요:"))
if 5<n<10:
    print("5보다 크고 10보다 작은수 입니다")
if 5<n and n<10:
    print('5보다 크고 10보다 작은수 입니다')

n=int(input("숫자를 쓰세요:"))
if n % 3 == 0:
    print("3의 배수입니다")
    
if n % 3 == 0 and n % 2 == 0:
    print("2의 배수이며 3의 배수입니다")
    
# if (n%2==0) and (n%3==0):
#     print('2의 배수이며 3의 배수입니다.')