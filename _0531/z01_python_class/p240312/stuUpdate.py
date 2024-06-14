def stu_print():
    print("[학생성적 프로그램]")
    print("1.학생성적입력")
    print("2.학생성적출력")
    print("3.학생성적검색")
    print("4.학생성적수정")
    print("5.학생성적삭제")



def stuUpdate(choice):
    print(f"[{s_title[choice]}성적 수정]")
    print(f"현재 {s_title[choice]}성적: ", {stu[choice+1]})
    print("-"*30)
    stu[2]=int(input("수정 점수를 입력하세요."))
    print("수정된 점수:  ", stu[choice+1])
    stu[5] = stu[2]+stu[3]+stu[4]  #합계수정
    stu[6]=float("{:.2f}").format(stu[5]/3)  #평균수정
    print(f"{s_title[choice]})점수가 수정되었습니다.")
    
    
stu =[1,'홍길동',100,100,100,300,100.0,1]
s_title=["","국어","영어","수학"]

while True:
    print("학생데이터",stu)
    print("3.학생성적수정")
    choice=int(input(("번호선택>>")))
    if choice ==3: 
        s_update(choice,stu,stuUpdate)
        