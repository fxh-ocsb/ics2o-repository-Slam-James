#Samuel James
#Q4_Numbers
#April 3, 2023 
#Display Numbers in a table like format 

from tabulate import tabulate

# VARIABLE DEFINITION

# INPUT

# PROCESSING

# OUTPUT

Num_1 =  int(input("Enter Number 1:"))
Num_2 = int(input("Enter Number 2:"))
Num_3 =  int(input("Enter Number 3:"))
Num_4 = int(input("Enter Number 4:"))
Num_5 =  int(input("Enter Number 5:"))

Sum = (Num_1 + Num_2 + Num_3 + Num_4 + Num_5)
Average = Sum / 5

#create data

  
#define header names
table = [["Average", Average],
         ["Sum", Sum]]
         
print(tabulate(table))