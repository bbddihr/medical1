import random
# 1. 0으로 25개 1차원 리스트 생성
# 2. 1로 5개를 변경
# 3. 랜덤섞기
# 4. 5*5 2차원 리스트에 넣기
# 추첨 5*5 2차원 배열
# 5. checkList 출력
# 6. viewList 출력
# 7. 좌표입력후 확인
# 5개의 당첨을 맞추면 프로그램 종료
# 10번 시도후 프로그램 종료
# 현재까지 입력한 좌표를 모두 출력하시오.


#0
aList = [0]*25    
print(aList)

aList=[0 for i in range(25)]
#1
for i in range(5):
    aList[i] = 1
print(aList)
print()
#2. 
random.shuffle(aList)
print(aList)
#3.
# b_list=[]
# b_list.append(aList)
# print(b_list)

#4.
checkList=[[0]*5 for i in range(5)]
for i in range(5):
    for j in range(5):
        checkList[i][j] = aList[5*i+j]




