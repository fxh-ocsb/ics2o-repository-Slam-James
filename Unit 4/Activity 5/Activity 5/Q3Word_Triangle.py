print("Make a triangle, with a computer??? That's impossi- or is it?!")
Word = str(input("What is your word?:"))
Characters = 0
Count = 1
for i in range(0, len(Word)):
    Characters = Characters + 1
while Count <= Characters:
    print(Word[0:Count])
    Count = Count + 1
