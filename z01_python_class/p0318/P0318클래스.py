#클래스 :사용자정의 ***변수****-함수도 포함
#클래스 첫글자 대문자 사용
#클래스:설계도


#클래스 선언
class Car :   
    color="white"
    door=5
    length = 4710
    width= 1800
    displace= 1600
    
    def upSpeed(self,sp):
        self.speed += sp
        
    def downSpeed(self,sp):
        self.speed -= sp


#객체선언을 할때마다 제품(Car)이 한개씩 생산
#c1이랑 c2는 다르다.
       
c1=Car()  #객체선언
print("샛상 : ", c1.color)
c1.color = "red"
print("변경 후 색상: ",c1.color)














   

# def func():
#     pass
    

# c1=Car() #클래스 객체선언:Car클래스에 있는 모든 변수를 사용함
# print(c1.length)
# c2=Car()
# c3=Car()

# a_l1=4710
# print(a_l1)
# a_w1 = 1800
# a_d1=1600

# a_l2=4710
# a_w2 = 1800
# a_d2 =1600

# a_l3=4710
# a_w3 = 1800
# a_d3 =1600


# a=1
# a1=1
# a2=1
# a3=1
# b=[1,2,3]
# print(a)
