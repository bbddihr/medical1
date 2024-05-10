#학생 이름, 국어, 영어, 수학 점수를 입력받아서
#아래와 같이 출력을 하고 
#만약에 평균이 80점 이상이면 합격입니다를 출력하세요


n1=input('이름')
kor1=int(input('국어'))
eng1=int(input('영어'))
math1=int(input('수학'))
total=kor1+eng1+math1
avg=total/3

print('번호\t이름\t국어\t영어\t수학\t합계\t평균\t등수')
print('{}\t{}\t{}\t{} \t{} \t{} \t{} \t{}'.format( 1, n1 ,kor1,eng1, math1,total,avg,1))

if avg>=80:
    print("{}님 합격입니다".format(n1))
else:
    print('{}님 불합격입니다.')
    
    

    

#print('번호\t이름\t국어\t영어\t수학\t합계\t평균\t등수')
#print('{}\t{}\t{}\t{} \t{} \t{} \t{} \t{}.format( 1, '홍길동',100,100,100,300,100.0,1)')
#print('홍길동님 합격입니다.')

