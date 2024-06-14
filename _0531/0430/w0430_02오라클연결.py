import oracledb

#sql
conn=oracledb.connect(user="ora_user",password="1111",dsn="localhost:1521/xe")
cursor = conn.cursor() #db와 연결되어 지시자 생성


#stu_score avg 90점 이상 A, 80점 이상 B,C,D  60점 미만 F
# 학번,이름, 합계,평균,학점 출력


#board 테이블모든 컬럼, member 테이블의name 컬럼을 가져와 출력
#board 정보에서 id,name 포함해서 데이터를 가져와 출력하시오.
#테이블, id, member 테이블 name
# select bno,a.id,name,btitle,bcontent,bdate,bgroup,bstep, bindent,bhit,bfile 
# from board a, member b
# where a.id=b.id;



# sql ='''select name, avg,
# case 
# when avg>=90 then 'A'
# when avg>=80 then 'B'
# when avg>=70 then 'C'
# when avg>=60 then 'D'
# else 'F'
# end as grade
# from stu_score'''


sql="select * from stu_score"

cursor.execute(sql)   #cursor에 select 한 결과값을 저장(결과값: list)
data=cursor.fetchall()    #fetchall():모든 데이터 가져옴. fetchaone() : 1개의 데이터 가져옴.

print("[모든 데이터 출력]")
for d in data[:5]:
    # print(d)
    print("총점:  ",d[5])
    print("평균:  ",d[6])
    if d[6]>=90:
        print("grade : ","A")
    elif d[6]>=80:
        print("grade:  ","B")
    elif d[6]>=70:
        print("grade:  ","C") 
    elif d[6]>=60:
        print("grade:  ","D")   
    else:
        print("grade:  ","F") 
    print("-") 
 
#salary 평균을 출력하시오.
#patchone 정보하나, patchall은 전부 
sql="select round(avg(salary),2) salary from employees"
cursor.execute(sql)  
data=cursor.fetchone()
print(data[0])

 
 
 
 
 
 
    
# print("_"*45)
# print("타입 : ",type(data))
conn.close()
#데이터 베이스 연결해제



#평균을 가지고 파이썬에서 프로그램하여 학점을 출력하시오.
#학번,이름,합계,평균,학점을 프로그램하여 학점 출력



# print("[모든 데이터 출력]")
# # print(data)
# for d in data:
#     # print(d)
#     print("학번:  ",d[0])
#     print("이름:  ",d[1])
#     print("국어:  ",d[2])
#     print("영어:  ",d[3])
#     print("수학:  ",d[4])
# print("-") 
# print("타입 :  ",type(data))