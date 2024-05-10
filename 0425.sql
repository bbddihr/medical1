--어제,오늘,내일
select sysdate-1, sysdate, sysdate+1 from dual;

--오늘,이달의 첫일, 이달의 마지막일
select sysdate,trunc(sysdate,'month'),last_day(sysdate) from dual;

--두날짜간 일수, 두 날짜간 달수********** 외우기
select round(sysdate-hire_date,3), trunc(months_between(sysdate,hire_date),2) from employees;

--trunc 일단위 버림
select trunc(kor,-1) kor,count(trunc(kor,-1)) from stu_score
group by trunc(kor,-1)
order by kor;

--hire_date 날짜에서 월만 출력하시오.
select hire_date from employees;

select to_char(sysdate,'yyyy-mm-dd') from employees;
select to_char(hire_date,'mm')from employees;

select to_char(hire_date,'mm') hire_date from employees
group by to_char(hire_date,'mm')
order by hire_date;
--퀴즈, hire_date yyyy 년도, 년도별 인원수를 출력
select to_char(hire_date, 'yyyy'), hire_date,count(to_char(hire_date,'yyyy')) from employees
group by to_char(hire_date,'yyyy')
order by hire_date;

--형변환-number,character,date
--number 사칙연산 가능,쉼표표시안됨,원화표시안됨.
--char 사칙연산(+,-)안됨, 쉼표표시가능,원화표시가능
--date +,- 가능 날짜출력형태는 변경불가
--시퀀스,날짜의 년도를 가지고 학번을 부여하시오.
--stu_seq시퀀시를 가지고 5명의 학번 출력
--ko+2024+0001



select 'ko'||to_char(sysdate,'yyyy')||trim(to_char(stu_seq.nextval,'0000'))from dual;
--문자형타입
--123,456,789, 156,778, 더하기 값
--(123,456,789)+(100,000)=123556789 출력
--#1
SELECT REPLACE('123,456,789',',','')+TO_NUMBER(REPLACE('100,000',',','')) FROM DUAL;
--#2
SELECT TO_CHAR(TO_NUMBER('123,456,789','999,999,999')+TO_NUMBER('100,000','999,999')

SELECT TO_CHAR(SALARY,'999,999') FROM EMPLOYEES;

--숫자타입을 날짜타입으로 변경
SELECT 20240425 FROM DUAL;
SELECT TO_CHAR(20240425+3)+3 FROM DUAL;
SELECT TO_DATE(20240425) FROM DUAL;

--숫자타입을 날짜타입으로 변경
SELECT EMP_NAME,HIRE_DATE FROM EMPLOYEES
WHERE HIRE_DATE > TO_DATE(20070101)
ORDER BY HIRE_DATE;

--퀴즈01,05, 08월 입사한, 사원이름 2번째에 A가 들어가 있는 사람을 출력하시오.
SELECT EMP_NAME,HIRE_DATE FROM EMPLOYEES
WHERE TO_CHAR(HIRE_DATE,'MM')='08' OR TO_CHAR(HIRE_DATE,'MM')='01' OR TO_CHAR(HIRE_DATE,'MM')='05';
WHERE EMP_NAME LIKE '_A%';
--방법2
SELECT HIRE_DATE FROM EMPLOYEES
WHERE TO_CHAR(HIRE_DATE,'MM') IN ('01','05','08');

--퀴즈. 20070101 이후 입사한 사원이름 2번째에 A가 들어가 있는 사람을 출력하시오.
SELECT EMP_NAME FROM EMPLOYEES
WHERE EMP_NAME LIKE '%A%';

--문자타입을 날짜타입으로 변경
SELECT SYSDATE-TO_DATE('20240401') FROM DUAL; 
select sysdate-to_date('20240401') from dual;
EMP_NAME, HIRE_DATE FROM EMPLOYEES
WHERE EMP_NAME LIKE'_A%' AND TO_CHAR(HIRE_DATE,'MM') IN ('08')
ORDER BY HIRE_DATE;


insert into m_date(m_no,m_yesterday,m_today,m_tomorrow,m_year) values (
seq_no.nextval, sysdate-1,sysdate,sysdate+1,sysdate+365 
);


select sysdate,'2024-04-01',sysdate-to_date('2024-04-01') from dual;
select * from m_date;
insert into m_date(m_no,m_yesterday) values(
seq_mno.nextval, '2024-04-01'
);

create table eventDate (
eno number,
e_today date,
e_choice_day date,
e_period number
);
--입력시 날짜타입에 문자(형태-날짜형태)를 입력해도 저장됨.
--날짜와 문자를 빼기는 불가능, 그래서 문자를 날짜타입으로 변경해야함.

select * from eventDate;

insert into eventDate values(
seq_mno.nextval,sysdate,'2024-04-01',sysdate-to_date('2024-04-01')
);
--문자타입을 숫자타입으로 변경
select to_number('20,000','99,999')-to_number('10,000,'99,999')from dual;

--null을 0으로 치환 nvl()
select salary, commission_pct,salary+(salary*nvl(commission_pct,0)) from employees;

--manager_id null ceo
select manager_id from employees
order by manager_id desc;

--숫자타입을 문자타입으로 변경
select nvl(to_char(manager_id),'ceo') from employees
order by manager_id desc
;

--그룹함수 COUNT
SELECT COUNT(EMP_NAME) FROM EMPLOYEES;
--결과값: 107명
SELECT COUNT(*) FROM EMPLOYEES;
--NULL값이 있으면 제외 -결과값:106명
SELECT COUNT(MANAGER_ID) FROM EMPLOYEES;
SELECT EMP_NAME,MANAGER_ID FROM EMPLOYEES;

--SUM:총합
SELECT SUM(SALARY) FROM EMPLOYEES;

--AVG:평균
SELECT AVG(SALARY) AVG_SAL FROM EMPLOYEES;

--MIN:최소값,MAX: 최대값
SELECT MIN(SALARY), MAX(SALARY) FROM EMPLOYEES;

--6461 달러보다 높은 사람을 출력하시오.
SELECT * FROM EMPLOYEES
WHERE SALARY > 6461;

--컬럼 한개끼리만 비교할수있음.이중쿼리
SELECT EMP_NAME,SALARY FROM EMPLOYEES
WHERE SALARY>(SELECT AVG(SALARY) AVG_SAL FROM EMPLOYEES);

--그룹함수:SUM,AVG,COUN(),COUNT(*),MIN, MAX


--개수:COUNT 
SELECT MIN(SALARY) FROM EMPLOYEES;
SELECT EMP_NAME,MIN(SALARY) FROM

--퀴즈 최소월급을 받는 사람의 사번,이름을 출력
SELECT EMPLOYEE_ID, EMP_NAME, SALARY FROM EMPLOYEES
WHERE SALARY=(SELECT MIN(SALARY) FROM EMPLOYEES);

--퀴즈 최대 월급 받는 사람의 사번,이름을 출력
SELECT EMPLOYEE_ID, EMP_NAME, SALARY FROM EMPLOYEES
WHERE SALARY=(SELECT MAX(SALARY) FROM EMPLOYEES);

--부서번호가 50번인 사원만 전체 월급
SELECT DEPARTMENT_ID, SALARY FROM EMPLOYEES;

SELECT SUM(SALARY) FROM EMPLOYEES
WHERE DAPARTMENT_ID = 50;

SELECT COUNT(*) FROM STU_SCORE

--퀴즈 STU_SCORE KOR 점수가 80점 이상인 학생을 출력하시오.
SELECT KOR FROM STU_SCORE
WHERE KOR>=80;

--Q.국어점수에서 국어점수 평균이상, 영어 평균이상인 학생을 출력하시오.

SELECT COUNT(*) FROM STU_SCORE
WHERE KOR>=(SELECT AVG(KOR) FROM STU_SCORE)
AND ENG>=(SELECT AVG(ENG) FROM STU_SCORE)
;

CREATE TABLE S_INFO (
SNO NUMBER,
S_COUNT NUMBER
);

INSERT INTO S_INFO VALUES(
STU_SEQ.NEXTVAL,(SELECT COUNT(*) FROM STU_SCORE
WHERE KOR>=(SELECT AVG(KOR) FROM STU_SCORE)
AND ENG>=(SELECT AVG(ENG) FROM STU_SCORE))
);
SELECT * FROM S_INFO;

--퀴즈.국어점수 최고점인 학생, 영어점수 최고점인 학생,수학점수 최고점인 학생을 출력하시오.
SELECT * FROM STU_SCORE
--WHERE KOR =(SELECT MAX(KOR) FROM STU_SCORE);
WHERE ENG =(SELECT MAX(ENG) FROM STU_SCORE);
WHERE MATH =(SELECT MAX(MATH) FROM STU_SCORE);

--Q .월급이 최대,최소,평균인 사원을 출력하시오.
SELECT * FROM EMPLOYEES
WHERE SALARY=(SELECT MIN(SALARY) FROM EMPLOYEES);
OR SALARY=(SELECT MAX(SALARY) FROM EMPLOYEES);
OR SALARY=(SELECT AVG(SALARY) FROM EMPLOYEES);

--최대값
SELECT EMP_NAME, SALARY FROM EMPLOYEES
WHERE SALARY=(SELECT MAX(SALARY) FROM EMPLOYEES); 

--평균값보다 낮은 사원 중에 최대값인 사원 출력하시오.
--평균값보다 낮은 사원을 검색 
--검색사원중 최대값 검색
SELECT EMP_NAME FROM EMPLOYEES 
WHERE SALARY = 
(SELECT MAX(SALARY) FROM (
SELECT EMP_NAME, SALARY FROM EMPLOYEES
WHERE SALARY <=(SELECT AVG(SALARY) FROM EMPLOYEES)
ORDER BY SALARY DESC)
);
--위아래 같음.
SELECT EMP_NAME,SALARY FROM EMPLOYEES 
WHERE SALARY = 6400;

--평균보다 낮은 값 107명
--SELECT MAX(SALARY) FROM (테이블)

--56명 최대값 6400
SELECT MAX(SALARY) FROM (
SELECT EMP_NAME, SALARY FROM EMPLOYEES
WHERE SALARY <=(SELECT AVG(SALARY) FROM EMPLOYEES)
ORDER BY SALARY DESC);

--문자함수
--LPAD, RPAD빈공백 채우기
SELECT EMP_NAME,LPAD(EMP_NAME,15,'#') FROM EMPLOYEES;
SELECT EMP_NAME,RPAD(EMP_NAME,20,'@') FROM EMPLOYEES;

--ITEM, RTRIM 지정한 문자를 잘라내고 출력
SELECT EMP_NAME,LTRIM(EMP_NAME,'DO')FROM EMPLOYEES;

--KO20240001
SELECT 'KO20240001',LTRIM('KO20240001','KO2024') FROM DUAL;
SELECT JOB_IDFROM DEP

--Q.JOB_ID FROM EMPLOYEES; 퀴즈 JOB_ID 앞 두글자와 사원번호를 결합해서 출력하시오.

SELECT SUBSTR(JOB_ID,0.2) ||EMPLOYEE_ID FROM EMPLOYEES;

SUBSTR(데이터,순서 개수) EX.SUBSTR('ABCDEFJ")
SELECT EMP_NAME,SUBSTR(EMP_NAME, SUBSTR(EMP_NAME,3,4) FROM EMPLOYEES;

--LENGTH:문자열의 길이
SELECT EMP_NAME,LENGTH(EMP_NAME) FROM EMPLOYEES
WHERE LENGTH(EMP_NAME)>15;

--날짜함수 +,- 가능, 날짜데이터끼리 더하기는 안됨.
--날짜데이터+숫자 가능
SELECT SYSDATE+1 FROM DUAL;
--날짜데이터-날짜데이터 가능
SELECT SYSDATE-HIRE_DATE FROM EMPLOYEE;
--날짜데이터+날짜데이터 불가능
SELECT SYSDATE+HIRE_DATE FROM EMPLOYEES;

SELECT SYSDATE,TRUNC(SYSDATE,'MONTH'),ROUND(SYSDATE,'MONTH') FROM DUAL;

SELECT ROUND(SYSDATE,'YEAR') FROM DUAL;
--개월수 추가
SELECT ADD_MONTHS(SYSDATE,-2) FROM DUAL;

SELECT CEIL(-4.2), FLOOR(-4.2), MOD(8,3),POWER(2,10) FROM DUAL;

SELECT EMP_NAME||TO_CHAR(HIRE_DATE,'YYYY"년"-MM"월"-DD"일" DAY')FROM EMPLOYEES;

--Q. 사원명,자리수 9자리 빈공백 0으로 표시
--SALARY*1400 앞에 원화표시와 쉼표를 넣어 출력하시오.

SELECT SALARY, TO_CHAR(SALARY*1400,'L000,000,000') FROM EMPLOYEES;
--자신의 생일과 자신의 생일이 속한달의 마지막 날짜
--'2010-10-10'
SELECT LAST_DAY('2010-01-01') FROM DUAL;

SELECT TRUNC(TO_DATE('2010-10-10'),'MONTH'),'2010-10-10', LAST_DAY('2010-01-01') FROM DUAL;

SELECT *FROM MEMBER;

DESC MEMBER;

--DDL(DATA DEFINITION LANGUAGE )- COLUMN 추가
--컬럼추가, 삭제
--DDL은 COMMIT,ROLLBACK이 안됨.바로 저장
ALTER TABLE MEMBER ADD GENDER VARCHAR(6) DEFAULT 'FEMALE' NOT NULL;

SELECT *FROM MEMBER;
UPDATE MEMBER SET=GENDER ='MALE';
COMMIT;

ALTER TABLE MEMBER DROP COLUMN PHONE;
DESC MEMBER;

SELECT * FROM MEMBER;

--컬럼수정-컬럼이름변경,타입변경
ALTER TABLE MEMBER RENAME COLUMN NAME TO STU_NAME;
DESC MEMBER;

--타입변경
ALTER TABLE MEMBER MODIFY(STU_NAME VARCHAR2(50));
--기존의 데이터가 변경하려는 크기보다 작을때만 가능
UPDATE MEMBER SET STU_NAME='1';
--컬럼의 타입을 변경하려면 컬럼데이터가 빈공백이거나 NULL일때 가능
ALTER TABLE MEMBER MODIFY(STU_NAME NUMBER(4));
ALTER TABLE MEMBER MODIFY(STU_NAME VARCHAR2(6));

SELECT STU_NAME FROM MEMBER ;
ALTER TABLE MEMBER MODIFY(STU_NAME NUMBER(100));
DESC MEMBER;
INSERT INTO STU_NAME(MNO,ID,PW,STU_NAME,GENDER) VALUES(4,BBB,'2222',"유관순",FEMALE);

