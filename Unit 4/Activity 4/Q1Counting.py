# Samuel James
# Counting 
# April 20, 2023  
# To count to a designated number, by a designated number, and back to 0.  

Large_Number = int(input("What is your large number:"))
Count_By = int(input("What is the number you want to count by:"))

Large_Number = Large_Number + 1
for i in range(0,Large_Number,Count_By):
    print(i)
    
Q2 = (input("Do You Want To Count Back Down?"))

Inverted_Count = Count_By * -1

if Q2 == "Yes":
    Large_Number = Large_Number - 1
    for j in range(Large_Number, -1, Inverted_Count):
        print(j)
    