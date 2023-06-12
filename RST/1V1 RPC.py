# Samuel James
# NAME OF THE PROGRAM: 1V1 RPC 
# DATE OF CREATION: RST Week
# PURPOSE OF PROGRAM: To Be Able To Play RPC either By Oneself, Or With A Friend
import os
from random import randint
from test.inspect_fodder2 import cls135
Player_1_score = 0
Computer_score = 0
#create a list of play options
Player_count = input("How many players (One or Two)")

if Player_count == "One":
    t = ["Rock", "Paper", "Scissors"]

#assign a random play to the computer
    computer = t[randint(0,2)]

#set player to False
    player = False

    while player == False:
#set player to True
        player = input("Rock, Paper, Scissors?")
        if player == computer:
            print("Tie!")
        elif player == "Rock":
            if computer == "Paper":
                print("You lose!", computer, "covers", player)
                Computer_score += 1

                print("Computer Score:", Computer_score)
                print("Player Score:", Player_1_score)
                print("\n")
            else:
                print("You win!", player, "smashes", computer)
                Player_1_score += 1
       
                print("Computer Score:", Computer_score)
                print("Player Score:", Player_1_score)
                print("\n")
        elif player == "Paper":
            if computer == "Scissors":
                print("You lose!", computer, "cut", player)
                Computer_score += 1
       
                print("Computer Score:", Computer_score)
                print("Player Score:", Player_1_score)
                print("\n")
            else:
                print("You win!", player, "covers", computer)
                Player_1_score += 1
      
                print("Computer Score:", Computer_score)
                print("Player Score:", Player_1_score)
                print("\n")
        elif player == "Scissors":
            if computer == "Rock":
                print("You lose...", computer, "smashes", player)
                Computer_score += 1
               
                print("Computer Score:", Computer_score)
                print("Player Score:", Player_1_score)
                print("\n")
            else:
                print("You win!", player, "cut", computer)
                Player_1_score += 1
         
                print("Computer Score:", Computer_score)
                print("Player Score:", Player_1_score)
                print("\n")
        else:
            print("That's not a valid play. Check your spelling!")
            print("Scores remain unchanged")
    #player was set to True, but need it to be False
    player = False
    computer = t[randint(0,2)]
    #create a list of play options
    t = ["Rock", "Paper", "Scissors"]
#assign a random play to the computer
    computer = t[randint(0,2)]

#set player to False
    player = False
    while player == False:
#set player to True
        player = input("Rock, Paper, Scissors?")
        print("\n")
        if player == computer:
            print("Tie!")
        elif player == "Rock":
            if computer == "Paper":
                print("You lose!", computer, "covers", player)
                Computer_score += 1
                print("Computer Score:", Computer_score)
                print("Player Score:", Player_1_score)
                print("\n")
            else:
                print("You win!", player, "smashes", computer)
                Player_1_score += 1

                print("Computer Score:", Computer_score)
                print("Player Score:", Player_1_score)
                print("\n")
        elif player == "Paper":
            if computer == "Scissors":
                print("You lose!", computer, "cut", player)
                Computer_score += 1

                print("Computer Score:", Computer_score)
                print("Player Score:", Player_1_score)
                print("\n")
            else:
                print("You win!", player, "covers", computer)
                Player_1_score += 1

                print("Computer Score:", Computer_score)
                print("Player Score:", Player_1_score)
                print("\n")
        elif player == "Scissors":
            if computer == "Rock":
                print("You lose...", computer, "smashes", player)
                Computer_score += 1

                print("Computer Score:", Computer_score)
                print("Player Score:", Player_1_score)
                print("\n")
            else:
                print("You win!", player, "cut", computer)
                Player_1_score += 1
                print("Computer Score:", Computer_score)
                print("Player Score:", Player_1_score)
                print("\n")
        else:
            print("That's not a valid play. Check your spelling!")
    #player was set to True, but we want it to be False so the loop continues
    player = False
    computer = t[randint(0,2)]\
    

elif Player_count == "Two":
    t = ["Player 1 choose: Rock", "Paper", "Scissors"]

    Player_1 = input("Player 1 Choose: Rock, Paper, Scissors?")
    os.system('cls')
    Player_2 = input("Player 2 Choose: Rock, Paper, Scissors?")
    os.system('cls')
    