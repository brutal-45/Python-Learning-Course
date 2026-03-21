"""
Exercises: Functions
Level: Intermediate
Description: Practice problems for functions, decorators, and advanced concepts.
"""

# =============================================================================
# EXERCISE 1: FUNCTION ARGUMENTS
# =============================================================================

"""
Exercise 1.1: Create a flexible calculator function that:
- Accepts any number of numbers
- Accepts an operation parameter (sum, avg, min, max, product)
- Returns the result
"""


def calculator(*numbers, operation='sum'):
    """
    Flexible calculator function.

    Args:
        *numbers: Variable number of numeric arguments
        operation: Operation to perform (sum, avg, min, max, product)

    Returns:
        Result of the calculation
    """
    if not numbers:
        return None

    operations = {
        'sum': sum,
        'avg': lambda x: sum(x) / len(x),
        'min': min,
        'max': max,
        'product': lambda x: eval('*'.join(map(str, x)))
    }

    if operation not in operations:
        raise ValueError(f"Unknown operation: {operation}")

    return operations[operation](numbers)


print("\n" + "=" * 50)
print("Exercise 1.1 Solution: Flexible Calculator")
print(f"  calculator(1,2,3,4,5): {calculator(1, 2, 3, 4, 5)}")
print(f"  calculator(1,2,3,4,5, operation='avg'): {calculator(1, 2, 3, 4, 5, operation='avg')}")
print(f"  calculator(1,2,3,4,5, operation='max'): {calculator(1, 2, 3, 4, 5, operation='max')}")


# =============================================================================
# EXERCISE 2: CLOSURES
# =============================================================================

"""
Exercise 2.1: Create a counter closure that:
- Returns a function that increments and returns a counter
- Optionally accepts a step value
"""


def make_counter(start=0, step=1):
    """
    Create a counter closure.

    Args:
        start: Starting value
        step: Increment step

    Returns:
        Function that returns incremented value
    """
    count = start

    def counter():
        nonlocal count
        current = count
        count += step
        return current

    return counter


print("\n" + "=" * 50)
print("Exercise 2.1 Solution: Counter Closure")
counter1 = make_counter()
print(f"  Counter 1: {[counter1() for _ in range(5)]}")

counter2 = make_counter(start=10, step=5)
print(f"  Counter 2 (start=10, step=5): {[counter2() for _ in range(5)]}")


# =============================================================================
# EXERCISE 3: DECORATORS
# =============================================================================

"""
Exercise 3.1: Create a decorator that:
- Measures execution time
- Prints the function name and time taken
"""

import time
from functools import wraps


def timing_decorator(func):
    """Decorator to measure function execution time."""

    @wraps(func)
    def wrapper(*args, **kwargs):
        start = time.time()
        result = func(*args, **kwargs)
        end = time.time()
        print(f"  {func.__name__} executed in {end - start:.4f} seconds")
        return result

    return wrapper


@timing_decorator
def slow_function(n):
    """A function that takes some time."""
    time.sleep(0.05)
    return sum(range(n))


print("\n" + "=" * 50)
print("Exercise 3.1 Solution: Timing Decorator")
result = slow_function(10000)
print(f"  Result: {result}")


# =============================================================================
# EXERCISE 4: RECURSION
# =============================================================================

"""
Exercise 4.1: Implement recursive functions for:
- Fibonacci with memoization
- Binary search
"""


def fibonacci_memo(n, memo=None):
    """Fibonacci with memoization."""
    if memo is None:
        memo = {}
    if n in memo:
        return memo[n]
    if n <= 1:
        return n
    memo[n] = fibonacci_memo(n - 1, memo) + fibonacci_memo(n - 2, memo)
    return memo[n]


def binary_search(arr, target, low=0, high=None):
    """Recursive binary search."""
    if high is None:
        high = len(arr) - 1

    if low > high:
        return -1

    mid = (low + high) // 2

    if arr[mid] == target:
        return mid
    elif arr[mid] > target:
        return binary_search(arr, target, low, mid - 1)
    else:
        return binary_search(arr, target, mid + 1, high)


print("\n" + "=" * 50)
print("Exercise 4.1 Solution: Recursion")
print(f"  Fibonacci(20): {fibonacci_memo(20)}")

arr = [1, 3, 5, 7, 9, 11, 13, 15]
target = 7
print(f"  Binary search for {target}: index {binary_search(arr, target)}")


# =============================================================================
# EXERCISE 5: GENERATORS
# =============================================================================

"""
Exercise 5.1: Create generator functions for:
- Fibonacci sequence (infinite)
- Prime numbers (infinite)
"""


def fibonacci_generator():
    """Generate infinite Fibonacci sequence."""
    a, b = 0, 1
    while True:
        yield a
        a, b = b, a + b


def prime_generator():
    """Generate infinite prime numbers."""
    num = 2
    while True:
        if all(num % i != 0 for i in range(2, int(num ** 0.5) + 1)):
            yield num
        num += 1


print("\n" + "=" * 50)
print("Exercise 5.1 Solution: Generators")

print("  Fibonacci (first 10):")
fib = fibonacci_generator()
print(f"    {[next(fib) for _ in range(10)]}")

print("  Primes (first 10):")
primes = prime_generator()
print(f"    {[next(primes) for _ in range(10)]}")


# =============================================================================
# MAIN EXECUTION
# =============================================================================

if __name__ == "__main__":
    print("\n" + "=" * 50)
    print("✅ All function exercises completed!")
    print("📚 Continue practicing with more complex problems!")
    print("=" * 50)
