drop table member;
-- 무결성 제약조건 : 부적합한 자료가 입력되지 않도록 하기 위한 규칙
-- not null, unique, primary key, foreign key, check
-- 테이블 생성
create table member(
memNo number(4) not null,
id varchar2(30) primary key,
pw varchar2(30) not null,
name varchar2(30),
gender varchar2(6) check(gender in('남자','여자')),
mdate date default sysdate
);

-- 데이터 입력,출력,수정,삭제 부분
insert into member (memNo,id,pw,name,gender,mdate) values (
member_seq.nextval,'aaa','1111','홍길동','남자',sysdate
);

insert into member(memNo,id,pw,name,gender) values(
member_seq.nextval,'bbb','1111','유관순','여자'
);

insert into member values(
member_seq.nextval,'ccc','1111','이순신','남자',sysdate
);

select * from member;

--drop table board;

--테이블생성 : 게시판 테이블구조
create table board (
bno number(4) primary key,
id varchar2(30), -- 외래키 등록
btitle varchar2(1000),
bcontent varchar2(4000),
bdate date default sysdate,
bgroup number(4),
bstep number default 0,
bindent number default 0,
bhit number default 1,
bfile varchar2(100) default '',
constraint fk_board_id foreign key(id) -- 외래키(foreign key)의 별칭: fk_id
references member(id)    -- member테이블의 primary key id  
);


insert into board(bno,id,btitle,bcontent,bdate,bgroup,bstep,bindent,bhit,bfile) values (
board_seq.nextval,'aaa','제목입니다.','내용입니다',sysdate,board_seq.currval,0,0,1,''
);

insert into board values (
board_seq.nextval,'bbb','제목입니다2.','내용입니다2',sysdate,board_seq.currval,0,0,1,''
);

insert into board(bno,id,btitle,bcontent,bgroup) values (
board_seq.nextval,'aaa','제목입니다.3','내용입니다3',board_seq.currval
);

-- primary key를 삭제하려면 foreign key 등록되어 있는 데이터를 우선 삭제를 모두해야 함.
-- primary key 삭제되면 모두삭제하는 방법 - on delete cascade, 모두 존재하는 방법 on update cascade

select * from board;

-- 삭제
delete board where bno=3;

commit;
select * from member;
select * from board;

delete member where id='aaa';


-- DECODE 조건문
select emp_name,department_id,
decode(department_id,
10,'총무기획부',
20,'마케팅',
30,'구매/생산부',
40,'인사부'
) as depart_name
from employees
order by department_id asc;

select * from stu_score order by avg desc;
-- 90점-A, 80점-B, 70점-C

select avg,
decode(avg,
90,'A',
80,'B',
70,'C'
) as grade
from stu_score order by avg desc;

select job_id,salary from employees;

-- 월급
-- sh_clerk salary * 15%,  ad_asst *10%,  MK_rep * 5%;
-- decode



















