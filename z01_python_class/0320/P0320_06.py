
#input 입력받은 데이터를
#p0320.txt 파일을 생성해서 저장하세오
#p_0320은 현재날짜를 사용하시오.
import datetime


now=datetime.datetime.now()
print("현재날짜: ", now)
f=open("p0320.txt","w",encoding="utf8")

