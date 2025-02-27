def longest_subarray_with_sum(arr, target_sum):
    prefix_map = {}  # Stores first occurrence of prefix_sum
    prefix_sum = 0
    max_length = 0

    for i in range(len(arr)):
        prefix_sum += arr[i]

        # If the sum equals target_sum, update max_length
        if prefix_sum == target_sum:
            max_length = i + 1

        # If prefix_sum - target_sum exists in map, update max_length
        if (prefix_sum - target_sum) in prefix_map:
            max_length = max(max_length, i - prefix_map[prefix_sum - target_sum])

        # Store first occurrence of prefix_sum
        if prefix_sum not in prefix_map:
            prefix_map[prefix_sum] = i

    return max_length

# Example Usage
arr = [1, 2, 3, 7, 5]
target_sum = 12
print("Longest Subarray Length:", longest_subarray_with_sum(arr, target_sum))
