students= []    #학생성적저장
students = [[1, "홍길동", 100,100,99,299,99.67,1],
            [2, "유관순", 99,99,98,296,98.67,1],
            [3, "이순신", 80,80,81,241,80.33,1],
            [4, "김구",100,100,90,290,96.67,1],
            [5, "김유신", 90,70,50,210,70.0,1]]

cnt = len(students)  #학번사용
while True:
    print("-"*40)
    print("[학생성적프로그램]")
    print("-"*40)
    print("1. 학생성적입력")
    print("2. 학생성적전체출력")
    print("3. 학생검색")
    print("4. 학생수정")
    print("5. 등수처리")
    print("6. 학생정렬")
    print("7. 학생삭제")
    print("0. 프로그램생검색 종료")
    print("-"*40)
    choice = input("원하는 번호를 입력하세요.>>")
    if not choice.isdigit():
        print("숫자만 입력가능합니다.")
        continue   #반복문 다시 실행
    choice = int(choice)
    
    #1. 학생성적입력 프로그램
    if choice == 1:
        while True:
              #학번
            print("학생성적을 입력합니다.")
            print("-"*10)
            student = []
            name=input("이름을 입력하세요.(0.취소)")
            if name =="-1":
                break
            cnt += 1 
            student.append(cnt)   #학번
            student.append(name)
            student.append(int(input('국어점수를 입력하시오')))
            student.append(int(input('영어점수를 입력하시오')))
            student.append(int(input('수학점수를 입력하시오')))
            #student[0]=학번, student[1] =이름
            sum = student[2]+student[3]+student[4]
            #합계 저장
            student.append(sum)
            #평균저장
            student.append("{:.2f}".format(sum/3))
            students.append(student)
            #전체출력
            print(students)
    
    elif choice == 2: 
        print("[학생성적 출력]")
        print("-"*50)
        print("학번\t이름\t국어\t영어\t수학\t합계\t평균")
        print("-"*50)
        for stu in students:
            for s in stu:
                print(s,end="\t")
            print()
        print("-"*50) 
        
    elif choice == 4:
        while True:
            search = input("찾는 학생의 이름을 입력하세요.")
            chk=0
            count=0
            for stu in students:
                if search in stu:
                    chk = 1
                    break
                count +=1   # 찾는 학생의 위치값
            if chk== 0:
                print("찾는 학생의 정보가 없습니다.")
            else:
                print("입력한 학생이름 {}을(를) 찾았습니다".format(search))
                print("[변경할 과목 선택]")
                print("1. 국어 2. 영어 3. 수학 0. 취소")
                print("-"*20)
                num=int(input(">>"))
            
                if num ==1:
                    print("국어를 선택하셨습니다.")
                    print("현재 국어점수:",students[count][2])
                    num =int(input ("변경점수를 입력하세요."))
                    students[count][2] = num
                    print("국어점수가 변경되었습니다.")
                    #합계, 평균도 수정 
                    students[count][5]=students[count][2]+students[count][3]
                    students[count][6] =float("{:.2f}".format(students[count][5]/3))
                    print(students)
                    #성적수정 프로그램 구현
                elif num ==2:
                    print("영어를 선택하셨습니다.")
                    print("현재 국어점수:",students[count][3])
                    num =int(input ("변경점수를 입력하세요."))
                    students[count][3] = num
                    print("영어점수가 변경되었습니다.")
                    #합계, 평균도 수정 
                    students[count][5]=students[count][2]+students[count][3]
                    students[count][6] =float("{:.2f}".format(students[count][5]/3))
                    print(students)
                elif num ==3:
                    print("수학을 선택하셨습니다.")  
                    print("현재 국어점수:",students[count][4])
                    num =int(input ("변경점수를 입력하세요."))
                    students[count][4] = num
                    print("수학점수가 변경되었습니다.")
                    #합계, 평균도 수정 
                    students[count][5]=students[count][2]+students[count][3]
                    students[count][6] =float("{:.2f}".format(students[count][5]/3)) 
                    print(students)
                # 등수처리 프로그램(정렬), 총점으로 비교
                
    elif choice ==5:
        while True:
            choice = input("등수처리를 실행하시겠습니까? (1.실행 0.취소)")
            if choice =="0" :
                print("등수처리를 취소하셨습니다.")
                break
            else:
                #등수처리 진행
                for i_stu in students:
                    no = 1 #초기화
                    for j_stu in students:
        #각각의 총합 비교
                        if i_stu[5] < j_stu[5]:
                            no += 1  #비교대상 총합이 더 크면 1 증가 
                            i_stu[7] = no #등수위치에 no 저장
                            print("등수처리가 완료되었습니다.")
                            print("-"*40)
                            print('[ 등수확인 ]')
                            print(students)
                        else:
                            print("성적수정 취소를 선택하셨습니다")
            
    elif choice ==7:
        
        while True:
            
            #강감찬
            search= input("삭제하려는 학생의 이름을 입력하세요.")
            
            
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
                input("{}학생을 찾았습니다.삭제 하시겠습니까?(1.삭제 0.취소)".format(search))
                
                if choice == "1":
                    print("{}학생의 데이터가 삭제되었습니다.".format(search))
                    del students[cnt]
                else:
                    print("삭제가 취소되었습니다.")    
                    
            print(students)    
            print('-'*50)           
                
        #0.프로그램종료
    
    elif choice == 0:
        print("프로그램을 종료합니다.")
        break     #반복문종료
        
    