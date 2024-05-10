'''
리스트 공간을 먼저 생성
a=[[],[],[],[],[]]
리스트 공간 초기화를 먼저 해주어야함.
for i in range(0,5):
    for j in range(0,5):
        a[0][0] =1
        a[0][1] =2
        a[0][2] =3
        a[0][3] =4
        a[0][4] =5
        a[1][0] =6
        
        
        
        a[i][j] = (5*i)+j+1 

print


a=[[0,0,0,0,0],[0,0,0,0,0],[0,0,0,0,0],[0,0,0,0,0],[0,0,0,0,0]]
# 2차원 리스트 1-25까지 데이터 넣기
value=1
for i in range(0,5): # 0,1,2,3,4
    for j in range(0,5):   #0,1,2,3,4,
        a[i][j] =value  # 외우기 (5*i)+j+1
        value +=1
        
print(a)
print()

#좌표를 입력하면 좌표를 0으로 변경하는 프로그램을 구현
while True:
    # 2차원 리스트 출력
    print(0,"|",0,1,2,3,4,sep="\t")
    print('-'*50)
    for i in range(0,5):
        print(i,sep="\t")
        print(i,"\t","|", end="\t")
        
        for j in range(0,5):
            print(a[i][j],end="\t")
        print()    
    x=int(input('X좌표를 입력하세요'))
    y=int(input('Y좌표를 입력하세요'))
    #입력ㄱ된 좌표값이 0으로 변경
    a[x][y] ="X"

'''
a=[[0,0,0,0,0],[0,0,0,0,0],[0,0,0,0,0],[0,0,0,0,0],[0,0,0,0,0]]
value=1
for i in range(0,5):
    for j in range(0,5):
        a[i][j]=value
        value+=1
print(a)



while True:
    print(0,1,2,3,4,sep="\t")
    for i in range(0,5):
        print(i,sep="/t")
        
        for j in range(0,5):
            print(a[i][j],end="\t")
        print()
    x=int(input('X좌표를 입력하세요'))
    y=int(input('Y좌표를 입력하세요'))
    