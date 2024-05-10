#str.txt 파일의 내용을 모두 출력하시오.
#파일열기
f=open("str.txt","r")
#파일읽기
while True:
    content = f.readline()
    if content.strip() =="":break  #strip 빈공백enter키 삭제
    print(content, end='')
#파일닫기
f.close()

#str.txt 파일 내용을 읽어와서 
#str1.txt에 그 내용을 추가해보세요.

f= open("str.txt","r")
ff=open("str1.txt","a")
while True:
    content=f.readline()   #파일내용을 읽어오기 
    if content.strip() =="" :break
    ff.write(content)      #파일내용을 추가하기 
    
f.close()
ff.close()   

fff=open("str1.txt","r")
while True:
    content=fff.readline()
    if content.strip() =="":break
    print(content,end='')
fff.close()
    

'''
f=open("str.txt","r")
while True:
    content = f.readline()
    if content == "":break
    print(content,end="")
    
    f=open("str1.txt","a")
    print("[아래 글을 입력하세요]")
    with open("str1.txt","a") as f:
        for txt in txt_list:
            print(txt,end="")
            print("파일에 글자를 저장했습니다.")   
        print() 
        



          

            # #파일쓰기
            # while True:
            #     txt_input = input('')
            #     if txt_input == "-1":break
            #     f.write(txt_input+"\n")
           '''