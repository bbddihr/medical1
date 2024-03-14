f=open("k001.csv","r")

cnt=0
sum=0

while True:
    content=f.readline()
    if cnt==0:
        cnt+=1
        continue
    if content =="":break
    print(content,end='')
    print()
   
f.close()

'''
    c_list=content.split(",")
    print(c_list,len(c_list))
    c_list[4]=int(c_list[4])
    sum+= c_list[4]
    print(c_list,len(c_list))
print("인원수: ",sum)
    
#파일닫기   
'''