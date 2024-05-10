# a_list=[1,2,3]
# #얕은복사
# b_list = a_list

# b_list[0] = 100

# print(a_list)

#리스트에는 return 받을 필요 없음.
#함수선언
def stu_update(student): #지역변수 ->주소값이 저장 
    student[0]=2
    student[1] = "유관순"
    student[5] = student[2]+student[3]+student[4] 
    student[6]=student[5]/3
   
    
#프로그램 구현
student = [1,"홍길동",100,100,100,0,0]   #2개이 이상의 변수


#함수호출
stu_update(student)  #전역변수

print("학생1: ",student)

