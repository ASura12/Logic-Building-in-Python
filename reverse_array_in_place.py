
def swapArray(arr,n):
    start , end = 0,len(arr)-1

    while start < end:
        arr[start],arr[end] = arr[end],arr[start]

        start+=1
        end =- 1

n = int(input("Enter the number : "))
arr = []
for i in range (n):
    arr.append(int(input(f"Enter element {i + 1} : ")))
swapArray(arr,n)
for i  in range (n):
    print(arr[i],end = " ")

