'''
fibonacci with different approaches
'''

# Approach 1: Recursion

# The simplest way to implement the Fibonacci sequence is to use a recursive function.


def fibonacci(n):
    if n <= 1:
        return n
    return fibonacci(n - 1) + fibonacci(n - 2)

# Approach 2: Recursion with Memoization

# The recursive approach has a time complexity of O(2^n) because each call branches into two more calls. This results in an exponential time complexity.

# We can improve the time complexity by using memoization to store the results of subproblems.


def fibonacci(n, memo={}):
    if n in memo:
        return memo[n]
    if n <= 1:
        return n
    memo[n] = fibonacci(n - 1, memo) + fibonacci(n - 2, memo)
    return memo[n]

# Approach 3: Iterative Approach


def fibonacci(n):
    # Base cases
    if n <= 1:
        return n

    # Initialize variables
    a, b = 0, 1

    # Calculate Fibonacci sequence iteratively
    for _ in range(2, n + 1):
        a, b = b, a + b

    return b


print(fibonacci(6))  # 8
