students = [
    {'stuNo': 'S001', 'name': '홍길동', 'kor': 100, 'eng': 99, 'math': 87, 'total': 286, 'avg': 95.33},
    {'stuNo': 'S002', 'name': '유관순', 'kor': 98, 'eng': 93, 'math': 87, 'total': 278, 'avg': 92.67},
    {'stuNo': 'S003', 'name': '이순신', 'kor': 88, 'eng': 76, 'math': 30, 'total': 194, 'avg': 64.67},
    {'stuNo': 'S004', 'name': '김구', 'kor': 100, 'eng': 100, 'math': 100, 'total': 300, 'avg': 100.0},
    {'stuNo': 'S005', 'name': '강감찬', 'kor': 98, 'eng': 85, 'math': 44, 'total': 227, 'avg': 75.67}
]

#학생성적 입력부분 구현하시오.

choice=int(input(["원하는 번호를 입력하세요>(1. 학생성적입력선택 0.취소)"]))
student={}
cnt=len(students)+1
if choice== 1 :
    print(["학생성적입력"])
    while True:
        name=input("학생이름을 입력하세요(0.취소)")
        if name == '0':
            print("학생입력을 취소합니다.")
            break
        student={}
        student["stuNo"]='S{:03d}'.format(cnt)
        student["name"]=name
        kor=int(input("국어점수를 입력하세요>"))
        student["kor"]=kor
        eng=int(input("영어점수를 입력하세요>"))
        student["eng"]=eng
        math=int(input("수학점수를 입력하세요>"))
        student["math"]=math
        total=kor+eng+math
        student["total"]=total
        avg=total/3
        student["avg"]=float('{:.2f}'.format(avg))
        students.append(student)
        cnt+=1
        print(students)
elif choice==2:
    cul=input("번호를 입력하세요 1. 학생성적출력 0.취소")
    if cul==1:
        print(['성적출력'])
        
        
       

    
    
        
    
 
 
 
