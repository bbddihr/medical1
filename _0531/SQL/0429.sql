--drop table member;

--���Ἲ ��������: �������� �ڷᰡ �Էµ��� �ʵ��� �ϱ� ���� ��Ģ
--not null, unique,primary key, foreign key, check
--���̺� ����

create table member(
memNo number(4) not null,
id varchar2(30) primary key,
pw varchar2(30) not null,
name varchar2(30),
gender varchar2(6) check(gender in('����', '����')),
mdate date default sysdate
);

--������ �Է�, ���,����,���� �κ�
insert into member(memNo, id,pw,name,gender,mdate) values (
member_seq.nextval, 'aaa','1111','ȫ�浿','����', sysdate
);




