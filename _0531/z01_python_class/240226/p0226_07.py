student = [[1,'홍길동',100,100,100,300,100.0,1],
          [2,'유관순',90,90,90,270,90.0,1]]
print('-' *35)
print('\t[학생성적프로그램]')
print('1.학생성적입력')  #1명만 입력> (이름, 국, 영,수 ) print(student) 
print('4. 학생성적전체출력')  #2명이 출력
print('-' *35)
ch=int(input('원하는 번호를 입력하세요'))

if ch == 1:
    print('[학생 성적 입력]')
    name=input("이름을 입력하세요>>")
    kor=int(input('국어점수를 입력하세요>>'))
    eng =int(input('영어점수를 입력하세요>>'))
    math=int(input('수학점수를 입력하세요>>'))
    total = kor+eng+math
    avg = total/3
    stu1 =[ 3, name, kor, eng,math]
    stu1.append(total)
    stu1.append(avg)
    stu1.append(3)
    
    student.append(stu1)
    print(student)
    
    
elif ch ==4:#학생 성적 전체 출력
    print('[학생 성적 출력]')
    print('번호\t이름\t국어\t영어\t수학\t총점\t평균\t등수')
    print('{}\t{}\t{}\t{}\t{}\t{}\t{}\t{}'.format(student[0][0],student[0][1],student[0][2],student[0][3], student[0][4], student[0][5],student[0][6],student[0][7]))    
else:
    pass









'''''
stu1=student[0]
stu2=student[1]

if ch==1:
    print(stu1)
    stu1.append(stu2)
    print(stu1)
    print('이름\t국어\t영어\t수학')
    print('{}\t{}\t{}\t{}'.format(student[0][1],student[0][2],student[0][3],student[0][4]))
# if ch==4:
#     print(stu1,stu2)
    
#4번 경우

if ch==4:
    print('[학생 성적 출력]')
    print('번호\t이름\t국어\t영어\t수학\t총점\t평균\t등수')
    print('{}\t{}\t{}\t{}\t{}\t{}\t{}\t{}'.format(stu1[0],stu1[1],stu1[2],stu1[3], stu1[4], stu1[5],stu1[6],stu1[7]))
    print('{}\t{}\t{}\t{}\t{}\t{}\t{}\t{}'.format(stu2[0],stu2[1],stu2[2],stu2[3], stu2[4], stu2[5],stu2[6],stu2[7]))
    

# name=input("학생1 이름을 입력하세요>>")
# kor=int(input("국어점수는>>"))
# eng=int(input("영어점수는>>"))
# math=int(input("수학점수는>>"))      
# total=kor+eng+math
# avg=total/3
    
#     stu3=[name, kor, eng, math]

'''