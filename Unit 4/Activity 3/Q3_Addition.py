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
    Person_Answer = (input("What is The Answer?"))
    if Person_Answer == Addition:
        print("Congrats, You Are Correct!")
        
    else:
        print("Sorry, That's incorrect... The Correct Answer Was", Addition)
        