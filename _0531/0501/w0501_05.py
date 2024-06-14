import oracledb


#DB연결
conn=oracledb.connect(user="ora_user",password="1111",dsn="localhost:1521/xe")
cursor=conn.cursor()  #커서생성=명령어 입력받는 함수

sql ="create table mem(id varchar2(30) primary key,pw varchar2(30), name varchar(30),mdate date)"
cursor.execute(sql)

##ddl 명령어는 commit이 없음. create,alter,drop
##dml 명령어: insert update delete select
##dcl grant revoke commit rollback

print("테이블 생성완료")

cursor.close()
conn.close()