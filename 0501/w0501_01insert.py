import oracledb
import time

conn=oracledb.connect(user="ora_user",password="1111",dsn="localhost:1521/xe")
cursor=conn.cursor()  #커서생성=명령어 입력받는 함수



sql="select *from member"
cursor.execute(sql)
cursor.execute('commit')


# insert,update,delete 저장하기
#sql="insert into member values(member_seq.nextval,'ggg','1111','홍길순','여자',sysdate)"

sql='select *from member'
cursor.execute(sql)
data=cursor.fetchall()

for d in data:
    print(d)


#select 읽어오기
#fetchone(),fetchall()
#data=cursor.fetchall()











cursor.close()
