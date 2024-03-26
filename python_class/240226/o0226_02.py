#1.나이가 10살 이상이고 150 이상만 탑승가능
#나이, 키를 입력받아
#[탑승가능] [탑승불가능]을 출력해보세요

#2. 숫자 3개 (정수)를 입력받고, 연산1개(+-*/)를 입력받아
# 조건문 연산자가 +를 입력받으면,
#연산자가 -로 입력 받으면: (1-2-3 = -4)
# +++ --- *** /// (나누기값은 둘째자리까지 표현)
# ex) a + b + c = d의 형태로 출력 (1 + 2 + 3 = 6)

age=10
height=150
a=int(input("나이를 입력하세요>>"))
h=int(input("키를 입력하세요>>>"))

if a>=10:
    
    if h>=150:
        print("탑승가능")
    else:
        print("탑승불가능")
else:
    print("탑승불가능")
    
# n1=int(input("숫자1 입력하세요 :"))
# n2=int(input("숫자2 입력하세요 :"))
# n3=int(input("숫자3 입력하세요:"))
# b= input("수식을 입력하세요 :")

# if b == '+':
#     print("{}+{}+{}={}".format(n1,n2,n3,n1+n2+n3)) 
# if b == '-':
#     print("{}-{}-{}={}".format(n1,n2,n3,n1-n2-n3))
# if b == '*':
#     print("{}*{}*{}={}".format(n1,n2,n3,n1*n2*n3))
# if b == '/':
#     print("{}/{}/{}={:.2f}".format(n1,n2,n3,n1/n2/n3))
    
    
if cal == '+':
    result = a+ b+ c
    print('{}+{}+{}={}'.format(a,b,c,result))
elif cal == '-':
    result a - b -c 
    print('{}-{}-{}={}'.format(a,b,c,result))
elif cal == '-':
    result a * b * c 
    print('{}*{}*{}={}'.format(a,b,c,result))
elif cal == ' /':
    result a / b / c 
    print('{}/{}/{}={}'.format(a,b,c,result))
else:
    print('잘못입력하셧습니다')
    
print('{},{},{} 연산의 결과값은: {}'.format(a,b,c,result))

