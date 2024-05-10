--drop table member;

--무결성 제약조건: 부적합한 자료가 입력되지 않도록 하기 위한 규칙
--not null, unique,primary key, foreign key, check
--테이블 생성

create table member(
memNo number(4) not null,
id varchar2(30) primary key,
pw varchar2(30) not null,
name varchar2(30),
gender varchar2(6) check(gender in('남자', '여자')),
mdate date default sysdate
);

--데이터 입력, 출력,수정,삭제 부분
insert into member(memNo, id,pw,name,gender,mdate) values (
member_seq.nextval, 'aaa','1111','홍길동','남자', sysdate
);




