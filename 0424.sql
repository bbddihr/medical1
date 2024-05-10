--trunc ����, round �ݿø�
select sysdate, hire_date,trunc(sysdate-hire_date,3) from employees;
select sysdate,hire_date,3,round(sysdate-hire_date,3) from employees;

--���� sysdate-1, ���� sysdate +1 
select sysdate-1 ����, sysdate ����, sysdate+1 ���� from dual;

--����
--m_no -������ 1 -9999 1�� ���� 5�� �ݺ��ؼ� ���� 
--m_yesterday, m_today, m_tomorrow,m_year ��¥ �÷��� ���� ���̺� m_date  
--���� ���� ���� 1���� ��¥�� �����Ͻÿ�.

drop sequence m_no;

create sequence m_no
increment by 1
start with 1
minvalue 1
maxvalue 9999
nocycle
nocache;

select seq_no.currval from dual;
--���̺����  date(�ʱ���), timestamp(�и���������� ����)
create table m_date(
m_no number(4),
m_yesterday date,
m_today date,
m_tomorrow date,
m_year date );
drop table m_date;
--1�� row ����
insert into m_date(m_no,m_yesterday,m_today,m_tomorrow,m_year)values(seq_m_no.nextval,sysdate-1,sysdate,sysdate+1,sysdate+365);

select * from m_date;

--abs ���밪, ceil,floor round,trunc-�ڸ���
select abs(hire_date-sysdate) from employees;
--��¥�� ���� �������� �ݿø�
select hire_date,round(hire_date,'month') from employees;
--��¥�� ���� �������� ����
select hire_date,trunc(hire_date,'month') from employees;

select trunc(hire_date,'month') ������, hire_date from employees
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

update stu_score set name='ȫ����'
where no=9;
select * from stu_score;

update stu_score set avg=(total/3,3);

--2���� ��¥���� �� ������ Ȯ��
SELECT HIRE_DATE,FLOOR(MONTHS_BETWEEN(SYSDATE,HIRE_DATE)),TRUNC(SYSDATE-HIRE_DATE,2) FROM EMPLOYEES;

--���� �߰�
SELECT HIRE_DATE,ADD_MONTHS(HIRE_DATE,6) FROM EMPLOYEES;

--LAST DAY
SELECT HIRE_DATE,LAST_DAY(HIRE_DATE),ROUND(HIRE_DATE,'D') FROM EMPLOYEES;
SELECT SYSDATE ������,TRUNC(SYSDATE,'MONTH') ó����,LAST_DAY(SYSDATE) �������� FROM DUAL;
SELECT SYSDATE,TRUNC(SYSDATE,'MONTH') FROM EMPLOYEES;

--Ư�� ������ ��¥�� Ȯ��
SELECT SYSDATE,NEXT_DAY(SYSDATE,'�����') FROM DUAL;

--TRUNC 'D'�� ;������ ó���� 
SELECT SYSDATE,TRUNC(SYSDATE,'D'),NEXT_DAY(SYSDATE,'�����') FROM DUAL;


--BOARD(�Խ���) TABLE
--ERROR
CREATE TABLE BOARD(
BNO NUMBER(4) PRIMARY KEY, --�ߺ��� �ȵ�, NULL������� ����.�⺻Ű�� ����.
ID VARCHAR2(30),
BTITLE VARCHAR2(1000),
BCONTENT CLOB, --VARCHAR2(3000) CLOB -������VARCHAR2�� Ÿ��;���ڼ��� ���Ѿ���
BDATE DATE DEFAULT SYSDATE,
BHIT NUMBER DEFAULT 0, 
BGROUP NUMBER,
BSTEP NUMBER DEFAULT 0,
BINDENT NUMBER DEFAULT 0,
BFILE VARCHAR2(100)
);--



--BOARD ���̺� DEFAULT�� �Է½� ������ ������ ������ �ڵ� �Էµ�.
create table board(
    bno number(4) primary key,--�ߺ��� �ȵ� �⺻Ű�� ����
    id varchar2(30),
    btitle varchar2(1000),
    bcontent clob, --bcontent varchar2(3000)-������ �� ����
    bdate date default sysdate,
    bhit number default 0,
    bgroup number,
    bstep number default 0,
    bindent number default 0,
    bfile varchar2(100) --����÷��
  );
  
INSERT INTO BOARD VALUES (
BOARD_SEQ.NEXTVAL,'AAA','�����Դϴ�.','�����Դϴ�.',SYSDATE,0,BOARD_SEQ.CURRVAL,0,0,'1.JPG'
);

INSERT INTO BOARD(BNO,ID,BTITLE,BCONTENT,BGROUP,BFILE) VALUES(
BOARD_SEQ.NEXTVAL,'BBB','�̺�Ʈ ��û','�̺�Ʈ�� ��û�մϴ�.',BOARD_SEQ.CURRVAL,'2.JPG'
);
SELECT * FROM BOARD;

--����ȯ --NUMBER,CHARACTER, DATE

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


--��¥���� ��� �����Ͱ� �� �ִ� ����� �Ͻÿ�.

--*****************
SELECT C_DATE,COUNT(C_DATE) FROM STU_SCORE
GROUP BY C_DATE
ORDER BY C_DATE;

--������ ��Ģ����(+,-,*,/)�ȵ�, �ڸ��� ǥ��, ��ǥǥ��
--������ ��Ģ���� ���� �÷��� ��Ģ���갡��,�ڸ���ǥ��(0001->�ȵ�.),��ǥǥ�� �ȵ�.
--��¥�� +,- ������ ����, MONTHS-BETWEEN 2����¥ �� ���, ��¥ ������ �����ؼ� ����� �ȵ�.

--������ �ȿ� �ִ� �����Ͱ� �����̸� �ڵ����� ����ȯ�ؼ� �������.
--������ �ȿ� ���ڰ� ������ �ڵ�����ȯ �Ұ�
SELECT 10 A,100 B,(10+100) AB, TO_CHAR(100), 10+ TO_CHAR(100) FROM DUAL;
SELECT 10 A,100 B,(10+100) AB, TO_CHAR(100), 10+'100��' FROM DUAL;

--'0000' ���ڸ��� 0���� ä��, '9999'���ڸ��� ���ڸ� ��.
SELECT 12340000, TO_CHAR(12340000),LENGTH(TO_CHAR(12340000,'999,999,999'))FROM DUAL;
SELECT LENGTH(12340000), TO_CHAR(12340000),LENGTH(TO_CHAR(12340000,'000,999,999'))FROM DUAL;

--L�� ��ȭ ǥ��
SELECT 12340000, TO_CHAR(12340000,'l999,999') FROM DUAL;
--$�� $ ǥ��
SELECT 12340000,TO_CHAR(12340000,'$999,999,999') FROM DUAL;
--
SELECT 1234.1234, TO_CHAR(1234.1234,'000,999.99') FROM DUAL;

--10�� �ڸ��� ǥ��
SELECT LENGTH(TRIM(TO_CHAR(12345,'0000000000'))),LENGTH(TRIM(TO_CHAR(12345,'999,999'))) FROM DUAL;

-- �������� ���� �Լ�
SELECT LENGTH('�ȳ��ϼ���') FROM DUAL;
SELECT LENGTH(1234000) FROM DUAL;

--����
--123,456,789 + 100,000 =���� ����Ͻÿ�, õ���� ǥ���Ұ�

SELECT 123456789, TO_CHAR(123456789,'000000000')A, TO_CHAR(100,000,'000000')B, FROM DUAL;

SELECT 123456789+100000 FROM DUAL;
--��ǥ���� =���÷��̽��� 
--123,456,789 ��ǥ���� -REPLACE('123,456,789',',', '') FROM DUAL;
--Ÿ���� NUMBER ������ ����  ���ѹ�
--���ϱ⸦ ��.
--������ Ÿ������ �����ؼ� ��ǥ ǥ��
--L����ȭǥ��
--WIRE = '100,000'

SELECT (123,456,789)+(100,000)FROM DUAL;

SELECT TO_NUMBER(REPLACE('123,456,789',',', '')), TO_NUMBER(REPLACE('100,000',',','')) FROM DUAL;
SELECT TO_CHAR(TO_NUMBER(REPLACE('123,456,789',',', ''))+TO_NUMBER(REPLACE('100,000',',','')), 'L999,999,999')
FROM DUAL;

select to_char(to_number(replace('123,456,789',',',''))+to_number(replace('100,000',',','')), 'L999,999,999'  )
from dual;

SELECT TO_NUMBER('0000123') FROM DUAL;

--��¥��
--�������� +,- �ȵ�.
SELECT '2024-04-24'-'2024-04-01' FROM DUAL; --����

SELECT TO_DATE('2024-04-24')-TO_DATE('2024-04-01') FROM DUAL;
SELECT TO_DATE('2024/04/24')-TO_DATE('2024/04/01') FROM DUAL;
SELECT TO_DATE('20240401') FROM DUAL;

--���� '20240401'
--2024-04-01Ÿ������ �����ؼ� ���.
SELECT TO_DATE('20240401') FROM DUAL;
SELECT TO_CHAR(TO_DATE('20240401'),'YYYY-MM-DD HH:MI:SS') FROM DUAL;

SELECT HIRE_DATE FROM EMPLOYEES; 
WHERE HIRE_DATE >= '20080101' 

--����
--20,000/ 10,000 �������� ���� ������ �ؼ� 10,000 ����Ͻÿ�.
--NUMBER�� ��ȯ
SELECT TO_CHAR(TO_NUMBER('20,000','99,999')-TO_NUMBER('10,000','99,999'),'99,999' ) FROM DUAL;

--����
SELECT COMMISSION_PCT FROM EMPLOYEES;
--���� ����=����+(����*Ŀ�̼�)�������� ����Ͻÿ�.
--NVL(������,0)
SELECT SALARY,SALARY+(SALARY*NVL(COMMISSION_PCT,0)),COMMISSION_PCT FROM EMPLOYEES;

--COMMISSION_PCT NULL���� ����Ͻÿ�.
SELECT EMP_NAME,COMMISSION_PCT FROM EMPLOYEES 
WHERE COMMISSION_PCT IS NULL;

SELECT MANAGER_ID FROM EMPLOYEES
ORDER BY MANAGER_ID DESC;

--���� MANAGER_ID NULL �̸� 0 NVL(������,0)
SELECT NVL(MANAGER_ID,0) FROM EMPLOYEES 
ORDER BY MANAGER_ID DESC;

--���� MANAGER_ID NULL �̸� CEO�� �Է��Ͻÿ�.
SELECT NVL(TO_CHAR(MANAGER_ID),'CEO') FROM EMPLOYEES
ORDER BY MANAGER_ID DESC;

















