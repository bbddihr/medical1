#리스트에 1,25 까지 숫자를 리스트에 입력하시오.
# a=[]
# for i in range(1,26):
#     a.append(i)
# print(a)

#1부터 25까지 2차원 리스트 생성
#[[1,2,3,4,5],[6,7,8,9,10],....,[21,22,23,24,25]]
b=[]
b_i =[]
for i in range(0,25):
    if (i+1)%5==0:
         b.append(i+1)
    
    else:
        pass
   
print(b)
print("-"*40)