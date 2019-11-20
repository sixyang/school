1. select * from students order by score limit 0,1;

2. select * from students where sno = 10;

3. insert into students values('11', '王子强', '21', '男', '1999-1-1', Null, 3);

4. select avg(score) from students;

5. select sname, polity, score from students;


-- 存储过程
1.
    delimiter $$
    CREATE PROCEDURE stuscoreinfo()
    BEGIN
        select * from students;
        select * from course;
        select * from score;

    END$$

    delimiter;　
    call stuscoreinfo();
    
2.
    create procedure stupoint(in num int)
    BEGIN       
        select * from students where id = num;
    end $$
    set @num = 2;
    call stupoint(@num);

3.
    create procedure stu_age(in num int)
    BEGIN
        select age from students where id = num;
    end $$
    set @num = 2;
    call stu_age(@num);



-- 自定义函数

1.
    create function fun_avgscores(subject varchar(20))
    returns varchar(300)
    BEGIN
        declare c1 varchar(300);
        select avg(score) into c1 from students group by polity having polity = subject;
        return c1;
    end;;

2.
    create function fun_sumscores(subject varchar(20))
    returns varchar(300)
    BEGIN
        declare c1 varchar(300);
        select sum(score) into c1 from students group by polity having polity = subject;
        return c1;
    end;;

3.
    create function find_student(name varchar(20))
    returns varchar(300)
    BEGIN
        declare c1 varchar(300);
        select count('student') into c1 from students where sname = name;
        return c1;
    end;;
