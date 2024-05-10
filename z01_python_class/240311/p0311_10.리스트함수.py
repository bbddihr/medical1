#매개변수로 리스트 사용할 경우 return할 필요가 없음.
#함수선언 
def func1(a,a_list):
    a=100 #지역변수
    a_list[0]=100
    return a

a=10   #전역변수
a_list = [1,2,3]
#함수호출
a =func1(a,a_list) #2개 이상의 데이터를 저장하는 변수. 주소값을지정함.

#데이터출력 
print(a)
print(a_list)

