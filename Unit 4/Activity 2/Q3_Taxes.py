# Samuel James
# Taxes
# March 31st 
# Calculate Taxes For 10 Items  

# VARIABLE DEFINITION
Item_1 = float(input("Enter Price Of Item 1:"))
Item_2= float(input("Enter Price Of Item 2:"))
Item_3 = float(input("Enter Price Of Item 3:"))
Item_4 = float(input("Enter Price Of Item 4:"))
Item_5 = float(input("Enter Price Of Item 5:"))
Item_6 = float(input("Enter Price Of Item 6:"))
Item_7 = float(input("Enter Price Of Item 7:"))
Item_8 = float(input("Enter Price Of Item 8:"))
Item_9 = float(input("Enter Price Of Item 9:"))
Item_10 = float(input("Enter Price Of Item 10:"))
# INPUT
Main_Price = Item_1 + Item_2 + Item_3 + Item_4 + Item_5 + Item_6 + Item_7 + Item_8 + Item_9 + Item_10
Tax = Main_Price * 0.13
Grand_Total = Main_Price + Tax


# PROCESSING

RoundTax = "{:.2f}".format(Tax)
RoundGT = "{:.2f}".format(Grand_Total)
RoundMP = "{:.2f}".format(Main_Price)
# OUTPUT
print("Tax", "=", RoundTax)
print("Main Price", "=", RoundMP)
print("Grand Total", "=", RoundGT)