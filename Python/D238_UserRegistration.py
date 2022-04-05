import sqlite3
import re

print("Welcome to our site")
u_input = int(input("1. Register \n2. Log In \n"))

	
def register():
	name=input("Enter your name: ")
	email = input("Enter yout Email: ").lower()
	phone_number = input("Enter your phone number: ")
	password = input("Enter your password: ")


	def v_name(n):
	  pat = re.compile("[a-zA-Z]*")
	  if (pat.match(n)!= None):
	  	return True
	  else:
	  	True

	def v_email(n):
	  pat = re.compile("[A-Za-z0-9]+@gmail.com")
	  if (pat.match(n)!= None):
	  	return True
	  else:
	  	return True

	def v_phonenumber(n):
	  pat = re.compile("\+91?[\d]{11}")
	  if (pat.match(n)!= None):
	  	return True
	  else:
	  	return True
	  

	def v_password(n):
	  pat = re.compile("([A-z])([a-z])([0-9])([@#-])")
	  if (pat.match(n)!= None ):
	  	return True
	  else:
	  	return True
	  	
	name_v = v_name(name)
	email_v = v_email(email)
	pass_v = v_password(password)
	phone_v = v_phonenumber(phone_number)

	lst = [(name,email,password,phone_number)]

	con = sqlite3.connect("Demo.db")

	crsr = con.cursor()

	  	
	if(name_v == True and email_v == True and pass_v == True and phone_v == True):
		
		sql_command = """insert into user (name,email,password,phoneno) values(?,?,?,?);"""
		crsr.executemany(sql_command,lst)
		print("Registration Successful")
		

	con.commit()
	con.close()

	
def login():
	email = input("Enter email address: ").lower()
	password = input("Enter your password : ")
	
	con = sqlite3.connect("Demo.db")

	crsr = con.cursor()
	sql_cmd = "select * from user"
	u_data = crsr.execute(sql_cmd)
	for i in u_data:
		for j in i:
			if(i[2] == email and i[4] == password):
				print("Logged in Successful")
				v_input = int(input("Press 1 for view details \nPress 2 for update details \n"))
				if v_input == 1:
					print (i)
					return 0
				elif v_input == 2:
					n_name = input("Enter new name: ")
					n_email = input("Enter new email: ")
					n_phoneno = input("Enter new phone no: ")
					n_password = input("Enter new password: ")
					c_id = i[0]
					n_list = [(n_name,n_email,n_phoneno,n_password,c_id)]
					
					update_cmd = """UPDATE user 
					SET name = ?, 
					email = ?,
					phoneno = ?,
					password=? 
					WHERE id=?  ;"""
					crsr.executemany(update_cmd,n_list)
					con.commit()
					con.close()
					print("Deatils updated successfully")
					return 0
				
	else:
		print("Invalid Details")
		print("Try Again")
		login()
		
	
if u_input == 1:
	register()
elif u_input == 2:
	login()
else:
	print("Invalid Input")
