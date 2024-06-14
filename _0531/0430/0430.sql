select * from stu_score;

select * from stu_score where name like "_a%" order by no asc;

select a.*,name from board a,member b
where a.id=b.id
;
select bno,a.id,name,btitle,bcontent,bdate,bgroup,bstep, bindent,bhit,bfile 
from board a, member b
where a.id=b.id;



select employee_id,emp_name,salary,salary+(salary*nvl(commission_PCT,0)),to_char(salary*1410,'L999,999,999')from employees
;

select department_id,round(avg(salary),2),max(salary),min(salary) from employees 
where department_id is not null
group by department_id
order by department_id; 


select * from stu_score;
where name like '%홍%';

 
select avg from stu_score
where avg>=60
order by no
;

--사원번호, 사원명,부서번호, 부서명을 출력하시오.
select employee_id,emp_name,b.department_id,department_name
from employees a,departments b
where a.department_id = b.department_id and emp_name like '_a%'
and salary >=(select avg(salary) from employees)
;

--그리고, 이름 두번째 자리에 a가 들어가는 사원을 검색하시오.
select emp_name from employees
where emp_name like '_a%'
;

-월급이 평균이상인 사람만 검색하시오.
select salary from employees
where salary >=(select avg(salary) from employees)
;


select employee_id,emp_name, a.department_id, department_name, a.job_id, job_title
from employees a, departments b ,jobs c
where a.department_id = b.department_id and a.job_id=c.job_id
;
--사원번호 e, 사원명e,부서번호e, 부서명d,직급번호e, 직급명jobs 출력하세요.


--사원번호,사원명,월급,최소월급분,인상분,직급,직급타이틀 출력하시오
--최소월급 몇 %받고 있는 지 출력(최소월급 / 현재월급*100)
select employee_id,emp_name,salary, min_salary, to_char(round(salary-min_salary/salary)*100,2))||'%',a.job_id, job_title
from employees a, jobs b
where a.job_id = b.job_id
;

select job_id,job_title from jobs;


--job_title Manager 글자가 들어가있는
--사원번호 e, 사원명e,지급번호e,직급명j,월급e,최대월급j 을 출력하시오.

select job_id, job_title from jobs;

select employee_id, emp_name, a.job_id, job_title, salary, max_salary 
from employees a, jobs j
where a.job_id = j.job_id and job_title like '%manager%';


select user_id, user_name, user_phone, user_address1, user_address2
user_address3
from User a, Deliver_Address b
where a.user_id = b.user_id
;
--drop table stu_grade;
create table stu_grade(
grade varchar2(1) primary key,
low_score number(3) not null,
high_score number(3)
);


insert into stu_grade values(
'A',90,100
);
insert into stu_grade values(
'B',80,90
);
insert into stu_grade values(
'C',70,79
);
insert into stu_grade values(
'D',60,69
);
insert into stu_grade values(
'F',0,59
);
commit;

select * from stu_grade;
select avg from stu_score;

--case when then grade컬럼 90점 이상 A. 80점이상 B...학점을 출력


select avg,
case
when avg>=90 then 'A'
when avg>=80 then 'B'
when avg>=70 then 'C'
when avg>=60 then 'D'
else 'F' end as grade
from stu_score 
order by no;

--non-equi join
select no,name,avg,grade
from stu_score,stu_grade
where avg between low_score and high_score
order by no
;

--stu_score,stu_grade같은 컬럼이 없음.
--2개의 테이블을 join: non-equi join
select *from stu_score;
select *from stu_grade;

update stu_grade set low_score=92
where grade = 'A'
;
update stu_grade set low_score=82, high_score=91
where grade = 'B'
;
update stu_grade set low_score=72, high_score=81
where grade = 'C'
;

update stu_grade set low_score=62, high_score=71
where grade = 'D'
;
update stu_grade set high_score=62
where grade = 'F'
;

--월별매출액을 기준으로 고객등급
select * from kor_loan_status;

select region,sum(loan_jan_amt)
from kor_loan_status
group by region
order by region
;

--지역별 대출합계를 출력하시오.
select region,sum(loan_jan_amt)
from kor_loan_status
order by region;

--연도별, 지역별, 대출합계금액
select substr(period,1,4), region, sum(loan_jan_amt)
from kor_loan_status
group by to_char(period,1,4), region
order by region
;


--부서별 월급 합계를 출력하시오.
select department_id,sum(salary) a
from employees
group  by department_id
order by a
;

--시간대별,연령대별 판매량 총합을 출력하시오.
select * from lotte_product;

select time_cd, age_cd*10, sum(purh_amt)a
from lotte_product
group by time_cd,age_cd
order by a desc
;

select *from shop_product;

--이름별, 금액합계를 출력 하시오.
select name, sum(amount), rank
from shop_product,customer_rank
where pdate>='2024/03/01'
group by name
;
-- customer_rank테이블 생성
-- rank
-- 100만원미만 BRONZE
-- 200만원미만 SILVER
-- 300만원미만 GOLD
-- 300만원이상 PLATINUM
-- name,sum(amount),rank 출력하시오.
-- non-equi join으로 처리
select name,s_amount,rank
from (select name,sum(amount) s_amount from shop_product where pdate>='2024/03/01'
group by name), customer_rank
where s_amount between lower_amount and high_amount
;


select name, sum(amount),rank
from shop_product, customer rank 
where plate=> '2024/03/01' and sum(amount)between lower_amount and high_amount
group by name, rank
;

select *from lotte_product
order by std_ym
;

--순번을 새롭게 부여해서 출력해주는 함수
--rownum, row_number()
select rownum,std_ym,sex_cd,time_cd,purh_amt
from lotte_product
;

select rownum,a.*
from lotte_product a
;

select rownum,a.* from lotte_product a;
where rownum<= 10; 


select *from lotte_product;


--21번부터 30번 데이터 가져오기
select * from stu_score 
where no>=21 and no<=30
order by no;

select rownum rnum,a.* from lotte_product a

--rownum 21-30 데이터가져오고 싶을때 rnum 지정해놓고 
select rnum,std_ym,sex_cd,age_cd,time_cd,purh_amt
from(
select rownum rnum,a.* from lotte_product a
)b
where rnum >=21 and rnum <=30;


select rnum,b.* 
from (select * from lotte_product order by std_ym) b
;

select * from stu_score
order by no;

--kor점수가 높은순으로 21~30등까지 출력하시오.
--순번을 21,22,23,,,,30번을 부여하세요.
select rnum,no,name,kor,eng,math,total,avg,rank,c_date
from(
select rownum,b.* from 
(select a.* from stu_score a
order by kor desc) b
)
where rnum>=21 and rnum<=30
;



--non-equi join 같은컬럼없을때 사용
select no,name,avg,grade
from stu_score,stu_grade
where avg between low_score and high_score
order by no
;



select * from customer_rank; s_amount from shop_product group by name;

select * from customer_rank;

create table customer_rank(
grade varchar2(6) primary key,
low_price number (7) not null,
high_price number (7)
);

drop table customer_rank;
insert into customer_rank values(
'Bronze',100000,990000
);

insert into customer_rank values(
'silver',1000000,1990000
);

insert into customer_rank values(
'Gold',2000000,2990000
);

insert into customer_rank values(
'Platinum',3000000,2990000
);

select amount,
case
when amount=<1000000 then 'Bronze'
when amount=<2000000 then 'silver'
when amount>3000000 then 'gold'
when amount=<3000000 then 'platinum'


select * from customer_rank;


select name,sum(amount),rank
from shop_product
where 




select name,sum(amount)
from shop_product, customer)rank
gorup by name
;






select avg,
case
when avg>=90 then 'A'
when avg>=80 then 'B'
when avg>=70 then 'C'
when avg>=60 then 'D'
else 'F' end as grade
from stu_score 
order by no;


