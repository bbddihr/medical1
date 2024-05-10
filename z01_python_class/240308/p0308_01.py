#리스트 
#1.
list=[]
for i in range(1,11):
    list.append(i)
print(list)

#2.
list=[0]*10
for i in range(0,10):
    list[i]=i+1
print(list)

#3.
list=[i for i in range(1,11)]
print(list)

#3가지 방법. 