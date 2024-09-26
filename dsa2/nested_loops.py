# nested loop is a loop within the another loop and its big "O" notation is O(2)

'''
rows = int(input("enter the numbers of rows: "))
columns = int(input("enter the number of columns: "))

for i in range(1 , rows+1): # incharge of rows
    for j in range(1, columns+1): # incharge of columns
        print("*", end="")
    print()
'''

n = 5

# increasing triangle pattern
'''
for i in range(0,n):
    for j in range(i+1):
        print("*", end="")
    print()
'''

# decreasing triangle pattern
'''
for i in range(n):
    for _ in range(i , n):
        print("*", end="")
    print()
'''

# increasing pattern from right side
'''
for i in range(n):
    # we will print decreasing pattern for " "
    for j in range(i , n): # this will print " " j times then second loop will work
        print(" " , end="")

    for j in range(i+1):
        print("*" , end="")

    print()
'''

# decreasing pattern from left side
'''
for i in range(n):
    # we will print increasing pattern for " "
    for j in range(i+1):
        print(" " , end="")
    
    for _ in range(i , n):
        print("*" , end="")
    
    print()
'''

# hill pattern
'''
for i in range(n):
    for _ in range(i , n):
        print(" " , end='')
    for _ in range(i+1):
        print("*" , end='')
    for _ in range(i):
        print("*" , end='')

    print()
'''

# reverse hill pattern
'''
for i in range(n):
    for _ in range(i+1):
        print(' ' , end='')
    for _ in range(i,n):
        print('*' , end='')
    for _ in range(i , n-1):
        print('*' , end='')
    print()
'''

# diamond pattern
'''
for i in range(n):
    for _ in range(i , n):
        print(' ' , end='')
    for _ in range(i+1):
        print('*' , end='')
    for _ in range(i):
        print('*' , end='')
    print()

    
for i in range(n):
    for _ in range(i+1):
        print(' ' , end='')
    for _ in range(i , n):
        print('*' , end='')
    for _ in range(i , n-1):
        print('*' , end='')
    print()
'''