import oracledb
import time


##데이터베이스 연결함수
def connection():
    conn=oracledb.connect(user="ora_user",password="1111",dsn="localhost:1521/xe")
    cursor=conn.cursor()  #커서생성=명령어 입력받는 함수
    return cursor


cursor = connection()
sql="select emp_name from employees"
cursor.execute(sql)
data=cursor.fetchall()

def close(cursor,conn):
    cursor.close()
    conn.close()
#employees 이름으로 검색하는 부분 로직을 구현하시오.
#무한반복, -1 프로그램 종료

while True:
    print("1.이름으로 검색")
    print("1.같은부서에서 근무하는 사원 조회")
    choice=input("원하는 번호를 입력하세요>>")
    if choice=="-1":
        break
    elif choice == "1":
        search=input("찾는 이름을 입력하세요.")
        if search==-1:
            print("프로그램종료")
            break
        sql=f"select *from employees where emp_name like'%{search}%'"
        conn,cursor=connection()
        cursor.execute(sql)
        data=cursor.fetchall()
        for d in data:
            print(d[0],end="\t") 
            print(d[1],end="\t") 
            print(d[2],end="\t")    
        print("-"*30)

    elif choice=="2":
        search=input("이름으로 함께 근무하는 사원을 검색합니다. 이름을 입력하세요>")
        ##프로그램 구현
        sql =f'''select a.emp_name,a.department_id,c.department_name, b.emp_name from employees a,employees b,departments c
where a.department_id = b.department_id and a.emp_name = '{search}'
and a.department_id = c.department_id'''

        print("-"*30)
    else:
        print("프로그램을 종료합니다.")
        
    print()
    close(cursor,conn)
        