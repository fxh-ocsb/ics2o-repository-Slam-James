# Samuel James
# Pythagoras
# April 12, 2023
# To Measure The Length Of Angle C
import math

Hypot = (input("Do You Have A Hypotenuse:"))

if Hypot == "Yes":
  print("Alright, Please Enter The Hypotenuse And The Second Length Below!")
  Hypotenuse = int(input("Enter Hypotenuse Here:"))
  Second_Angle = int(input("Enter Second Side Length Here:"))
  Units = (input("Enter Units Here:"))
  C_Squared = math.pow(Hypotenuse,2)
  A_Squared = math.pow(Second_Angle, 2)
  
  B_Squared = C_Squared - A_Squared
  B = math.sqrt(B_Squared)
  print("The Missing Side Length Is",B,Units)
  
  
else:
    print("Alright, Please Enter Both Side Lengths Below!")
    Side_A = int(input("Enter Side Length A Here:"))
    Side_B = int(input("Enter Second Side Length Here:"))
    Units = (input("Enter Units Here:"))
    Side_A_Squared = math.pow(Side_A,2)
    Side_B_Squared = math.pow(Side_B, 2)
    
    Hypotenuse = Side_A_Squared + Side_B_Squared
    Hypot = math.sqrt(Hypotenuse)
    print("The Missing Side Length Is",Hypot,Units)