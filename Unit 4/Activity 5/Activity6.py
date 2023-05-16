# Samuel James
# Activity 6
# May 16th, 2023
# Make a guessing game
import random

i = 0

print("HELLO! Welcome to Sam's Amazing Guessing Game!")
RULES = (input("Would You Like To See The Rules?"))
if RULES == "Yes":
    print("Alright!")
    print("1. You must input 2 numbers you wish to guess between. ")
    print("2. The computer will randomly select a value within your range.")
    print("3. Your job is to guess the random number in the smallest amount of guesses.")
    Start = (input("Are you ready to start?"))
    
 
    if Start == "No":
        print("Okay! Have a nice day!")
        
    elif Start == "Yes":
        Num1 = int(input("Please enter the first number:"))
        Num2 = int(input("Please enter the second number:"))
        Num3 = int(input("Please enter 0 to start guessing:"))
        if Num1 > Num2:
            Power_Num = random.randint(Num2,Num1)
            
            while Num3 != Power_Num:
                Num3 = float(input("Enter Your Guess: "))
                i += 1
    
    else:
        print("Alright, Have a nice day!")
        
    
        
