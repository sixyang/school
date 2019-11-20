数据操纵！

1
    (1). select Sname, bplace from students;
    (2). select tsex, count('sex') from js group by tsex;
    (3). select sno, sname, age from students where age>20&&age<23 order by age;
    (4). select * from (select avg(age) aage from students)a join students on students.age > a.aage; (烦)
    (5). select sname,sno,polity,score from students where score < 60;
    (6). select * from js where dept = '电信';
    (7). select * from js where birthday < '1971-1-1';
    (8). select * from js where dept = '';
2
    (1). insert into students values(10, '尹鸿涛', 22, '男', '1998-1-1', '英语', 100);
    (2). insert into js values('T010', '王子强', '男', '1999-1-1', '英语', '461031197309153855', '镇江');
    (3). create table girls (select * from students where sex='女');
3
    (1). update students set age = age + 1;
    (2). update students set score = score +5 where polity = '电信';
    (3). update students set score = 0 where sno = 10;
4
    (1). delete from js where age > 60;
    (2). select sno from students where sname like '张%'        (👍)

思考与实践：
    (1). select * from ts where tnum >50;
    (2). select sum(tnum) from ts;
    (3). select * from ts order by tnum limit 5;
    (4). select * from ts where Cno = 55;
    (5). select * from students join (select pid from ts where dtime > 1)late on students.id = late.pid;
    (6). select * from ts where name = 'xx';
    (7). create table db (select * from ts where tname like '%数据库%');
    (8). update ts set dtime = now();


完整性约束！

JS
    alter table js modify tno varchar(10) primary key;
    alter table js modify tname varchar(10) not null;
    alter table js modify tsex varchar(4) check(tsex in ('男', '女'));
    alter table js modify birthday date null;
    alter table js modify dept varchar(10) null;
    alter table js modify sid varchar(50) unique;

Course
    alter table course modify cno int primary key;
    alter table course modify cname varchar(10) not null;
    alter table course modify credit unsigned int;
    alter table course modify property default '必修';

SK
    alter table sk add foreign key (tno) references JS(Tno);
    alter table sk modify tno int primary key;
    alter table sk add foreign key (cno) references JS(cno);
    alter table sk modify cno int primary key;    
    alter table sk modify hours unsigned int;
    
