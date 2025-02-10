-- use school;
-- drop database school;
-- use scl;
-- drop database scl;
-- create database school;
-- use school;
-- use school;
CREATE TABLE students (
    Id INT AUTO_INCREMENT PRIMARY KEY,
    fname VARCHAR(20),
    lname VARCHAR(20),
    dob DATE,
    gender VARCHAR(1),
    country VARCHAR(50)
);
INSERT INTO students (fname, lname, dob, gender, country)
VALUES ('John', 'Doe', '2000-01-15', 'M', 'USA');
INSERT INTO students (fname, lname, dob, gender, country)
VALUES 
    ('Alice', 'Williams', '1998-02-20', 'F', 'USA'),
    ('David', 'Smith', '1996-12-05', 'M', 'Canada'),
    ('Sophia', 'Johnson', '1999-08-30', 'F', 'Australia');
select *from students;
select fname,
lname from students; 
SELECT fname, lname, dob
FROM students
WHERE gender = 'M';
INSERT INTO students (fname, lname, dob, gender, country)
VALUES 
    ('Jane', 'Smith', '1999-05-22', 'F', 'Canada'),
    ('Emily', 'Johnson', '2001-07-30', 'F', 'UK'),
    ('Michael', 'Brown', '2000-11-12', 'M', 'Australia');
select *
from students 
where country="USA";
 
