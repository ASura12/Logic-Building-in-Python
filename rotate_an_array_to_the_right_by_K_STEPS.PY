def rotateArray(arr,k):
    n = len(arr)
    k = k% n
    rotated = arr[-k:] + arr[:-k]

    return rotated

# Taking Input
n,k = map(int,input().split())
arr = list(map(int,input().split()))
# Printing the array
print(*rotateArray(arr,k))