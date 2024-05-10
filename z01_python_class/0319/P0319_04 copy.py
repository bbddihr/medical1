#student 클래스 생성,파일불러와서 클래스에 저장 후 출력하세요
class Student:

    def stu_main_print():
        print('-'*40)
        print('\t[학생성적프로그램]')
        print('-'*40)
        print('1. 학생성적입력')
        print('2. 학생성적전체출력')
        print('3. 학생검색')
        print('4. 학생수정')
        print('5. 등수처리')
        print('6. 학생삭제')
    
        print('0. 프로그램 종료')
        print('-'*40)
        choice = input('원하는 번호를 입력하세요:  ')
        print('-'*40)
        if not choice.isdigit():
            print('숫자만 입력 가능합니다.')
        choice = int(choice)
        
    def __str__(self): 
        return f"학생성적 : {self.stuNo},{self.name},{self.kor},{self.eng},{self.math},{self.total},{self.avg},{self.rank}"

    # def score(choice):
    #     print(f"학생성적:{self.stuNo},{self.name},{self.kor},{self.eng},{self.math},{self.total},{self.avg}")
          
       
#stu_main_print()
       
students = []
f = open("stu.txt","r",encoding="utf8")
while True:
    txt = f.readline()
    if txt == "": break
    txt_list = txt.split(",")
    
    s = Student(txt_list[1],int(txt_list[2]),int(txt_list[3]),int(txt_list[4]),int(txt_list[0]),int(txt_list[7]))
    students.append(s)
for stu in students:
    print(stu)
# choice1=Student()

# # s1=Student()
# # while True:
# #     print('1. 학생성적입력')
