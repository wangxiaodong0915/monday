CREATE TABLESPACE monday DATAFILE 'D:\app\59290\oradata\monday\monday01.dbf' size 10G;

create user monday identified by monday
default tablespace monday
temporary tablespace TEMP;

grant connect,resource to monday;
grant create any sequence to monday;
grant create any table to monday;
grant delete any table to monday;
grant insert any table to monday;
grant select any table to monday;
grant unlimited tablespace to monday;
grant execute any procedure to monday;
grant update any table to monday;
grant create any view to monday;