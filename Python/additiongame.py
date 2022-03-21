# addition game

import random

level = 1
chance=3
while(chance>0):
    a = random.randint(10**(level-1),10**(level)-1)
    b = random.randint(10**(level-1),10**(level)-1)
    print("Addition of",a,"and",b,"is: ")
    i=int(input())
    if(a+b==i):
      level=level+1
      chance=31
      print("You reach to level: ",level)
    else:
      chance= chance-1
      continue
print("Game over")

