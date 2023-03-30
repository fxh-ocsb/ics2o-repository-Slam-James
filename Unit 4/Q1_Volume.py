# Samuel James 
#Q1_Volume.py 
# March 30, 2023 
# Display Volume Of A Prism.  

# VARIABLE DEFINITION
print("Hello, and welcome to the Cowculator... ")
print("Here, we have the cows do the math so you don't have too.")
print("Please enter the dimensions of your rectangular prism below! If you have a different prism, please look at our website to find the other Cowculators.")
# INPUT
Depth = int(input("Enter Depth:"))
Height = int(input("Enter Height:"))
Width = int(input("Enter Width:"))

Your_Answer =  int(input("Enter Your Answer:"))

# PROCESSING

Correct_Answer = Depth * Height * Width

if Correct_Answer == Your_Answer:
  print("Congrats. You Are Right!")
else:
  print("Good Try, The Correct Answer Was", Correct_Answer)
    

# OUTPUT
