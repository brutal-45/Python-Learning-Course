"""
Exercises: Advanced Python
Level: Advanced
Description: Practice problems for advanced Python concepts.
"""

import time
from functools import wraps
from contextlib import contextmanager
import asyncio


# =============================================================================
# EXERCISE 1: CUSTOM CONTEXT MANAGER
# =============================================================================

@contextmanager
def timer(name="Block"):
    """Context manager to time code execution."""
    start = time.time()
    print(f"  {name} started...")
    yield
    elapsed = time.time() - start
    print(f"  {name} completed in {elapsed:.4f}s")


print("=" * 50)
print("Exercise 1: Timer Context Manager")
with timer("Processing"):
    time.sleep(0.1)
    print("  Working...")


# =============================================================================
# EXERCISE 2: RETRY DECORATOR
# =============================================================================

def retry(max_attempts=3, delay=0.1):
    """Retry decorator."""
    def decorator(func):
        @wraps(func)
        def wrapper(*args, **kwargs):
            for attempt in range(max_attempts):
                try:
                    return func(*args, **kwargs)
                except Exception as e:
                    if attempt == max_attempts - 1:
                        raise
                    time.sleep(delay)
        return wrapper
    return decorator


print("\n" + "=" * 50)
print("Exercise 2: Retry Decorator")

attempts = 0

@retry(max_attempts=3)
def flaky_function():
    global attempts
    attempts += 1
    if attempts < 3:
        raise ValueError("Failed")
    return "Success!"

print(f"  Result: {flaky_function()}")


# =============================================================================
# EXERCISE 3: GENERATOR PIPELINE
# =============================================================================

def positive_squares(numbers):
    """Generator: filter negatives and square."""
    for n in numbers:
        if n >= 0:
            yield n ** 2


print("\n" + "=" * 50)
print("Exercise 3: Generator Pipeline")
import random
random.seed(42)
numbers = [random.randint(-5, 5) for _ in range(10)]
result = sum(positive_squares(numbers))
print(f"  Input: {numbers}")
print(f"  Sum of positive squares: {result}")


# =============================================================================
# EXERCISE 4: DESCRIPTOR
# =============================================================================

class PositiveNumber:
    """Descriptor ensuring positive values."""
    
    def __set_name__(self, owner, name):
        self.name = f"_{name}"

    def __get__(self, obj, objtype=None):
        return getattr(obj, self.name, 0)

    def __set__(self, obj, value):
        if value < 0:
            raise ValueError("Must be positive")
        setattr(obj, self.name, value)


print("\n" + "=" * 50)
print("Exercise 4: Descriptor")

class Account:
    balance = PositiveNumber()

acc = Account()
acc.balance = 100
print(f"  Balance: {acc.balance}")

try:
    acc.balance = -50
except ValueError as e:
    print(f"  Error: {e}")


# =============================================================================
# EXERCISE 5: ASYNC OPERATIONS
# =============================================================================

async def fetch_data(name, delay):
    """Simulate async fetch."""
    await asyncio.sleep(delay)
    return f"Data from {name}"


async def fetch_all():
    """Fetch concurrently."""
    results = await asyncio.gather(
        fetch_data("API-1", 0.1),
        fetch_data("API-2", 0.2),
        fetch_data("API-3", 0.1)
    )
    return results


print("\n" + "=" * 50)
print("Exercise 5: Async Operations")
results = asyncio.run(fetch_all())
print(f"  Results: {results}")


# =============================================================================
# CHALLENGE: LRU CACHE
# =============================================================================

from threading import Lock
from collections import OrderedDict


class SimpleCache:
    """Simple LRU cache with TTL."""
    
    def __init__(self, maxsize=100, ttl=60):
        self.maxsize = maxsize
        self.ttl = ttl
        self.cache = OrderedDict()
        self.lock = Lock()

    def get(self, key):
        with self.lock:
            if key in self.cache:
                value, timestamp = self.cache[key]
                if time.time() - timestamp < self.ttl:
                    self.cache.move_to_end(key)
                    return value
                del self.cache[key]
        return None

    def set(self, key, value):
        with self.lock:
            if key in self.cache:
                del self.cache[key]
            elif len(self.cache) >= self.maxsize:
                self.cache.popitem(last=False)
            self.cache[key] = (value, time.time())


print("\n" + "=" * 50)
print("Challenge: Simple Cache")

cache = SimpleCache(maxsize=3, ttl=10)
cache.set("a", 1)
cache.set("b", 2)
cache.set("c", 3)
print(f"  Get 'a': {cache.get('a')}")
cache.set("d", 4)  # Evicts 'b'
print(f"  Get 'b' (evicted): {cache.get('b')}")


# =============================================================================
# MAIN
# =============================================================================

if __name__ == "__main__":
    print("\n" + "=" * 50)
    print("✅ Advanced exercises completed!")
    print("=" * 50)
