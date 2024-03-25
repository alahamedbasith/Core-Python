create database python_db;
use python_db;
create table users(
ID integer auto_increment primary key,
NAME varchar(50),
AGE integer,
CITY varchar(50)

);

select *from users;

insert into users(NAME,AGE,CITY) values("Ahamed",34,"Tenkasi")