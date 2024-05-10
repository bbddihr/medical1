# list = [[0,0,0],[0,0,0],[0,0,0]]

# for i in list:
#     for f in i:
#         print(f, end="\t")
#     print()
  
  
#1-9까지의 1차원 리스트에 숫자를 입력하시오.
list=[]
list1=[]
for i in range(9):
    list.append(i+1)
print(list)
print()
#컴플리헨션
list2=[2*n+1 for n in range(9)]
print(list2)

list3 = [[n]*3 for n in range(3)]
print(list3)
print()

numList = [num*num for num in range(1,6)]
print(numList)

#1-9까지의 2차원 리스트에 숫자를 입력하시오.
# [[1,2,3]
# [4,5,6],
# [7,8,9]]

# a_lists=[]
# for i in range(3):
#     a_list = []
#     for j in range(3):
#         a_lists.append(3*i+j+1)  #[0,1,2]
#     a_lists.append(a_list)  #[[0,1,2][0,1,2]]

# print(a_lists)