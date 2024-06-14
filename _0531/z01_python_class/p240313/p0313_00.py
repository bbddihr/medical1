def cal(num1,num2):
    result1 = num1 + num2
    result2 = num1 - num2
    result3 = num1 * num2
    result4 = num1 / num2
    return result1,result2,result3,result4
# 두수입력을 받아 값을 리턴 받은 다음, 출력하시오. 10,20 -> 30,-10,200,0.5
num1 = int(input("1번째 숫자를 입력하세요.>> "))
num2 = int(input("2번째 숫자를 입력하세요.>> "))
# print("1.+ 2.- 3.* 4./")
# c = input("원하는 사칙연산을 입력하세요.")
# 함수호출
# result = cal(num1,num2,c)
result1,result2,result3,result4 = cal(num1,num2)
print("{},{} 결과값 : {},{},{},{}".format(num1,num2,result1,result2,result3,result4))


num1 = int(input("1번째 숫자를 입력하세요.>> "))
num2 = int(input("2번째 숫자를 입력하세요.>> "))

result1,result2,result3,result4 = cal(num1,num2)
print("{},{} 결과값: {},{},{},{}".format(num1,num2,result1,result2,result3,result4))