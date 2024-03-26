stu_name1 = input('첫번째 학생이름을 입력하세요 >>')
kor1=int(input('첫번째 학생의 국어점수를 입력하세요'))
eng1=int(input("첫번째 학생의 영어점수를 입력하세요"))
math1=int(input('첫번째 학생의 수학점수를 입력하세요'))
total1=kor1+eng1+math1
avg=total1/3
print('번호\t이름\t국어\t영어\t수학\t합계\t평균\t등수')
print('{}\t {}\t{} \t{}\t{}\t{:.2f} \t{}'.format(stu_name1,kor1,eng1,math1,total1,avg,1))

stu_name2 = input('두번째 학생이름을 입력하세요 >>')
kor2=int(input('국어점수'))
eng2=int(input('영어점수'))
math2=int(input('수학점수'))
total2=kor2+eng2+math2
avg=total2/3
print('번호\t이름\t국어\t영어\t수학\t합계\t평균\t등수')
print('{}\t{}\t{}\t{}\t{}\t{}\t{:.2f}'.format(stu_name2, kor2,eng2, math2, total2,avg,2))