alter session set "_ORACLE_SCRIPT"=true;
--user 생성하는 명령어
create user "ora_user" identified by "1111";

--권한부여
grant connect, resource,dba to "ora_user";