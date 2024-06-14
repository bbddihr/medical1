
#튜플(), 딕셔너리 {} 리스트는 []
#두명 이상의 학생의 
#이름, 국, 영, 수 점수를 입력받아
#리스트를 생성 후,
#student 리스트에 넣어주세요

#student 리스트 전체 출력
# student =[]   
# name=input("학생1 이름을 입력하세요>>")
# kor=int(input("국어점수는>>"))
# eng=int(input("영어점수는>>"))
# math=int(input("수학점수는>>"))

# #리스트에 값 넣기
# #방법 1
# stu1=[name,kor, eng, math]
# print(stu1)
# s2=input("학생2 이름을 입력하세요>>")
# k2=int(input("국어점수는>>"))
# e2=int(input("영어점수는>>"))
# m2=int(input("수학점수는>>"))
student1=[name1,kor1,eng1, math1]
name1= input("학생1 이름을 입력하세요?")
kor1=int(input("국어점수는?"))
eng1=int(input("영어점수는?"))
math1=int(input("수학점수는?"))

# stu1=['',0,0,0,0,0,0] #기본값 설정 길이 설정
# stu1[0] = #이름을 넣을 예정 
''''
stu1 = [name, kor, eng, math]
stu1.append(kor+eng+math) #총점
stu1.append((kor+eng+math)/3) #평균
print(stu1)


stu2 = []
name=input("학생2 이름을 입력하세요>>")
kor=int(input("국어점수는>>"))
eng=int(input("영어점수는>>"))
math=int(input("수학점수는>>"))
stu2=[name, kor, eng, math]
stu2.append(kor+eng+math) #총점
stu2.append((kor+eng+math)/3) #평균
print(stu2)
''''''''