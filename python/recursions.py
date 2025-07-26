def recursive_function():
    # base condition
    if condition:
        return result
    else:
        # recursive call
        return recursive_function()

def factorial(n):
    if n == 0 or n == 1:       # base case
        return 1
    else:
        return n * factorial(n - 1)  # recursive call

print(factorial(5))  # Output: 120


def fibonacci(n):
    if n == 0:
        return 0
    elif n == 1:
        return 1
    else:
        return fibonacci(n - 1) + fibonacci(n - 2)

print(fibonacci(6))  # Output: 8
