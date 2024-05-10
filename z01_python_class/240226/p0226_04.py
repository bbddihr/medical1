'''''
stu = ['홍길동','유관순','이순신','김구','강감찬']

#1. 이순신 학생 출력
# 2. 김구 이름을 안창호로 변경
#3. 유관순부터 강감찬 출력
#4. 왕건을 추가
# 5. 홍길동 삭제

print(stu[2])
stu[3]='안창호'
print(stu)
# print(stu[1:])
print(stu[1:4+1])   #4+1
stu.append('왕건')
print(stu)
del(stu[0])
print(stu)
# stu.remove('홍길동')
# print(stu)
'''''
'''''
f= ['사과','복숭아','딸기', '배','포도', '수박']
#     0     1        2      3    4       5
#딸기출력
#포도를 망고로 바꾸기
#배부터 끝까지 출력
#복숭아 딸기 출력
#사과 추가
#감 추가
#사과 삭제 
#수박이 있으면 수박이 있습니다 출력

print(f[2])
f[4]='망고'
print(f)
print(f[3:5+1])
print(f[1:3])       #딸기(2)+1  =3
f.append('사과')
print(f)
f.append('감')
print(f)
f.remove('사과')
print(f)
if '수박' in f:
    print("수박이 있습니다")

num=[10,20,30,40,50]
# 60 이 없으면 60 추가
if 60 not in num:
    num.append(60)  
    print(num) 

if 20 in num:
    num.append(70)
    num.remove(20)
    print(num)
    
aa = [[1,2],[3,4]]
print(aa[0][1]) #2
print(aa[1][1])  #4
a1 = [1,2]
a2= [3,4]
a3[a1,a2]
'''''
stu1 = ['홍길동', 90]
stu2 = ['유관순', 100]
student = [stu1, stu2]

#[['홍길동', 90], ['유관순',  100]]
#   [0][0] [0][1]  [1][0]  [1][1]

#student 리스트를 사용해서 유관순 출력
#student 리스트를 사용해서 홍길동 점수를 80으로 수정
#이순신 95점을 student에 추가
# 만약 student [][] (유관순 100점이용) 100점이면 100점입니다 출력 


print(student[1][0])

student[0][1]=80
print(stu1) 
student.append('이순신')
student.append(90)
#stu3['이순신', 95]
# student.append(stu3)
# print(student)
print(student)

if student[1][1] == 100:
    print("100점입니다")


