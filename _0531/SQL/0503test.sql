--[ ����Ŭ ���� ]
--[ 1 ] �������(Employees) ���̺��� �����ȣ, �̸�, �޿�, ����, �Ի���, ����� �����ȣ�� ����Ͻÿ�.
--�̶� �̸��� �̸��� ������ �����Ͽ� Name�̶�� ��Ī���� ����Ͻÿ�(107��).
--[ 2 ] �������(Employees) ���̺��� ����� �̸��� ���� Name, ������ Job, �޿��� Salary, ������ $100 ���ʽ��� �߰��Ͽ� ����� ���� Increase Ann_Salary, �޿��� $100 ���ʽ��� �߰��Ͽ� ����� ������ Increase Salary��� ��Ī�� �ٿ� ����Ͻÿ�(107��).
--[ 3 ] H R �μ����� ���� �� ������ �޿� ���� ������ �ۼ��Ϸ��� �Ѵ�. �������(Employees) ���̺��� �޿��� $7,000~$10,000 ���� �̿��� ����� �̸��� ��(Name���� ��Ī) �� �޿��� �޿��� ���� ������ ����Ͻÿ�(75��).
--[ 4 ] ����� ��(last_name) �߿� ��e�� �� ��o�� ���ڰ� ���Ե� ����� ����Ͻÿ�. �̶� �Ӹ����� ��e or o Name���̶�� ����Ͻÿ�(8��).
--[ 5 ] �̹� �б⿡ 60�� IT �μ������� �ű� ���α׷��� �����ϰ� �����Ͽ� ȸ�翡 �����Ͽ���. �̿� �ش� �μ��� ��� �޿��� 12.3% �λ��ϱ�� �Ͽ���. 60�� IT �μ� ����� �޿��� 12.3% �λ��Ͽ� ������(�ݿø�) ǥ���ϴ� ������ �ۼ��Ͻÿ�. ������ �����ȣ, ���� �̸�(Name���� ��Ī), �޿�, �λ�� �޿�(Increase Salary�� ��Ī)������ ����Ͻÿ�(5��).
--[ 6 ] ��� ����� ������ ǥ���ϴ� ������ �ۼ��Ϸ��� �Ѵ�. ������ ����� �̸��� ��(Name���� ��Ī), �޿�, ���翩�ο� ���� ������ �����Ͽ� ����Ͻÿ�. ���翩�δ� ������ ������ ��Salary + Commission��, ������ ������ ��Salary only����� ǥ���ϰ�, ��Ī�� ������ ���̽ÿ�. ���� ��� �� ������ ���� ������ �����Ͻÿ�(107��).
--[ 7 ] �� ����� �Ҽӵ� �μ����� �޿� �հ�, �޿� ���, �޿� �ִ�, �޿� �ּڰ��� �����ϰ��� �Ѵ�. ���� ��°��� ���� �ڸ��� �� �ڸ� ���б�ȣ, $ ǥ�ÿ� �Բ� �Ʒ��� ���� ����Ͻÿ�. ��, �μ��� �Ҽӵ��� ���� ����� ���� ������ �����ϰ�, ��� �� �Ӹ����� ���� �׸�ó�� ��Ī(alias) ó���Ͻÿ�(11��).
--[ 8 ] ������� ������ ��ü �޿� ����� $10,000���� ū ��츦 ��ȸ�Ͽ� ������ �޿� ����� ����Ͻÿ�. �� ������ ���(CLERK)�� ���Ե� ���� �����ϰ� ��ü �޿� ����� ���� ������� ����Ͻÿ�(7��).
--[ 9 ] �� ����� ���� ������ ���踦 �̿��Ͽ� ������ ���� ������ ������ �ۼ��ϰ��� �Ѵ�.
--(��) ȫ�浿�� ��տ��� �����Ѵ� �� Eleni Zlotkey report to Steven King
--� ����� �������� �����ϴ��� �� ���� �����Ͽ� ����Ͻÿ�. ��, ������ ��簡 ���� ����� �ִٸ� �� ������ �����Ͽ� ����ϰ�, ����� �̸��� ���� �빮�ڷ� ����Ͻÿ�(107��).
--[ 10 ] Employees, Departments ���̺��� ������ �ľ��� �� ��� ���� �ټ� �� �̻��� �μ��� �μ��̸��� ��� ���� ����Ͻÿ�. �̶� ��� ���� ���� ������ �����Ͻÿ�(5��).


--[ 1] ������� (Employees)���̺���
--�����ȣ,�̸�,�޿�,�μ�,�Ի���,����� �����ȣ�� ����Ͻÿ�.
--�̶� �̸��� �̸��� ������ �����Ͽ� Name�̶�� ��Ī���� ����Ͻÿ�(107��).

SELECT EMPLOYEE_ID, EMP_NAME Name,SALARY,DEPARTMENT_ID, HIRE_DATE,MANAGER_ID FROM EMPLOYEES;

SELECT EMPLOYEE_ID, EMP_NAME||'/'||JOB_ID AS NAME, SALARY,DEPARTMENT_ID,HIRE_DATE,MANAGER_ID
FROM EMPLOYEES;

--[2] ������� (employees) ���̺��� ����� �̸��� ���� Name, ������ Job, �޿��� Salary, ������ $100 ���ʽ��� �߰��Ͽ�
--����� ���� Increase Ann_salary,
--�޿��� $ 10���ʽ��� �߰��Ͽ� ����� ������ Increase Salary ��� ��Ī�� �ٿ� ����Ͻÿ�(107��).
SELECT EMPLOYEE_ID, EMP_NAME Name, JOB_ID Job, SALARY, (SALARY*12+100) Increase_Ann_salary,
(SALARY+10) Increase_Salary FROM EMPLOYEES;

--[ 3 ] H R �μ����� ���� �� ������ �޿� ���� ������ �ۼ��Ϸ��� �Ѵ�. 
--�������(Employees) ���̺��� �޿��� $7,000~$10,000 ���� �̿��� ����� �̸��� ��(Name���� ��Ī) �� �޿��� �޿��� ���� ������ ����Ͻÿ�(75��).
SELECT EMP_NAME Name,SALARY FROM EMPLOYEES 
WHERE SALARY>=7000 AND SALARY<=10000   --7000�� 10000����
--WHERE SALARY<7000 OR SALARY >10000               ���� �̿�
ORDER BY SALARY;

--NOT�� ��� �ݴ���
--WHERE SALARY BETWEEN 7000 AND 10000
--WHERE SALARY NOT BETWEEN 7000 AND 10000


--[ 4 ] ����� ��(EMP_name) �߿� ��e�� �� ��o�� ���ڰ� ���Ե� ����� ����Ͻÿ�. �̶� �Ӹ����� ��e or o Name���̶�� ����Ͻÿ�(8��).
SELECT SUBSTR(EMP_NAME,-1,) AS e_or_o_Name FROM EMPLOYEES;
WHERE e_or_o_Name LIKE '%E%' OR e_or_o_Name LIKE '%O%';

SELECT EMP_NAME FROM EMPLOYEES
ORDER BY EMP_NAME;

SELECT EMP_NAME FROM EMPLOYEES
WHERE LOWER(EMP_NAME) LIKE '%o%' OR LOWER(EMP_NAME) LIKE '%e%'
ORDER BY EMP_NAME;

--[ 5 ] �̹� �б⿡ 60�� IT �μ������� �ű� ���α׷��� �����ϰ� �����Ͽ� ȸ�翡 �����Ͽ���. 
--�̿� �ش� �μ��� ��� �޿��� 12.3% �λ��ϱ�� �Ͽ���. 60�� IT �μ� ����� �޿��� 12.3% �λ��Ͽ� ������(�ݿø�) ǥ���ϴ� ������ �ۼ��Ͻÿ�.
--������ �����ȣ, ���� �̸�(Name���� ��Ī), �޿�, �λ�� �޿�(Increase Salary�� ��Ī)������ ����Ͻÿ�(5��).

SELECT DEPARTMENT_ID, EMPLOYEE_ID, EMP_NAME AS Name, DEPARTMENT_ID, SALARY, ROUND(SALARY+(SALARY*0.123)) AS Increase_Salary FROM EMPLOYEES
WHERE DEPARTMENT_ID=60;

--[ 6 ] ��� ����� ������ ǥ���ϴ� ������ �ۼ��Ϸ��� �Ѵ�. ������ ����� �̸��� ��(Name���� ��Ī), �޿�, ���翩�ο� ���� ������ �����Ͽ� ����Ͻÿ�. 
--���翩�δ� ������ ������ ��Salary + Commission��, ������ ������ ��Salary only����� ǥ���ϰ�, ��Ī�� ������ ���̽ÿ�. ���� ��� �� ������ ���� ������ �����Ͻÿ�(107��).

SELECT EMP_NAME AS Name, SALARY, COMMISSION_PCT FROM EMPLOYEES;
SELECT EMP_NAME AS Name, SALARY, NVL2(COMMISSION_PCT,'Salary + Commission','SALARY ONLY')AS COMMISSION_PCT FROM EMPLOYEES
ORDER BY SALARY;
--CASE
SELECT EMP_NAME,SALARY,SALARY+SALARY*NVL(COMMISSION_PCT,0) AS COMM_SALARY,COMMISSION_PCT,
CASE WHEN COMMISSION_PCT IS NULL THEN 'SALARY ONLY'
WHEN COMMISSION_PCT IS NOT NULL THEN 'SALARY+COMMISSION'
END AS "COMMISSION_ISNULL"
FROM EMPLOYEES
ORDER BY SALARY DESC;
--DECODE ��õ.������ ���� NVL2����
DECODE(COMMISSION_PCT,NULL,'SALARY ONLY','SALARY+COMMISSION')
DECODE(DEPARTMENT_ID,
'3000','A',
'4000','B',
'5000','C') AS DEPT
FROM EMPLOYEES
ORDER BY SALARY DESC
;
--[ 7 ] �� ����� �Ҽӵ� �μ����� �޿� �հ�, �޿� ���, �޿� �ִ�, �޿� �ּڰ��� �����ϰ��� �Ѵ�. 
--���� ��°��� ���� �ڸ��� �� �ڸ� ���б�ȣ, $ ǥ�ÿ� �Բ� �Ʒ��� ���� ����Ͻÿ�. 
--��, �μ��� �Ҽӵ��� ���� ����� ���� ������ �����ϰ�, ��� �� �Ӹ����� ���� �׸�ó�� ��Ī(alias) ó���Ͻÿ�(11��).



select department_id,
to_char(sum(salary),'$000,999,999') sum_sal,
to_char(round(avg(salary),2),'$000,999,999') avg_sal,
to_char(max(salary),'$000,999,999') max_sal,
to_char(min(salary),'$000,999,999') min_sal
from employees
group by department_id
;

--[ 8 ] ������� ������ ��ü �޿� ����� $10,000���� ū ��츦 ��ȸ�Ͽ� ������ �޿� ����� ����Ͻÿ�. 
--�� ������ ���(CLERK)�� ���Ե� ���� �����ϰ� ��ü �޿� ����� ���� ������� ����Ͻÿ�(7��).
SELECT EMP_NAME, JOB_ID, SALARY FROM EMPLOYEES
WHERE SALARY >(SELECT AVG(SALARY) FROM EMPLOYEES)
ORDER BY SALARY DESC;

--[ 9 ] �� ����� ���� ������ ���踦 �̿��Ͽ� ������ ���� ������ ������ �ۼ��ϰ��� �Ѵ�.
--(��) ȫ�浿�� ��տ��� �����Ѵ� �� Eleni Zlotkey report to Steven King
--� ����� �������� �����ϴ��� �� ���� �����Ͽ� ����Ͻÿ�. 
--��, ������ ��簡 ���� ����� �ִٸ� �� ������ �����Ͽ� ����ϰ�, ����� �̸��� ���� �빮�ڷ� ����Ͻÿ�(107��).
select a.employee_id,a.emp_name,a.manager_id, b.emp_name
from employee a, employee b
where a.manager_id=b.employee_id(+);

--[ 10 ] Employees, Departments ���̺��� ������ �ľ��� �� 
--��� ���� �ټ� �� �̻��� �μ��� �μ��̸��� ��� ���� ����Ͻÿ�. 
--�̶� ��� ���� ���� ������ �����Ͻÿ�(5��).
--1. �μ���ȣ, �����
--2. ����� >=5
--3. ������� ����
SELECT DEPARTMENT_ID, COUNT(department_id)
from employees
group by department_id
having count(department_id) >=5
order by count(department_id) desc;

-- [ �߰� ] HR �μ��� � ����� �޿������� ��ȸ�ϴ� ������ �ð� �ִ�.
-- Tucker�� ���Ե� ������� �޿��� ���� �ް� �ִ� ����� �̸�, ����, �޿��� ����Ͻÿ�(15��).

select salary from employees
where emp_name like '%Tucker%'
;

--��ü��� �����̻��� ����� ���� ���
select salary from employees
where salary>(select avg(salary) from employees)
order by salary desc
;

-- [ �߰� ] ��� ����� �ҼӺμ� ��տ����� ����Ͽ� ������� �̸�, ����,
-- �޿�, �μ���ȣ, �μ���տ���(Department Avg Salary�� ��Ī)�� ����Ͻÿ�(107��).

select avg(salary) from employees;

select emp_name, job_id, salary, department_id,
(select round(avg(salary),2)from employees a 
where department_id=e.department_id) 
from employees e;

--join
select a.emp_name, a.job_id, a.salary, a.department_id
from employees a, 
select department_id, round(avg(salary),2)from employees group by department_id) b 
where a.department_id=b.department_id;

select emp_name from (select *from employees where salary >=(select avg(salary) from employees))
where emp_name like '%a%';



--equi join
select salary, a.department_id,department_name
from employees a, departments b
where a.department_id=b.department_id;

select department_id, round(avg(salary),2) as Department_Avg_Salary from employees
group by department_id;







create table daum_movie(
DNO_SEQ.nextval,
title varchar2(100),
img varchar2(100),
audience number(10),
ddate date
);


select * from daum_movie;

