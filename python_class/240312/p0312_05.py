def multi(num1,num2):
    result_list=[]  #지역변수
    result_list.append(num1+num2)
    result_list.append(num1-num2)
    return result_list
 
num1 = int(input("숫자를 입력하세요.>>"))
num2 = int(input("숫자를 입력하세요.>>"))
result_list= multi(num1,num2)
print("결과값:  ",result_list)