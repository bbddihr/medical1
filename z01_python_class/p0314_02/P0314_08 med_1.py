#medical_1.csv 파일을 읽어와서 출력하시오.
f=open("med_1.csv","r")

cnt=0
sum=0

while True:
    content= f.readline()
    if cnt ==0:
        cnt +=1
        continue
    if content=="":break
    print(content,end="")
    print()
    c_list=content.split(",")
    print(c_list,len(c_list))
    c_list[1]=int(c_list[1])
    sum+= c_list[1]
    print(c_list,len(c_list))
print("기초생활수급대상자 전체 수: ",sum)
    
#파일닫기   
f.close()