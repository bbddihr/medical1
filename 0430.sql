drop table member;
-- ���Ἲ �������� : �������� �ڷᰡ �Էµ��� �ʵ��� �ϱ� ���� ��Ģ
-- not null, unique, primary key, foreign key, check
-- ���̺� ����
create table member(
memNo number(4) not null,
id varchar2(30) primary key,
pw varchar2(30) not null,
name varchar2(30),
gender varchar2(6) check(gender in('����','����')),
mdate date default sysdate
);

-- ������ �Է�,���,����,���� �κ�
insert into member (memNo,id,pw,name,gender,mdate) values (
member_seq.nextval,'aaa','1111','ȫ�浿','����',sysdate
);

insert into member(memNo,id,pw,name,gender) values(
member_seq.nextval,'bbb','1111','������','����'
);

insert into member values(
member_seq.nextval,'ccc','1111','�̼���','����',sysdate
);

select * from member;

--drop table board;

--���̺���� : �Խ��� ���̺���
create table board (
bno number(4) primary key,
id varchar2(30), -- �ܷ�Ű ���
btitle varchar2(1000),
bcontent varchar2(4000),
bdate date default sysdate,
bgroup number(4),
bstep number default 0,
bindent number default 0,
bhit number default 1,
bfile varchar2(100) default '',
constraint fk_board_id foreign key(id) -- �ܷ�Ű(foreign key)�� ��Ī: fk_id
references member(id)    -- member���̺��� primary key id  
);


insert into board(bno,id,btitle,bcontent,bdate,bgroup,bstep,bindent,bhit,bfile) values (
board_seq.nextval,'aaa','�����Դϴ�.','�����Դϴ�',sysdate,board_seq.currval,0,0,1,''
);

insert into board values (
board_seq.nextval,'bbb','�����Դϴ�2.','�����Դϴ�2',sysdate,board_seq.currval,0,0,1,''
);

insert into board(bno,id,btitle,bcontent,bgroup) values (
board_seq.nextval,'aaa','�����Դϴ�.3','�����Դϴ�3',board_seq.currval
);

-- primary key�� �����Ϸ��� foreign key ��ϵǾ� �ִ� �����͸� �켱 ������ ����ؾ� ��.
-- primary key �����Ǹ� ��λ����ϴ� ��� - on delete cascade, ��� �����ϴ� ��� on update cascade

select * from board;

-- ����
delete board where bno=3;

commit;
select * from member;
select * from board;

delete member where id='aaa';


-- DECODE ���ǹ�
select emp_name,department_id,
decode(department_id,
10,'�ѹ���ȹ��',
20,'������',
30,'����/�����',
40,'�λ��'
) as depart_name
from employees
order by department_id asc;

select * from stu_score order by avg desc;
-- 90��-A, 80��-B, 70��-C

select avg,
decode(avg,
90,'A',
80,'B',
70,'C'
) as grade
from stu_score order by avg desc;

select job_id,salary from employees;

-- ����
-- sh_clerk salary * 15%,  ad_asst *10%,  MK_rep * 5%;
-- decode



















