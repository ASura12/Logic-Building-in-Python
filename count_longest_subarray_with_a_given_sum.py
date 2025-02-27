def subarray_sum_equals_k(arr, k):
    prefix_map = {0: 1}  # Stores frequency of prefix sums
    prefix_sum = 0
    count = 0

    for num in arr:
        prefix_sum += num  # Update prefix sum
        
        # Check if prefix_sum - k exists in map
        if (prefix_sum - k) in prefix_map:
            count += prefix_map[prefix_sum - k]

        # Update prefix sum frequency
        prefix_map[prefix_sum] = prefix_map.get(prefix_sum, 0) + 1

    return count

# Example Usage
arr = [1, 1, 1]
k = 2
print("Number of subarrays with sum", k, ":", subarray_sum_equals_k(arr, k))
