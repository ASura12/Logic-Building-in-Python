import heapq

def second_largest(arr):
    return heapq.nlargest(2, set(arr))[-1] if len(set(arr)) > 1 else None

arr = [10, 20, 4, 45, 99, 99, 22]
print("Second Largest:", second_largest(arr))

