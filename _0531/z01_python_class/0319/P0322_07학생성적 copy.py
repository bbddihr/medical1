# print("-"*40)
# print("[ 학생성적프로그램 ]")
# print("-"*40)
# print("1. 학생성적입력")
# print("2. 학생성적전체입력")
# print("3. 학생검색")
# print("4. 학생성적수정")
# print("5. 학생성적삭제")
# print("6. 등수처리")
# print("0. 종료")
# print("-"*40)
# choice = input("원하는 번호를 입력하세요.>> ")
# choice = int(choice)

class Student:
    count=1
    def __init__(self,name,kor,eng,math,stuNo=0,rank=0):
        if stuNo==0:
            self.stuNo=Student.count
        else:
            self.stuNo=stuNo
        self.name=name
        self.kor=kor
        self.eng=eng
        self.math=math
        self.total=kor+eng+math
        self.avg=float("{:.2f}".format(self.total/3))
        self.rank=rank
    def __str__(self):
        return f"{self.stuNo}\t{self.name}\t{self.kor}\t{self.eng}\t{self.math}\t{self.total}\t{self.avg}\t{self.rank}\t"
students=[]
f=open("stu.txt","r",encoding="utf8")
while True:
    txt = f.readline()
    if txt =="": break
    txt_list=txt.split(",")
    s= Student(txt_list[1]),int(txt_list[2]),int(txt_list[3]),int(txt_list[4]),int(txt_list[0]),int(txt_list[7])
    students.append(s)
f.close()

Student.count=len(students)+1
search_txt=["","찾고자 하는 학생이름을 입력하세요.",
            "몇점이상 검색하시겠습니까?>>",
            "몇점이하 검색하시겠습니까?>>"]


def main_title_print():
    print("-"*40)
    print("[ 학생성적프로그램 ]")
    print("-"*40)
    print("1. 학생성적입력")
    print("2. 학생성적전체입력")
    print("3. 학생검색")
    print("4. 학생성적수정")
    print("5. 학생성적삭제")
    print("6. 등수처리")
    print("0. 종료")
    print("-"*40)
    choice = input("원하는 번호를 입력하세요.>> ")
    choice = int(choice)
    return choice
def stu_main_print():
    print('\t[ 학생성적출력 ]')
    print('-'*65)
    print('학번\t이름\t국어\t영어\t수학\t합계\t평균\t등수\t')
    print('-'*65)
def stu_insert():
    while True:
        name=input(f"{len(students)+1}번째 학생의 이름을 입력하세요(0.취소)")   
        if (name=="0"):
            print("학생 입력을 취소합니다.")
            break
        kor=int(input("국어점수를 입력하세요"))
        eng=int(input("영어점수를 입력하세요"))
        math=int(input("수학점수를 입력하세요"))
        s=Student(name,kor,eng,math)
        students.append(s)
        print("입력데이터:  ",s)
        
def stu_print():
    stu_main_print()
    for i in students:
        print(i)
    print()
    
def search_title_print():
    print("\t[학생성적 검색]")
    print("-"*40)
    print("1.학생이름으로 검색")
    print("2.총점이상 검색")
    print("3.총점이하 검색")
    print("0.이전화면 이동")
    choice=int(input("원하는 번호를 입력하세요.>"))
    return choice
def stu_search(choice):
    if choice ==1:
        search=input(search_txt[choice])
        # search_txt=["","찾고자 하는 학생이름을 입력하세요.",
        #     "몇점이상 검색하시겠습니까?>>",
        #     "몇점이하 검색하시겠습니까?>>"]
    else:
        search=int(input(search_txt[choice]))
    s_list = []
    for i in students:
        if choice==1:
            if i.name.find(search) != -1:
                s_list.append(i)
        elif choice ==2:
            if i.total >= search:
                s_list.append(i) 
        elif choice ==3:
            if i.total <= search:
                s_list.append(i)
    if len(s_list) != 0:
        stu_main_print()
        for i in s_list:
            print(i)
    else:
        print("찾고자 하는 학생이 없습니다. 다시 검색하세요.")
        
def stu_update():
    search=input("찾고자 하는 이름을 입력하세요 . >>")
    cnt =0 
    for s in students:
        if s.name ==search:
            break
        cnt+= 1 
    if cnt >= len(students):
        print("찾고자 하는 학생이 없습니다. 다시검색하세요")
    else:
        print(f"{search} (으)로 검색한 학생을 찾았습니다.")
        print()
        print("[ 수정할 과목 선택 ]")
        print("-"*30)
        print("1. 국어")
        print("2. 영어")
        print("3. 수학")
        print("-"*30)
        choice = int(input("원하는 번호를 입력하세요.>> "))
        if choice ==1:
            print(f"변경전 점수: {students[cnt].kor}")
            students[cnt].kor=int(input("변경할 점수를 입력하세요"))
            students[cnt].total=students[cnt].kor + students[cnt].eng+students[cnt].math
            students[cnt].avg=float("{:.2f}".format(students[cnt].total/3))
            print(f"{students[cnt].kor}으로 점수가 변경되었습니다.")


def stu_delete():
    search=input("삭제하고자 하는 학생이름을 입력하세요>")
    cnt=0
    for s in students:
        if s.name ==search:
            break
        cnt+=1
    if cnt>=len(students):
        print("찾는학생이 없습니다. 다시검색하세요.")
    else:
        print(f"{search} 로 검색한 학생이름을 찾았습니다.")
        print("[학생성적 삭제] 1. 실행  0.취소")
        choice =int(input("원하는 번호를 입력하세요.>> "))
        if choice ==1:
            del students[cnt]
            print(f"{search}학생 성적이 삭제 되었습니다.")
        else:
            print("학생성적 삭제를 취소하였습니다.")
            
def stu_rank():
    print("[등수처리 진행] 1. 진행  0.취소")
    choice =int(input("원하는 번호를 입력하세요.>>"))
    if choice == 1:
        for s in students:
            rank_count = 1
            for ss in students:
                if s.total< ss.total:
                    rank_count +=1
                s.rank= rank_count


# # 등수처리 함수
# def stu_rank():
#     # 등수처리는 합계를 가지고 처리함.
#     for s_dic in students: #enumerate수정함
#         rank_cnt = 1 #등수처리변수
#         for i_dic in students:
#             if s_dic["total"]<i_dic["total"]: #두수를 비교
#                 rank_cnt += 1 # 현재 학생의 합계보다 크면 1증가
#         s_dic["rank"] = rank_cnt

#     print("등수처리가 완료되었습니다.")
#    print(students)



while True:
    choice=main_title_print()
    if choice == 1:
        stu_insert()
    elif choice==2:
        search_title_print()
    elif choice ==3:
        while True:
            choice=search_title_print()
            if choice ==0:
                print("이전 화면으로 이동합니다.")
                print()
                break
            stu_search(choice)
    elif choice ==4:
        stu_update()
    elif choice ==5:
        
            
                  