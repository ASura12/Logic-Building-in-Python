def rotate_and_compare(arr1, arr2):
    # Reverse the arrays using slicing (O(n))
    reversed_arr1 = arr1[::-1]
    reversed_arr2 = arr2[::-1]

    # Compare the reversed arrays with the original ones
    if reversed_arr1 == arr2:
        print("Arr1 is matched with Arr2")
    if reversed_arr2 == arr1:
        print("Arr2 is matched with Arr1")
    else:
        print("Arr1 and Arr2 are not a rotation of each other ")
# Taking input
n = int(input())
arr1 = list(map(int, input().split()))
arr2 = list(map(int, input().split()))

rotate_and_compare(arr1, arr2)
