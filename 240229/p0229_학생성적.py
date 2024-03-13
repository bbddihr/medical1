students=[]
cnt=0
while True:
    print('-'*35)
    print('\t[학생성적프로그램]')
    print('-'*35)
    print('1.학생성적입력') ####이름, 국, 영, 수 점수를 입력 받으면 [번호,이름,국,영,수,총합,평균,0]
    print('2.학생성적수정')  #국, 영, 수 점수를 수정해볼수 있음(유의:국어를 바꾸면, 합,평균)
    print('3.학생성적삭제')
    print('4.학생성적전체출력') ####
    print('5.학생검색출력')
    print('6.등수처리')
    print('0.프로그램종료')   #####할수있어야
    print('-'*35)
    ch = int(input('원하는 번호를 선택하세요>')) 
    
    if ch == 1 :
        print('학생성적입력')
        cnt += 1
        stu_name =input('학생이름을 입력하세요 >>')
        kor=int(input('학생의 국어점수를 입력하세요'))
        eng=int(input("학생의 영어점수를 입력하세요"))
        math=int(input('학생의 수학점수를 입력하세요'))
        total = kor+eng+math
        avg = total/3
        rank =0
        student=[cnt,stu_name, kor,eng,math,total,avg,rank]
        students.append(student)
        print(student)
    elif ch == 2 : 
        print('학생성적수정')
    elif ch == 4:
        print('4.학생성적전체출력')
        print('번호\t이름\t국어\t영어\t수학\t총점\t평균\t등수')
        print('-'*60)
        for s in range(len(students)):
            print('{}\t{}\t{}\t{}\t{}\t{}\t{:.2f}\t{}'.format(
            students[s][0],students[s][1],students[s][2],
            students[s][3],students[s][4],students[s][5],
            students[s][6],students[s][7]))            
    
    













'''
# print('번호\t이름\t국어\t영어\t수학\t합계\t평균\t등수')
# print('{} \t {}\t {} \t{}  \t{} \t{} \t{} \t{}'.format(1, '홍길동', 100,100,100,300,100.0,1))

# 홍길동 100 100 100
# 유관순 90 100 90
# 두 정보를 입력을 받아서 출력해보세요





# stu_no1=input("번호:")
# kor1=input("국어")
# eng1=input("영어")
# math1=input("수학")
# total1=input("합계")
# avg1=input("평균")
# no1=input("등수")

# print('번호\t이름\t국어\t영어\t수학\t합계\t평균\t등수')




stu_name1 = input('첫번째 학생이름을 입력하세요 >>')
kor1=int(input('첫번째 학생의 국어점수를 입력하세요'))
eng1=int(input("첫번째 학생의 영어점수를 입력하세요"))
math1=int(input('첫번째 학생의 수학점수를 입력하세요'))
total1=kor1+eng1+math1
avg=total1/3
print('번호\t이름\t국어\t영어\t수학\t합계\t평균\t등수')
print('{}\t {}\t{} \t{}\t{}\t{} \t{}'.format(stu_name1,kor1,eng1,math1,total1,avg,1))
'''