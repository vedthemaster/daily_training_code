import sqlite3

con = sqlite3.connect("Demo.db")

crsr = con.cursor()
#sql_command = "insert into student(id,name,marks)values (1,'nikita',85);"
#sql_command = "update student set marks=95 where id=1;"
#sql_command = "select * from student;"
#sql_command = "update student set name='Ved' where id=1;"

sql_command = """ create table std(id integer(10) primary key, name varchar(10));
insert into std(id,name) values (2,'Ved');
insert into std(id,name) values (3,'Keyur');

"""

crsr.executescript(sql_command)
#d= crsr.fetchall()
#print (d)
con.commit()
con.close()
