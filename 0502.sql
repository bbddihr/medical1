--2�� ���̺�: department_id

select * from employees;
select * from departments;

select employee_id,emp_name, a.department_id, department_name
from employees a, departments b
where a.department_id = b.department_id
;

select *from stu_score;

select * from students;

insert into students(no) select no from stu_score;

--rownum������� ��ȣ�� no�� �ֱ�
update students set no=(select rnum from
(select rownum rnum,a.* from students a))
where a.id = b.id;




update students b
set no=( ) from 
select rnum from
(select rownum rnum,a.* from students a);
--ȫ�浿 �л�
-- �л������� ��� ����� ��ȭ��ȣ, �̸���,��,�г�

select no,name,kor,eng,math,total,avg,rank,c_date from stu_score
where name='ȫ�浿';

select id,name,phone,email,major,grade from students
where name ='ȫ�浿';

select no,id,a.name,phone,email,major,grade,kor,eng,math,total,avg,rank,c_date
from stu_score a,students b
where a.name='ȫ�浿' and a.name=b.name;


order by no;
select count(*) from stu_score;

desc stu_score;
select count(*) from students;
select table students add no number(38)

drop table students;
drop table stu_score;

--equi join
--2�� ���̺� join - 1���� ������ �÷� �־�� ��.
--������ �÷��� �ߺ��� �������. 2�� �� �ϳ� ���̺����� primaryŰ�� ����� �Ǿ����.

select a.id,a.name,phone,total,avg from students a, stu_score b
where a.id = b.id
;
select * from employees
order by employee_id
;
--self join
--������ ���̺� 2���� ������ ���� join
select a.employee_id, a.department_id, a.job_id, a.manager_id, b.emp_name
from employees a, employees b
where a.manager_id=b.employee_id
order by a.department_id;


desc stu_score;

drop table students;

select *from students;

select * from stu_score;

update stu_score a 
set rank=(select ranks from( select no,id, rank() 
over(order by total desc) as ranks, rank, total from stu_score) b
where a.no = b.no)
;

select * from students;

select * from member;

alter table member add no number;
select rownum,id from member ;

update member a 
set no= ( select rnum from (select rownum rnum,id from member)b
where a.id=b.id);

--rank,id
select rownum rnum, id from member;
--rnum
select rnum from(select rownum rnum, id from member) b
where id=b.id;


--rank
--select ranks from( select no,id, rank() over(order by total desc) 
--as ranks, rank, total from stu_score) b;

update stu_score set rank=0;
commit;

select total, rank from stu_score
order by total desc;

select total, rank() over(order by total desc) ranks from stu_score;
select row_number() over(order by total desc) rnum, total from stu_score;

--stu_score, rank ������ update�Ͻÿ�.
select no, rank() over(order by total desc) ranks from stu_score
where no= no;

--update���
update stu_score set rank = (
select ranks from (select no,rank() over(order by total desc) 
ranks from stu_score) b where a.no=b.no);

select * from stu_score;
--
select * from stu
(select rownum rnum,a.* from
(select *from stu_score order by total desc) a;
)
where rnum>=11 amd rnum<=20
;

select *from(
select rownum rnum,a.* from stu_score a
order by total desc;


select * from(
select row_number() over(order by total desc)rnum,a.* from stu_score a
)
where rnum>=11 amd rnum<=20
;

select employee_id,emp_name,manager_id from employees
order by employee_id
;

--
select * from
(
select rownum rnum,a.* from
( select * from stu_score order by total desc ) a
)
where rnum>=11 and rnum<=20
;

select * from (
select row_number() over(order by total desc) rnum,a.* from stu_score a
)
where rnum>=11 and rnum<=20
;
--self join ,manager_id,�̸� ��� 
--���� �������� �ʾƵ� ��µǵ��� outer join
--null ���� �ִ� �ݴ��� �׸� (+)��ȣ�� ������ ��.
select a.employee_id,a.emp_name,a.manager_id,b.emp_name
from employees a,employees b
where a.manager_id =b.employee_id(+)
;
select a.employee_id,a.emp_name,a.manager_id,b.emp_name
from employees a,employees b
where a.manager_id =b.employee_id(+)
;

select manager_id,emp_name from employees
where emp_name ='Diana Lorentz';

--equi join, outer join; null������ϰ������ 
select emp_name, a.department_id, department_name
from employees a,departments b
where a.department_id(+)= b.department_id
order by department_id
;
--10~270
select department_id from departments;

--ansi join
select *from employees cross join departments;
select *from employees,departments;

--equi join
select a.department_id, department_name 
from employees a,departments b 
where a.department_id = b.department_id
;
select * from employees a inner join departments b
on a.department_id = b.department_id
;

-- ansi inner join --using �̿��ؼ� �����ִ�.
select department_id,department_name 
from employees join departments 
using (department_id)
;


select a.*, department_name
from employees a, departments b
where a.department_id = b.department_id;



select * from employees natural join departments;

--ansi outer join 
select a.emp_name, a.manager_id, b.emp_name from employees a 
right outer join employees b
on a.manager_id = b.employee_id;

--�⺻ sql left outer join,right outer join, full outer join �Ұ�
select a.emp_name, a.manager_id, b.emp_name 
from employees a, employees b
where a.manager_id(+) = b.employee_id(+);


select * from employees;

select name from stu_score;
--�̸��˻�
select * from stu_score where id like '%a%'
order by no;

--row_number() over()
--11-~20���� ����Ͻÿ�.
select * from
(
select rownum rnum,a.* from
( select * from stu_score order by total desc ) a
)
where rnum>=11 and rnum<=20
;

