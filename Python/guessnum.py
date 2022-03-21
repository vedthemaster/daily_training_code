import random

a=random.randint(1,50)
b=int(input("Guess the num: "))

while(a!=b):
  if(a<b):
    print("Too High")
  elif(a>b):
    print("Too Low")
else:
  print("Yo guessed right number")