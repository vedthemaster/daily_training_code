import sqlite3

con = sqlite3.connect("Demo.db")

crsr = con.cursor()

sql_command = """ create table task(id integer(10) primary key, name nvarchar(10), email nvarchar(30),phoneno nvarchar(13), password navrchar(10)); """

crsr.execute(sql_command)
con.commit()
con.close()
