"""
Module: lists.py
Topic: Lists in Python
Level: Beginner

This file teaches you about:
- List creation and basics
- List indexing and slicing
- List methods
- List comprehensions
- List operations
"""

# =============================================================================
# SECTION 1: LIST CREATION
# =============================================================================

print("=" * 60)
print("LIST CREATION")
print("=" * 60)

# Different ways to create lists
list1 = [1, 2, 3, 4, 5]          # Direct creation
list2 = list(range(5))           # Using list() constructor
list3 = []                        # Empty list
list4 = list()                    # Empty list (constructor)
list5 = [x for x in range(5)]     # List comprehension

print(f"Direct creation: {list1}")
print(f"list(range(5)): {list2}")
print(f"Empty list []: {list3}")
print(f"list(): {list4}")
print(f"List comprehension: {list5}")

# Lists can contain different types
mixed = [1, "hello", 3.14, True, None, [1, 2]]
print(f"\nMixed type list: {mixed}")

# Nested lists
matrix = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
print(f"Nested list (matrix): {matrix}")

# =============================================================================
# SECTION 2: LIST INDEXING AND SLICING
# =============================================================================

print("\n" + "=" * 60)
print("LIST INDEXING AND SLICING")
print("=" * 60)

fruits = ['apple', 'banana', 'cherry', 'date', 'elderberry']

print(f"List: {fruits}")
print(f"\nIndexing:")
print(f"  fruits[0]: {fruits[0]}")      # First element
print(f"  fruits[-1]: {fruits[-1]}")    # Last element
print(f"  fruits[2]: {fruits[2]}")      # Third element

print(f"\nSlicing:")
print(f"  fruits[1:3]: {fruits[1:3]}")    # Elements 1 and 2
print(f"  fruits[:3]: {fruits[:3]}")      # First three elements
print(f"  fruits[2:]: {fruits[2:]}")      # From index 2 to end
print(f"  fruits[::2]: {fruits[::2]}")    # Every second element
print(f"  fruits[::-1]: {fruits[::-1]}")  # Reversed

# Nested list indexing
matrix = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
print(f"\nNested list indexing:")
print(f"  matrix[0]: {matrix[0]}")
print(f"  matrix[0][1]: {matrix[0][1]}")

# =============================================================================
# SECTION 3: LIST METHODS - ADDING ELEMENTS
# =============================================================================

print("\n" + "=" * 60)
print("LIST METHODS - ADDING ELEMENTS")
print("=" * 60)

# append() - Add single element at end
fruits = ['apple', 'banana']
print(f"Original: {fruits}")
fruits.append('cherry')
print(f"After append('cherry'): {fruits}")

# extend() - Add multiple elements
fruits.extend(['date', 'elderberry'])
print(f"After extend(['date', 'elderberry']): {fruits}")

# insert() - Add at specific position
fruits.insert(1, 'apricot')
print(f"After insert(1, 'apricot'): {fruits}")

# Using + operator
vegetables = ['carrot', 'broccoli']
produce = fruits + vegetables
print(f"\nUsing + operator: {produce}")

# =============================================================================
# SECTION 4: LIST METHODS - REMOVING ELEMENTS
# =============================================================================

print("\n" + "=" * 60)
print("LIST METHODS - REMOVING ELEMENTS")
print("=" * 60)

numbers = [1, 2, 3, 4, 5, 3, 6, 7]
print(f"Original: {numbers}")

# remove() - Remove first occurrence of value
numbers.remove(3)
print(f"After remove(3): {numbers}")

# pop() - Remove and return by index (default: last)
popped = numbers.pop()
print(f"After pop(): {numbers}, popped: {popped}")

popped = numbers.pop(0)
print(f"After pop(0): {numbers}, popped: {popped}")

# del - Delete by index or slice
del numbers[1]
print(f"After del numbers[1]: {numbers}")

# clear() - Remove all elements
temp = [1, 2, 3]
temp.clear()
print(f"After clear(): {temp}")

# =============================================================================
# SECTION 5: LIST METHODS - MODIFYING AND SORTING
# =============================================================================

print("\n" + "=" * 60)
print("LIST METHODS - MODIFYING AND SORTING")
print("=" * 60)

# Modify by index
numbers = [1, 2, 3, 4, 5]
numbers[0] = 10
print(f"Modify index 0: {numbers}")

# Modify slice
numbers[1:3] = [20, 30]
print(f"Modify slice [1:3]: {numbers}")

# sort() - Sort in place
numbers = [3, 1, 4, 1, 5, 9, 2, 6]
numbers.sort()
print(f"After sort(): {numbers}")

numbers.sort(reverse=True)
print(f"After sort(reverse=True): {numbers}")

# Sort with key function
words = ['apple', 'pie', 'a', 'longer']
words.sort(key=len)
print(f"Sort by length: {words}")

# sorted() - Returns new sorted list
numbers = [3, 1, 4, 1, 5]
sorted_numbers = sorted(numbers)
print(f"\nsorted() returns new list:")
print(f"  Original: {numbers}")
print(f"  Sorted: {sorted_numbers}")

# reverse() - Reverse in place
numbers = [1, 2, 3, 4, 5]
numbers.reverse()
print(f"\nAfter reverse(): {numbers}")

# reversed() - Returns iterator
reversed_list = list(reversed([1, 2, 3]))
print(f"reversed([1,2,3]): {reversed_list}")

# =============================================================================
# SECTION 6: LIST METHODS - SEARCHING AND COUNTING
# =============================================================================

print("\n" + "=" * 60)
print("LIST METHODS - SEARCHING AND COUNTING")
print("=" * 60)

fruits = ['apple', 'banana', 'cherry', 'banana', 'date']

# index() - Find first index of value
print(f"List: {fruits}")
print(f"  index('banana'): {fruits.index('banana')}")
print(f"  index('banana', 2): {fruits.index('banana', 2)}")  # Start from index 2

# count() - Count occurrences
print(f"  count('banana'): {fruits.count('banana')}")

# in operator
print(f"\nMembership:")
print(f"  'cherry' in fruits: {'cherry' in fruits}")
print(f"  'grape' in fruits: {'grape' in fruits}")

# =============================================================================
# SECTION 7: LIST COMPREHENSIONS
# =============================================================================

print("\n" + "=" * 60)
print("LIST COMPREHENSIONS")
print("=" * 60)

# Basic syntax: [expression for item in iterable]
squares = [x**2 for x in range(10)]
print(f"Squares: {squares}")

# With condition
even_squares = [x**2 for x in range(10) if x % 2 == 0]
print(f"Even squares: {even_squares}")

# With if-else
labels = ['even' if x % 2 == 0 else 'odd' for x in range(5)]
print(f"Labels: {labels}")

# Nested comprehension
matrix = [[i * j for j in range(1, 4)] for i in range(1, 4)]
print(f"Multiplication table: {matrix}")

# Flattening nested lists
nested = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
flattened = [num for row in nested for num in row]
print(f"Flattened: {flattened}")

# Using functions in comprehensions
def celsius_to_fahrenheit(c):
    return c * 9/5 + 32

celsius = [0, 10, 20, 30, 40]
fahrenheit = [celsius_to_fahrenheit(c) for c in celsius]
print(f"\nCelsius: {celsius}")
print(f"Fahrenheit: {fahrenheit}")

# =============================================================================
# SECTION 8: LIST OPERATIONS
# =============================================================================

print("\n" + "=" * 60)
print("LIST OPERATIONS")
print("=" * 60)

# Concatenation
list1 = [1, 2, 3]
list2 = [4, 5, 6]
print(f"Concatenation: {list1 + list2}")

# Repetition
print(f"Repetition: {list1 * 3}")

# Length
print(f"Length: {len(list1)}")

# Min, Max, Sum
numbers = [1, 5, 2, 8, 3]
print(f"\nNumbers: {numbers}")
print(f"  min(): {min(numbers)}")
print(f"  max(): {max(numbers)}")
print(f"  sum(): {sum(numbers)}")

# Membership
print(f"\nMembership:")
print(f"  3 in {numbers}: {3 in numbers}")
print(f"  10 in {numbers}: {10 in numbers}")

# Iteration
print(f"\nIteration with enumerate:")
for i, num in enumerate(numbers):
    print(f"  Index {i}: {num}")

# =============================================================================
# SECTION 9: COPYING LISTS
# =============================================================================

print("\n" + "=" * 60)
print("COPYING LISTS")
print("=" * 60)

original = [1, 2, [3, 4]]

# Shallow copy methods
copy1 = original.copy()
copy2 = original[:]
copy3 = list(original)

print(f"Original: {original}")
print(f"copy(): {copy1}")
print(f"[:] slice: {copy2}")
print(f"list(): {copy3}")

# Modifying shallow copy doesn't affect original (for top level)
copy1[0] = 100
print(f"\nAfter modifying copy1[0] = 100:")
print(f"  Original: {original}")
print(f"  Copy: {copy1}")

# BUT nested objects are shared!
copy1[2][0] = 300
print(f"\nAfter modifying copy1[2][0] = 300:")
print(f"  Original: {original}")  # Also changed!
print(f"  Copy: {copy1}")

# Deep copy
import copy
original = [1, 2, [3, 4]]
deep_copy = copy.deepcopy(original)
deep_copy[2][0] = 300
print(f"\nDeep copy:")
print(f"  Original: {original}")  # Unchanged
print(f"  Deep copy: {deep_copy}")

# =============================================================================
# SECTION 10: COMMON PATTERNS
# =============================================================================

print("\n" + "=" * 60)
print("COMMON PATTERNS")
print("=" * 60)

# Unpacking
coordinates = [10, 20, 30]
x, y, z = coordinates
print(f"Unpacking: x={x}, y={y}, z={z}")

# Extended unpacking
first, *middle, last = [1, 2, 3, 4, 5]
print(f"Extended unpacking: first={first}, middle={middle}, last={last}")

# Zip
names = ['Alice', 'Bob', 'Charlie']
ages = [25, 30, 35]
zipped = list(zip(names, ages))
print(f"\nZip: {zipped}")

# Filter with list comprehension
numbers = range(10)
evens = [n for n in numbers if n % 2 == 0]
print(f"Filter evens: {evens}")

# Map with list comprehension
doubled = [n * 2 for n in numbers]
print(f"Map doubled: {doubled}")

# =============================================================================
# SECTION 11: PRACTICAL EXAMPLES
# =============================================================================

print("\n" + "=" * 60)
print("PRACTICAL EXAMPLES")
print("=" * 60)


def find_duplicates(items):
    """Find duplicate elements in a list."""
    seen = []
    duplicates = []
    for item in items:
        if item in seen and item not in duplicates:
            duplicates.append(item)
        else:
            seen.append(item)
    return duplicates


print("\nFind Duplicates:")
data = [1, 2, 3, 2, 4, 5, 3, 6, 7, 5]
print(f"  Data: {data}")
print(f"  Duplicates: {find_duplicates(data)}")


def rotate_list(lst, k):
    """Rotate list by k positions."""
    if not lst:
        return lst
    k = k % len(lst)  # Handle k > len(lst)
    return lst[-k:] + lst[:-k]


print(f"\nRotate List:")
lst = [1, 2, 3, 4, 5]
print(f"  Original: {lst}")
print(f"  Rotate by 2: {rotate_list(lst, 2)}")
print(f"  Rotate by -1: {rotate_list(lst, -1)}")


def merge_sorted_lists(list1, list2):
    """Merge two sorted lists into one sorted list."""
    result = []
    i = j = 0
    while i < len(list1) and j < len(list2):
        if list1[i] <= list2[j]:
            result.append(list1[i])
            i += 1
        else:
            result.append(list2[j])
            j += 1
    result.extend(list1[i:])
    result.extend(list2[j:])
    return result


print(f"\nMerge Sorted Lists:")
list1 = [1, 3, 5, 7]
list2 = [2, 4, 6, 8]
print(f"  List 1: {list1}")
print(f"  List 2: {list2}")
print(f"  Merged: {merge_sorted_lists(list1, list2)}")


def chunk_list(lst, size):
    """Split list into chunks of specified size."""
    return [lst[i:i + size] for i in range(0, len(lst), size)]


print(f"\nChunk List:")
lst = [1, 2, 3, 4, 5, 6, 7, 8, 9]
print(f"  Original: {lst}")
print(f"  Chunks of 3: {chunk_list(lst, 3)}")

# =============================================================================
# MAIN EXECUTION
# =============================================================================

if __name__ == "__main__":
    print("\n" + "=" * 60)
    print("✅ You've learned about Python lists!")
    print("📚 Next: Learn about tuples in tuples.py")
    print("=" * 60)
