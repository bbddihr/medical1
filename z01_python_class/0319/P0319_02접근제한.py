class Car:
    color = ""
    door =5
    tire=4
    speed=0
    
    def __init__(self,color,door,tire,speed):
        self.__color=color
        self.__door=door
        self.__tire=tire
        self.__speed=speed   #class내부에서만 접근이 가능하게 만듬.캡슐화
        #변수에 언더바__
    def up_speed(self,smartKey):
        if smartKey == "0X1100":
            self.__speed+=10
        else:
            print("스마트기 다릅니다.")
            
        
    def down_speed(self):
        self.__speed-=10
    
    def get_speed(self):
        return self.__speed  
    def set_speed(self,speed):
        self.__speed = speed

c1= Car("white",5,4,0)
c1.up_speed("0X1100")
c1.up_speed("0X1100")
c1.set_speed(500)       #데이터 보안을 위해 장치를 걸어둠 "set"      
c1.speed=1000

print(c1.get_speed()) #클래스의 변수에 직접적으로 접근이 안됨.
#get을 통해서만 접근이 가능


# c2= Car("red",4,4,0)
# c1= Car("silver",5,4,0)
