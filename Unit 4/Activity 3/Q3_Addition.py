# Samuel James
# Random Range
# April 12, 2023  
# Give A Random Math Question

import random

Question_Type = (input("Do You Want An Addition, Subtraction, Multiplication, Or Division Question? :"))
if Question_Type == "Addition":
    Number_A = random.randint(0,1000)
    Number_B = random.randint(0,1000)
    Addition = Number_A + Number_B
    print("Add", Number_A, "+", Number_B)
    Person_Answer = int(input("What is The Answer?"))
    if Person_Answer == Addition:
        print("Congrats, You Are Correct!")
        
    else:
        print("Sorry, That's incorrect... The Correct Answer Was", Addition)
        
        
if Question_Type == "Multiplication":
    Number_A = random.randint(0,1000)
    Number_B = random.randint(0,1000)
    Multiplication = Number_A * Number_B
    print("Multiply", Number_A, "*", Number_B)
    Person_Answer = int(input("What is The Answer?"))
    if Person_Answer == Multiplication:
        print("Congrats, You Are Correct!")
        
    else:
        print("Sorry, That's incorrect... The Correct Answer Was", Multiplication)
        

if Question_Type == "Division":
    Number_A = random.randint(0,1000)
    Number_B = random.randint(0,1000)
    Division = Number_A / Number_B
    print("Divide", Number_A, "/", Number_B)
    Person_Answer = int(input("What is The Answer?"))
    if Person_Answer == Division:
        print("Congrats, You Are Correct!")
        
    else:
        print("Sorry, That's incorrect... The Correct Answer Was", Division)
        
        
if Question_Type == "Subtraction":
    Number_A = random.randint(0,1000)
    Number_B = random.randint(0,1000)
    Subtraction = Number_A - Number_B
    print("Subtract", Number_A, "-", Number_B)
    Person_Answer = int(input("What is The Answer?"))
    if Person_Answer == Subtraction:
        print("Congrats, You Are Correct!")
        
    else:
        print("Sorry, That's incorrect... The Correct Answer Was", Subtraction)
        #DONE