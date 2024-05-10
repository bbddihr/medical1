import random

#25개 1차원 리스트 생성
#0으로 20개, 1로 5개 넣기
#랜덤 섞기 
# 5*5 2차원 리스트에 넣기
#출력
#

#방법1
# list=[0]*25
# for i in range(5):
#     list[i]=1
# print(list)

# random.shuffle(list)
# print(list)


# list = [0 for i in range(25)]

# for i in range(5):
#     list[i] = 1
# random.shuffle(list)
# print(list)
# print()

#0으로 25개 1차원 리스트 생성

aList = [0]*25

#1로 5개를 변경 
for i in range(5):
    aList[i] =1
print(aList)

#랜덤섞기
random.shuffle(aList)
print(aList)
bList=[[0]*5 for i in range(5)]  # 5*5 공간을 생성
print(bList)

# 5*5 2차원 리스트에 넣기 
bLists=[]
for i in range(5):
    for j in range(5):
        bList[i][j] =aList[5*i+j]
        
        
#4. 5*5 2차원 리스트에 넣기
checkList=[[0]*5 for i in range(5)]    
for i in range(5):
    checkList[i][j]=aList[5*i+j]         
        
#5. checkList 출력

while True:
    
    print("\t[5*5 좌표]")
    print("-"*40)
    print("",0,1,2,3,4,sep="\t")
    print("-"*40)
    for i in range(5):
        print(i, end="\t")
        for j in range(5):
            print(checkList[i][j], end="\t")
    print("-"*40)


    #6.viewList출력
    print("\t[5*5 좌표]")
    print("-"*40)
    print("",0,1,2,3,4,sep="\t")
    print("-"*40)
    for i in range(5):
        print(i, end="\t")
        for j in range(5):
            print(viewList[i][j], end="\t")
        print()
    print("-"*40)

    # 7.좌표 입력 후 확인
    cnt=0
    x=int(input("가로 좌표를 입력하세요.>>"))
    y=int(input("세로 좌표를 입력하세요.>>"))
    if checkList[x][y] == 1:
        viewList[x][y] = "당첨"
        cnt+=1
    else:
        viewList[x][y] = "[꽝]"
print()

    # for i,j in enumerate(bList):
    #     if (i+1)%10 == 0:  #0,1,2,3,4,5,6,7,8,9
    #         bList.append(j)
    #         bList.append(j) 
    #         bLists.append(bList)
    #         bList=[] #100번 처음으로 초기화 
    #     else:
    #         bList.append(j)

    # print(bLists) '