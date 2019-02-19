
passwords = []    #calling all variables
usernames = []
Dice1 = 0
Dice2 = 0
Dice3 = 0
total1 = 0
total2 = 0
Dice1e = 0
Dice2e = 0
winningScore = 0
saveScore = 0
import random
number = 2
attempts = 0
number2 = 2
attempts2 = 0
times = -1
times2 = -1
name1 = ""
name2 = ""
#works out if it is odd even or double for player one (function)
def oddEvenDouble1(Dice1, Dice2):
    global total1
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

#works out if it is odd even or double for player two (function)
def oddEvenDouble2(Dice1, Dice2):
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
Even = True
diceEven1 = 0
diceEven2 = 0

def even(diceEven1, diceEven2):
    global Even
    global winningScore
    print("the scores are even, you must each roll a dice to see who is the winner")
    while Even == True:
        diceEven1 = random.randint(1,6)
        input(name1 + " press enter to roll")
        print(diceEven1)
        diceEven2 = random.randint(1,6)
        input(name2 + " press enter to roll")
        print(diceEven2)
        if diceEven1 > diceEven2:
            print(name1 + " wins")
            winningScore = winningScore + total1 + diceEven1
            Even = False
        elif diceEven2 > diceEven1:
            print(name2 + " wins")
            winningScore = winningScore + total1 + diceEven1
            Even = False
        else:
            Even = True

#password entry for player1

users = [["tward", "noonewillguessthis"], ["thomash", "nice"], ["Kentyboy", "Iamamazing"]]


number = 3
attempts = 0
number2 = 2
attempts2 = 0
times2 = -1
allowIn = False

#password login for p1

userEntry = ""
found_Name = 0
while userEntry == "":
    userEntry = input("Player1 please enter your user name")
    userLen = len(users)
    for i in range(0, userLen):
        if userEntry == users[i][0]:
            found_Name = 1
            name1 = userEntry
            while attempts < 3 and allowIn == False:
                number = number -1
                passwordEntry = input("Please enter your password")
                if passwordEntry == users[i][1]:
                    print("Username and password are correct, you may play the game")
                    allowIn = True
                else:
                    print("Sorry, the password is incorrect")
                    print("attempts remaining", number)
                    attempts = attempts + 1
                    if attempts == 3:
                        print("You have run out of attempts sorry")

    if found_Name == 0:
        print("User name not recognised")
        userEntry = ""
print("Details correct you can play")
#Password login for p2
number = 2
attempts = 0
number2 = 2
attempts2 = 0
times = -1
times2 = -1
allowIn = False

userEntry = ""
found_Name = 0
while userEntry == "":
    userEntry = input("Player2 please enter your user name")
    userLen = len(users)
    for i in range(0, userLen):
        if userEntry == users[i][0]:
            found_Name = 1
            name2 = userEntry
            while attempts < 3 and allowIn == False:
                number = number -1
                passwordEntry = input("Please enter your password")
                if passwordEntry == users[i][1]:
                    print("Username and password are correct, you may play the game")
                    allowIn = True
                else:
                    print("Sorry, the password is incorrect")
                    print("attempts remaining", number)
                    attempts = attempts + 1
                    if attempts == 3:
                        print("You have run out of attempts sorry")

    if found_Name == 0:
        print("User name not recognised")
        userEntry = ""
print("Details correct you can play")

#main part of the game

print("The game is simple, 2 players take turns to roll two dice each, if an even number is rolled when the two die are added up 10 is added to the players score, if odd 5 is subtracted, if you roll a double you get to roll again. This continues for 5 rounds")
for i in range(0,5):
    input(name1 + " press enter to roll")
    print("")
    Dice1 =  random.randint(1,6)
    Dice2 = random.randint(1,6)
    print("your two die are", Dice1,"and",Dice2)
    print("")
    total1 = total1 + (Dice1 + Dice2)
    oddEvenDouble1(Dice1, Dice2)
    Dice1 = 0
    Dice2 = 0
    split = input(name2 + " press enter to roll")
    print("")
    Dice1 =  random.randint(1,6)
    Dice2 = random.randint(1,6)
    print("your two die are", Dice1,"and",Dice2)
    print("")
    total2 = total2 + (Dice1 + Dice2)
    oddEvenDouble2(Dice1, Dice2)
    print(name2 + "'s score is", total1)
   
if total1 > total2:
    print(name1 + " is the winner")
    winningScore = winningScore + total1
elif total2 > total1:
    print(name2 + " is the winner")
    winningScore = winningScore + total2
else:
    even(diceEven1, diceEven2)

#adds winning score to list

saveName = input("Please enter the name you want on the leader board").title()
saveScore = winningScore

textFile = open("highscores.txt", "a")
textFile.write(str(saveScore) + ' ' + saveName + "\n")
textFile.close()

print ("\n")
textFile = open("highscores.txt", "r")
wholeThing = textFile.read().splitlines()

#prints out top 5
temp = 0
n = len(wholeThing)

counter = 0
swapped  = True
while swapped == True:
    swapped = False
    for x in range(1,n):
        if wholeThing[x-1] > wholeThing[x]:
            temp = wholeThing[x-1]
            wholeThing[x-1] = wholeThing[x]
            wholeThing[x] = temp
            swapped = True

c = len(wholeThing) - 1
s = 1
print("These are the top 5 highest scores")
for z in range(0,5):

    print(s,"-", wholeThing[c])
    c = c - 1
    s = s + 1
textFile.close()
