import random 


def game1():
    import random
    movie = ["krish", "run", "mahan"]
    name = random.choice(movie)
    print(name)
    n = len(name)
    ans = []
    for i in range(n):
        ans.append("*")
    print(ans)

    counter = 0
    chance = 3
    while counter < n and chance > 0:
        ch = input("Guess Character :")
        ch = ch.lower()
        flag = False
        for j in range(n):
            if ch == name[j]:
                ans[j] = ch
                counter = counter + 1
                print(ans)
                flag = True
        if(flag == False):
            chance = chance - 1
            print("You guessed Wrong, remaining chances :", chance)
    if chance <= 0:
        print("YOU LOST ")
        return False
    else:
        print("YOU WON")
        return True


def game2():
    import random
    user_pos = 0
    comp_pos = 0
    snakes = {
        97: 78,
        95: 56,
        88: 24,
        62: 18,
        48: 26,
        36: 6,
        32: 10
    }
    ladders = {
        1: 38,
        4: 14,
        8: 30,
        28: 76,
        21: 42,
        50: 67,
        71: 92,
        80: 99
    }

    while user_pos < 100 and comp_pos < 100:
        choice = int(input("Enter 1 to throw dice\n"))
        if choice == 1:
            user_dice = random.randint(1, 6)
            if 100 - user_pos < user_dice:
                print("Waste move\n")

                comp_dice = random.randint(1, 6)
                if 100 - comp_pos < comp_dice:
                    continue
                comp_pos += comp_dice
                if comp_pos in snakes.keys():
                    comp_pos = snakes[comp_pos]
                if comp_pos in ladders.keys():
                    comp_pos = ladders[comp_pos]
                print("Computer is on ", comp_pos)
                continue

            print("dice number is ", user_dice)
            user_pos += user_dice
            if user_pos in snakes.keys():
                print("Snake bite, dropped from ", user_pos, " to ", snakes[user_pos])
                user_pos = snakes[user_pos]
            if user_pos in ladders.keys():
                print("Got ladder from ", user_pos, " to ", ladders[user_pos])
                user_pos = ladders[user_pos]
            print("Your current position is ", user_pos)

            comp_dice = random.randint(1, 6)
            if 100 - comp_pos < comp_dice:
                continue
            comp_pos += comp_dice
            if comp_pos in snakes.keys():
                print("Snake bite, dropped from ", comp_pos, " to ", snakes[comp_pos])
                comp_pos = snakes[comp_pos]
            if comp_pos in ladders.keys():
                print("Got ladder from ", comp_pos, " to ", ladders[comp_pos])
                comp_pos = ladders[comp_pos]
            print("Computer is on ", comp_pos)

    if user_pos == 100:
        print("User Won")
        return True
    else:
        print("User Lost")
        return False


def game3():
    import random
    p1 = 0
    for i in range(3):
        print("1.ROCK\n2.PAPER\n3.SCISSOR")
        c1 = int(input("Select any One:"))
        c2 = random.randint(1, 3)
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
    n1 = input("Enter your name : ").upper()
    n2 = input("Enter second name : ").upper()
    name = n1 + n2

    for i in name:
        if name.count(i) != 1:
            name = name.replace(i, "")
    print("FLAMES")
    print("F = Friend \nL = Love \nA = Affection \nM = Marriage \nE = Enemy \nS = Siblings \n\n")
    num = len(name) % 6

    rel = ""
    if num == 1:
        rel += "Friends"
    elif num == 2:
        rel += "Love"
    elif num == 3:
        rel += "Affection"
    elif num == 4:
        rel += "Marriage"
    elif num == 5:
        rel += "Enemy"
    elif num == 0:
        rel += "Siblings"

    print(rel)


points = 500
while points > 0:
    choice = int(input("Enter \n1 Play Game\n2 Buy from Cafe\n3 Exit\n"))

    if choice == 1:
        if points < 30:
            print("You dont have enough money")
        else:
            points = points - 30
            game_choice = int(
                input("Enter \n1 Movie Guess Game\n2 Snake and Ladder\n3 Rock Paper & Scissor\n4 FLAMES\n"))

            if game_choice == 1:
                if game1():
                    points += 50
            elif game_choice == 2:
                if game2():
                    points += 50
            elif game_choice == 3:
                if game3():
                    points += 50
            elif game_choice == 4:
                game4()
            else:
                print("Invalid Input")

            print("balance is ", points)
    elif choice == 2:
        menu = int(input("MENU :\n1.Pizza : 70\n2.Burger : 60\n3.Coffee : 50\n"))
        if menu == 1:
            if points < 70:
                print("You dont have enough money")
            else:
                points = points - 70
                print("You bought Pizza , Balance is ", points)
        elif menu == 2:
            if points < 60:
                print("You dont have enough money")
            else:
                points = points - 60
                print("You bought Burger , Balance is ", points)
        elif menu == 3:
            if points < 50:
                print("You dont have enough money")
            else:
                points = points - 50
                print("You bought Coffee , Balance is ", points)
        else:
            print("Invalid Input")
    elif choice == 3:
        break
    else:
        print("Invalid Input")