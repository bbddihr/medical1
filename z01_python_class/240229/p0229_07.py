from random import *
#랜덤숫자를 만들어서 (1-100사이)
#내가 입력한 값이 랜덤한 숫자랑 같으면 당첨(프로그램종료).
#아니면 다시 입력해주세요
#를 출력하는 프로그램을 만들어보세요

#입력한 숫자가 랜덤숫자보다 작으면 작습니다 더 큰수를 입력해주세요
#입력한 숫자가 랜덤숫자보다 크면 더 작은수를 입력해주세요
#1. 현재 입력한 숫자 모두를 input에 넣으세요

#2. 10회 도전 후 프로그램이 종료가 되게 해주세요 

randNum=randint(1,100)
'''
while True:
    userInput = int(input('숫자입력>>'))
    if randNum == userInput:
        print('당첨')
        break
    elif userInput > randNum:
        print('입력숫자가 랜덤숫자보다 큽니다.더 큰수를 입력해주세요')
    elif userInput < randNum:
        print('입력숫자가 랜덤숫자보다 작습니다. 더 작은 수를 입력해주세요')
    else:
        print('다시입력')
        
      

'''
inputList=[]

count=0
while count <10:
    count += 1
    userInput = int(input('{}번째 도전! 숫자를 입력하세요'.format(count)))
    inputList.append(userInput)
    if randNum == userInput:
        
        print('당첨')
        break
    elif userInput > randNum:
        print('입력숫자가 랜덤숫자보다 큽니다.더 작은수를 입력해주세요')
    elif userInput < randNum:
        print('입력숫자가 랜덤숫자보다 작습니다. 더 큰수를 입력해주세요')
    else:
        print('다시입력')
        
if count == 10:
    print('10회 입력을 초과하셨습니다. 정답은',randNum)
    
print('사용자가 입력한 숫자들은:',inputList)