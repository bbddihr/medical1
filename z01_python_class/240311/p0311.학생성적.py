students=[]
cnt= len(students)+1
while True:
    print(('-'*40))
    print('[학생성적프로그램]')
    print(('-'*40))
    print('1.학생성적입력')
    print('2.학생성적전체출력')
    print('3.학생검색')
    print('4.학생수정')
    print('5.등수처리')
    print('6.학생삭제')
    print('0.프로그램 종료')
    print(('-'*40))
    choice=input('원하는 번호를 입력해주세요>>')
    if not choice.isdigit():
        print("숫자만 입력가능합니다.")
        continue
    choice=int(choice)
    if choice==1:
        print('1.학생성적입력을 선택하였습니다.')
        while True:
            name=input('{}번째 학생의 이름을 입력하세요.(0.취소)'.format(cnt))
            if name=="0":
                print("학생입력을 취소합니다.")
                break
            student={}
            student["stuNo"]='S'+'{:03d}'.format(cnt)
            student["name"]=name
            kor=int(input('국어점수를 입력하세요>>'))
            student["kor"]=kor
            eng=int(input('영어점수를 입력하세요>>'))
            student["eng"]=eng
            math=int(input('수학점수를 입력하세요>>'))
            student["math"]=math
            total=kor+eng+math
            student["total"]=total
            avg=total/3
            student["avg"]=float("{:.2f}".format(avg))
            students.append(student)
            cnt+=1
            print("입력데이터:",student)
            print(students)
    elif choice==2:
        count=input('2.학생성적전체출력을 선택하시겠습니까?(1.확인 0.취소)')
        if count == "0":
            break
        print("\t[학생성적전체출력]")
        print('-'*60)
        print('학번\t이름\t국어\t영어\t수학\t총점\t평균\t등수')
        print('-'*60)
        for s_dic in students:
            for s_key in s_dic:
                print(s_dic[s_key],end='\t')
            print()
    elif choice==3:
        pass
                     
    elif choice==4:
        s_title=['','국어','영어','수학']
        while True:
            search=input("찾고자하는 학생의 이름을 입력하세요(0.취소)>>")
            chk = 0
            if search =='0':
                break
            for s_dic in students:
                if s_dic["name"]==search:
                    break
                chk +=1
            print("찾고자하는 학생의 위치:",chk)
            
            if chk ==len(students):
                print(f"{search}학생은 없습니다. 다시 입력하세요.")
            else:
                print(f"{search}학생을 찾았습니다.")
            while True:
                print("수정할 과목 선택") 
                print("1.국어\t2.영어\t3.수학")
                s_input=int(input("수정하려는 과목을 택하세요.(0.취소)")) 
                if s_input == 1:
                    s_1="kor"
                    print("[{} 수정]".format(s_title[s_input]))
                    print("현재{}점수:{}".format(s_title[s_input],students[chk][s_1]))
                    print('-'*20)
                    score=int(input("수정할 {}점수를 입력하세요".format(s_title[s_input])))
                    students[chk][s_1]=score
                    students[chk]["avg"]=float("{:.2f}".format(students[chk["total"]/3]))
                    
        
            
            
        
        
    