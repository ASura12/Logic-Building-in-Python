def find_pairs(arr, target):
    seen = set()
    
    for num in arr:
        complement = target - num
        if complement in seen:
            print(f"({num}, {complement})")
        seen.add(num)  # Store current number

# Input Handling
n, target = map(int, input().split())
arr = list(map(int, input().split()))

find_pairs(arr, target)
