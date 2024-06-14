
student=[]
for i in range(3):         # for를 사용해서 5번 반복
    print('-'*35)
    print('\t[학생성적프로그램]')
    print('1.학생성적입력') # if 문을 사용해서 1 누르면 [학생성적입력]
    print('4.학생성적전체출력') # 4 누르면[학생성적전체출력]
    print('0.프로그램 종료') # 0 누르면 [프로그램 종료]  
    print('-'*35)
    ch=input('원하는 번호를 입력하세요>>')
    if ch == '1':
        print('학생성적입력')
        name=input("이름을 입력하세요>>")
        kor=int(input('국어점수를 입력하세요>>'))
        eng =int(input('영어점수를 입력하세요>>'))
        math=int(input('수학점수를 입력하세요>>'))
        s=[1, name, kor, eng, math,(kor+eng+math),(kor+eng+math)/3]
        student.append(s)
        print(student)
        # 출력 for를 사용해서 학생 수 만큼 출력
    elif ch == '4':
        print('학생성적출력')
        for s in range(len(student)):
            print('번호\t이름\t국어\t영어\t수학\t합계\t평균\t등수')
            print('{}\t{}\t{}\t'. format(student[s][0], member[s][1], member[s][2]))
            print('{}\t{}\t{}\t'. format(student[s][0], member[1][1], member[1][2]))
            print('{}\t{}\t{}\t'. format(student[s][0], member[2][1], member[2][2]))
            print('{}\t{}\t{}\t{}\t'. format(student[s][0], member[s][1], member[s][2]))
  
  
    elif ch == '0' :
        print('프로그램 종료')
    else:
        print('잘못입력하셨습니다.')

print('*'*35)
print('*'*35)

    
   
