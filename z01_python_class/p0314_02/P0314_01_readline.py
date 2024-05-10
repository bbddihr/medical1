#stu.txt파일을 출력하시오.

file=open("stu.txt","r",encoding="utf8")
f_list = []
# while True:
txt=file.readline()
# if txt =="":
#    break
f_list=txt.split(",")
f_list [0] = int(f_list[0])
f_list [1] = (f_list[1])
f_list [2] = int(f_list[2])
f_list [3] = int(f_list[3])
f_list [4] = int(f_list[4])
f_list [5] = int(f_list[5])
f_list [6] = float(f_list[6])

print(f_list)

for i in f_list:
   print(i)


# # content = file.read()  
# # content = content.strip()
# # print(content)

# while True:
#    txt=file.readline()
#    if txt =="0":
#       break   
#    print(txt,end="")


# file.close()
# # file.close()





# list = [0]*5
# print(list)    


 

# content = file.read() 
# content = content.strip()

#파일 읽어오기

# file =open("str.txt","r",encoding="utf8")
# while True:
#    txt=file.readline()
#    if txt =="":
#       break   
#    print(txt,end="")


# file.close()


# #파일저장
# file = open("str.txt","w",encoding="utf8")

# file.write("안녕하세요.반갑습니다.\n")
# file.write("저는 홍길동입니다.\n")
# file.write("파이썬 수업을 열심히 듣고 있습니다.\n")

# file.close()
# print("파일이 저장되었습니다.")
