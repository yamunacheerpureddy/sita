use clg;
select tname,salary from teachers
order by country asc;
-- select count(*) from teachers where salary >35000;
select sum(salary) from teachers;
select sum(salary) from teachers where country="india";
select sum(salary) as india_sum 
from teachers where country="india";
select avg(salary) from teachers;
select max(salary) from teachers where country="india";
select gender, count(*) as no_of_people from teachers group by gender;

select country, count(country) as no_of_people from teachers  group by  country
order by country asc;

select sum, avg, max, min, count(salary)  
from teachers where salary;
select country, sum(salary) , avg(salary) ,
min(salary) 
from teachers
group by country
order by country;

select tname, country, sum(salary) , avg(salary) ,
min(salary) ,max(salary)
from teachers
group by tname , country
order by tname, country;


