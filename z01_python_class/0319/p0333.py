class Student:
    count = 1 # 클래스 변수 사용
    def __init__(self,name,kor,eng,math,stuNo=0,rank=0):
        if stuNo == 0:
            self.stuNo = Student.count  # 클래스변수 사용
        else:
            self.stuNo = stuNo
        self.name = name
        self.kor = kor
        self.eng = eng
        self.math = math
        self.total = kor + eng + math
        self.avg = float("{:.2f}".format(self.total/3))
        if rank != 0:
            self.rank = rank
    def __str__(self): 
        return f"{self.stuNo}\t{self.name}\t{self.kor}\t{self.eng}\t{self.math}\t{self.total}\t{self.avg}\t{self.rank}"

students = []
f = open("stu.txt","r",encoding="utf8")
while True:
    txt = f.readline()
    if txt == "": break
    txt_list = txt.split(",")
    # 1,홍길동,99,99,87,285,95.0,1
    s = Student(txt_list[1],int(txt_list[2]),int(txt_list[3]),int(txt_list[4]),int(txt_list[0]),int(txt_list[7]))
    students.append(s)
f.close()
#------------------------------------------
def stu_main_print():

    print('\t[ 학생성적출력 ]')
    print('-'*65)
    print('학번\t이름\t국어\t영어\t수학\t합계\t평균\t등수')
    print('-'*65)
    
def stu_main_print():
    
    print(students[s_cnt])
    print("[학생성적 검색]")
    search =input("찾고자하는학생 이름을 입력하세요.>")
    s_cnt =0
    for i in students:
        if search == i.name:
            break
        s_cnt +=1
    if s_cnt != len(students):
        stu_main_print()
        print(students[s_cnt])
    else:
        print("찾고자 하는 학생이 없습니다. 다시 검색하세요")
                
#-------------------------------------------
#파일 불러오기 한후 학생수에서 +1추가
Student.count=len(students)+1
# def stu_main_print():
          
while True: 
    print('-'*40)
    print('\t[학생성적프로그램]')
    print('-'*40)
    print('1. 학생성적입력')
    print('-'*40)
    print('0. 프로그램 종료')
    choice = input('원하는 번호를 입력하세요:  ')
    choice=int(choice)

    if choice ==1:
        while True :
            Student.count=len(students)
            name = input(f"{len(students)+1}번째 학생의 이름을 입력하세요.(0.취소)")
            if(name=="0"):
                print("학생 입력을 취소합니다.")
                break
            kor = int(input("국어점수를 입력하세요."))
            eng = int(input("영어점수를 입력하세요."))
            math = int(input("수학점수를 입력하세요."))
        
            s=Student(name,kor,eng,math)
            students.append(s)
            print("입력 데이터 :",s)
            print(students)
            
    elif choice ==2:
            search=int(input("몇점이상 검색하시겠습니까?>>"))
            s_list =[]
            for i in students:
                if i.total <= search:
                    s_list.append(i)
                    
            if len(s_list) !=0:
                stu_main_print()
                for i in s_list:
                    print(i)
            else:
                print("찾고자하는 학생이 없습니다. 다시 검색>>")

    elif choice ==3:
        while True:
            print("1.학생성적검색")
            print("-"*40)
            print("1.학생이름으로 검색")
            print("1 총점이상 검색")
            print("1.총점이하 검색")
            print("0.이전화면 이동")

            choice =input("원하는 번호를 입력하세요>>")
            
            if choice ==1:
                search==input("찾고자하는 학생 검색")
        
        s_cnt=0
        s_list=[]
        for i in students:
            if i.name.find(search) != -1:
                s_list.append(i)
        
        if len(s_list) !=0:
            stu_main_print()
            for i in s_list:
                print(i)
                 
        # print("[학생성적 검색]")
        #  for s in stu:
        #     if s[1] >= score:  
        #          print("찾는 사람이 있습니다. name리스트 위치 : ",cnt)
        #         search_list.append(cnt)
        #     cnt += 1
        # # 검색된 사람들 출력
        # if len(search_list) == 0:
        #     print(f"{score} 보다 큰 점수는 없습니다.")
        # else:
        #     print(f"[ {score} 보다 큰 점수 ] ")
        #     for i in search_list:
        #         print(stu[i][0],":",stu[i][1])
        #     print()
        #     print()
        
        
        
        
        
        
        
           
   
      
    
        
'''                
Student.stu_main_print()

s1=Student()
s1.stuNo=1
s1.stu_name="홍길동"
s1.kor=99
s1.eng=99
s1.math=87
s1.total=s1.total+s1.eng+s1.math
s1.avg=float("{:.2f}".format(s1.total/3))
s1.rank=1
print(f"1번학생: {s1.stuNo},{s1.stu_name},{s1.kor},{s1.eng},{s1.math},{s1.total},{s1.avg},{s1.rank}")


'''