def cal(input1,input2):
    
    result1 = input1+input2
    result2= input1-input2
    result3 = input1*input2
    result4 = input1*input2
    return result1,result2,result3,result4
    
    

    
    

input1=int(input("`1번재 숫지를 입력하세요?"))
input2=int(input("`2번재 숫지를 입력하세요?"))
#함수의 return을 사용해서 입력된 두수의 사칙연산 결과값을 출력하시오

result1,result2,result3,result4= cal(input1,input2)
data=cal(input1,input2)
print("더하기: ",result1)
print("빽기: ",result2)
print("곱하기: ",result3)
print("나누기: ",result4)
print("결과값: ",result1,result2, result3,result4)
print("결과값: ,result1,result2, result3,result4)
print("나누기: ",result2,result2,result3,result4)


'''

for i in range(10):   #i는 지역변수. 
    sum=0
    sum +=i
    print(i)
    
for i in range(5):
    result= 1
    result += 1
    
    
print(sum)
print(result) 
 
    
    
    
def plus(v1,v2):
    v1=100
    v2=200
    return v1,v2 #함수밖에서 사용하려면 return 값을 돌려줘야함.
    

#함수호출
v1=1
v2=2
v1,v2 = plus(v1,v2)
plus(v1,v2)
print(v1,v2)
'''