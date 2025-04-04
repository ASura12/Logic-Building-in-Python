# Recursive Approach
def fibonacci_recursive(n):
    return n if n <= 1 else fibonacci_recursive(n - 1) + fibonacci_recursive(n - 2)

# Iterative Approach
def fibonacci_iterative(n):
    fib_series = [0, 1]
    for i in range(2, n):
        fib_series.append(fib_series[-1] + fib_series[-2])
    return fib_series[:n]

# Example usage
n = 10
print("Fibonacci (Recursive for nth term):", fibonacci_recursive(n))
print("Fibonacci Series (Iterative):", fibonacci_iterative(n))
