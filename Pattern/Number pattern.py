#total number of rows in the pattern
rows = 5
#variable to store the digit for each column
b = 0
#loop to determine the number of rows
for i in range(rows, 0, -1):
    b += 1 #for each consequent row the number increases by 1
    for j in range(1, i + 1): #
        print(b, end= " ") 
    print("\r")
