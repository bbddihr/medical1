select * from stu_score;

select * from students;
--drop table students;

update students set id ='aaa', name='ȫ�浿', gender='M' where id='Joelynn' and pw='6856';
update students set id='bbb', name='������', gender='F' where id='Bambie';
update students set id='ccc', name='�̼���', gender='M' where id='Orin';
update students set id='ddd', name='������', gender='M' where id='Puff';
update students set id='eee', name='�豸', gender='M' where id='Godfree';
update students set id='fff', name='������', gender='M' where id='Penny' and pw='8503';
update students set id='ggg', name='ȫ����', gender='F' where id='Matti' and pw='3737';

select * from students where name='������';
commit;
rollback;
--���Ӱ� ������ ��ȣ ����: rownum
select rownum,a.* from students a
order by grade;
--1.select����
select a.* from students a;

2.rownum �Լ� ����
select rownum,a.* from students a;

3. order by �������� 
select rownum,a.* from students a
order by grade 
;

--1.select  2.order by ����  3.rownum
select * from students
order by grade
;
select rownum,a.* from
(
select * from students
order by grade

)a
;

--���avg 85�� �̻��̸鼭 no>=500 ����Ͻÿ�
select *from stu_score
where avg>=85 and no>=500
;

select * from
(select * from stu_score where avg>=85)
where no>=500
;

--���̺�� shop_product
select name, amount,pdate from shop_product
where pdate>='2024-03-01';

--�̸��� ���ų��� �հ踦 ���Ͻÿ�.
--sum(amount)�� �������� ������� �÷�
select * from shop_product;
select * from customer_rank;
drop table customer_rank;
create table customer_rank(
rank varchar2(10) primary key,
lower_amount number,
high_amount number
);
insert into customer_rank values('BRONZE',0,999999);
insert into customer_rank values('SILVER',1000000,1999999);
insert into customer_rank values('GOLD',2000000,2999999);
insert into customer_rank values('PLATINUM',3000000,99999999);
commit;



--equi join: ���� �÷��� 2���� ���̺� �����Ͽ� 2�� �÷��� �̿��� �˻��ϴ� ���
--non-equi join: ���� �÷��� �����鼭 2�� ���̺��� ����� �˻��ϴ� ��� 

select name,s_amount,rank from (
select name,sum(amount) as s_amount from shop_product
where pdate>='2024/03/01'
group by name),customer_rank
where
s_amount between lower_amount and high_amount
;

select * from customer_rank;

--shop_product,customer_rank ->non-equi join 
select name, avg, grade from stu_score,stu_grade 
where avg between low_score and high_score 
;

select *from customer_rank;

select rownum,a.* from students a
;



select rnum,b.* from
(
(select rownum rnum,a.* from students order by id) a
)
where rnum>=11 and rnum <=20
;


select rownum,a.* from
(select * from students order by id) a
where rownum>=11 and rownum<=20
;


select *from
(select rownum rnum,b.* from
(select * from studnets order by id) b)
where rnum>=11 and rnum<=20;


--over() �����ؼ�
select * from(
select row_number() over(order by id) rnum,a.*
from students a )
where rnum>=11 and rnum<=20
;


select employee_id,emp_name, department_id, manager_id from employees
order by department_id;


select employee_id, emp_name, a.department_id, department_name,a.manager_id 
from employees a, departments b
where a.department_id=b.department_id
order by a.department_id;

--cross join 107*107
--self join,equi-join�Բ� ���
--equi join: 2���� ���̺� ���� �÷��� ������ �˻�
select a.employee_id,a.emp_name, c.department_id, department_name, a.manager_id, b.emp_name
from employees a, employees b,departments c
where a.manager_id= b.employee_id and a.department_id=c.department_id
order by a.employee_id
;

--self join 
select a.employee_id, a.emp_name, a.manager_id, b.emp_name
from employees a, employees b
where a.manager_id=b.employee_id
;

--john chen�� ������ �μ��� �ٹ��ϴ� ����� ����Ͻÿ�.
--�÷�: �����, �μ���ȣ, ���� �ٹ��ϴ� ��� �μ���ȣ, ���� �ٹ��ϴ� �����
--1. john �μ��� ���
--2. �μ���ȣ�� ������ ���� ����� ���
--3. �μ���ȣ �μ��� ����� �غ�����.

select emp_name, department_id from employees 
where emp_name='Guy Himuro'
;

select emp_name, department_id from employees
where department_id = 30;

select e1.emp_name, e1.department_id, e2.emp_name
from employees e1, employees e2
where e1.department_id = e2.department_id and e1.emp_name='Guy Himuro'
;
select * from member;

insert into member values(
member_seq.nextval,'ggg','1111','ȫ���','����',sysdate
)
;
commit;
desc member;

rollback;

select * from member;
update member set name='ȫ�浿' where id='aaa'
;


select * from employees;
--a�� ��� ��� 
--select a.* from employees a,employees b
--where a.department_id = b.department_id and a.emp_name = 'Pat Fay';

select a.emp_name,a.department_id,c.department_name, b.emp_name from employees a,employees b,departments c
where a.department_id = b.department_id and a.emp_name = 'sarah Bell'
and a.department_id = c.department_id
;

select * from member order by id;
hhh,1111,ȫ����,����,sysdate

select *from member where id='aaa';

--���̺� ����
create table mem(
id varchar2(30) primary key,pw varchar2(30), name varchar(30),mdate date);

drop table mem;
select * from mem;


create table yeogi (
yno number(4) primary key,
title varchar2(100) not null,
region varchar2(30),
score number,
member number,
img varchar2(100),
price number
);

select * from yeogi;









