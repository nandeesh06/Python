
""" What is Memoization?
      Memoization is a performance optimization technique where we can cache the result of function call so that
      repeated calls with same input don't recompute the result

    Why memoization?
        Without memoization:
            Same computation runs again and again
            Time complexity explodes (classic example: Fibonacci)
        With memoization:
            First call → compute + store
            Next call → fetch from cache (O(1))

    Note: Decorators not only added beatifies the function it can also change the behavior of the function
"""

# Example (without memoization)
def fib(n):
    print(f"finding fib({n})")
    return n if n<=1 else fib(n-1) + fib(n-2)

# output:
# finding fib(5)
# finding fib(4)
# finding fib(3)
# finding fib(2)
# finding fib(1)
# finding fib(0)
# finding fib(1)
# finding fib(2)
# finding fib(1)
# finding fib(0)
# finding fib(3)
# finding fib(2)
# finding fib(1)
# finding fib(0)
# finding fib(1)
# This will take exponential time


# Memoization using decorator
from functools import wraps
def memoization(func):
    cache = dict()
    @wraps(func)
    def wrapper(*args):
        if args not in cache:
            cache[args] = func(*args)
        return cache[args]
    return wrapper

@memoization
def fib_with_dec(n):
    print(f"finding fib({n})")
    return n if n <= 1 else fib_with_dec(n - 1) + fib_with_dec(n - 2)

fib_with_dec(5)


# Where Memoization with Decorators used in API or UI Automation framework?



