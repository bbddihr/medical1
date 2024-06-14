--테이블생성
create table emp01(
emp_id number(6),
emp_name varchar2(80),
hire_date date
);

--테이블 구조만 복사하기
desc employees;


--태이블 생성, 테이블구조및데이터모두복사
create table emp02 as 
select * from employees;

--테이블 구조만 복사하기
create table emp03 as
select * from employees where 1=2;

--테이블 구조가 다르면서, 데이터를 복사하기 (칼럼3개 ->14개)
insert into emp01(emp_id,emp_name,hire_date)
select employee_id, emp_name, hire_date from employees;



select * from emp01 order by emp_id desc;

--데이터 한개 추가
insert into emp01 values(
207,'홍길동','2024-04-26'
);


--테이블 구조가 같으면서, 데이터만 복사
insert into emp03
select * from employees;

select *from emp03;
select * from emp01 order by emp_id desc;

select * from employees;

--drop table s_info;
--drop table m_date;

desc member;

--컬럼 타입변경
alter table member
modify(stu_name varchar2(30));

--컬럼 삭제
alter table member
drop column pw;

--컬럼추가
alter table member 
add (pw varchar2(30));

select * from member;

select mno,id,pw,stu_name,gender from member;

insert into member values(
seq_mno.nextval,'fff','김유신','male','1111'
);

--컬럼순서 변경
--숨김
alter table member modify stu_name invisible;
alter table member modify gender invisible;
alter table member modify stu_name visible;
alter table member modify gender visible;


insert into member values(
seq_mno.nextval,'ggg',,'1111','홍길자','male'
);--에러(순서바껴서)

--컬럼 일시적 사용 제한
alter table member
set unused(id);

--사용제한 해제
alter table member
drop unused columns;

drop table emp03;

--table 이름 변경
rename emp01 to employees01; 

desc employees;

--무결성 제약조건
--foreign key는 다른 테이블에서 데이터 입력시 
--선언되어 있는 기존 테이블에 입력하려는 데이터가 있는지 확인

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
'aaa','1111','홍길동','male'
);

insert into member(id) values(
'ddd'
);


insert into member(id,pw,name) values(
'a','1111','홍길동'
);

select * from member;


--NOT NULL   -NULL값은 제외
--제약조건: UNIQUE -중복만 제거,NULL허용
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
1, '홍길동','1',1
);

create table emp03 as
select * from EMP02 where 1=2;
--DROP TABLE EMP03;
INSERT INTO EMP03 VALUES(
3, '이순신','3',2 
);
--Q. 홍길동을 검색하시오.
SELECT * FROM EMP03
WHERE EMPNO='1';

--Q. NULL 홍길동검색
SELECT * FROM EMP03
WHERE EMPNO IS NULL AND ENAME='홍길동;
--오류 : WHERE EMPNO=NULL;
--Q .NULL인 모든 사람 검색
SELECT * FROM EMP03
WHERE EMPNO IS NULL;

CREATE TABLE EMP01(
EMPNO NUMBER(4) PRIMARY KEY,
ENAME VARCHAR2(20) NOT NULL,
JOB VARCHAR(9),
DEPTNO NUMBER(2)
);

--5개 NULL, 1,2,3,1
--PRIMARY 키로 지정해놔서 NULL 값 안들어감.
INSERT INTO EMP01 VALUES(
1,'김구','1',1
);


SELECT * FROM EMP01;
WHERE EMPNO=3;


--FOREIGN KEY (외래키)
--DROP TABLE EMP01;

--EMP01 테이블 생성
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
1,'홍길동','0001', 10
);

INSERT INTO EMP01 VALUES(
2,'유관순','0002',20
);
INSERT INTO EMP01 VALUES(
3,'이순신','0002',20
);

--DEPTNO 10-270 
INSERT INTO EMP01 VALUES(
4, '김구','0003',270
);

INSERT INTO EMP01 VALUES(
5, '강감찬','0004',1
);

 
 SELECT*FROM EMP01; 
COMMIT;

--EMP01 FOREIGN KEY 추가
--FK_DEPTNO 별칭
--ADD CONSTRAINT 별칭 FOREIGN KEY(현재컬럼) REFERENCES 다른테이블(컬럼이름)
ALTER TABLE EMP01
ADD CONSTRAINT FK_DEPTNO FOREIGN KEY(DEPTNO)
REFERENCES DEPT01(DEPTNO)
;

--FOREIGN KEY 삭제
ALTER TABLE EMP01
DROP CONSTRAINT FK_DEPTNO;

ALTER TABLE EMP01

--DKEPT01 테이블 생성
CREATE TABLE DEPT01(
DEPTNO NUMBER(2) PRIMARY KEY,
DEPT_NAME VARCHAR2(80)
);
--컬럼의 내용 추가
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
1,'AAA','게시글1','내용1'
);
INSERT INTO BOARD VALUES(
7,'BBB','게시글7','내용7'
);


SELECT * FROM COMMENTS;

ALTER TABLE BOARD
ADD CONSTRAINT FK_ID FOREIGN KEY(ID)
REFERENCES MEMBER(ID);

--COMMENT 테이블 댓글테이블


--댓글 달기
INSERT INTO COMMENTS VALUES(
1,5,'1111','댓글내용1'
);

FK를 등록할때 설정
FK키로 등록되어있는 모든 데이터를 삭제시키는 것.

DELETE BOARD WHERE BNO=1;
ALTER TABLE BOARD

--CHECK 제약조건 특정값의 범위, 특정값만 입력되도록 함.
CREATE TABLE EMP(
EMPNO NUMBER(4) PRIMARY KEY,
ENAME VARCHAR2(20) NOT NULL,
JOB VARCHAR2(9) DEFAULT '0001', --컬럼에 데이터 넣지않으면 자동으로 0001이 저장됨.
SAL NUMBER(7,2) CHECK(SAL BETWEEN 2000 AND 20000),
GENDER VARCHAR2(6) CHECK(GENDER IN ('남자','여자'))
);


INSERT INTO EMP(EMPNO,ENAME,JOB,SAL,GENDER) VALUES(
2,'유관순','0003',4000,'여자'
);

INSERT INTO EMP(EMPNO,ENAME,JOB,SAL,GENDER) VALUES(
3,'이순신','0004',5000,'남'
);

--ERROR
INSERT INTO EMP(EMPNO,ENAME,JOB,SAL,GENDER) VALUES(
5,'김구','0006',1000,'남자'
);

--JOB DEFAULT '0001'

INSERT INTO EMP(EMPNO,ENAME,JOB,SAL,GENDER) VALUES(
6,'김유신','10000',4000,'여자'
);

SELECT * FROM TABLE EMP;


