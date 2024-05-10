class Car:
    count=0   
    def __init__(self,color="white",door=5,tire=4,speed=0):
            self.color=color
            self.speed=speed
            self.door=door
            self.tire=tire
    def up_speed(self):
        self.speed+= 10
        
    def down_speed(self):
        self.speed -=10
        
    def stop_speed(self):  
        self.speed -=10

#Car 클라스 상속
class Ambul_car(Car):
    #Car클라스의 모든걸 가져옴
    def up_speed(self):   #함수의 오버라이딩. 재정의
        self.speed+=20
        #return super().up_speed()
    def up_speed2(self):   #기존 부모의 함수를 다시 호출하고싶을때
        return super().up_speed2()  #부모의 요소를 가져올 때 super()
    
    # color="white"
    # def __init__(self,color):
    #     self.color=color
        
    def siren(self):
        print("싸이렌이 울리는 기능이 추가됩니다.")
        
class FireTruck_car(Car):
    
    
    def water(self):
        print("물을 뿌리는 기능이 추가됩니다.")
        
       
a1 =Ambul_car("white")
print("현재속도: ", a1.speed)  
a1.up_speed()   #자식의 오버라이딩이 된 함수를 호출
print("현재속도: ", a1.speed)  
a1.up_speed2() #부모의 함수를 호출
a1.stop_speed()   
print("현재속도: ", a1.speed)  
print("앰블런스색상: ",a1.color)
