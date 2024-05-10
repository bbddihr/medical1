import random


w_title=["","명사","동사","형용사"]

def w_quiz(choice):
    print("{}를 선택하셨습니다.".format(w_title[choice]))
    chk = input("퀴즈가 나갑니다. 준비되셨나요?(1.실행,0.취소)")
    if chk ==
'''
aList = [0]*25
for i in range(5):
    
    aList[i] = 1
random.shuffle(aList)

checkList = [[0]*5 for i in range(5)]
for i in range(5):
    for j in range(5):
        checkList[i][j] = aList[5*i+j]

viewList= [["추첨"]*5 for i in range(5)]
c_count=1
answer_count=0
while True:
    print("\t[5*5 checkList좌표]")
    print("-"*40)
    print("",1,2,3,4,5,sep="\t")
    print("-"*40)
    for i in range(5):
        print(i,end='\t')
        for j in range(5):
            print(viewList[i][j],end="\t")
'''



