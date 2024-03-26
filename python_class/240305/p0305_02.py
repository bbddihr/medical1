a=[]
for i in range(0,25):
    a.append(i+1)
print(a)
print('-'*40)
b=[]
b_i=[]

for i in range(0,25):
    if (i+1)%5 ==0:
        b_i.append(i+1)
        b.append(b_i)
        b_i=[]
        pass
    else:
        b_i.append(i+1) 
    
print(b)
print('-'*40)