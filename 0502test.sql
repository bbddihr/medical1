--이름검색
select * from stu_score where id like '%a%'
order by no;

--row_number() over()
--11-~20까지 출력하시오.
select * from
(select rownum rnum,a.* from ( select * from stu_score order by total desc ) a)
where rnum>=11 and rnum<=20;

select rownum,a.* from stu_score a
order by no;

select *from( select row_number() over(order by no) rnum,a.* from stu_score a\ 
where id like '%a%')where rnum>=11 and rnum<=20


select count(*) from( select row_number() over(order by no) rnum,a.* from stu_score a\ 
where id like '%a%')where rnum>=11 and rnum<=20

sql=f"select count(*)from( select row_number() over(order by no) rnum,a.* from stu_score a\ 
where id like '%{search}%')"



create table melon(
mno number primary key,
rank number,
v_rank number,
img varchar2(100),
title varchar2(100),
singer varchar(100),
likeNum number
);
alter table melon modify img varchar2(300);

create table yanolja (
yno number primary key,
img varchar2(100),
title varchar2(100),
grade number,
grade_num number,
price number 
);

alter table yanolja modify img varchar2(300);


