import random
passwords = []    #calling all variables
usernames = []
users = [["tward", "noonewillguessthis"], ["thomash", "nice"], ["Kentyboy", "Iamamazing"]]
Dice1 = 0
Dice2 = 0
Dice3 = 0
total1 = 0
total2 = 0
Dice1e = 0
Dice2e = 0
winning_score = 0
save_score = 0
attempts = 0
attempts2 = 0
name1 = ""
name2 = ""
number = 3
attempts = 0
number2 = 2
attempts2 = 0
times2 = -1
allow_in = False
dice_even1 = 0
dice_even2 = 0
Even = True
user_entry = ""
found_Name = 0

#works out if it is odd even or double for player one (function)

def odd_even_double(Dice1, Dice2):
    global total1
    if p1 == True:
        if Dice1 == Dice2:
            print("You rolled a double that means you get to roll again")
            Dice3 = random.randint(1,6)
            print("you rolled a", Dice3)
            total1 = total1 + Dice3
            print(name1 + "’s score is", total1)
        elif (Dice1 + Dice2)% 2 == 0:
            print("You rolled an even number that means 10 is added to your score")
            total1 = total1 + 10
            print(name1 + "’s total is", total1)
        else:
            print("You rolled and odd number 5 is deducted")
            total1 = total1 - 5
            if total1 < 0:
                total1 = 0
            print(name1 + "’s score is", total1)
    else:        
        global total2
        if Dice1 == Dice2:
            print("You rolled a double that means you get to roll again")
            Dice3 = random.randint(1,6)
            print("you rolled a", Dice3)
            total2 = total2 + Dice3
            print(name2 + "’s score is", total2)
        elif (Dice1 + Dice2)% 2 == 0:
            print("You rolled an even number” that means 10 is added to your score")
            total2 = total2 + 10
            print(name2 + "’s total is", total2)
        else:
            print("you rolled and odd number 5 is deducted")
            total2 = total2 - 5
            if total2 < 0:
                total2 = 0
            print(name2 + "’s score is", total2)

        #follows the procedures if the scores are even (function)

def even(dice_even1, dice_even2):
    global Even
    global winning_score
    print("the scores are even, you must each roll a dice to see who is the winner")
    while Even == True:
        dice_even1 = random.randint(1,6)
        dice_even2 = random.randint(1,6)
        input(name1 + " press enter to roll")
        print(dice_even1)
        dice_even2 = random.randint(1,6)
        input(name2 + " press enter to roll")
        print(dice_even2)
        if dice_even1 > dice_even2:
            print(name1 + " wins")
            winning_score = winning_score + total1 + dice_even1
            Even = False
        elif dice_even2 > dice_even1:
            print(name2 + " wins")
            winning_score = winning_score + total1 + dice_even1
            Even = False
        else:
            Even = True

#password login for p1

while user_entry == "":
    user_entry = input("Player1 please enter your user name")
    user_len = len(users)
    for i in range(0, user_len):
        if user_entry == users[i][0]:
            found_Name = 1
            name1 = user_entry
            while attempts < 3 and allow_in == False:
                number = number -1
                password_entry = input("Please enter your password")
                if password_entry == users[i][1]:
                    print("Username and password are correct, you may play the game")
                    allow_in = True
                else:
                    print("Sorry, the password is incorrect")
                    print("attempts remaining", number)
                    attempts = attempts + 1
                    if attempts == 3:
                        print("You have run out of attempts sorry")

    if found_Name == 0:
        print("User name not recognised")
        user_entry = ""
print("Details correct you can play")

#Password login for p2

number = 2
attempts = 0
number2 = 2
attempts2 = 0
allow_in = False

user_entry = ""
found_Name = 0
while user_entry == "":
    user_entry = input("Player2 please enter your user name")
    user_len = len(users)
    for i in range(0, user_len):
        if user_entry == users[i][0]:
            found_Name = 1
            name2 = user_entry
            while attempts < 3 and allow_in == False:
                number = number -1
                password_entry = input("Please enter your password")
                if password_entry == users[i][1]:
                    print("Username and password are correct, you may play the game")
                    allow_in = True
                else:
                    print("Sorry, the password is incorrect")
                    print("attempts remaining", number)
                    attempts = attempts + 1
                    if attempts == 3:
                        print("You have run out of attempts sorry")

    if found_Name == 0:
        print("User name not recognised")
        user_entry = ""
print("Details correct you can play")

#main part of the game

print("The game is simple, 2 players take turns to roll two dice each, if an even number is rolled when the two die are added up 10 is added to the players score, if odd 5 is subtracted, if you roll a double you get to roll again. This continues for 5 rounds")
for i in range(0,5):
    p1 = True
    input(name1 + " press enter to roll")
    print("")
    Dice1 =  random.randint(1,6)
    Dice2 = random.randint(1,6)
    print("your two die are", Dice1,"and",Dice2)
    print("")
    total1 = total1 + (Dice1 + Dice2)
    odd_even_double(Dice1, Dice2)
    Dice1 = 0
    Dice2 = 0
    p1 = False
    split = input(name2 + " press enter to roll")
    print("")
    Dice1 =  random.randint(1,6)
    Dice2 = random.randint(1,6)
    print("your two die are", Dice1,"and",Dice2)
    print("")
    total2 = total2 + (Dice1 + Dice2)
    odd_even_double(Dice1, Dice2)
    print(name1 + "'s score is", total1)
   
if total1 > total2:
    print(name1 + " is the winner")
    winning_score = winning_score + total1
elif total2 > total1:
    print(name2 + " is the winner")
    winning_score = winning_score + total2
else:
    even(dice_even1, dice_even2)

#adds winning score to list

save_name = input("Please enter the name you want on the leader board").title()
save_score = winning_score
text_file = open("highscores.txt", "a")
text_file.write(str(save_score) + ' ' + save_name + "\n")
text_file.close()
print ("\n")
text_file = open("highscores.txt", "r")
whole_thing = text_file.read().splitlines()

#prints out top 5

temp = 0
n = len(whole_thing)

#bubble sort

counter = 0
swapped  = True
while swapped == True:
    swapped = False
    for x in range(1,n):
        if whole_thing[x-1] > whole_thing[x]:
            temp = whole_thing[x-1]
            whole_thing[x-1] = whole_thing[x]
            whole_thing[x] = temp
            swapped = True

c = len(whole_thing) - 1
s = 1
print("These are the top 5 highest scores")
for z in range(0,5):
    print(s,"-", whole_thing[c])
    c = c - 1
    s = s + 1
text_file.close()
