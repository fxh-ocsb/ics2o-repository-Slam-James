print("Ello Ello! Welcome to the program.!")
CountAgain = "yes"

while CountAgain == "yes":
    Word = input("What is your word?:")
    count = 0
    for i in range(0, len(Word)):
        count = count + 1
    print("The total number of characters in your word is " + str(count) + ".")
    CountAgain = input('Would You Like To Count Again?? (type "yes" or "no"):')
print("Have a nice day... Come Back Any Time")