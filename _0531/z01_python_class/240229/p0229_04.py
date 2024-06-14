#숫자 두개를 입력받고,
#연산자를 입력받아서 (+=*/)
#계산결과 출력(if)
#무한히 계산하는 계산기를 만드는데 (while)
#while 조건식: #조건식이 참일때 실행문 수행,
#               즉 조건식이 거짓일 때 while 종료
#첫번째 숫자에 0을 입력하면 프로그림이 종료가 되는 코드를 만드세요 
#break




n1=1
n2=1
cal=1
while True:
    n1=int(input('첫번째 숫자를 입력해주세요(종료 0)'))
    if n1 == 0 :
        print('종료되었습니다.')
        break
    n2=int(input('두번째 숫자를 입력해주세요'))
    cal=input('연산자 입력>>')
    if cal=='+':
        print('{}+{}={}'.format(n1,n2,n1+n2))
    elif cal=='-':
        print('{}-{}={}'.format(n1,n2,n1-n2))
    elif cal=='*':
        print('{}*{}={}'.format(n1,n2,n1*n2))
    elif cal=='/':
        print('{}'.format(n1,n2,n1/n2))
    else:
        print('연산을 잘못입력하셨습니다. 다시입력해주세요>>')
'''
if '+':
'{}+{}',n1 n2
'''