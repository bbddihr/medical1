students = [] # 전체학생의 리스트
with open("stu.txt","r",encoding="utf8") as f:
    while True:
        txt = f.readline() # 1줄씩 읽기
        if txt == "": break
        t_list = txt.split(",") 
        s_dic = {
            "stuNo":int(t_list[0]),"name":t_list[1],
            "kor":int(t_list[2]),"eng":int(t_list[3]),"math":int(t_list[4]),
            "total":int(t_list[5]),"avg":float(t_list[6]),"rank":int(t_list[7])
        }
        students.append(s_dic)
print(students)


cnt=len(students)
def stu_main_print():
    print('-'*40)
    print('[학생성적프로그램]')
    print('-'*40)
    print('1. 학생성적입력')
    print('2. 학생성적전체출력')
    print('3. 학생검색')
    print('4. 학생수정')
    print('5. 등수처리')
    print('6. 학생삭제')
    print('7.학생성적 파일저장')
    print('0. 프로그램 종료')
    print('-'*40)
    choice = input('원하는 번호를 입력하세요:  ')
    print('-'*40)
    if not choice.isdigit():
        print('숫자만 입력 가능합니다.')
        
    choice = int(choice)
    
    return choice

    # 1. 학생성적입력
def stu_insert():
    while True :
        name = input(f"{len(students)+1}번째 학생의 이름을 입력하세요.(0.취소)")
        if(name=="0"):
            print("학생 입력을 취소합니다.")
            break
        student= {} #데이터 초기화
        student["stuNo"] = "S"+"{:03d}".format(cnt)
        student["name"] = name  # 딕셔너리 추가
        kor = int(input("국어점수를 입력하세요."))
        student["kor"] = kor
        eng = int(input("영어점수를 입력하세요."))
        student["eng"] = eng
        math = int(input("수학점수를 입력하세요."))
        student["math"] = math
        total = kor+eng+math
        student["total"] = total
        avg = total/3
        student["avg"] = float("{:.2f}".format(avg))
        students.append(student)
        cnt += 1
        print("입력 데이터 :",student) 
        print(students)
            
            

def stu_all_print():
    print('\t[ 학생성적전체출력 ]')
    print('-'*65)
    print('학번\t이름\t국어\t영어\t수학\t합계\t평균\t등수')
    print('-'*65)
    for s_dic in students:
        for s_key in s_dic:
            print(s_dic[s_key],end="\t")
        print()
    print('-'*65)
    print()
# def stu_search():
#     search = input("찾고자 하는 학생의 이름을 입력하세요.(0.취소)")
#     chk = 0
#     if search == "0":
#         break
    
#     for s_dic in students:
#         if s_dic["name"] == search:
#             break
#         chk += 1
#     print("찾고자 하는 학생의 위치 :",chk)
#     if chk == len(students): 
#         print(f"{search} 학생은 없습니다. 다시 입력하세요.")
#     else:
#         print(f"{search} 학생을 찾았습니다.")


#등수처리 함수       
def stu_rank():
    for i, s_dic in enumerate(students):
        rank_cnt=1    
        for i_dic in students:
            if s_dic["total"]<i_dic["total"]: 
                rank_cnt += 1 
        s_dic["rank"] = rank_cnt
        print("등수처리가 완료되었습니다.")
        print(students)

#학생성적파일 열기함수
def stu_open():
    students=[]
    with open("stu.txt","r",encoding="utf8") as f:
        for s in students:
            stuNo=s["stuNo"]
            name=s["name"]
            kor=s["kor"]
            eng=s["eng"]
            math=s["math"]
            total=s["total"]
            avg=s["avg"]
            rank=s["rank"]
            f.write(f"{stuNo},{name},{kor},{eng},{math},{total},{avg},{rank}")
        print("모든 내용이 파일에 저장되었습니다.")
        print()

def stu_update():
    pass   
        
        
while True:
    choice=stu_main_print()
    
    if choice == 1 :
        stu_insert(cnt)
        stu.file.stu_save(students)     
    elif choice == 2 :
        stu_all_print()
    elif choice == 3 :
        stu_search()
    elif choice ==4:
        s_title()  
    elif choice ==5:
        stu_rank()
    elif choice ==6:
        stu_del()
    elif choice ==7:
        stu_file.stu_save(students)      
         
            
                






'''



def stu_title(choice):
    print("학생성적수정")
    print(["1. 국어  2. 영어    3. 수학"])
    choice = int(input("원하는 번호를 입력하세요>>"))   
    
    print(f"[{s_[choice]}성적 수정]")
    print(f"현재 {s_title[choice]}성적: ", {s_dic[choice+1]})
    print("-"*30)
    s_dic[choice+1]=int(input("수정 점수를 입력하세요."))
    print("수정된 점수:  ", students[choice+1])
    s_dic[5] = students[2]+students[3]+students[4]  
    students[6]=float("{:.2f}").format(students[5]/3) 
    print(f"{s_title[choice]})점수가 수정되었습니다.")
    


    if s_input == 1:
        s_1 = "kor"
        print("[ {} 수정 ]".format(s_title[s_input]))
        print("현재 {}점수 : {}".format(s_title[s_input],students[chk][s_1]))
        print("-"*20)
        score = int(input("수정할 {}점수를 입력하세요.".format(s_title[s_input])))
        students[chk][s_1] = score
        # 합계수정
        students[chk]["total"] = students[chk]["kor"] + students[chk]["eng"] + students[chk]["math"]
        students[chk]["avg"] = float("{:.2f}".format(students[chk]["total"]/3))
        print("{}점수 : {}점으로 수정이 완료되었습니다.".format(s_title[s_input],students[chk][s_1]))
        print(students[chk])
    elif s_input == 2:
        s_1 = "eng"
        print("[ {} 수정 ]".format(s_title[s_input]))
        print("현재 {}점수 : {}".format(s_title[s_input],students[chk][s_1]))
        print("-"*20)
        score = int(input("수정할 {}점수를 입력하세요.".format(s_title[s_input])))
        students[chk][s_1] = score
        # 합계수정
        students[chk]["total"] = students[chk]["kor"] + students[chk]["eng"] + students[chk]["math"]
        students[chk]["avg"] = float("{:.2f}".format(students[chk]["total"]/3))
        print("{}점수 : {}점으로 수정이 완료되었습니다.".format(s_title[s_input],students[chk][s_1]))
        print(students[chk])
    elif s_input == 3:
        s_1 = "math"
        print("[ {} 수정 ]".format(s_title[s_input]))
        print("현재 {}점수 : {}".format(s_title[s_input],students[chk][s_1]))
        print("-"*20)
        score = int(input("수정할 {}점수를 입력하세요.".format(s_title[s_input])))
        students[chk][s_1] = score
        # 합계수정
        students[chk]["total"] = students[chk]["kor"] + students[chk]["eng"] + students[chk]["math"]
        students[chk]["avg"] = float("{:.2f}".format(students[chk]["total"]/3))
        print("{}점수 : {}점으로 수정이 완료되었습니다.".format(s_title[s_input],students[chk][s_1]))
        print(students[chk])
    else:
        print("과목 수정을 취소합니다.")
        break
    
def stu_del():
     while True:
        search = input("삭제하고자 하는 학생의 이름을 입력하세요.(0.취소)")
        chk = 0
        if search == "0":
            break
        for s_dic in students: #5명이 있으면 5번반복
            if s_dic["name"] == search:
                break
            chk += 1
        print("찾고자 하는 학생의 위치 :",chk)
        if chk >= len(students):
            print("찾고자 하는 학생이 없습니다.")
        else:
            print("{} 학생을 찾았습니다.".format(search))
            s_input = input("{} 학생 성적을 삭제하시겠습니까?(1.실행, 0.취소)".format(search))
            # 삭제
            if s_input != "1":
                print("삭제를 취소합니다.")
                break
            else:
                del students[chk]
                print("{} 학생성적이 삭제 되었습니다.".format(search))
                print(students)



#______________________________________

        
'''          
