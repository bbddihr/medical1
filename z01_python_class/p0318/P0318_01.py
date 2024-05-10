
class Car:
    car_name=""
    color = ""
    door =0
    length = 0
    width = 0
    speed = 0
    
    def up_speed(self,s):   ###클라스내에는 self 를 꼭넣어야한다.
        self.speed += s
        

c1=Car()
c1.car_name = "드뉴아반떼"
c1.color ="white"
c1.door=5
c1.length = 2000
c1.width = 1000

c1.up_speed(60)    #현재 speed 60을 더해 줌. #함수사용
c1.up_speed(40)    #현재 speed는얼마? 100
c1.up_speed(50)    #현재 speed는얼마? 150    #캡슐화(정보보안차원에서 변수를 감추다)
c1.speed = 50      #현재 spped는 얼마? 50


#영희의 차를 1대 생산해서, 색상은 green, 나머지 동일, speed = 100 설정해서 출력하시오.
c2=Car()
c2.car_name="드뉴아반떼"
c2.color ="green"
c2.length=2000
c2.width=1000
c2.up_speed(150)


print("철수차 성능: " , c1.car_name.c1.color,c1.door,c1.length,c1.width,c1.speed)
print("철수차 성능: " , c2.car_name.c2.color,c2.door,c2.length,c2.width,c2.speed)
print("반장차 성능: " , c3.car_name.c3.color,c3.door,c3.length,c3.width,c3.speed)

     
'''
#철수차

color = "red"
speed = 60



#반장차- 디올뉴그랜저, 화이트펄, 길이:2500 폭:1400, speed=150

c3=Car()
car_name3="디올뉴그랜저"
c3.color="화이트펄"
door3=5
c3.length=2500
c3.width=1400
c3speed=150
print("반장차: ", c3.car_name,color,door,length,width,speed)
'''