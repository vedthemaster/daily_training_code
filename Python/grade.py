name = input("Enter Your Name: ")
marks =int(input("Enter your marks here:"))

if (marks > 95):
    print(name,"Your Grade is A")
elif(marks>=80 and marks <95):
    print(name,"Your Grade is B")
elif(marks>=70 and marks <80):
    print(name,"Your Grade is C")
elif(marks>=50 and marks <70):
    print(name,"Your Grade is D")
elif(marks>=35 and marks <50):
    print(name,"Your Grade is E")
else:
    print("You are fail")
