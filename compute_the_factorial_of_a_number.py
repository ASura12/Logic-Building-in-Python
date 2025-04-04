# Recursive Approach
def factorial_recursive(n):
    return 1 if n == 0 else n * factorial_recursive(n - 1)

# Iterative Approach
def factorial_iterative(n):
    fact = 1
    for i in range(1, n + 1):
        fact *= i
    return fact

# Example usage
n = 5
print("Factorial (Recursive):", factorial_recursive(n))
print("Factorial (Iterative):", factorial_iterative(n))
