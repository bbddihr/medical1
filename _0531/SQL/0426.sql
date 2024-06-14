--���̺����
create table emp01(
emp_id number(6),
emp_name varchar2(80),
hire_date date
);

--���̺� ������ �����ϱ�
desc employees;


--���̺� ����, ���̺����׵����͸�κ���
create table emp02 as 
select * from employees;

--���̺� ������ �����ϱ�
create table emp03 as
select * from employees where 1=2;

--���̺� ������ �ٸ��鼭, �����͸� �����ϱ� (Į��3�� ->14��)
insert into emp01(emp_id,emp_name,hire_date)
select employee_id, emp_name, hire_date from employees;



select * from emp01 order by emp_id desc;

--������ �Ѱ� �߰�
insert into emp01 values(
207,'ȫ�浿','2024-04-26'
);


--���̺� ������ �����鼭, �����͸� ����
insert into emp03
select * from employees;

select *from emp03;
select * from emp01 order by emp_id desc;

select * from employees;

--drop table s_info;
--drop table m_date;

desc member;

--�÷� Ÿ�Ժ���
alter table member
modify(stu_name varchar2(30));

--�÷� ����
alter table member
drop column pw;

--�÷��߰�
alter table member 
add (pw varchar2(30));

select * from member;

select mno,id,pw,stu_name,gender from member;

insert into member values(
seq_mno.nextval,'fff','������','male','1111'
);

--�÷����� ����
--����
alter table member modify stu_name invisible;
alter table member modify gender invisible;
alter table member modify stu_name visible;
alter table member modify gender visible;


insert into member values(
seq_mno.nextval,'ggg',,'1111','ȫ����','male'
);--����(�����ٲ���)

--�÷� �Ͻ��� ��� ����
alter table member
set unused(id);

--������� ����
alter table member
drop unused columns;

drop table emp03;

--table �̸� ����
rename emp01 to employees01; 

desc employees;

--���Ἲ ��������
--foreign key�� �ٸ� ���̺��� ������ �Է½� 
--����Ǿ� �ִ� ���� ���̺� �Է��Ϸ��� �����Ͱ� �ִ��� Ȯ��

--drop table employees01;
--drop table emp02;
--drop table member;
--drop table board;

create table member (
id varchar2(30) primary key,
pw varchar2(30) not null,
name varchar2(30),
gender varchar2(6)
);

insert into member values(
'aaa','1111','ȫ�浿','male'
);

insert into member(id) values(
'ddd'
);


insert into member(id,pw,name) values(
'a','1111','ȫ�浿'
);

select * from member;


--NOT NULL   -NULL���� ����
--��������: UNIQUE -�ߺ��� ����,NULL���
CREATE TABLE EMP02(
EMPNO NUMBER(4) NOT NULL,
ENAME VARCHAR2(10) NOT NULL,
JOB VARCHAR2(9),
DEPTNO NUMBER(2)
);

CREATE TABLE EMP03(
EMPNO NUMBER(4) UNIQUE,
ENAME VARCHAR2(10) NOT NULL,
JOB VARCHAR2(9),
DEPTNO NUMBER(2)
);


SELECT * FROM EMP03;

INSERT INTO EMP03 VALUES(
1, 'ȫ�浿','1',1
);

create table emp03 as
select * from EMP02 where 1=2;
--DROP TABLE EMP03;
INSERT INTO EMP03 VALUES(
3, '�̼���','3',2 
);
--Q. ȫ�浿�� �˻��Ͻÿ�.
SELECT * FROM EMP03
WHERE EMPNO='1';

--Q. NULL ȫ�浿�˻�
SELECT * FROM EMP03
WHERE EMPNO IS NULL AND ENAME='ȫ�浿;
--���� : WHERE EMPNO=NULL;
--Q .NULL�� ��� ��� �˻�
SELECT * FROM EMP03
WHERE EMPNO IS NULL;

CREATE TABLE EMP01(
EMPNO NUMBER(4) PRIMARY KEY,
ENAME VARCHAR2(20) NOT NULL,
JOB VARCHAR(9),
DEPTNO NUMBER(2)
);

--5�� NULL, 1,2,3,1
--PRIMARY Ű�� �����س��� NULL �� �ȵ�.
INSERT INTO EMP01 VALUES(
1,'�豸','1',1
);


SELECT * FROM EMP01;
WHERE EMPNO=3;


--FOREIGN KEY (�ܷ�Ű)
--DROP TABLE EMP01;

--EMP01 ���̺� ����
CREATE TABLE EMP01(
EMPNO NUMBER(4) PRIMARY KEY,
ENAME VARCHAR2(20) NOT NULL,
JOB VARCHAR2(9),
DEPTNO NUMBER(6)
);

ALTER TABLE EMP01
MODIFY(DEPTNO NUMBER(6))
;

INSERT INTO EMP01 VALUES(
1,'ȫ�浿','0001', 10
);

INSERT INTO EMP01 VALUES(
2,'������','0002',20
);
INSERT INTO EMP01 VALUES(
3,'�̼���','0002',20
);

--DEPTNO 10-270 
INSERT INTO EMP01 VALUES(
4, '�豸','0003',270
);

INSERT INTO EMP01 VALUES(
5, '������','0004',1
);

 
 SELECT*FROM EMP01; 
COMMIT;

--EMP01 FOREIGN KEY �߰�
--FK_DEPTNO ��Ī
--ADD CONSTRAINT ��Ī FOREIGN KEY(�����÷�) REFERENCES �ٸ����̺�(�÷��̸�)
ALTER TABLE EMP01
ADD CONSTRAINT FK_DEPTNO FOREIGN KEY(DEPTNO)
REFERENCES DEPT01(DEPTNO)
;

--FOREIGN KEY ����
ALTER TABLE EMP01
DROP CONSTRAINT FK_DEPTNO;

ALTER TABLE EMP01

--DKEPT01 ���̺� ����
CREATE TABLE DEPT01(
DEPTNO NUMBER(2) PRIMARY KEY,
DEPT_NAME VARCHAR2(80)
);
--�÷��� ���� �߰�
INSERT INTO DEPT01(DEPTNO,DEPT_NAME)
SELECT DEPARTMENT_ID,DEPARTMENT_NAME FROM DEPARTMENTS;


ALTER TABLE DEPT01
MODIFY ( DEPTNO NUMBER(6));

DESC DEPARTMENTS;
SELECT * FROM DEPARTMENTS;

DESC MEMBER;
--
CREATE TABLE BOARD (
BNO NUMBER(4) PRIMARY KEY,
ID VARCHAR2(30),
BTITLE VARCHAR2(1000),
BCONTENT VARCHAR2(3000)
);

INSERT INTO BOARD VALUES(
1,'AAA','�Խñ�1','����1'
);
INSERT INTO BOARD VALUES(
7,'BBB','�Խñ�7','����7'
);


SELECT * FROM COMMENTS;

ALTER TABLE BOARD
ADD CONSTRAINT FK_ID FOREIGN KEY(ID)
REFERENCES MEMBER(ID);

--COMMENT ���̺� ������̺�


--��� �ޱ�
INSERT INTO COMMENTS VALUES(
1,5,'1111','��۳���1'
);

FK�� ����Ҷ� ����
FKŰ�� ��ϵǾ��ִ� ��� �����͸� ������Ű�� ��.

DELETE BOARD WHERE BNO=1;
ALTER TABLE BOARD

--CHECK �������� Ư������ ����, Ư������ �Էµǵ��� ��.
CREATE TABLE EMP(
EMPNO NUMBER(4) PRIMARY KEY,
ENAME VARCHAR2(20) NOT NULL,
JOB VARCHAR2(9) DEFAULT '0001', --�÷��� ������ ���������� �ڵ����� 0001�� �����.
SAL NUMBER(7,2) CHECK(SAL BETWEEN 2000 AND 20000),
GENDER VARCHAR2(6) CHECK(GENDER IN ('����','����'))
);


INSERT INTO EMP(EMPNO,ENAME,JOB,SAL,GENDER) VALUES(
2,'������','0003',4000,'����'
);

INSERT INTO EMP(EMPNO,ENAME,JOB,SAL,GENDER) VALUES(
3,'�̼���','0004',5000,'��'
);

--ERROR
INSERT INTO EMP(EMPNO,ENAME,JOB,SAL,GENDER) VALUES(
5,'�豸','0006',1000,'����'
);

--JOB DEFAULT '0001'

INSERT INTO EMP(EMPNO,ENAME,JOB,SAL,GENDER) VALUES(
6,'������','10000',4000,'����'
);

SELECT * FROM TABLE EMP;


