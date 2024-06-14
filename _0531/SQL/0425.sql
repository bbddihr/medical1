--����,����,����
select sysdate-1, sysdate, sysdate+1 from dual;

--����,�̴��� ù��, �̴��� ��������
select sysdate,trunc(sysdate,'month'),last_day(sysdate) from dual;

--�γ�¥�� �ϼ�, �� ��¥�� �޼�********** �ܿ��
select round(sysdate-hire_date,3), trunc(months_between(sysdate,hire_date),2) from employees;

--trunc �ϴ��� ����
select trunc(kor,-1) kor,count(trunc(kor,-1)) from stu_score
group by trunc(kor,-1)
order by kor;

--hire_date ��¥���� ���� ����Ͻÿ�.
select hire_date from employees;

select to_char(sysdate,'yyyy-mm-dd') from employees;
select to_char(hire_date,'mm')from employees;

select to_char(hire_date,'mm') hire_date from employees
group by to_char(hire_date,'mm')
order by hire_date;
--����, hire_date yyyy �⵵, �⵵�� �ο����� ���
select to_char(hire_date, 'yyyy'), hire_date,count(to_char(hire_date,'yyyy')) from employees
group by to_char(hire_date,'yyyy')
order by hire_date;

--����ȯ-number,character,date
--number ��Ģ���� ����,��ǥǥ�þȵ�,��ȭǥ�þȵ�.
--char ��Ģ����(+,-)�ȵ�, ��ǥǥ�ð���,��ȭǥ�ð���
--date +,- ���� ��¥������´� ����Ұ�
--������,��¥�� �⵵�� ������ �й��� �ο��Ͻÿ�.
--stu_seq�����ø� ������ 5���� �й� ���
--ko+2024+0001



select 'ko'||to_char(sysdate,'yyyy')||trim(to_char(stu_seq.nextval,'0000'))from dual;
--������Ÿ��
--123,456,789, 156,778, ���ϱ� ��
--(123,456,789)+(100,000)=123556789 ���
--#1
SELECT REPLACE('123,456,789',',','')+TO_NUMBER(REPLACE('100,000',',','')) FROM DUAL;
--#2
SELECT TO_CHAR(TO_NUMBER('123,456,789','999,999,999')+TO_NUMBER('100,000','999,999')

SELECT TO_CHAR(SALARY,'999,999') FROM EMPLOYEES;

--����Ÿ���� ��¥Ÿ������ ����
SELECT 20240425 FROM DUAL;
SELECT TO_CHAR(20240425+3)+3 FROM DUAL;
SELECT TO_DATE(20240425) FROM DUAL;

--����Ÿ���� ��¥Ÿ������ ����
SELECT EMP_NAME,HIRE_DATE FROM EMPLOYEES
WHERE HIRE_DATE > TO_DATE(20070101)
ORDER BY HIRE_DATE;

--����01,05, 08�� �Ի���, ����̸� 2��°�� A�� �� �ִ� ����� ����Ͻÿ�.
SELECT EMP_NAME,HIRE_DATE FROM EMPLOYEES
WHERE TO_CHAR(HIRE_DATE,'MM')='08' OR TO_CHAR(HIRE_DATE,'MM')='01' OR TO_CHAR(HIRE_DATE,'MM')='05';
WHERE EMP_NAME LIKE '_A%';
--���2
SELECT HIRE_DATE FROM EMPLOYEES
WHERE TO_CHAR(HIRE_DATE,'MM') IN ('01','05','08');

--����. 20070101 ���� �Ի��� ����̸� 2��°�� A�� �� �ִ� ����� ����Ͻÿ�.
SELECT EMP_NAME FROM EMPLOYEES
WHERE EMP_NAME LIKE '%A%';

--����Ÿ���� ��¥Ÿ������ ����
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
--�Է½� ��¥Ÿ�Կ� ����(����-��¥����)�� �Է��ص� �����.
--��¥�� ���ڸ� ����� �Ұ���, �׷��� ���ڸ� ��¥Ÿ������ �����ؾ���.

select * from eventDate;

insert into eventDate values(
seq_mno.nextval,sysdate,'2024-04-01',sysdate-to_date('2024-04-01')
);
--����Ÿ���� ����Ÿ������ ����
select to_number('20,000','99,999')-to_number('10,000,'99,999')from dual;

--null�� 0���� ġȯ nvl()
select salary, commission_pct,salary+(salary*nvl(commission_pct,0)) from employees;

--manager_id null ceo
select manager_id from employees
order by manager_id desc;

--����Ÿ���� ����Ÿ������ ����
select nvl(to_char(manager_id),'ceo') from employees
order by manager_id desc
;

--�׷��Լ� COUNT
SELECT COUNT(EMP_NAME) FROM EMPLOYEES;
--�����: 107��
SELECT COUNT(*) FROM EMPLOYEES;
--NULL���� ������ ���� -�����:106��
SELECT COUNT(MANAGER_ID) FROM EMPLOYEES;
SELECT EMP_NAME,MANAGER_ID FROM EMPLOYEES;

--SUM:����
SELECT SUM(SALARY) FROM EMPLOYEES;

--AVG:���
SELECT AVG(SALARY) AVG_SAL FROM EMPLOYEES;

--MIN:�ּҰ�,MAX: �ִ밪
SELECT MIN(SALARY), MAX(SALARY) FROM EMPLOYEES;

--6461 �޷����� ���� ����� ����Ͻÿ�.
SELECT * FROM EMPLOYEES
WHERE SALARY > 6461;

--�÷� �Ѱ������� ���Ҽ�����.��������
SELECT EMP_NAME,SALARY FROM EMPLOYEES
WHERE SALARY>(SELECT AVG(SALARY) AVG_SAL FROM EMPLOYEES);

--�׷��Լ�:SUM,AVG,COUN(),COUNT(*),MIN, MAX


--����:COUNT 
SELECT MIN(SALARY) FROM EMPLOYEES;
SELECT EMP_NAME,MIN(SALARY) FROM

--���� �ּҿ����� �޴� ����� ���,�̸��� ���
SELECT EMPLOYEE_ID, EMP_NAME, SALARY FROM EMPLOYEES
WHERE SALARY=(SELECT MIN(SALARY) FROM EMPLOYEES);

--���� �ִ� ���� �޴� ����� ���,�̸��� ���
SELECT EMPLOYEE_ID, EMP_NAME, SALARY FROM EMPLOYEES
WHERE SALARY=(SELECT MAX(SALARY) FROM EMPLOYEES);

--�μ���ȣ�� 50���� ����� ��ü ����
SELECT DEPARTMENT_ID, SALARY FROM EMPLOYEES;

SELECT SUM(SALARY) FROM EMPLOYEES
WHERE DAPARTMENT_ID = 50;

SELECT COUNT(*) FROM STU_SCORE

--���� STU_SCORE KOR ������ 80�� �̻��� �л��� ����Ͻÿ�.
SELECT KOR FROM STU_SCORE
WHERE KOR>=80;

--Q.������������ �������� ����̻�, ���� ����̻��� �л��� ����Ͻÿ�.

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

--����.�������� �ְ����� �л�, �������� �ְ����� �л�,�������� �ְ����� �л��� ����Ͻÿ�.
SELECT * FROM STU_SCORE
--WHERE KOR =(SELECT MAX(KOR) FROM STU_SCORE);
WHERE ENG =(SELECT MAX(ENG) FROM STU_SCORE);
WHERE MATH =(SELECT MAX(MATH) FROM STU_SCORE);

--Q .������ �ִ�,�ּ�,����� ����� ����Ͻÿ�.
SELECT * FROM EMPLOYEES
WHERE SALARY=(SELECT MIN(SALARY) FROM EMPLOYEES);
OR SALARY=(SELECT MAX(SALARY) FROM EMPLOYEES);
OR SALARY=(SELECT AVG(SALARY) FROM EMPLOYEES);

--�ִ밪
SELECT EMP_NAME, SALARY FROM EMPLOYEES
WHERE SALARY=(SELECT MAX(SALARY) FROM EMPLOYEES); 

--��հ����� ���� ��� �߿� �ִ밪�� ��� ����Ͻÿ�.
--��հ����� ���� ����� �˻� 
--�˻������ �ִ밪 �˻�
SELECT EMP_NAME FROM EMPLOYEES 
WHERE SALARY = 
(SELECT MAX(SALARY) FROM (
SELECT EMP_NAME, SALARY FROM EMPLOYEES
WHERE SALARY <=(SELECT AVG(SALARY) FROM EMPLOYEES)
ORDER BY SALARY DESC)
);
--���Ʒ� ����.
SELECT EMP_NAME,SALARY FROM EMPLOYEES 
WHERE SALARY = 6400;

--��պ��� ���� �� 107��
--SELECT MAX(SALARY) FROM (���̺�)

--56�� �ִ밪 6400
SELECT MAX(SALARY) FROM (
SELECT EMP_NAME, SALARY FROM EMPLOYEES
WHERE SALARY <=(SELECT AVG(SALARY) FROM EMPLOYEES)
ORDER BY SALARY DESC);

--�����Լ�
--LPAD, RPAD����� ä���
SELECT EMP_NAME,LPAD(EMP_NAME,15,'#') FROM EMPLOYEES;
SELECT EMP_NAME,RPAD(EMP_NAME,20,'@') FROM EMPLOYEES;

--ITEM, RTRIM ������ ���ڸ� �߶󳻰� ���
SELECT EMP_NAME,LTRIM(EMP_NAME,'DO')FROM EMPLOYEES;

--KO20240001
SELECT 'KO20240001',LTRIM('KO20240001','KO2024') FROM DUAL;
SELECT JOB_IDFROM DEP

--Q.JOB_ID FROM EMPLOYEES; ���� JOB_ID �� �α��ڿ� �����ȣ�� �����ؼ� ����Ͻÿ�.

SELECT SUBSTR(JOB_ID,0.2) ||EMPLOYEE_ID FROM EMPLOYEES;

SUBSTR(������,���� ����) EX.SUBSTR('ABCDEFJ")
SELECT EMP_NAME,SUBSTR(EMP_NAME, SUBSTR(EMP_NAME,3,4) FROM EMPLOYEES;

--LENGTH:���ڿ��� ����
SELECT EMP_NAME,LENGTH(EMP_NAME) FROM EMPLOYEES
WHERE LENGTH(EMP_NAME)>15;

--��¥�Լ� +,- ����, ��¥�����ͳ��� ���ϱ�� �ȵ�.
--��¥������+���� ����
SELECT SYSDATE+1 FROM DUAL;
--��¥������-��¥������ ����
SELECT SYSDATE-HIRE_DATE FROM EMPLOYEE;
--��¥������+��¥������ �Ұ���
SELECT SYSDATE+HIRE_DATE FROM EMPLOYEES;

SELECT SYSDATE,TRUNC(SYSDATE,'MONTH'),ROUND(SYSDATE,'MONTH') FROM DUAL;

SELECT ROUND(SYSDATE,'YEAR') FROM DUAL;
--������ �߰�
SELECT ADD_MONTHS(SYSDATE,-2) FROM DUAL;

SELECT CEIL(-4.2), FLOOR(-4.2), MOD(8,3),POWER(2,10) FROM DUAL;

SELECT EMP_NAME||TO_CHAR(HIRE_DATE,'YYYY"��"-MM"��"-DD"��" DAY')FROM EMPLOYEES;

--Q. �����,�ڸ��� 9�ڸ� ����� 0���� ǥ��
--SALARY*1400 �տ� ��ȭǥ�ÿ� ��ǥ�� �־� ����Ͻÿ�.

SELECT SALARY, TO_CHAR(SALARY*1400,'L000,000,000') FROM EMPLOYEES;
--�ڽ��� ���ϰ� �ڽ��� ������ ���Ѵ��� ������ ��¥
--'2010-10-10'
SELECT LAST_DAY('2010-01-01') FROM DUAL;

SELECT TRUNC(TO_DATE('2010-10-10'),'MONTH'),'2010-10-10', LAST_DAY('2010-01-01') FROM DUAL;

SELECT *FROM MEMBER;

DESC MEMBER;

--DDL(DATA DEFINITION LANGUAGE )- COLUMN �߰�
--�÷��߰�, ����
--DDL�� COMMIT,ROLLBACK�� �ȵ�.�ٷ� ����
ALTER TABLE MEMBER ADD GENDER VARCHAR(6) DEFAULT 'FEMALE' NOT NULL;

SELECT *FROM MEMBER;
UPDATE MEMBER SET=GENDER ='MALE';
COMMIT;

ALTER TABLE MEMBER DROP COLUMN PHONE;
DESC MEMBER;

SELECT * FROM MEMBER;

--�÷�����-�÷��̸�����,Ÿ�Ժ���
ALTER TABLE MEMBER RENAME COLUMN NAME TO STU_NAME;
DESC MEMBER;

--Ÿ�Ժ���
ALTER TABLE MEMBER MODIFY(STU_NAME VARCHAR2(50));
--������ �����Ͱ� �����Ϸ��� ũ�⺸�� �������� ����
UPDATE MEMBER SET STU_NAME='1';
--�÷��� Ÿ���� �����Ϸ��� �÷������Ͱ� ������̰ų� NULL�϶� ����
ALTER TABLE MEMBER MODIFY(STU_NAME NUMBER(4));
ALTER TABLE MEMBER MODIFY(STU_NAME VARCHAR2(6));

SELECT STU_NAME FROM MEMBER ;
ALTER TABLE MEMBER MODIFY(STU_NAME NUMBER(100));
DESC MEMBER;
INSERT INTO STU_NAME(MNO,ID,PW,STU_NAME,GENDER) VALUES(4,BBB,'2222',"������",FEMALE);

