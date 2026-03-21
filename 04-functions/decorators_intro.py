"""
Module: decorators_intro.py
Topic: Introduction to Decorators
Level: Intermediate

This file teaches you about:
- What are decorators
- Creating decorators
- Decorators with arguments
- functools.wraps
- Common decorator patterns
"""

# =============================================================================
# SECTION 1: WHAT ARE DECORATORS
# =============================================================================

print("=" * 60)
print("WHAT ARE DECORATORS")
print("=" * 60)

# A decorator is a function that modifies another function
# It "wraps" the original function, adding functionality

# Basic concept: functions as objects
def my_function():
    return "Hello"


# Assign function to variable
f = my_function
print(f"Calling f(): {f()}")

# Pass function as argument
def call_function(func):
    return func()


print(f"call_function(my_function): {call_function(my_function)}")

# Return function from function
def get_function():
    def inner():
        return "Inner function"
    return inner


new_func = get_function()
print(f"get_function()(): {new_func()}")

# =============================================================================
# SECTION 2: CREATING BASIC DECORATORS
# =============================================================================

print("\n" + "=" * 60)
print("CREATING BASIC DECORATORS")
print("=" * 60)


def my_decorator(func):
    """A simple decorator that prints before and after function call."""
    def wrapper():
        print("  Before function call")
        result = func()
        print("  After function call")
        return result
    return wrapper


# Apply decorator manually
def say_hello():
    return "Hello!"


say_hello = my_decorator(say_hello)
print("Manual decoration:")
print(f"  Result: {say_hello()}")

# Using @ syntax (syntactic sugar)
@my_decorator
def say_goodbye():
    return "Goodbye!"


print("\nUsing @ syntax:")
print(f"  Result: {say_goodbye()}")

# =============================================================================
# SECTION 3: DECORATORS WITH ARGUMENTS
# =============================================================================

print("\n" + "=" * 60)
print("DECORATORS WITH ARGUMENTS")
print("=" * 60)


def decorator_with_args(func):
    """Decorator that handles function arguments."""
    def wrapper(*args, **kwargs):
        print(f"  Calling {func.__name__} with args={args}, kwargs={kwargs}")
        result = func(*args, **kwargs)
        print(f"  Result: {result}")
        return result
    return wrapper


@decorator_with_args
def add(a, b):
    return a + b


@decorator_with_args
def greet(name, greeting="Hello"):
    return f"{greeting}, {name}!"


print("Decorator with args:")
add(3, 5)
print()
greet("Alice", greeting="Hi")

# =============================================================================
# SECTION 4: PRESERVING FUNCTION METADATA
# =============================================================================

print("\n" + "=" * 60)
print("PRESERVING FUNCTION METADATA")
print("=" * 60)

from functools import wraps


def bad_decorator(func):
    """Decorator without wraps - loses metadata."""
    def wrapper(*args, **kwargs):
        return func(*args, **kwargs)
    return wrapper


def good_decorator(func):
    """Decorator with wraps - preserves metadata."""
    @wraps(func)
    def wrapper(*args, **kwargs):
        return func(*args, **kwargs)
    return wrapper


@bad_decorator
def example_bad():
    """This is the original docstring."""
    pass


@good_decorator
def example_good():
    """This is the original docstring."""
    pass


print("Without @wraps:")
print(f"  Name: {example_bad.__name__}")
print(f"  Docstring: {example_bad.__doc__}")

print("\nWith @wraps:")
print(f"  Name: {example_good.__name__}")
print(f"  Docstring: {example_good.__doc__}")

# =============================================================================
# SECTION 5: PRACTICAL DECORATOR EXAMPLES
# =============================================================================

print("\n" + "=" * 60)
print("PRACTICAL DECORATOR EXAMPLES")
print("=" * 60)

import time
from functools import wraps


def timing_decorator(func):
    """Measure and print function execution time."""
    @wraps(func)
    def wrapper(*args, **kwargs):
        start = time.time()
        result = func(*args, **kwargs)
        end = time.time()
        print(f"  {func.__name__} took {end - start:.4f} seconds")
        return result
    return wrapper


@timing_decorator
def slow_function():
    """A function that takes time."""
    time.sleep(0.1)
    return "Done!"


print("Timing decorator:")
result = slow_function()


def retry_decorator(max_attempts=3, delay=1):
    """Retry function on failure."""
    def decorator(func):
        @wraps(func)
        def wrapper(*args, **kwargs):
            for attempt in range(max_attempts):
                try:
                    return func(*args, **kwargs)
                except Exception as e:
                    if attempt == max_attempts - 1:
                        raise
                    print(f"  Attempt {attempt + 1} failed: {e}")
                    time.sleep(delay)
        return wrapper
    return decorator


# Simulating an unreliable function
call_count = 0


@retry_decorator(max_attempts=3, delay=0.1)
def unreliable_function():
    """A function that fails sometimes."""
    global call_count
    call_count += 1
    if call_count < 3:
        raise ValueError("Random failure")
    return "Success!"


print("\nRetry decorator:")
print(f"  Result: {unreliable_function()}")


def cache_decorator(func):
    """Simple caching decorator (memoization)."""
    cache = {}

    @wraps(func)
    def wrapper(*args):
        if args in cache:
            print(f"  Cache hit for {args}")
            return cache[args]
        print(f"  Computing for {args}")
        result = func(*args)
        cache[args] = result
        return result

    return wrapper


@cache_decorator
def fibonacci(n):
    """Calculate Fibonacci number."""
    if n <= 1:
        return n
    return fibonacci(n - 1) + fibonacci(n - 2)


print("\nCache decorator:")
print(f"  fibonacci(10): {fibonacci(10)}")


def log_decorator(level="INFO"):
    """Logging decorator with configurable level."""
    def decorator(func):
        @wraps(func)
        def wrapper(*args, **kwargs):
            print(f"  [{level}] Calling {func.__name__}({args}, {kwargs})")
            result = func(*args, **kwargs)
            print(f"  [{level}] {func.__name__} returned {result}")
            return result
        return wrapper
    return decorator


@log_decorator(level="DEBUG")
def add_numbers(a, b):
    return a + b


print("\nLogging decorator:")
add_numbers(3, 5)

# =============================================================================
# SECTION 6: DECORATORS WITH OPTIONAL ARGUMENTS
# =============================================================================

print("\n" + "=" * 60)
print("DECORATORS WITH OPTIONAL ARGUMENTS")
print("=" * 60)


def flexible_decorator(_func=None, *, option1="default", option2=True):
    """
    A decorator that can be used with or without arguments.

    Usage:
        @flexible_decorator
        @flexible_decorator()
        @flexible_decorator(option1="custom")
    """
    def decorator(func):
        @wraps(func)
        def wrapper(*args, **kwargs):
            print(f"  Options: option1={option1}, option2={option2}")
            return func(*args, **kwargs)
        return wrapper

    if _func is None:
        # Called with arguments: @flexible_decorator(...)
        return decorator
    else:
        # Called without arguments: @flexible_decorator
        return decorator(_func)


@flexible_decorator
def example1():
    return "No arguments"


@flexible_decorator()
def example2():
    return "Empty arguments"


@flexible_decorator(option1="custom", option2=False)
def example3():
    return "Custom arguments"


print("Flexible decorator:")
print(f"  Result: {example1()}")
print(f"  Result: {example2()}")
print(f"  Result: {example3()}")

# =============================================================================
# SECTION 7: CLASS-BASED DECORATORS
# =============================================================================

print("\n" + "=" * 60)
print("CLASS-BASED DECORATORS")
print("=" * 60)


class CountCalls:
    """Decorator that counts function calls."""

    def __init__(self, func):
        self.func = func
        self.count = 0
        wraps(func)(self)

    def __call__(self, *args, **kwargs):
        self.count += 1
        print(f"  Call #{self.count} of {self.func.__name__}")
        return self.func(*args, **kwargs)


@CountCalls
def say_hi():
    return "Hi!"


print("Class-based decorator:")
say_hi()
say_hi()
say_hi()

# =============================================================================
# SECTION 8: BUILT-IN DECORATORS
# =============================================================================

print("\n" + "=" * 60)
print("BUILT-IN DECORATORS")
print("=" * 60)


class Example:
    """Example class demonstrating built-in decorators."""

    def __init__(self, value):
        self._value = value

    @property
    def value(self):
        """Getter for value."""
        return self._value

    @value.setter
    def value(self, new_value):
        """Setter for value."""
        self._value = new_value

    @value.deleter
    def value(self):
        """Deleter for value."""
        del self._value

    @staticmethod
    def static_method():
        """Static method - doesn't need instance."""
        return "Static method called"

    @classmethod
    def class_method(cls):
        """Class method - receives class as first argument."""
        return f"Class method called from {cls.__name__}"


obj = Example(42)

print("Built-in decorators:")
print(f"  Property: {obj.value}")
obj.value = 100
print(f"  After setter: {obj.value}")
print(f"  Static method: {Example.static_method()}")
print(f"  Class method: {Example.class_method()}")

# functools.lru_cache
from functools import lru_cache


@lru_cache(maxsize=128)
def expensive_computation(n):
    """An expensive computation with caching."""
    print(f"  Computing for n={n}")
    return sum(i * i for i in range(n))


print("\nlru_cache decorator:")
print(f"  Result for n=1000: {expensive_computation(1000)}")
print(f"  Cached result: {expensive_computation(1000)}")  # No computation
print(f"  Cache info: {expensive_computation.cache_info()}")

# =============================================================================
# SECTION 9: DECORATOR STACKING
# =============================================================================

print("\n" + "=" * 60)
print("DECORATOR STACKING")
print("=" * 60)


def decorator1(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        print("  Decorator1 - before")
        result = func(*args, **kwargs)
        print("  Decorator1 - after")
        return result
    return wrapper


def decorator2(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        print("  Decorator2 - before")
        result = func(*args, **kwargs)
        print("  Decorator2 - after")
        return result
    return wrapper


@decorator1
@decorator2
def stacked_function():
    print("  Function body")
    return "Result"


print("Stacked decorators (decorator1 wraps decorator2):")
result = stacked_function()

# =============================================================================
# MAIN EXECUTION
# =============================================================================

if __name__ == "__main__":
    print("\n" + "=" * 60)
    print("✅ You've learned about decorators!")
    print("📚 Next: Move to 05-modules to learn about Python modules")
    print("=" * 60)
