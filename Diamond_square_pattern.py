n = int(input("Enter the number of lines : "))
for i in range (1,n):
    for j in range (i, n+1):
        print(" ",end = "")
    for k in range (1 ,i):
        print("*",end = "")
    for k in range (1 , i +1):
        print("*",end = "")
    print()
for i in range (1,n+1):
    for j in range (1,i+1):
        print(" ",end = "")
    for k in range (i ,n):
        print("*",end = "")
    for k in range (i ,n+1):
        print("*",end = "")
    print()
