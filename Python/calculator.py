num1= int(input("Enter first number: "))
num2= int(input("Enter second number: "))

Op = int(input("Enter 1 for sum,2 for substration,3 for multiplication,4 for division,5 for modulo: "))

if(Op == 1):
    print(num1+num2)
elif(Op==2):
    print(num1-num2)
elif(Op==3):
    print(num1*num2)
elif(Op==4):
    print(num1/num2)
elif(Op==5):
    print(num1%num2)
else:
    print("Invalid Operation")

