a_list = [1,2,[3,4],[6,7,8,9],[10,11]]

# for a in a_list:
#     print(a,end=" ")
    #1,2,3,4,5,6,7,
aa_list=[]
for a in a_list:
    if type(a) == list:
        for i in a:
            aa_list.append(i)
            print(i,end=" ")
    else:
        print(a,end=" ")
        aa_list.append(a)
print()    
print(aa_list)