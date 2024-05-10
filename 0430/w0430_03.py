import oracledb

# DB connect 연결
conn = oracledb.connect(user="ora_user",password="1111",dsn="localhost:1521/xe")
cursor= conn.cursor()

#sql실행
#employees테이블에서 사번,이름,월급,실제월급(월급+(월급*커미션)),월급*1410 kor_salary 환산해서
#kor_salary만 원화표시, 천단위표시해서 출력.
# sql='''select employee_id,emp_name,salary,salary+(salary*nvl(commission_PCT,0)),to_char(salary*1410,'L999,999,999')from employees'''


#부서별 평균월급,최대월급,최소월급

sql='''select department_id,round(avg(salary),2),max(salary),min(salary) from employees 
where department_id is not null
group by department_id
order by department_id '''
cursor.execute(sql)
data = cursor.fetchall()

print("[데이터출력]")
print("-"*40)
print("사원번호\t사원명\t월급\t실제월급\t원화환산")
for d in data:
    print(d[0],end="\t")
    print(d[1],end="\t")
    print(d[2],end="\t")
    print(d[3],end="\t")
    print("￦"+d[4].strip())
    

