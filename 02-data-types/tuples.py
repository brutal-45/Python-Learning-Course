"""
Module: tuples.py
Topic: Tuples in Python
Level: Beginner

This file teaches you about:
- Tuple creation and basics
- Tuple indexing and slicing
- Tuple methods
- Tuple unpacking
- Named tuples
- When to use tuples vs lists
"""

# =============================================================================
# SECTION 1: TUPLE CREATION
# =============================================================================

print("=" * 60)
print("TUPLE CREATION")
print("=" * 60)

# Different ways to create tuples
tuple1 = (1, 2, 3, 4, 5)          # With parentheses
tuple2 = 1, 2, 3, 4, 5            # Without parentheses (tuple packing)
tuple3 = tuple(range(5))          # Using tuple() constructor
tuple4 = ()                        # Empty tuple
tuple5 = tuple()                   # Empty tuple (constructor)
tuple6 = (42,)                     # Single element tuple (comma required!)

print(f"With parentheses: {tuple1}")
print(f"Without parentheses: {tuple2}")
print(f"tuple(range(5)): {tuple3}")
print(f"Empty tuple (): {tuple4}")
print(f"Single element (42,): {tuple6}")  # Note the comma!

# Common mistake: single element without comma
not_a_tuple = (42)  # This is just an integer!
print(f"\nWithout comma (42): {not_a_tuple}, type: {type(not_a_tuple)}")
print(f"With comma (42,): {tuple6}, type: {type(tuple6)}")

# =============================================================================
# SECTION 2: TUPLE CHARACTERISTICS
# =============================================================================

print("\n" + "=" * 60)
print("TUPLE CHARACTERISTICS")
print("=" * 60)

# Tuples are immutable
coordinates = (10, 20)
print(f"Tuple: {coordinates}")

try:
    coordinates[0] = 15  # This raises TypeError
except TypeError as e:
    print(f"Attempting to modify tuple raises: {type(e).__name__}")

# But tuples can contain mutable objects
mixed = (1, [2, 3], 4)
print(f"\nTuple with mutable list: {mixed}")
mixed[1].append(5)  # This works!
print(f"After appending to inner list: {mixed}")

# Tuple with different types
person = ("Alice", 25, "Engineer", True)
print(f"\nMixed types: {person}")

# Nested tuples
nested = ((1, 2), (3, 4), (5, 6))
print(f"Nested tuple: {nested}")

# =============================================================================
# SECTION 3: TUPLE INDEXING AND SLICING
# =============================================================================

print("\n" + "=" * 60)
print("TUPLE INDEXING AND SLICING")
print("=" * 60)

fruits = ('apple', 'banana', 'cherry', 'date', 'elderberry')

print(f"Tuple: {fruits}")
print(f"\nIndexing:")
print(f"  fruits[0]: {fruits[0]}")
print(f"  fruits[-1]: {fruits[-1]}")
print(f"  fruits[2]: {fruits[2]}")

print(f"\nSlicing:")
print(f"  fruits[1:3]: {fruits[1:3]}")
print(f"  fruits[:3]: {fruits[:3]}")
print(f"  fruits[2:]: {fruits[2:]}")
print(f"  fruits[::-1]: {fruits[::-1]}")

# Nested tuple indexing
matrix = ((1, 2, 3), (4, 5, 6), (7, 8, 9))
print(f"\nNested indexing:")
print(f"  matrix[0]: {matrix[0]}")
print(f"  matrix[0][1]: {matrix[0][1]}")

# =============================================================================
# SECTION 4: TUPLE UNPACKING
# =============================================================================

print("\n" + "=" * 60)
print("TUPLE UNPACKING")
print("=" * 60)

# Basic unpacking
point = (10, 20)
x, y = point
print(f"Basic unpacking: x={x}, y={y}")

# Unpacking with multiple variables
person = ("Alice", 25, "Engineer")
name, age, job = person
print(f"Multiple unpacking: name={name}, age={age}, job={job}")

# Extended unpacking with *
numbers = (1, 2, 3, 4, 5)
first, *middle, last = numbers
print(f"\nExtended unpacking:")
print(f"  first={first}, middle={middle}, last={last}")

first, *rest = numbers
print(f"  first={first}, rest={rest}")

*beginning, last = numbers
print(f"  beginning={beginning}, last={last}")

# Swapping variables
a, b = 10, 20
print(f"\nBefore swap: a={a}, b={b}")
a, b = b, a
print(f"After swap: a={a}, b={b}")

# Unpacking in loops
print("\nUnpacking in loops:")
pairs = [(1, 'a'), (2, 'b'), (3, 'c')]
for num, letter in pairs:
    print(f"  {num} -> {letter}")

# =============================================================================
# SECTION 5: TUPLE METHODS
# =============================================================================

print("\n" + "=" * 60)
print("TUPLE METHODS")
print("=" * 60)

# Tuples have only two methods: count() and index()
numbers = (1, 2, 3, 2, 4, 2, 5)

print(f"Tuple: {numbers}")
print(f"  count(2): {numbers.count(2)}")
print(f"  index(3): {numbers.index(3)}")
print(f"  index(2, 2): {numbers.index(2, 2)}")  # Start from index 2

# =============================================================================
# SECTION 6: TUPLE OPERATIONS
# =============================================================================

print("\n" + "=" * 60)
print("TUPLE OPERATIONS")
print("=" * 60)

# Concatenation
tuple1 = (1, 2, 3)
tuple2 = (4, 5, 6)
print(f"Concatenation: {tuple1 + tuple2}")

# Repetition
print(f"Repetition: {tuple1 * 3}")

# Membership
print(f"\nMembership:")
print(f"  2 in {tuple1}: {2 in tuple1}")
print(f"  5 in {tuple1}: {5 in tuple1}")

# Length, Min, Max, Sum
numbers = (3, 1, 4, 1, 5, 9)
print(f"\nTuple: {numbers}")
print(f"  len(): {len(numbers)}")
print(f"  min(): {min(numbers)}")
print(f"  max(): {max(numbers)}")
print(f"  sum(): {sum(numbers)}")

# Comparison (lexicographic)
print(f"\nComparison:")
print(f"  (1, 2, 3) < (1, 2, 4): {(1, 2, 3) < (1, 2, 4)}")
print(f"  (1, 2) < (1, 2, 3): {(1, 2) < (1, 2, 3)}")

# =============================================================================
# SECTION 7: TUPLES AS DICTIONARY KEYS
# =============================================================================

print("\n" + "=" * 60)
print("TUPLES AS DICTIONARY KEYS")
print("=" * 60)

# Tuples can be dictionary keys (lists cannot!)
locations = {
    (40.7128, -74.0060): "New York",
    (51.5074, -0.1278): "London",
    (35.6762, 139.6503): "Tokyo"
}

print("Using tuples as dictionary keys:")
for coords, city in locations.items():
    print(f"  {coords}: {city}")

# Look up by coordinates
ny_coords = (40.7128, -74.0060)
print(f"\nLookup {ny_coords}: {locations[ny_coords]}")

# Lists cannot be dictionary keys
try:
    bad_dict = {[1, 2]: "value"}
except TypeError as e:
    print(f"\nUsing list as key raises: {type(e).__name__}")

# =============================================================================
# SECTION 8: NAMED TUPLES
# =============================================================================

print("\n" + "=" * 60)
print("NAMED TUPLES")
print("=" * 60)

from collections import namedtuple

# Create a named tuple class
Point = namedtuple('Point', ['x', 'y'])
Person = namedtuple('Person', 'name age job')

# Create instances
p = Point(10, 20)
alice = Person("Alice", 25, "Engineer")

print(f"Point: {p}")
print(f"Person: {alice}")

# Access by name or index
print(f"\nAccess by name: p.x = {p.x}, p.y = {p.y}")
print(f"Access by index: p[0] = {p[0]}, p[1] = {p[1]}")

# Named tuple methods
print(f"\nNamed tuple methods:")
print(f"  _fields: {alice._fields}")
print(f"  _asdict(): {alice._asdict()}")

# Create from iterable
coords = [30, 40]
p2 = Point._make(coords)
print(f"  _make([30, 40]): {p2}")

# =============================================================================
# SECTION 9: TUPLES VS LISTS
# =============================================================================

print("\n" + "=" * 60)
print("TUPLES VS LISTS")
print("=" * 60)

import sys

# Memory usage
list_data = [1, 2, 3, 4, 5]
tuple_data = (1, 2, 3, 4, 5)

print("Memory usage comparison:")
print(f"  List size: {sys.getsizeof(list_data)} bytes")
print(f"  Tuple size: {sys.getsizeof(tuple_data)} bytes")

# Performance comparison
import timeit

print("\nCreation time (100000 iterations):")
list_time = timeit.timeit('[1, 2, 3, 4, 5]', number=100000)
tuple_time = timeit.timeit('(1, 2, 3, 4, 5)', number=100000)
print(f"  List: {list_time:.4f} seconds")
print(f"  Tuple: {tuple_time:.4f} seconds")

print("\nWhen to use TUPLES:")
print("  ✓ Data that shouldn't change (coordinates, constants)")
print("  ✓ Dictionary keys")
print("  ✓ Return multiple values from functions")
print("  ✓ Heterogeneous data (like a record)")

print("\nWhen to use LISTS:")
print("  ✓ Data that needs to be modified")
print("  ✓ Need to add/remove elements")
print("  ✓ Homogeneous data (like a collection)")
print("  ✓ Need sorting, reversing, etc.")

# =============================================================================
# SECTION 10: PRACTICAL EXAMPLES
# =============================================================================

print("\n" + "=" * 60)
print("PRACTICAL EXAMPLES")
print("=" * 60)


def get_statistics(numbers):
    """Return multiple statistics as a tuple."""
    if not numbers:
        return (None, None, None, None)
    
    minimum = min(numbers)
    maximum = max(numbers)
    total = sum(numbers)
    average = total / len(numbers)
    
    return (minimum, maximum, total, average)


print("\nReturning multiple values:")
data = [10, 20, 30, 40, 50]
stats = get_statistics(data)
print(f"  Data: {data}")
print(f"  Statistics: min={stats[0]}, max={stats[1]}, sum={stats[2]}, avg={stats[3]:.1f}")

# Unpack returned tuple
minimum, maximum, total, average = get_statistics(data)
print(f"  Unpacked: min={minimum}, max={maximum}")


def find_min_max(iterable):
    """Find minimum and maximum in a single pass."""
    iterator = iter(iterable)
    try:
        first = next(iterator)
    except StopIteration:
        return (None, None)
    
    minimum = maximum = first
    for value in iterator:
        if value < minimum:
            minimum = value
        if value > maximum:
            maximum = value
    
    return (minimum, maximum)


print(f"\nSingle pass min/max:")
numbers = [3, 1, 4, 1, 5, 9, 2, 6]
min_val, max_val = find_min_max(numbers)
print(f"  Numbers: {numbers}")
print(f"  Min: {min_val}, Max: {max_val}")


# Using tuples for safe data
DAYS_OF_WEEK = ('Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday', 'Sunday')
print(f"\nConstants (immutable): {DAYS_OF_WEEK}")

# =============================================================================
# MAIN EXECUTION
# =============================================================================

if __name__ == "__main__":
    print("\n" + "=" * 60)
    print("✅ You've learned about Python tuples!")
    print("📚 Next: Learn about dictionaries in dictionaries.py")
    print("=" * 60)
