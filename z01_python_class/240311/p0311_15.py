#함수선언 
sum=0
def cal(num1,num2):
    temp=0
    if num1>num2:
        num1,num2=num2,num1   #방법1. 2개변수 치환
        temp=num1              #방법2. 2개변수 치환(다른언어에서도 쓰인다)
        num1=num2
        num2=temp
    for i in range(num1,num2+1):
        global sum
        sum+=i
    result=sum
    return result
    

#1,10 ->  1+2+3+...10 = 55
#두수를 입력받아, 입력한 사이의 합계를 구하는 프로그램을 구혆하시오.


sum=0
num1=int(input("1번째 숫자를입력하세요.>>"))
num2=int(input("2번째 숫자를입력하세요.>>"))

sum = cal(num1,num2)

print("합계 : ",sum)