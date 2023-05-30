# opens the file to read - this file must already exist
inFile = open("questions.txt", 'r')
# reads the first line of the file into a variable
line=" "
# outputs the file contents
while line != '': #check for the end of the file
    for i in range (0,5,1):
         
        line = inFile.readline()
        print (line.strip('\n'))
     # the next line is read
    Person_Answer = (input("What is the answer? A, B, C, or D?"))
    line = inFile.readline()
    print(line.strip('\n'))
inFile.close()