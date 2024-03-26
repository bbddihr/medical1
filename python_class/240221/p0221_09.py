# 두 수를 입력받아서 사칙연산을 출력해보세요
# 예: 30,6을 입력받아서(input)
# 출력:
# 30+6 = 36
# 30-6 = 30
# 30 *6 = 180
# 30 / 6 = 5.0

# n1 = input("첫번째 숫자를 입력하세요 >>")
# n2 = input("두번째 숫자를 입력하세요 >>")
# print(int(n1)+int(n2))

# a=30
# b=6
# #변수를 사용해서 출력하기; 숫자가 아닌것 '' 안에 넣기
# print(a,'+',b,'=', a+b)
# print(a, '-',b,'=',a-b)
# print(a,'*',b,'=', a*b)
# print(a, '/',b, '=', a/b)

# #input함수를 사용해서 입력받은거 출력하기
# c=input("아무거나 입력하세요>>")
# print('c의값은 :',c)

a=input("첫번째 숫자를 입력하세요 >>")
b=input("두번째 숫자를 입력하세요 >>")

print(a,'+',b,'=',int(a)+int(b))
print(a,'-',b,'=',int(a)-int(b))
print(a,'*',b,'=',int(a)*int(b))
print(a,'/',b,'=',int(a)/int(b))

#print(a,'+',b,'=',a+b)
