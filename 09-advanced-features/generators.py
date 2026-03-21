"""
Module: generators.py
Topic: Generators in Python
Level: Advanced

This file teaches you about:
- Generator functions and yield
- Generator expressions
- yield from
- Generator pipelines
- Memory efficiency
"""

# =============================================================================
# SECTION 1: GENERATOR FUNCTIONS
# =============================================================================

print("=" * 60)
print("GENERATOR FUNCTIONS")
print("=" * 60)


def count_up_to(n):
    """A simple generator that counts up to n."""
    count = 1
    while count <= n:
        yield count
        count += 1


# Using the generator
print("count_up_to(5):")
for num in count_up_to(5):
    print(f"  {num}")

# Generators return an iterator
counter = count_up_to(3)
print(f"\nType: {type(counter)}")
print(f"next(): {next(counter)}")
print(f"next(): {next(counter)}")
print(f"next(): {next(counter)}")
# next(counter)  # Would raise StopIteration

# =============================================================================
# SECTION 2: GENERATOR EXPRESSIONS
# =============================================================================

print("\n" + "=" * 60)
print("GENERATOR EXPRESSIONS")
print("=" * 60)

# List comprehension (creates entire list in memory)
squares_list = [x**2 for x in range(10)]
print(f"List: {squares_list}")

# Generator expression (lazy evaluation)
squares_gen = (x**2 for x in range(10))
print(f"Generator: {squares_gen}")
print(f"Values: {list(squares_gen)}")

# Memory efficiency demo
import sys

big_list = [x for x in range(10000)]
big_gen = (x for x in range(10000))

print(f"\nMemory comparison:")
print(f"  List size: {sys.getsizeof(big_list)} bytes")
print(f"  Generator size: {sys.getsizeof(big_gen)} bytes")

# =============================================================================
# SECTION 3: YIELD FROM
# =============================================================================

print("\n" + "=" * 60)
print("YIELD FROM")
print("=" * 60)


def flatten(nested):
    """Flatten a nested list using yield from."""
    for item in nested:
        if isinstance(item, list):
            yield from flatten(item)
        else:
            yield item


nested = [1, [2, 3], [4, [5, 6]], 7]
print(f"Nested: {nested}")
print(f"Flattened: {list(flatten(nested))}")


# yield from with generators
def chain_generators(*gens):
    """Chain multiple generators together."""
    for gen in gens:
        yield from gen


gen1 = (x for x in range(3))
gen2 = (x for x in range(3, 6))
print(f"\nChained: {list(chain_generators(gen1, gen2))}")

# =============================================================================
# SECTION 4: GENERATOR PIPEELINES
# =============================================================================

print("\n" + "=" * 60)
print("GENERATOR PIPELINES")
print("=" * 60)


def read_lines(text):
    """Yield lines from text."""
    for line in text.split('\n'):
        yield line.strip()


def filter_comments(lines):
    """Filter out comment lines."""
    for line in lines:
        if line and not line.startswith('#'):
            yield line


def to_uppercase(lines):
    """Convert lines to uppercase."""
    for line in lines:
        yield line.upper()


# Pipeline
text = """
# Configuration file
name: alice
age: 25
# End of config
"""

pipeline = to_uppercase(filter_comments(read_lines(text)))
print("Pipeline result:")
for line in pipeline:
    print(f"  {line}")

# =============================================================================
# SECTION 5: INFINITE GENERATORS
# =============================================================================

print("\n" + "=" * 60)
print("INFINITE GENERATORS")
print("=" * 60)

from itertools import islice


def fibonacci():
    """Generate infinite Fibonacci sequence."""
    a, b = 0, 1
    while True:
        yield a
        a, b = b, a + b


def primes():
    """Generate infinite prime numbers."""
    num = 2
    while True:
        if all(num % i != 0 for i in range(2, int(num ** 0.5) + 1)):
            yield num
        num += 1


# Using islice to limit output
print("First 10 Fibonacci numbers:")
print(f"  {list(islice(fibonacci(), 10))}")

print("\nFirst 10 prime numbers:")
print(f"  {list(islice(primes(), 10))}")

# =============================================================================
# SECTION 6: COROUTINE-STYLE GENERATORS
# =============================================================================

print("\n" + "=" * 60)
print("COROUTINE-STYLE GENERATORS (send)")
print("=" * 60)


def accumulator():
    """A generator that accumulates sent values."""
    total = 0
    while True:
        value = yield total
        if value is None:
            break
        total += value


acc = accumulator()
next(acc)  # Prime the generator

print("Accumulator:")
print(f"  Send 10: {acc.send(10)}")
print(f"  Send 20: {acc.send(20)}")
print(f"  Send 30: {acc.send(30)}")

acc.close()

# =============================================================================
# SECTION 7: PRACTICAL EXAMPLES
# =============================================================================

print("\n" + "=" * 60)
print("PRACTICAL EXAMPLES")
print("=" * 60)


def chunked(iterable, size):
    """Yield chunks of specified size."""
    chunk = []
    for item in iterable:
        chunk.append(item)
        if len(chunk) == size:
            yield chunk
            chunk = []
    if chunk:
        yield chunk


print("Chunked [1-10] into 3s:")
for chunk in chunked(range(1, 11), 3):
    print(f"  {chunk}")


def sliding_window(iterable, size):
    """Yield sliding windows."""
    from collections import deque
    window = deque(maxlen=size)
    for item in iterable:
        window.append(item)
        if len(window) == size:
            yield tuple(window)


print("\nSliding window of size 3:")
for window in sliding_window([1, 2, 3, 4, 5], 3):
    print(f"  {window}")


def file_lines(filename):
    """Yield lines from a file (example)."""
    # In real use:
    # with open(filename) as f:
    #     for line in f:
    #         yield line.strip()
    pass


def batch_processor(items, process_func, batch_size=100):
    """Process items in batches."""
    batch = []
    for item in items:
        batch.append(process_func(item))
        if len(batch) >= batch_size:
            yield batch
            batch = []
    if batch:
        yield batch


# =============================================================================
# MAIN EXECUTION
# =============================================================================

if __name__ == "__main__":
    print("\n" + "=" * 60)
    print("✅ You've learned about generators!")
    print("=" * 60)
