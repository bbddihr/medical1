select * from student;

update student set rank=0;
commit;
select * from student;
select total, rank from student;


alter table student add rank number(3);
update student set rank=(rank);

select* from student
order by total desc;

update student set total=(kor+eng+math);

update student set rank=(select no, rank() over 

update student a set rank=(select no,rank() over(order by total desc) rank
from student) b where a.no =b.no;

update student s1 set rank = (select ranks 
from (select no, rank() over(order by total desc ) as ranks from student) s2
where s1.no = s2.no )
;

--4.student ���̺��� ranks�� ���ִ� ���̺��� �־���.
update student a set rank=(select ranks
from (select no, rank() over(order by total desc ) ranks
from student) b where a.no = b.no;


--(select no,rank() over(order by total desc) ranks from student) b;
select hire_date from employees
order by hire_date desc
;

--���� ����
select no,total,rank from student
order by total desc;

select hire_date from employees
order by hire_date asc
;

--no���� ����
select no,total,rank from student
order by no;

select no,kor,eng,math,total,rank from student
order by kor desc, eng asc;

select manager_id from employees
order by manager_id desc;

select hire_date from employees 
order by hire_date desc;

select max(kor)-min(kor) from student;
select max(kor),max(eng),max(math) from student;

--���� 
--1.hire_date �� asc ,column; 
select employee_id, emp_name, job_id, hire_date, salary from employees
order by hire_date asc;

--2. �޿��� ���� �޴� ������ ����ϵ� ������ ������, ��������� ���������Ͻÿ�.
select emp_name, salary from employees 
order by salary asc, emp_name desc;

--�����Լ�
--abs
select -10, abs(-10) from dual;


select 34.789, floor(34.789) as f, round(34.789)as r from dual;

--round(���,�ڸ���) ex)round(34.178,2) 2�ڸ����� ǥ�� 
select 34.178, round(34.178), round(34.178,2) from dual;

select avg from student;
select round(avg,2) avg from student;
select 34.5678 a ,round(34.5678,-1) b from dual;

--trunc ������ �ڸ��� ���� ���� 
select trunc(34.5678,2)t from dual; --�Ҽ��� ���ڸ�
select trunc(34.5678,-1)t from dual; -- -1�ڸ�
select trunc(34.5678) t from dual;

--ceil �ø�
select ciel(34.123) from dual;

--�������� �ϴ��� �����ؼ� ����Ͻÿ�.
select kor from student;
select trunc(kor,-1) from student --60���� 70���� ...
order by kor;

--����, ����, ����, �ϴ��� �����ؼ� ��,��,�� �հ��� ����Ͻÿ�.
select trunc(kor,-1)����,trunc(eng,-1)����,trunc(math,-1)����,(trunc(kor,-1)+trunc(eng,-1)+trunc(math,-1))�հ� from student;

--mod ������
select round(100/7,2) from dual;
select mod(10,7) from dual;
--������. �������� 0�̸� ¦��, 1�̸� Ȧ��
select 10/7 from dual;
--��
select floor(10/7) from dual;

--����. �����ȣ�� ¦���ΰ��� ���
select employee_id from employees
where mod(employee_id,2)=0;

--�й��� 3�� ��� �ΰ͸� ����Ͻÿ� 
select no from student
where mod(no,3)=0;

--������
create sequence seq_no 
increment by 1 --���� 1�� 
start with 1 -- ������ 1���� ����
minvalue 1  --�ּҰ� 1
maxvalue 9999  --�ִ��� 9999
nocycle        --��ȯ���� ����
no cache ;      --ĳ�� ������� ����
;
--nextval ��������ȣ 1�� ����
select seq_no.nextval from dual;

--currval ������ ��ȣ Ȯ��
select seq_no.currval from dual;

--drop table member;

--drop table mem3;

create table member(
mno number(4),
id varchar2(30),
pw varchar2(20),
name varchar2(30),
phone varchar2(15)
);

create sequence seq_mno
increment by 1
start with 1
minvalue 1
maxvalue 9999
nocycle
nocache
;

select seq_mno.nextval from dual;

insert into member values(
seq_mno.nextval,'eee','1111','�豸','010-5555-5555'
);

select * from member;


select sysdate from dual;
select to_char(sysdate,'yy') from dual;
select 's0000'||to_char(seq_mno.currval) from dual;
--'00000'�ڸ���
select 's'||to_char(seq_mno.nextval,'00000') from dual;
--�ѱ����б� ko202400001, ko202400002   9�ڸ�
--������ seq_kono 1-99999

create sequence seq_kono
increment by 1
start with 1
minvalue 1
maxvalue 99999
nocycle
nocache;
--������
--trim(��������)
select 'ko'||to_char(sysdate,'yyyy')||trim(to_char(seq_kono.nextval,'00000')) as stuno from dual;

--select sysdate from dual;
--select to_char(sysdate,'yyyy') from dual;
--select 'ko000000000'||to_char(seq_kono.currval) from dual;

--�Խ���

create table board (
bno number(5) primary key,
btitle varchar2(1000),
bcontent varchar2(3000),
id varchar2(30),
bdate date,
bhit number(10),
);

--����
--seq_dept
--������ ���� 1001 ���� 10 1,99999
--5�� ������ �غ�����.

--currval ���簪��ȯ
--nextval ��������ȯ

create sequence seq_dept
increment by 10
start with 1001
minvalue 1
maxvalue 99999
nocycle
nocache;

create table emp01(
empno number(4) primary key,
ename varchar(30),
hire_date date
);

create sequence emp_seq
increment by 1
start with 1
minvalue 1
maxvalue 9999
nocycle
nocache;

alter sequence emp_seq
increment by 1001
;



insert into emp01 values(
emp_seq.nextval, '�̼���', sysdate
);
select * from emp01;
commit;

--������� �Ի��� �ϼ��� �Բ� ����Ͻÿ�. �ݿø�.

select employee_id, emp_name, job_id, hire_date from employees
order by hire_date desc;




























