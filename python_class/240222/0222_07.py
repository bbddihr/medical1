#대입연산자
# =
# a=3 ; 3을 a에 넣는다.
# a=3
# a +=1  # a+1

# print(a)
# a=3
# a += 2 #a= a+2
# print(a)
# a += 100 # a=a+100

# +=, -+, *=, /=, %=, //=, **=
#즉, 좌변과 우변에 동일한 변수명이 사용될 경우,
# #변수명을 생갹하고 축약시킬수 있다.
# a=3
# b=2
# a*=2+b
# # 1. a= a*2 +b (오답)
# # 2. a= a*(2+b)  (정답)
#      a= *(2+b) => a*=(2+b)
# print(a)

#num이 20에서 시작해서 값이 누적됨
num = 20
num += 2
print(num)
num -= 2
print(num)
num *= 2
print(num)
num **=2
print(num)
num /= 2
print(num)
