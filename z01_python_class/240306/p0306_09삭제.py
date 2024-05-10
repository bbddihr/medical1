# students = [[S001, "홍길동", 100,99,87,286,95.33,2],
#             [S002, "유관순", 98,93,87,296,98.67,1],
#             [S003, "이순신", 88,76,30,194,80.33,1],
#             [S004, "김구",100,100,90,300,100.00,1],
#             [S005, "강감찬", 98,85,44,227,75.67,4]]

students=[
{'stuNo': 'S001', 'name': '홍길동', 'kor': 100, 'eng': 99, 'math': 87, 'total': 286, 'avg': 95.33}, 
{'stuNo': 'S002', 'name': '유관순', 'kor': 98, 'eng': 93,'math': 87, 'total': 278, 'avg': 92.67}, 
{'stuNo': 'S003', 'name': '이순신', 'kor': 88, 'eng': 76, 'math': 30, 'total': 194, 'avg': 64.67}, 
{'stuNo': 'S004', 'name': '김구', 'kor': 100, 'eng':100, 'math': 90, 'total': 290, 'avg': 96.67}, 
{'stuNo': 'S005', 'name': '강감찬', 'kor': 98, 'eng': 85,'math': 44, 'total': 227, 'avg': 75.67}]
subject=['순번','학번','이름','국어','영어','수학','합계','평균','등수']
s_title = ['','국어','영어','수학']
cnt=len(students)+1   #학번
while True:
    #찾는 부분 프로그램 작성.
    search = input("삭제할 학생의 이름을 입력하세요.(0.취소)")
    chk=0
    if search == "0":
        break
    for s_dic in students:   #5명이 있으면 5번 반복
        if s_dic["name"] == search:
            break
        chk += 1
            
    print("찾고자 하는 학생의 위치:",chk)
    
    if chk != len(students):  #학생수만큼 for문을 돌면
        print("찾고자 하는 학생이 없습니다.")
    else:
        print("{}학생을 찾았습니다.".format(search))
        s_input=input("{}학생의 성적을 삭제하시겠습니까?(1.실행 0.취소)".format(search))
        #삭제
        if s_input != "1":
            print("삭제를 취소합니다.")
            break
        else:
            del students[chk]
            print("{}학생성적이 삭제되었습니다.".format(search))
     
     
     
    '''
        while True:
            print("[수정할 과목 선택]")
            print("-"*30)
            s_input =int( input("수정하려는 과목을 선택하세요.(0.취소)>>"))
            print("1.국어\t2.수학\t3.수학")
            
            if s_input ==1 :
                s_1 ='kor'
                #함수호출
                #s_update(s_1)
                print("[{}수정]".format(s_title[s_input]))
                chk=0
                print("현재 {}점수:".format(s_title[s_input],students[chk]["s_1"]))
                print("-" *20)
                score=int(input("수정할 국어점수를 입력하세요."))
                students[chk]["s_1"]=score
                #합계 수정
                students[chk]["total"] = students[chk]["kor"]+student[chk]["eng"]+students[chk]["math"]
                students[chk]["avg"] = float("{:.2f}".format(student[chk]["total"]/3))
                print("수학점수: {}점으로 수정이 완료되었습니다.", students[chk]["s_1"])
                print(students[chk])
                
            elif s_input ==2 :
                s_1 ='eng'
                #함수
                #s_update(s_1)

            elif s_input ==3 :
                 s_1 ='math'
                 #함수
                 #s_update(s_1)
                
            else:
                print("과목 수정을 취소합니다.")
                break
#함수 선언
def s_update(s_1):
    
    # print("[{}수정]".format(s_title[s_input]))
            
    # print("현재 {}점수:".format(s_title[s_input],students[chk]["s_1"]))
    # print("-" *20)
    # score=int(input("수정할 국어점수를 입력하세요."))
    # students[chk]["s_1"]=score
    #   #합계 수정
    # students[chk]["total"] = students[chk]["kor"]+student[chk]["eng"]+students[chk]["math"]
    # students[chk]["avg"] = float("{:.2f}".format(student[chk]["total"]/3))
    # print("수학점수: {}점으로 수정이 완료되었습니다.", students[chk]["s_1"])
    # print(students[chk])
            
# while True:
#     search=input("찾고자 하는 학생의 이름을 입력.(0.취소)")
     
    
        
        
        
        
    
        
        
    #이름찾기
    cnt=0   #찾은 학생의 위치
    #전체학생 검색
    for stu in students:
        if stu[1] ==search:
            break
        cnt+= 1
        
    if cnt == len(students): #전체학생수
        print("{}학생이 없습니다.".format(search))
    else:    
        print("{}학생을 찾았습니다.".format(search))
            
            
    print("찾은위치:",cnt)
    del students[cnt]
    print(students)    
    print('-'*50)
            
        
        
            
   
print('[ 학생성적전체출력 ]')
        print('-'*55)
        
        print('-'*55)
        for stu in students:
            for s in stu:
                print(s, end='\t')
            print()
        kors, engs, maths,totals = 0,0,0,0
        for j, stu in enumerate(students):
            kors+=stu[2]
            engs+= stu[3]
            maths+=stu[4]
            totals+=stu[5]
        avgs = totals/len(students)
        print()
        print('--\t합계\t{}\t{}\t{}\t{}\t{:.2f}'.format(kors,engs,maths,totals,avgs))
        print()    
        '''  