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
  user_pos=0
  comp_pos=0
  snakes={
      97:78,
      95:56,
      88:24,
      62:18,
      48:26,
      36:6,
      32:10
  }
  ladders={
      1:38,
      4:14,
      8:30,
      28:76,
      21:42,
      50:67,
      71:92,
      80:99
  }

  while user_pos<100 and comp_pos<100:
    choice=int(input("Enter 1 to throw dice\n"))
    if choice==1:
      user_dice=random.randint(1,6)
      if 100-user_pos<user_dice:
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

      print("dice number is ",user_dice)
      user_pos+=user_dice
      if user_pos in snakes.keys():
        print("Snake bite, dropped from ",user_pos," to ",snakes[user_pos])
        user_pos=snakes[user_pos]
      if user_pos in ladders.keys():
        print("Got ladder from ",user_pos," to ",ladders[user_pos])
        user_pos=ladders[user_pos]
      print("Your current position is ",user_pos)

      comp_dice=random.randint(1,6)
      if 100-comp_pos<comp_dice:
        continue
      comp_pos+=comp_dice
      if comp_pos in snakes.keys():
        comp_pos=snakes[comp_pos]
      if comp_pos in ladders.keys():
        comp_pos=ladders[comp_pos]
      print("Computer is on ",comp_pos)
    
  if user_pos==100:
    print("You Won")
    return True
  else:
    print("You Lost")
    return False


def game3():
  import random
  print("Winning Rules of the Stone paper scissor game as follows: \n"
                  +"Stone vs paper->paper wins \n"
                  + "Stone vs scissor->Stone wins \n"
                  +"paper vs scissor->scissor wins \n")

  user_choice = random.randint(1, 3)
    
  if user_choice==1:
    user_choice_name="Stone"
  elif user_choice==2:
    user_choice_name="paper"
  else:
    user_choice_name="scissor"	

  comp_choice=random.randint(1,3)

  while comp_choice==user_choice:
    comp_choice=random.randint(1,3)

  if comp_choice==1:
    comp_choice_name="Stone"
  elif comp_choice==2:
    comp_choice_name="paper"
  else:
    comp_choice_name="scissor"

  print("User's choice is :",user_choice_name)
  print("computer's choice is :",comp_choice_name)
  print(user_choice_name +" VS "+comp_choice_name)


  if (user_choice==1 and comp_choice==2) or (user_choice==2 and comp_choice==1):
    print("paper wins---",end='')
    result="paper"

  elif (user_choice==1 and comp_choice==3) or (user_choice==3 and comp_choice==1):
    print("Stone wins---",end='')
    result="Stone"

  else:
    print("scissor wins---",end='')
    result="scissor"

  if result==user_choice_name:
    print("You Won---")
    return True
  else:
    print("You Lost---")
    return False


def game4():
  n1=input("Enter your name : ").upper()
  n2=input("Enter second name : ").upper()
  name=n1+n2

  for i in name:
    if name.count(i)!=1:
      name=name.replace(i,"")
  print("FLAMES")
  print("F = Friend \nL = Love \nA = Affection \nM = Marriage \nE = Enemy \nS = Siblings \n\n")
  num=len(name)%6

  rel=""
  if num==1:
    rel+="Friends"
  elif num==2:
    rel+="Love"
  elif num==3:
    rel+="Affection"
  elif num==4:
    rel+="Marriage"
  elif num==5:
    rel+="Enemy"
  elif num==0:
    rel+="Siblings"

  print(rel)



points=500
while points>0:
    choice=int(input("Enter \n1 Play Game\n2 Buy from Cafe\n3 Exit\n"))

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
        menu=int(input("MENU :\n1.Pizza : 70\n2.Burger : 60\n3.Coffee : 50\n"))
        if menu==1:
          if points<70:
            print("You dont have enough money")
          else:
            points=points-70
            print("You bought Pizza , Balance is ",points)
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