# Samuel James
# Random Range  
# April 14, 2023
# To give a random number between 2 numbers given.

import random
  
Min = int(input("What is the minimum number:"))
Max = int(input("What is the maximum number:"))
  
Random_Num = random.randint(Min, Max)
  
print(Random_Num)