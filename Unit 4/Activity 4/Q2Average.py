# Samuel James
# Average  
# April 20, 2023  
# To take the average of an unregulated amount of numbers  

# Variables
i = 0
subtotal = 0.0
# Program Title
print ("Averaging Program")
print ()

# Input - User prompt, with a sentinel (-1) to signal completion
price = float(input("Enter price (000 to Exit): "))

# Input - Continue adding to the subtotal until the user is done
while price != 000:
    subtotal = subtotal + price
    price = float(input("Enter price (000 to Exit): "))
    i += 1

# Processing - calculation of tax
Average = subtotal / i
# Processing - calculation of total, including tax
print("Your average is going to be", Average)

Total = subtotal
print("Your Grand Total Is Going To Be:", Total)