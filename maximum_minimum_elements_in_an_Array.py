def find_maxi(arr):
    maxi = max(arr)
    return maxi

def find_mini(arr):
    mini = min(arr)
    return mini


n = int(input("Enter the number of elements you want to store in an array : "))
arr = []
for i in range (n):
    arr.append(int(input(f"Enter the element {i+1} : ")))
print("The maximum element in an array : ",find_maxi(arr))
print("The minimum element in an array : ",find_mini(arr))
