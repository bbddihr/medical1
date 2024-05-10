#두 수를 입력받아서 사칙연산을 출력해보세요
#변수 n1, n2
#출력
# 10 + 3 =13
# 10 - 3 = 7
# 10 * 3 = 30
# 10 / 3 = 3.333


# print("{}+{}={}".format(10,3,10+3))
# print("{}-{}={}".format(10,3,10-3))
# print("{}*{}={}".format(10,3,10*3))
# print("{}/{}={:.3f}".format(10,3,10/3))

# n1=10
# n2=3
# print("{}+{}={}".format(n1,n2,n1+n2))
# print("{}-{}={}".format(n1,n2,n1-n2))
# print("{}*{}={}".format(n1,n2,n1*n2))
# print("{}/{}={:.3f}".format(n1,n2,n1/n2))


n1=input("첫번째 숫자를 입력하세요 >>")
n2=input("두번째 숫자를 입력하세요 >>")

print(n1,'+',n2,'=',int(n1)+int(n2))
print(n1,'-',n2,'=',int(n1)-int(n2))
print(n1,'*',n2,'=',int(n1)*int(n2))
print(n1,'/',n2,'=',int(n1)/int(n2))

