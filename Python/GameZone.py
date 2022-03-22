import random as ran
point=500


print("---WELCOME IN GAME ZONE---")
while(point>0):
  print("What you whant to do:\n1.Play Game\n2.Buy Snacks")
  c=int(input("Enter Your Choice:"))
  if(c==1):
    point=game(point)
  elif(c==2):
    point=snacks(point)
  else:
    print("Wrong Choice")
  print(point)
  
  
  def game(point):
    point-=30
    print("What you whant to Paly:\n1.Movie Guess\n2.Snake and ladder\n3.Rock-Paper-Scissor\n4.FLAMES")
    ch=int(input("Enter Your Choice:"))
    if(ch==1):
        print("---Movie Guess---")
        point=movie(point)
    elif(ch==2):
        print("---Snake and ladder---")
        point=snakelad()
    elif(ch==3):
        print("---Rock-Paper-Scissor---")
        point=rock()
    elif(ch==4):
        print("---FLAMES---")
        point=flames()
    else:
        print("Wrong Choice")
    return point
  
  def movie(point):
    movie=["akla","bdc","xyzv"]
    m1=list(ran.choice(movie))
    m2=['_']*len(m1)
    print(m2)
    ch=3
    while(m1!=m2 and ch>0):
        c=input("CHAR:")
        t=0
        for i in range(len(m1)):
        if c==m1[i] and m2[i]=='_':
            t=1
            m2[i]=c
        print(m2)
        if t==0:
            ch-=1
        print("CHANCE LEFT",ch)
    if m1!=m2:
        print("---GAME-OVER---")
    else:
        print("---YOU WIN---")
        point+=20
    return point
    
  
  def snakelad(point):
    snake={32:10,36:6,48:26,62:18,88:24,95:56,97:78}
    lad={2:38,4:14,8:30,21:42,28:76,50:67,71:92,80:99}
    i=0
    j=0
    dice=[1,2,3,4,5,6]
    while(i!=100 and j!=100):
        d1=ran.choice(dice)
        print("\nYou Got:",d1)
        if(i+d1<=100):
            i+=d1
        if(i in snake):
            i=snake[i]
        elif(i in lad):
            i=lad[i]
        d2=ran.choice(dice)
        print("Computer Got:",d2)
        if(j+d2<=100):
            j+=d2
        if(j in snake):
            j=snake[j]
        elif(j in lad):
            j=lad[j]
        print("---Position---")
        print("Your position:",i)
        print("Computer position:",j)
    if(i==100):
        point+=20
        print("\n---YOU WIN---")
    else:
        print("\n---GAME OVER---")  
    return point
  
  
  def rock(point):
    p1=0
    for i in range(3):
        print("1.ROCK\n2.PAPER\n3.SCISSOR")
        c1=int(input("Select any One:"))
        c2=ran.randint(1,3)
        print("Opponent Selected:",c2)
        if(c1==1):
            if(c2==2):
                print("---You Lose---")
            elif(c2==1):
                print("---Draw---")
            else:
                print("---You Win---")
            p1+=1
        elif(c1==2):
            if(c2==3):
                print("---You Lose---")
            elif(c2==2):
                print("---Draw---")
            else:
                print("---You Win---")
                p1+=1
        else:
            if(c2==1):
                print("---You Lose---")
            elif(c2==3):
                print("---Draw---")
            else:
                print("---You Win---")
                p1+=1
    if(p1>1):
        print("\n---YOU WIN---")
        point+=20
    else:
        print("\n---GAME-OVER---")
    return point


def flames():
  x=list(input("Name 1:"))
  y=list(input("Name 2:"))
  for i in x:
      if i in y:
        x.remove(i)
        y.remove(i)
  c=len(x)+len(y)
  r = ["Friends", "Love", "Affection", "Marriage", "Enemy", "Siblings"] 
  while len(r) > 1:
    i=(c%len(r)-1)
    if i>=0:
      right=r[i+1:]
      left=r[:i]
      r=right+left
    else:
      r=r[:len(r)-1]
  print(r[0])
  
  
  def snacks(point):
    menu={"burger":50,"pizza":100,"dabeli":30,"sandwitch":50,"bhajiya":20}
    add=1
    bill=0
    order={}
    print(menu)
    while(add==1):
        m=input("Enter your order:")
        c=int(input("Enter quantity:"))
        bill+=(menu[m]*c)
        order[m]=c
        cho=input("You want to continue(Enter 'yes' or 'no'):")
        if(cho=='no'):
            add=0
            out=input("You want to checkout(Enter 'yes' or 'no'):")
            if(out=='yes'):
                print(order)
                print("bill:",bill)
            else:
                add=1
                print("1.edit order\n2.add order\n3.remove order\n4.check-out")
            t=int(input("Enter what u want to do:"))
            if(t==1):
                m=input("Enter your order:")
                bill=(bill-menu[m]*order[m])
                c=int(input("Enter quantity:"))
                bill+=(menu[m]*c)
            elif(t==3):
                m=input("Enter your order:")
                bill=(bill-menu[m]*order[m])
                order.remove(m)
            elif(t==2):
                m=input("Enter your order:")
                c=int(input("Enter quantity:"))
                bill+=(menu[m]*c)
                order[m]=c
            else:
                print(order)
                print("bill:",bill)
                break
    point-=bill
    return point
    