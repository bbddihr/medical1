select * from stu_score;

select * from students;
--drop table students;

update students set id ='aaa', name='홍길동', gender='M' where id='Joelynn' and pw='6856';
update students set id='bbb', name='유관순', gender='F' where id='Bambie';
update students set id='ccc', name='이순신', gender='M' where id='Orin';
update students set id='ddd', name='강감찬', gender='M' where id='Puff';
update students set id='eee', name='김구', gender='M' where id='Godfree';
update students set id='fff', name='김유신', gender='M' where id='Penny' and pw='8503';
update students set id='ggg', name='홍길자', gender='F' where id='Matti' and pw='3737';

select * from students where name='김유신';
commit;
rollback;
--새롭게 순차적 번호 생성: rownum
select rownum,a.* from students a
order by grade;
--1.select구문
select a.* from students a;

2.rownum 함수 실행
select rownum,a.* from students a;

3. order by 구문실행 
select rownum,a.* from students a
order by grade 
;

--1.select  2.order by 구문  3.rownum
select * from students
order by grade
;
select rownum,a.* from
(
select * from students
order by grade

)a
;

--평균avg 85점 이상이면서 no>=500 출력하시오
select *from stu_score
where avg>=85 and no>=500
;

select * from
(select * from stu_score where avg>=85)
where no>=500
;

--테이블명 shop_product
select name, amount,pdate from shop_product
where pdate>='2024-03-01';

--이름별 구매내역 합계를 구하시오.
--sum(amount)는 가상으로 만들어진 컬럼
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



--equi join: 같은 컬럼이 2개의 테이블에 존재하여 2개 컬럼을 이용해 검색하는 방법
--non-equi join: 같은 컬럼이 없으면서 2개 테이블을 사용해 검색하는 방법 

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


--over() 정렬해서
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
--self join,equi-join함께 사용
--equi join: 2개의 테이블에 같은 컬럼을 가지고 검색
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

--john chen과 동일한 부서에 근무하는 사람을 출력하시오.
--컬럼: 사원명, 부서번호, 같이 근무하는 사원 부서번호, 같이 근무하는 사원명
--1. john 부서를 출력
--2. 부서번호를 가지고 같은 사람을 출력
--3. 부서번호 부서명도 출력을 해보세요.

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
member_seq.nextval,'ggg','1111','홍길순','여자',sysdate
)
;
commit;
desc member;

rollback;

select * from member;
update member set name='홍길동' where id='aaa'
;


select * from employees;
--a의 모든 요소 
--select a.* from employees a,employees b
--where a.department_id = b.department_id and a.emp_name = 'Pat Fay';

select a.emp_name,a.department_id,c.department_name, b.emp_name from employees a,employees b,departments c
where a.department_id = b.department_id and a.emp_name = 'sarah Bell'
and a.department_id = c.department_id
;

select * from member order by id;
hhh,1111,홍길자,여자,sysdate

select *from member where id='aaa';

--테이블 생성
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









