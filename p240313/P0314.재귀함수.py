
def count(num):
    if num >= 1:
        print(num,end=" ")
        count(num-1) #함수를 다시 호출: 재귀함수
    else:
        return
    
count(3)


# for i in range(10,1-1,-1):
#     print(i,end=" ")