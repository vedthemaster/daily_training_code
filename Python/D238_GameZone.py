def game1():
  import random
  movie=["pqr","surya","bcd","abc"]
  name=random.choice(movie)
  name=name.lower()
  name.replace(" ","")
  print(name)
  n=len(name)
  ans=[]
  for i in range(n):
    ans.append("*")
  print(ans)

  counter=0
  chance=3
  while counter<n and chance>0:
    ch=input("Guess Character :")
    flag=False
    for j in range(n):
      if ch==name[j]:
        ans[j]=ch
        counter=counter+1
        print(ans)
        flag=True
    if(flag==False):
      chance=chance-1
      print("Wrong guessing, chances remaining :",chance)
  if chance<=0:
    print("YOU LOST NOOB")
    return False
  else:
    print("YOU WON")
    return True


def game2():
  import random
  player_pos=0
  comp_pos=0
  snakes={
      97:78,95:56,88:24,62:18,48:26,36:6,32:10
  }
  ladders={
      1:38,4:14,8:30,28:76,21:42,50:67,71:92,80:99
  }

  while player_pos<100 and comp_pos<100:
    choice=int(input("Enter 1 to throw dice\n"))
    if choice==1:
      player_dice=random.randint(1,7)
      if 100-player_pos<player_dice:
        print("Waste move\n")

        comp_dice=random.randint(1,6)
        if 100-comp_pos<comp_dice:
          continue
        comp_pos+=comp_dice
        if comp_pos in snakes.keys():
          comp_pos=snakes[comp_pos]
        if comp_pos in ladders.keys():
          comp_pos=ladders[comp_pos]
        print("Computer is on ",comp_pos)
        continue

      print("dice number is ",player_dice)
      player_pos+=player_dice
      if player_pos in snakes.keys():
        print("Snake bite, dropped from ",player_pos," to ",snakes[player_pos])
        player_pos=snakes[player_pos]
      if player_pos in ladders.keys():
        print("Got ladder from ",player_pos," to ",ladders[player_pos])
        player_pos=ladders[player_pos]
      print("Your current position is ",player_pos)

      comp_dice=random.randint(1,7)
      if 100-comp_pos<comp_dice:
        continue
      comp_pos+=comp_dice
      if comp_pos in snakes.keys():
        comp_pos=snakes[comp_pos]
      if comp_pos in ladders.keys():
        comp_pos=ladders[comp_pos]
      print("Computer is on ",comp_pos)
    
  if player_pos==100:
    print("You Won")
    return True
  else:
    print("You Lost")
    return False


def game3():
  import random
  p1 = 0
  for i in range(3):
      print("1.ROCK\n2.PAPER\n3.SCISSOR")
      c1 = int(input("Select any One:"))
      c2 = random.randint(1, 4) 
      print("Opponent Selected:", c2)
      if (c1 == 1):
          if (c2 == 2):
              print("---You Lose---")
          elif (c2 == 1):
              print("---Draw---")
          else:
              print("---You Win---")
              p1 += 1
      elif (c1 == 2):
          if (c2 == 3):
              print("---You Lose---")
          elif (c2 == 2):
              print("---Draw---")
          else:
              print("---You Win---")
              p1 += 1
      else:
          if (c2 == 1):
              print("---You Lose---")
          elif (c2 == 3):
              print("---Draw---")
          else:
              print("---You Win---")
              p1 += 1
  if (p1 > 1):
      print("\n---YOU WIN---")
      return True
  else:
      print("\n---GAME-OVER---")
      return False

def game4():
  name1=(input("Enter first name:")).lower()
  name2=(input("Enter second name:")).lower()


  name1=name1.replace(" ","")
  name2=name2.replace(" ","")
  print(name1)
  print(name2)

  for i in name1:
    for j in name2:
      if i==j:
        name1=name1.replace(i,"",1)
        name2=name2.replace(i,"",1)
        break
  print


  count=len(name1+name2)
  print(count)

  if(count>0):
    list1=["Friends","lover","Affectionate","Maariage","Enemies","Siblings"]
    while len(list1)>1:
      c=count%len(list1)
      s_index=c-1
      if s_index>+0:
        left=list1[:s_index]
        right=list1[s_index+1:]
        list1=right+left
      else:
        list1=list1[:len(list1)-1]

    print("Relationship is :",list1[0])
  else:
    print("Enter diffrenet name")




points=500
while points>0:
    print("Welcome to Zolter Gaming Zone")
    choice=int(input("Enter \n1. Play Game\n2. Buy from Restaurant\n3. Quit\n"))

    if choice==1:
        if points<30:
            print("You dont have enough money")
        else:
            points=points-30
            game_choice=int(input("Enter \n1 Movie Guess Game\n2 Snake and Ladder\n3 Stone Paper & Scissor\n4 FLAMES\n"))

            if game_choice==1:
              if game1():
                points+=20
            elif game_choice==2:
              if game2():
                points+=20
            elif game_choice==3:
               if game3():
                points+=20
            elif game_choice==4:
              game4()
            else:
              print("Invalid Input")

            print("balance is ",points)
    elif choice==2:
        menu=int(input("MENU :\n1.Pani Puri : 70\n2.Burger : 60\n3.Coffee : 50\n"))
        if menu==1:
          if points<70:
            print("You dont have enough money")
          else:
            points=points-70
            print("You bought Pani Puri , Balance is ",points)
        elif menu==2:
          if points<60:
            print("You dont have enough money")
          else:
            points=points-60
            print("You bought Burger , Balance is ",points)
        elif menu==3:
          if points<50:
            print("You do not have enough money")
          else:
            points=points-50
            print("You bought Coffee , Balance is ",points)
        else:
            print("Invalid")
    elif choice==3:
        break
    else:
        print("Invalid")