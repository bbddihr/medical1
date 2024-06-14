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
where name like '%ȫ%';

 
select avg from stu_score
where avg>=60
order by no
;

--�����ȣ, �����,�μ���ȣ, �μ����� ����Ͻÿ�.
select employee_id,emp_name,b.department_id,department_name
from employees a,departments b
where a.department_id = b.department_id and emp_name like '_a%'
and salary >=(select avg(salary) from employees)
;

--�׸���, �̸� �ι�° �ڸ��� a�� ���� ����� �˻��Ͻÿ�.
select emp_name from employees
where emp_name like '_a%'
;

-������ ����̻��� ����� �˻��Ͻÿ�.
select salary from employees
where salary >=(select avg(salary) from employees)
;


select employee_id,emp_name, a.department_id, department_name, a.job_id, job_title
from employees a, departments b ,jobs c
where a.department_id = b.department_id and a.job_id=c.job_id
;
--�����ȣ e, �����e,�μ���ȣe, �μ���d,���޹�ȣe, ���޸�jobs ����ϼ���.


--�����ȣ,�����,����,�ּҿ��޺�,�λ��,����,����Ÿ��Ʋ ����Ͻÿ�
--�ּҿ��� �� %�ް� �ִ� �� ���(�ּҿ��� / �������*100)
select employee_id,emp_name,salary, min_salary, to_char(round(salary-min_salary/salary)*100,2))||'%',a.job_id, job_title
from employees a, jobs b
where a.job_id = b.job_id
;

select job_id,job_title from jobs;


--job_title Manager ���ڰ� ���ִ�
--�����ȣ e, �����e,���޹�ȣe,���޸�j,����e,�ִ����j �� ����Ͻÿ�.

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

--case when then grade�÷� 90�� �̻� A. 80���̻� B...������ ���


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

--stu_score,stu_grade���� �÷��� ����.
--2���� ���̺��� join: non-equi join
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

--����������� �������� �����
select * from kor_loan_status;

select region,sum(loan_jan_amt)
from kor_loan_status
group by region
order by region
;

--������ �����հ踦 ����Ͻÿ�.
select region,sum(loan_jan_amt)
from kor_loan_status
order by region;

--������, ������, �����հ�ݾ�
select substr(period,1,4), region, sum(loan_jan_amt)
from kor_loan_status
group by to_char(period,1,4), region
order by region
;


--�μ��� ���� �հ踦 ����Ͻÿ�.
select department_id,sum(salary) a
from employees
group  by department_id
order by a
;

--�ð��뺰,���ɴ뺰 �Ǹŷ� ������ ����Ͻÿ�.
select * from lotte_product;

select time_cd, age_cd*10, sum(purh_amt)a
from lotte_product
group by time_cd,age_cd
order by a desc
;

select *from shop_product;

--�̸���, �ݾ��հ踦 ��� �Ͻÿ�.
select name, sum(amount), rank
from shop_product,customer_rank
where pdate>='2024/03/01'
group by name
;
-- customer_rank���̺� ����
-- rank
-- 100�����̸� BRONZE
-- 200�����̸� SILVER
-- 300�����̸� GOLD
-- 300�����̻� PLATINUM
-- name,sum(amount),rank ����Ͻÿ�.
-- non-equi join���� ó��
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

--������ ���Ӱ� �ο��ؼ� ������ִ� �Լ�
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


--21������ 30�� ������ ��������
select * from stu_score 
where no>=21 and no<=30
order by no;

select rownum rnum,a.* from lotte_product a

--rownum 21-30 �����Ͱ������� ������ rnum �����س��� 
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

--kor������ ���������� 21~30����� ����Ͻÿ�.
--������ 21,22,23,,,,30���� �ο��ϼ���.
select rnum,no,name,kor,eng,math,total,avg,rank,c_date
from(
select rownum,b.* from 
(select a.* from stu_score a
order by kor desc) b
)
where rnum>=21 and rnum<=30
;



--non-equi join �����÷������� ���
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


