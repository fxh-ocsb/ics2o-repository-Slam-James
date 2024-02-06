# Samuel James
# NAME OF THE PROGRAM: 1V1 RPC 
# DATE OF CREATION: RST Week
# PURPOSE OF PROGRAM: To Be Able To Play RPC either By Oneself, Or With A Friend
import random

import pygame
from random import randint

from pygame import mixer

#Instantiate mixer
mixer.init()

#Load audio file

mixer.music.load('song.mp3')

#Set preferred volume
mixer.music.set_volume(0.3)

#Play the music
mixer.music.play()

Player_1_score = 0
Player_2_score = 0
Computer_score = 0
#create a list of play options
Player_count = input("How many players (One or Two)")
Player = False
if Player_count == "One":
    t = ["Rock", "Paper", "Scissors"]

#assign a random play to the computer
   

#set player to False
    Player = False

    while Player == False:
#set player to True
        computer = t[randint(0,2)]
        player = input("Rock, Paper, Scissors? (Press Q To Quit)")
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
                
        elif player == "Sniper":
            print("WOW, You found the super secret weapon! You Automatically win the round.")
            Player_1_score += 1
            print("Computer Score:", Computer_score)
            print("Player Score:", Player_1_score)
            
        elif player == "Q":
            if Player_1_score > Computer_score:
                print("Congrats! You Won By A Score Of:", Player_1_score, "To", Computer_score, " Win(s).")
            elif Player_1_score < Computer_score:
                print("Better Luck Next Time, You Lost With A Score Of:", Computer_score, "To", Player_1_score, "Win(s).")
            else:
                print("You Tied With The Computer Both At", Player_1_score, "Win(s).")
                
            print("Have a nice day")
            Player = True
        else:
            print("That's not a valid play. Check your spelling!")
            print("Scores remain unchanged")
    #player was set to True, but need it to be False
   
    

elif Player_count == "Two":
    t = ["Player 1 choose: Rock", "Paper", "Scissors"]



    while Player == False:
#set player to True
        player = input("Player 1 Choose: Rock, Paper, Scissors? (Press Q To Quit)")
        if player == "Q":
            print("Alright, have a nice day")
            Player = True
            exit("See You Later")
        Player_2 = input("Player 2 Choose: Rock, Paper, Scissors?")
        Player = False
    
        if player == Player_2 :
            print("Tie!")
        elif player == "Rock":
            if Player_2 == "Paper":
                print("Player 2 Wins!", Player_2, "covers", player)
                Player_2_score += 1

                print("Player 1 Score:", Player_1_score)
                print("Player 2 Score:", Player_2_score)
                print("\n")
            else:
                print("Player 1 Wins!", player, "smashes", Player_2)
                Player_1_score += 1
       
                print("Player 1 Score:", Player_1_score)
                print("Player 2 Score:", Player_2_score)
                print("\n")
        elif player == "Paper":
            if Player_2 == "Scissors":
                print("Player 2 Wins!", Player_2, "cut", player)
                Player_2_score += 1
       
                print("Player 1 Score:", Player_1_score)
                print("Player 2 Score:", Player_2_score)
                print("\n")
            else:
                print("Player 1 Wins!", player, "covers", Player_2)
                Player_1_score += 1
      
                print("Player 1 Score:", Player_1_score)
                print("Player 2 Score:", Player_2_score)
                print("\n")
        elif player == "Scissors":
            if Player_2 == "Rock":
                print("Player 2 Wins", Player_2, "smashes", player)
                Player_2_score += 1
               
                print("Player 1 Score:", Player_1_score)
                print("Player 2 Score:", Player_2_score)
                print("\n")
            else:
                print("Player 1 Wins!", player, "cut", Player_2)
                Player_1_score += 1
         
                print("Player 1 Score:", Player_1_score)
                print("Player 2 Score:", Player_2_score)
                print("\n")
                
       
        else:
            print("That's not a valid play. Check your spelling!")
            print("Scores remain unchanged")
            print(player)
            print(Player_2)
    #player was set to True, but need it to be False
    Player = False
    computer = t[randint(0,2)]
    #create a list of play options
    t = ["Rock", "Paper", "Scissors"]
#assign a random play to the computer
    computer = t[randint(0,2)]
