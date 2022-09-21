#variable to generate the number of rows
n = 5
#variable to determine the first spaces in each row
k = n - 1
#loop to generte the row number
for i in range(0, n):
    #loop to give the initial spaces in each row
    for j in range(0, k):
    #end statement overrides the default setting of print to go to the next line after excecution
        print(end=" ") 
    #the initial spaces reduce by one for every next line
    k = k - 1
    #loop to enter the stars in specific columns
    for j in range(0, i+1):
        print("*", end=" ")
    #next line after putting stars in each row
    print("\r")


