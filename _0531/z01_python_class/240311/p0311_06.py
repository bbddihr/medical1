#함수선언할때 매개변수의 갯수를 맞춰야한다. 아님에러

sum =0
def plus(num):
    global sum
    sum = sum+num
    
n_input=int(input("숫자를 입력하세요.>>"))
plus(n_input)

print("총합: ",sum)