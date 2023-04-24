# Samuel James
# Asterisks  
# April 24, 2023
# To make rows of asterisks.

Rows = int(input("How Many Rows Do You Want?:"))
Columns = int(input("How Many Asterisks Do You Want In Each Row?:"))

num_rows = Rows
num_cols = Columns

for i in range(num_rows):
    print('*', end=' ')
    for j in range(num_cols-1):
        i=j*i
        print('*', end=' ')
    print('')