#파일읽어오기
#1. 파일 열기
#read() : 모든 문자열을 가져옴. 
#readline() : 1줄씩 가져옴.
#readlines() : 1줄씩 리스트 타입에 입력해서 모두 가져옴.
#2. 파일 닫기
# 파일 확인
import os
if not os.path.exists("str.txt"):#파일존재 확인
#f=open("str.txt","r")
    with open("str.txt","r") as f:
        txt_list=f.readlines()   
        
        for txt in txt_list:
            print(txt,end="")
        print() 
    
#with를 쓰면 f.close() 생략가능 
    




# #readlines
# f=open("str.txt","r")
# #1줄씩 리스트타입으로 저장
# txt_list=f.readlines()
# txt=f.readlines()

# print(txt)
# print(txt_list[0])
###f.close() #파일종료를 반드시 해야함. 중요 


# readlines #1줄씩 리스트 타입으로 가져옴 .
# f = open("str.txt","r")
# while True:
#     txt= f.readline()
#     if txt == "":break
    
#     print(txt)
    
# print("모든 파일을 읽어 왔습니다.")
