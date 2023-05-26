Account_Balance = 0.00
i = "Yes"
print("Welcome to ICS2O Banking")
while i == "Yes":
    Choice = (input("Do You Want To Make A Deposit, or a Withdrawal?:"))


    if Choice == "Deposit":
        Dep_Amount = int(input("How much would you like to deposit?"))
        Account_Balance = Account_Balance + Dep_Amount
        print("Your new balance is", Account_Balance)
        i = (input("Would you like to do something else?"))


    elif Choice == "Withdrawal":
        if Account_Balance == 0.00:
            print("You cannot make a withdrawal right now. You're Broke...")
            i = (input("Would you like to do something else?"))
    
        else:
            print("You can make a withdrawal from $0.01 to", Account_Balance, '.')
            Withdrawal_Amount = int(input("How much would you like to withdrawal?"))
            Account_Balance = Account_Balance - Withdrawal_Amount
            print("Your new balance is", Account_Balance)
            i = (input("Would you like to do something else?"))
                
                
    if i == "No":
        print("Alright, you total balance is", Account_Balance, "Thank you for picking ICS2O Banking!")
            
            

        
