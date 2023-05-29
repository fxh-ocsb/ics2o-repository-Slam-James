Question = (input("What is Your Question?"))
A = (input("Choice 1 (A)"))
B = (input("Choice 2 (B)"))
C = (input("Choice 3 (C)"))
D = (input("Choice 4 (D) (This is the last option)"))

Correct_Choice = (input("Is A, B, C, or D Correct?"))

Question2 = (input("What is the second question?"))
A2 = (input("Choice 1 (A)"))
B2 = (input("Choice 2 (B)"))
C2 = (input("Choice 3 (C)"))
D2 = (input("Choice 4 (D) (This is the last option)"))

Correct_Choice_2 = (input("Is A, B, C, or D Correct?"))


filehandle = open("questions.txt",'w')
print ('Writing to the file.')
filehandle.write("Question 1")
filehandle.write(Question) 
filehandle.write("\n")
filehandle.write(A)
filehandle.write("\n")
filehandle.write(B)
filehandle.write("\n")
filehandle.write(C)
filehandle.write("\n")
filehandle.write(D+"\n")
filehandle.write(Correct_Choice+"\n")
("\n")

filehandle.write(Question2) 
filehandle.write("\n")
filehandle.write(A2)
filehandle.write("\n")
filehandle.write(B2)
filehandle.write("\n")
filehandle.write(C2)
filehandle.write("\n")
filehandle.write(D2+"\n")
filehandle.write(Correct_Choice_2+"\n")



print ('Finished creating the file.')
filehandle.close()