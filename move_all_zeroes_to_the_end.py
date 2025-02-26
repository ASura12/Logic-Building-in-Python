def move_zeros_to_end(arr):
    n = len(arr)
    nonZeroIndex = 0  # Pointer for non-zero elements

    # Move all non-zero elements forward
    for i in range(n):
        if arr[i] != 0:
            arr[i], arr[nonZeroIndex] = arr[nonZeroIndex], arr[i]
            nonZeroIndex += 1

# Example usage
arr = list(map(int, input("Enter elements separated by space: ").split()))
move_zeros_to_end(arr)
print("Array after moving zeros:", arr)
