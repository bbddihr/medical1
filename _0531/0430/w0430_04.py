import oracledb
conn=oracledb.connect(user="ora_user",password="1111",dsn="localhost:1521/xe")
cursor=conn.cursor()

#프로그램을 반복하는 형태로 구성하고, -1을 입력하면 종료되도록 하시오.
#홍이라고 검색하면 홍에 관련된 학생이 모두 출력되도록 하시오.



while True:
    search=input("찾고자하는 이름을 입력하시오")
    if search==-1:
        print("프로그램을 종료합니다.")
        break
    sql=f"select * from stu_score where name like '%{search}%'"
    cursor.execute(sql)
    data=cursor.fetchall()
    for d in data:
        print(d)
    print("검색된데이터 개수: ",len(data))
    
    
    
conn.close() 