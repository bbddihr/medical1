import os



#폴더 생성
os.mkdir("hello")
#폴더 삭제
os.rmdir("hello")

#파일생성
# with open ("students.txt","w") as f:
#     f.write("1",'홍길동',100,99,87,286,95.33,2)

str1= "1,'홍길동',100,99,87,286,95.33,2"
s_list =str1.split(",")

for i in s_list:
    print(i)