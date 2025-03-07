def has_zero_sum_subarray(arr):
    prefix_sum_set = set()
    sum = 0

    for num in arr:
        sum += num  # Compute prefix sum

        if sum == 0 or sum in prefix_sum_set:
            return True  # Subarray with sum 0 found

        prefix_sum_set.add(sum)

    return False  # No zero-sum subarray found

# Example usage
arr = [4, 2, -3, 1, 6]
if has_zero_sum_subarray(arr):
    print("Subarray with sum 0 exists")
else:
    print("No subarray with sum 0 found")
