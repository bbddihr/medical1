#매개변수 순서 중요, 매개변수 타입도 중요


def str_print(num,txt):
    for i in range(num):
        print(txt,end='')
    #글자반복출력

txt=input("출력하고 싶은 글자를 입력하세요.>>")
num = int(input("출력하고 싶은 글자 반복횟수를 입력하세요>>"))
str_print(num,txt)

#안녕하세요.
#3
