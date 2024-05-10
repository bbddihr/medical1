# a_list=[1,2,3]
# #얕은복사
# b_list = a_list

# b_list[0] = 100

# print(a_list)

#리스트에는 return 받을 필요 없음.
#함수선언
def stu_update(student): #지역변수 ->주소값이 저장 
    student['stuNo']=2
    student['name'] = "유관순"
    student['total'] = student['kor']+student['eng']+student['math'] 
    student['avg']=student['total']/3
   
    
#프로그램 구현
student = {'stuNo': 1, 'name': '홍길동', 
           'kor': 100, 'eng': 99, 'math': 87, 
           'total': 0, 'avg': 0}


#함수호출
stu_update(student)  #전역변수

print("학생1: ",student)

