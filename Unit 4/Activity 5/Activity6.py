# Samuel James
# Activity 6
# May 16th, 2023
# Make a guessing game
import random
RULES = (input("Say HELLO!"))
i = 0
Num1 = 0
Num2 = 0
Num3 = 0
Power_Num = 0
Failed_Attempted = True

print("HELLO! Welcome to Sam's Amazing Guessing Game!")

while RULES != "Yes" and RULES != "No":
    RULES = (input("Would You Like To See The Rules? (Yes or No)"))
    if RULES == "Yes":
        print("Alright!")
        print("1. You must input 2 numbers you wish to guess between. ")
        print("2. The computer will randomly select a value within your range.")
        print("3. Your job is to guess the random number in the smallest amount of guesses.")
        Start = (input("Are you ready to start? (Yes or No)"))
    
    elif RULES == "No":
        print("Alright, Good Luck!")
        Start = (input('Type "Yes" to Start'))
    
    else:
         print("Invalid Responce, please be sure to capitalize either 'Yes' or 'No'")
     
if Start == "No":
    print("Okay! Have a nice day!")
        
elif Start == "Yes":
    while Start == "Yes":
        while Failed_Attempted == True:
            try:
                Num1 = int(input("Please enter the first number:"))
                Num2 = int(input("Please enter the second number:"))
                Num3 = int(input("Please enter 0 to start guessing:"))
                
            except:
                    print("Make sure you used whole numbers and does not involve letters")
                    Failed_Attempted = True
        if Num1 > Num2:
            Power_Num = random.randint(Num2,Num1)
            
        while Num3 != Power_Num:
            print("Good Luck, Guess Again")
            Num3 = float(input("Enter Your Guess: "))
            i += 1
                
                
        if Num3 == Power_Num:
            print("Congrats, Your total guesses is", i, "Attempt(s)!")
            
        elif Num1 < Num2:
            Power_Num = random.randint(Num1,Num2)
            
            while Num3 != Power_Num:
                print("Good Luck, Guess Again")
                Num3 = float(input("Enter Your Guess: "))
                i += 1
                
                
        if Num3 == Power_Num:
            print("Congrats, You guessed it in", i, "Attempt(s)!")
            Start = (input("would you like to play again?"))
    
    else:
        print("Alright, Have a nice day!")
        
    
else:
    print("Alright, have a nice day!")
