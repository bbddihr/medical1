'''
#list 만드는방법
list=[ [],[],[]]
#2차원 리스트 -크기가 지정이 안됨.
a_list =[]
a_list.append(0)  #리스트 append추가를 하게되면 속도가 느림.
a_list.append(1)
a_list.append(2)
print(a_list)
#[0,1,2]
a_list[0]=3    #리스트에 값을 넣는 것이 속도면으로는 빠름
print(a_list)
print()

#공간을 만들어 놓고 for 문 사용
list = [0]*10 
for i in range(10):
    list[i] = i+1
print(list)

#컴프리헨션을 사용하는 방법
list1=[i+1 for i in range(10)]
print(list1)

'''
list=[i+1 for i in range(10)]
print(list)



numList= [num for num in range(1,6)]
numList=[num*num for num in range(1,6)]
numL=[num for num in range(1,2)ifnum %3==0]

#zip() 함수
