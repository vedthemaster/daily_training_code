import sqlite3
import re


name=input("Enter your name: ")
email = input("Enter yout Email: ")
phone_number = input("Enter your phone number: ")
password = input("Enter your password")


def v_name(n):
  pat = re.compile("[a-zA-Z]*")
  if (pat.match(n)!= None):
    return n
  else:
    print("Enter name correctly")

def v_email(n):
  pat = re.compile("[A-Za-z0-9]+@gmail.com")
  if (pat.match(n)!= None):
    return n
  else:
    print("Enter email correctly")

def v_phonenumber(n):
  pat = re.compile("\+91?[\d]{11}")
  if (pat.match(n)!= None):
    return n
  else:
    print("Enter phone number correctly")

def v_password(n):
  pat = re.compile("([A-z])([a-z])([0-9])([@#-])")
  if (pat.match(n)!= None ):
    return n
  else:
    print("Enter password correctly")
    

sql_command = """ insert into """

con = sqlite3.connect("Demo.db")

crsr = con.cursor() 
