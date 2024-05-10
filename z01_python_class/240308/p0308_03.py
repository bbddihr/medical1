# a_list=[0]*52 
# print(a_list)


# c_list=[0 for i in range(52)]
# b_list=[]
# for i in range(52):
#     b_list.append(0)
    
# print(a_list)
# print(b_list)
# print(c_list)


#2차원 리스트 생성방법
aa=[[0]*1] *52 #얕은복사이기에 쓸수 없음.
bb=[[0]*2 for i in range(52)]
bb[0][0] = 1
bb[51][1] =10
print(bb)

cc=[]
for i in range(52):
    dd=[]
    for i in range(2):
        dd.append(0)
    cc.append(dd)
    
print(cc)

        