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

--4.student 테이블에서 ranks가 들어가있는 테이블을 넣어줌.
update student a set rank=(select ranks
from (select no, rank() over(order by total desc ) ranks
from student) b where a.no = b.no;


--(select no,rank() over(order by total desc) ranks from student) b;
select hire_date from employees
order by hire_date desc
;

--역순 정렬
select no,total,rank from student
order by total desc;

select hire_date from employees
order by hire_date asc
;

--no순차 정렬
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

--퀴즈 
--1.hire_date 로 asc ,column; 
select employee_id, emp_name, job_id, hire_date, salary from employees
order by hire_date asc;

--2. 급여를 적게 받는 순으로 출력하되 월급이 같으면, 사원명으로 역순정렬하시오.
select emp_name, salary from employees 
order by salary asc, emp_name desc;

--숫자함수
--abs
select -10, abs(-10) from dual;


select 34.789, floor(34.789) as f, round(34.789)as r from dual;

--round(대상,자리수) ex)round(34.178,2) 2자리까지 표시 
select 34.178, round(34.178), round(34.178,2) from dual;

select avg from student;
select round(avg,2) avg from student;
select 34.5678 a ,round(34.5678,-1) b from dual;

--trunc 지정한 자리수 이하 버림 
select trunc(34.5678,2)t from dual; --소수점 두자리
select trunc(34.5678,-1)t from dual; -- -1자리
select trunc(34.5678) t from dual;

--ceil 올림
select ciel(34.123) from dual;

--국어점수 일단위 절사해서 출력하시오.
select kor from student;
select trunc(kor,-1) from student --60점대 70점대 ...
order by kor;

--국어, 영어, 수학, 일단위 절사해서 국,영,수 합계을 출력하시오.
select trunc(kor,-1)국어,trunc(eng,-1)영어,trunc(math,-1)수학,(trunc(kor,-1)+trunc(eng,-1)+trunc(math,-1))합계 from student;

--mod 나머지
select round(100/7,2) from dual;
select mod(10,7) from dual;
--나머지. 나머지가 0이면 짝수, 1이면 홀수
select 10/7 from dual;
--몫
select floor(10/7) from dual;

--퀴즈. 사원번호가 짝수인것을 출력
select employee_id from employees
where mod(employee_id,2)=0;

--학번이 3의 배수 인것만 출력하시오 
select no from student
where mod(no,3)=0;

--시퀀스
create sequence seq_no 
increment by 1 --증감 1씩 
start with 1 -- 시작이 1부터 진행
minvalue 1  --최소값 1
maxvalue 9999  --최댜값 9999
nocycle        --순환하지 않음
no cache ;      --캐시 사용하지 않음
;
--nextval 시퀀스번호 1씩 증가
select seq_no.nextval from dual;

--currval 시퀀스 번호 확인
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
seq_mno.nextval,'eee','1111','김구','010-5555-5555'
);

select * from member;


select sysdate from dual;
select to_char(sysdate,'yy') from dual;
select 's0000'||to_char(seq_mno.currval) from dual;
--'00000'자리수
select 's'||to_char(seq_mno.nextval,'00000') from dual;
--한국대학교 ko202400001, ko202400002   9자리
--시퀀스 seq_kono 1-99999

create sequence seq_kono
increment by 1
start with 1
minvalue 1
maxvalue 99999
nocycle
nocache;
--시퀀스
--trim(공백제거)
select 'ko'||to_char(sysdate,'yyyy')||trim(to_char(seq_kono.nextval,'00000')) as stuno from dual;

--select sysdate from dual;
--select to_char(sysdate,'yyyy') from dual;
--select 'ko000000000'||to_char(seq_kono.currval) from dual;

--게시판

create table board (
bno number(5) primary key,
btitle varchar2(1000),
bcontent varchar2(3000),
id varchar2(30),
bdate date,
bhit number(10),
);

--퀴즈
--seq_dept
--시퀀스 시작 1001 증감 10 1,99999
--5번 실행을 해보세요.

--currval 현재값반환
--nextval 다음값반환

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
emp_seq.nextval, '이순신', sysdate
);
select * from emp01;
commit;

--현재까지 입사한 일수를 함께 출력하시오. 반올림.

select employee_id, emp_name, job_id, hire_date from employees
order by hire_date desc;




























