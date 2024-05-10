# 학생성적 입력

# 변수를 사용합니다
stu_name = '홍길동'
kor = 100
eng = 100
math = 100

#입력을 받아서 총점과 평균을 계산하고 

#출력해보세요
print(''.format())

#홍길동 100 100 100 300 100.0
avg=(kor+eng+math)/3   # avg=total/3
total=int(kor+eng+math)
n=input("학생이름>>")
k=int(input("국어점수>>"))
e=int(input("영어점수"))
m=int(input("수학점수"))

print('번호\t이름\t국어\t영어\t수학\t합계\t평균\t등수')
print('{}\t{}\t{}\t{}\t{}\t{}\t{}\t{}\t'.format(1,stu_name,kor,eng,math,total,avg,1))

stu = [1, '홍길동', 100,100,100,300,100.0,1]
stu1 = [1,stu_name,kor,eng,math,total,avg,1]

print(stu)
print(stu1)


choice=int(input('원하는 번호>>'))    
if choice ==1:                        
    print('학생성적입력')
    stu_name = input("이름을 입력하세요>>")
    kor = int(input("국어점수를 입력하세요>>"))
    eng = int(input())
    math = int(input())
    stu3= [3, stu_name, kor, eng, math, (kor+eng+math),(kor+eng+math)/3,1]
elif choice == 4 :
    print( )