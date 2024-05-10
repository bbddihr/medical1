#함수선언 def 이름() 정의
#함수값은 return
#함수호출;  이름()
#매개변수 : 함수로 데이터 전달하는 변수, 매개변수 개수는 항상같아야한다.
#가변매개변수선언; *values, 가변 매개변수는 일치하지 않아도 된다.
#리스트, 딕셔너리 매개변수는 주소값이 전달이 된다.


#퀴즈 1.
#함수를 사용하여 두수를 입력받아, 더하기,빼기,곱하기,나누기 결과값을 출력하시오. 
#함수선언



def cal(num1,num2,c):
        if c=='+':
            result=num1+num2
        elif c=='-':
            result=num1-num2
        elif c=='*':
            result=num1*num2
        elif c=='/':
            result=num1/num2
        return result
        
        
        

#두수입력을 받아 값을 리턴받은다음, 출력하시오.

num1 = int(input("1번째 숫자를 입력하세요>"))
num2 = int(input("2번째 숫자를 입력하세요>"))
print("1.+ 2.- 3. * 4./")
c=input("원하는 사칙연산을 입력하세요.")

#함수호출
result=cal(num1,num2,c)
print("{},{}의 결과값:{} ".format(num1,num2,result))



