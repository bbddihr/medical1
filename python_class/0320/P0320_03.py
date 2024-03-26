class Car:
    value = "부모의 값 1"
    def car_func(self):
        print("부모의 값을 출력합니다.")

class Am(Car):
    value= "자식의 값 2"
    def car_func(self):
        print("[자식클래스에서 부모값을 출력]")
        #부모의 값을 출력하고싶을때super()사용
        super().car_func()
        print("부모의 값: ",super().value) 
        print("자식의 값: ",self.value)
        
a1 = Am()
a1.car_func()
