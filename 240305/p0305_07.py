a=[1,2,3,4,5]
aa=[[1,[3,4,5],3,4],[5,6],[7,8,9]]   #2차원, 2중 for문
aaa=[[[1,2,],[3,4,5]],[[6],[7,8,9]]]

for i in a:
    print(i)
print("-"*50)
for i in aaa:
    for j in i:
        if j != list:
            print(j)
        else: 
            for k in j:
                print(k)
        
        