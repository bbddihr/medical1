alter session set "_ORACLE_SCRIPT"=true;
--user �����ϴ� ��ɾ�
create user "ora_user" identified by "1111";

--���Ѻο�
grant connect, resource,dba to "ora_user";