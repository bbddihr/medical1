#Car 클라스 선언
#carNo 클라스변수 이용해서
#carNo 에는 carCount 숫자를 이용해서 carNo를 넣으시오 . 
#up_speed 함수를 호출하면 10씩 증가
#down_speed 함수 호출하면 -10씩 감소
#c1 -white,5,4,0 ->speed 30
#c2 -red,5,4,0 ->speed 100
#c3- silver, 5,4,0 - > speed 70
#car_ list 추가하고
#car_ list에 있는 모든 객체의 모든 color, door, tire, speed 모두출력 

class Car:
    carCount=0
    carNo=0
    def __init__(self,carNo=0,color="",door=0,tire=0,speed=0):
        self.carNo=carNo
        self.color=color
        self.door=door
        self.tire=tire
        self.speed=speed
        self.carNo=Car.carCount
        
        Car.carCount+=1
         
    def up_speed(self,speed):
         self.speed+=10
    
            
    def down_speed(self,speed):
        self.speed-=10
        
    def car_print(self):
        print(f'car:{self.carNo},{self.color},{self.door},{self.tire},{self.speed}')   

c1=Car(0,"white",5,4,0)
c1.up_speed(10)
c1.up_speed(10)
c1.up_speed(10)
c1.car_print()
# c1=Car('',"white",5,4,0)
# c1.car_print()

c2=Car(0,"red",5,4,10)
c2.car_print()


c3=Car(0,"silver",5,4,7)
c3.car_print()

c_list=[]
c_list=[c1,c2,c3]
print(c_list)


'''
c1=Car()
c1.color="white"
c1.door=5
c1.tire=4
for i in range(3):
    c1.up_speed(10)
c1.car_print()

c2=Car()
c2.color="red"
c2.door=5
c2.tire=4
for i in range(10):
    c2.up_speed(10)
c2.car_print()

c3=Car()
c3.color="silver"
c3.door=5
c3.tire=4
for i in range(7):
    c3.up_speed(10)
c3.car_print()
c_list=[]
c_list=[c1,c2,c3]
print(c_list)


# c1=Car('',"white",5,4,0)
# c1.car_print()
# c2=Car("red",5,4,0)
# c3=Car("silver",5,4,0)
# car_list=[c1,c2,c3]
# print(f"철수 : {t1.color},{t1.channel},{t1.size}, {t1.volume}")

# 
# car_list=[c1]
# print(car_list)



print(f'1번차:{c1.carNo},{c1.color},{c1.door},{c1.tire},{c1.speed}')
     
c1=Car()
print("색상: ",c1.color)










print(f"1번학생: {s1.stuNo},{s1.stu_name},{s1.kor},{s1.eng},{s1.math},{s1.total},{s1.avg},{s1.rank}")

#매개변수가 있는 객return f"{self.stuNo},{{self.kor체(인스턴스) 선언



def tv_print(self):   #인스턴스함수  
        print(f"tv: {self.serial_no},{self.color},{self.name},{self.size}")
    
s1 = Student("홍길동",100,100,99)   #객체선언
s2 = Student("유관순",99,99,98)   #객체선언
print(s1)   #__str__함수호출 없으면 주소값 출력

s1.stu_print()
s2.stu_print()

#s1 stuNo를 출력하시오.
print(s1.stuNo)
s2=Student()
?

        
'''
