--trunc 버림, round 반올림
select sysdate, hire_date,trunc(sysdate-hire_date,3) from employees;
select sysdate,hire_date,3,round(sysdate-hire_date,3) from employees;

--어제 sysdate-1, 내일 sysdate +1 
select sysdate-1 어제, sysdate 오늘, sysdate+1 내일 from dual;

--퀴즈
--m_no -시퀀스 1 -9999 1씩 증가 5번 반복해서 저장 
--m_yesterday, m_today, m_tomorrow,m_year 날짜 컬럼을 가진 테이블 m_date  
--어제 오늘 내일 1년후 날짜를 저장하시오.

drop sequence m_no;

create sequence m_no
increment by 1
start with 1
minvalue 1
maxvalue 9999
nocycle
nocache;

select seq_no.currval from dual;
--테이블생성  date(초까지), timestamp(밀리세컨드까지 가능)
create table m_date(
m_no number(4),
m_yesterday date,
m_today date,
m_tomorrow date,
m_year date );
drop table m_date;
--1개 row 저장
insert into m_date(m_no,m_yesterday,m_today,m_tomorrow,m_year)values(seq_m_no.nextval,sysdate-1,sysdate,sysdate+1,sysdate+365);

select * from m_date;

--abs 절대값, ceil,floor round,trunc-자릿수
select abs(hire_date-sysdate) from employees;
--날짜의 월을 기준으로 반올림
select hire_date,round(hire_date,'month') from employees;
--날짜의 월을 기준으로 버림
select hire_date,trunc(hire_date,'month') from employees;

select trunc(hire_date,'month') 기준일, hire_date from employees
order by hire_date;

select * from channels;

select period,count(period) from kor_loan_status
order by period;

select period from kor_loan_status
where period='201111';

select trunc(kor,-1) t_kor,count(trunc(kor,-1)) from students
group by trunc(kor,-1)
order by t_kor;

select trunc(hire_date,'month'),count(trunc(hire_date,'month')) from employees
group by trunc(hire_date,'month')
order by m_hire_date
;

drop table stu_score;
drop table emp01;
drop table board;

select * from stu_score
order by no;

update stu_score set name='홍길자'
where no=9;
select * from stu_score;

update stu_score set avg=(total/3,3);

--2개의 날짜에서 월 간격을 확인
SELECT HIRE_DATE,FLOOR(MONTHS_BETWEEN(SYSDATE,HIRE_DATE)),TRUNC(SYSDATE-HIRE_DATE,2) FROM EMPLOYEES;

--개월 추가
SELECT HIRE_DATE,ADD_MONTHS(HIRE_DATE,6) FROM EMPLOYEES;

--LAST DAY
SELECT HIRE_DATE,LAST_DAY(HIRE_DATE),ROUND(HIRE_DATE,'D') FROM EMPLOYEES;
SELECT SYSDATE 현재일,TRUNC(SYSDATE,'MONTH') 처음일,LAST_DAY(SYSDATE) 마지막일 FROM DUAL;
SELECT SYSDATE,TRUNC(SYSDATE,'MONTH') FROM EMPLOYEES;

--특정 요일의 날짜를 확인
SELECT SYSDATE,NEXT_DAY(SYSDATE,'토요일') FROM DUAL;

--TRUNC 'D'는 ;요일의 처음일 
SELECT SYSDATE,TRUNC(SYSDATE,'D'),NEXT_DAY(SYSDATE,'토요일') FROM DUAL;


--BOARD(게시판) TABLE
--ERROR
CREATE TABLE BOARD(
BNO NUMBER(4) PRIMARY KEY, --중복이 안됨, NULL허용하지 않음.기본키로 사용됨.
ID VARCHAR2(30),
BTITLE VARCHAR2(1000),
BCONTENT CLOB, --VARCHAR2(3000) CLOB -무제한VARCHAR2의 타입;글자수의 제한없음
BDATE DATE DEFAULT SYSDATE,
BHIT NUMBER DEFAULT 0, 
BGROUP NUMBER,
BSTEP NUMBER DEFAULT 0,
BINDENT NUMBER DEFAULT 0,
BFILE VARCHAR2(100)
);--



--BOARD 테이블 DEFAULT는 입력시 없을시 지정한 데이터 자동 입력됨.
create table board(
    bno number(4) primary key,--중복이 안됨 기본키로 사용됨
    id varchar2(30),
    btitle varchar2(1000),
    bcontent clob, --bcontent varchar2(3000)-무제한 랑 같다
    bdate date default sysdate,
    bhit number default 0,
    bgroup number,
    bstep number default 0,
    bindent number default 0,
    bfile varchar2(100) --파일첨부
  );
  
INSERT INTO BOARD VALUES (
BOARD_SEQ.NEXTVAL,'AAA','제목입니다.','내용입니다.',SYSDATE,0,BOARD_SEQ.CURRVAL,0,0,'1.JPG'
);

INSERT INTO BOARD(BNO,ID,BTITLE,BCONTENT,BGROUP,BFILE) VALUES(
BOARD_SEQ.NEXTVAL,'BBB','이벤트 신청','이벤트를 신청합니다.',BOARD_SEQ.CURRVAL,'2.JPG'
);
SELECT * FROM BOARD;

--형변환 --NUMBER,CHARACTER, DATE

SELECT SYSDATE FROM DUAL;
SELECT SYSDATE,TO_CHAR(SYSDATE,'YYYY-MM-DD HH:MI:SS') FROM DUAL;
SELECT TO_CHAR(SYSDATE, 'YY/MM/DD') FROM DUAL;
SELECT TO_CHAR(SYSDATE,'YYYY') FROM DUAL;

--KO+2024+0001 
SELECT 'KO'||TO_CHAR(SYSDATE,'YYYY')||TRIM(TO_CHAR(SEQ_MNO.NEXTVAL,'0000'))FROM DUAL;

SELECT TO_CHAR(SYSDATE,'DY'),TO_CHAR(SYSDATE,'DAY') FROM DUAL;
SELECT TO_CHAR(SYSDATE,'YYYY-MM-DD HH:MI:SS MON DAY') FROM DUAL;

--HIRE_DATE, YYYY-MM-DD HH:MI:SS MON DAY
SELECT HIRE_DATE, TO_CHAR(SYSDATE,'YYYY-MM-DD HH:MI:SS MON DAY') FROM EMPLOYEES;

SELECT TO_CHAR(SYSDATE,'PM HH:MM:SS') FROM DUAL;
SELECT * FROM STU_SOCRE;

SELECT TO_CHAR(C_DATE,'YYYY-MM-DD HH:MI:SS DAY') FROM STU_SCORE
ORDER BY C_DATE;


--날짜별로 몇개의 데이터가 들어가 있는 지출력 하시오.

--*****************
SELECT C_DATE,COUNT(C_DATE) FROM STU_SCORE
GROUP BY C_DATE
ORDER BY C_DATE;

--문자형 사칙연산(+,-,*,/)안됨, 자리수 표시, 쉼표표시
--숫자형 사칙연산 가능 컬럼별 사칙연산가능,자리수표시(0001->안됨.),쉼표표시 안됨.
--날짜형 +,- 연산기능 가능, MONTHS-BETWEEN 2개날짜 달 계산, 날짜 유형을 지정해서 출력이 안됨.

--문자형 안에 있는 데이터가 숫자이면 자동으로 형변환해서 계산해줌.
--문자형 안에 문자가 있으면 자동형변환 불가
SELECT 10 A,100 B,(10+100) AB, TO_CHAR(100), 10+ TO_CHAR(100) FROM DUAL;
SELECT 10 A,100 B,(10+100) AB, TO_CHAR(100), 10+'100원' FROM DUAL;

--'0000' 빈자리는 0으로 채움, '9999'빈자리를 빈자리 둠.
SELECT 12340000, TO_CHAR(12340000),LENGTH(TO_CHAR(12340000,'999,999,999'))FROM DUAL;
SELECT LENGTH(12340000), TO_CHAR(12340000),LENGTH(TO_CHAR(12340000,'000,999,999'))FROM DUAL;

--L은 원화 표시
SELECT 12340000, TO_CHAR(12340000,'l999,999') FROM DUAL;
--$는 $ 표시
SELECT 12340000,TO_CHAR(12340000,'$999,999,999') FROM DUAL;
--
SELECT 1234.1234, TO_CHAR(1234.1234,'000,999.99') FROM DUAL;

--10개 자리수 표시
SELECT LENGTH(TRIM(TO_CHAR(12345,'0000000000'))),LENGTH(TRIM(TO_CHAR(12345,'999,999'))) FROM DUAL;

-- 데이터의 길이 함수
SELECT LENGTH('안녕하세요') FROM DUAL;
SELECT LENGTH(1234000) FROM DUAL;

--퀴즈
--123,456,789 + 100,000 =값을 출력하시오, 천단위 표시할것

SELECT 123456789, TO_CHAR(123456789,'000000000')A, TO_CHAR(100,000,'000000')B, FROM DUAL;

SELECT 123456789+100000 FROM DUAL;
--쉼표빼기 =리플레이스로 
--123,456,789 쉼표제거 -REPLACE('123,456,789',',', '') FROM DUAL;
--타입을 NUMBER 형으로 변경  투넘버
--더하기를 함.
--문자형 타입으로 변경해서 쉼표 표시
--L은원화표시
--WIRE = '100,000'

SELECT (123,456,789)+(100,000)FROM DUAL;

SELECT TO_NUMBER(REPLACE('123,456,789',',', '')), TO_NUMBER(REPLACE('100,000',',','')) FROM DUAL;
SELECT TO_CHAR(TO_NUMBER(REPLACE('123,456,789',',', ''))+TO_NUMBER(REPLACE('100,000',',','')), 'L999,999,999')
FROM DUAL;

select to_char(to_number(replace('123,456,789',',',''))+to_number(replace('100,000',',','')), 'L999,999,999'  )
from dual;

SELECT TO_NUMBER('0000123') FROM DUAL;

--날짜형
--문자형은 +,- 안됨.
SELECT '2024-04-24'-'2024-04-01' FROM DUAL; --에러

SELECT TO_DATE('2024-04-24')-TO_DATE('2024-04-01') FROM DUAL;
SELECT TO_DATE('2024/04/24')-TO_DATE('2024/04/01') FROM DUAL;
SELECT TO_DATE('20240401') FROM DUAL;

--퀴즈 '20240401'
--2024-04-01타입으로 변경해서 출력.
SELECT TO_DATE('20240401') FROM DUAL;
SELECT TO_CHAR(TO_DATE('20240401'),'YYYY-MM-DD HH:MI:SS') FROM DUAL;

SELECT HIRE_DATE FROM EMPLOYEES; 
WHERE HIRE_DATE >= '20080101' 

--퀴즈
--20,000/ 10,000 문자형을 빼기 연산을 해서 10,000 출력하시오.
--NUMBER형 변환
SELECT TO_CHAR(TO_NUMBER('20,000','99,999')-TO_NUMBER('10,000','99,999'),'99,999' ) FROM DUAL;

--퀴즈
SELECT COMMISSION_PCT FROM EMPLOYEES;
--실제 월급=월급+(월급*커미션)실제월급 출력하시오.
--NVL(데이터,0)
SELECT SALARY,SALARY+(SALARY*NVL(COMMISSION_PCT,0)),COMMISSION_PCT FROM EMPLOYEES;

--COMMISSION_PCT NULL값만 출력하시오.
SELECT EMP_NAME,COMMISSION_PCT FROM EMPLOYEES 
WHERE COMMISSION_PCT IS NULL;

SELECT MANAGER_ID FROM EMPLOYEES
ORDER BY MANAGER_ID DESC;

--퀴즈 MANAGER_ID NULL 이면 0 NVL(데이터,0)
SELECT NVL(MANAGER_ID,0) FROM EMPLOYEES 
ORDER BY MANAGER_ID DESC;

--퀴즈 MANAGER_ID NULL 이면 CEO로 입력하시오.
SELECT NVL(TO_CHAR(MANAGER_ID),'CEO') FROM EMPLOYEES
ORDER BY MANAGER_ID DESC;

















