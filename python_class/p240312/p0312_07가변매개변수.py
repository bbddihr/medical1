#가변매개변수

def str_title(num,*txt):
    print("txt타입: ",type(txt))
    for i in range(num):
        for t in txt:
            print(t,end=" ")
        print()
    
    
print()
str_title(2,"안녕","잘가","안녕하세요","반갑습니다") 

