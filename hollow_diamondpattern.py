n = int(input("Enter the number of lines : "  ))

for i in range(1,n+1):
    print(" " * (n - i),end = "")
    for j in range(1 , 2 * i):
        if(j == 1 or j == 2 * i - 1):
            print("*",end = "")
        else:
            print(" ",end = "")
    print()


for i  in range (n - 1,0,-1):
    print(" "* (n - i),end = "")
    for k  in range (1 , 2 * i):
        if(k == 1 or k == 2 * i - 1):
            print("*",end = "")
        else:
            print(" ",end = "")
    print()
