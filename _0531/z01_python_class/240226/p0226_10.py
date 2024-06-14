
student=[]
for i in range(10):         # for를 사용해서 5번 반복
    print('-'*35)
    print('\t[학생성적프로그램]')
    print('1.학생성적입력')
    print('4.학생성적전체출력')
    print('0.프로그램 종료')
    print('-'*35)
    ch=int(input('원하는 번호를 입력하세요>>'))
    print(ch)
# if 문을 사용해서 1 누르면 [학생성적입력]
# 4 누르면[학생성적전체출력]
# 0 누르면 [프로그램 종료]  
# 이름, 국, 영, 수 점수를 입력받아   

student2=[name, kor, eng, math]


if ch == 1:
    print('[학생 성적 입력]')
    name=input("이름을 입력하세요>>")
    kor=int(input('국어점수를 입력하세요>>'))
    eng =int(input('영어점수를 입력하세요>>'))
    math=int(input('수학점수를 입력하세요>>'))
    student1=[name, kor, eng, math]
    
   
elif ch == 4:
    print('학생성적출력')
  # 출력 for를 사용해서 학생 수 만큼 출력
elif ch == '0' :
    print('프로그램 종료')
else:
    print('잘못입력하셨습니다.')

print('*'*35)
print('*'*35)

