"""
Module: lambda_functions.py
Topic: Lambda Functions
Level: Intermediate

This file teaches you about:
- Lambda function syntax
- When to use lambdas
- map(), filter(), reduce()
- Lambda with sorted()
- Lambda pitfalls
"""

# =============================================================================
# SECTION 1: LAMBDA BASICS
# =============================================================================

print("=" * 60)
print("LAMBDA BASICS")
print("=" * 60)

# Lambda syntax: lambda arguments: expression

# Regular function
def square(x):
    return x ** 2


# Equivalent lambda
square_lambda = lambda x: x ** 2

print(f"Regular function: square(5) = {square(5)}")
print(f"Lambda function: square_lambda(5) = {square_lambda(5)}")

# Lambda with multiple arguments
add = lambda a, b: a + b
print(f"\nadd(3, 4) = {add(3, 4)}")

# Lambda with default arguments
greet = lambda name, greeting="Hello": f"{greeting}, {name}!"
print(f"greet('Alice') = {greet('Alice')}")
print(f"greet('Bob', 'Hi') = {greet('Bob', 'Hi')}")

# Lambda with conditional
is_even = lambda x: "even" if x % 2 == 0 else "odd"
print(f"\nis_even(4) = {is_even(4)}")
print(f"is_even(5) = {is_even(5)}")

# =============================================================================
# SECTION 2: WHEN TO USE LAMBDAS
# =============================================================================

print("\n" + "=" * 60)
print("WHEN TO USE LAMBDAS")
print("=" * 60)

# Good use case: short, simple operations
numbers = [1, 2, 3, 4, 5]
squared = list(map(lambda x: x ** 2, numbers))
print(f"Square numbers: {squared}")

# Good use case: callback functions
button_click = lambda: print("Button clicked!")
print("\nSimulating button click:")
button_click()

# Good use case: key functions
students = [('Alice', 85), ('Bob', 92), ('Charlie', 78), ('Diana', 95)]
sorted_by_grade = sorted(students, key=lambda x: x[1], reverse=True)
print(f"\nStudents sorted by grade: {sorted_by_grade}")

# Bad use case: complex logic (use regular functions instead)
# DON'T do this:
# complex_lambda = lambda x: x**2 if x > 0 else -x**2 if x < 0 else 0

# DO this instead:
def complex_function(x):
    """Complex logic belongs in a named function."""
    if x > 0:
        return x ** 2
    elif x < 0:
        return -(x ** 2)
    return 0


# =============================================================================
# SECTION 3: MAP FUNCTION
# =============================================================================

print("\n" + "=" * 60)
print("MAP FUNCTION")
print("=" * 60)

# map(function, iterable) applies function to each element
numbers = [1, 2, 3, 4, 5]

# Using lambda with map
doubled = list(map(lambda x: x * 2, numbers))
print(f"Doubled: {doubled}")

# Map with multiple iterables
list1 = [1, 2, 3]
list2 = [10, 20, 30]
sums = list(map(lambda x, y: x + y, list1, list2))
print(f"Sum of two lists: {sums}")

# Map vs list comprehension (comprehension often more readable)
numbers = [1, 2, 3, 4, 5]

# Using map
squares_map = list(map(lambda x: x ** 2, numbers))

# Using list comprehension (Pythonic way)
squares_comp = [x ** 2 for x in numbers]

print(f"\nMap result: {squares_map}")
print(f"Comprehension result: {squares_comp}")

# Map with built-in functions
words = ['hello', 'world', 'python']
uppercased = list(map(str.upper, words))
print(f"\nUppercased: {uppercased}")

# Map with None (converts to list of tuples)
keys = ['name', 'age', 'city']
values = ['Alice', 25, 'NYC']
pairs = list(zip(keys, values))
print(f"\nZipped pairs: {pairs}")

# =============================================================================
# SECTION 4: FILTER FUNCTION
# =============================================================================

print("\n" + "=" * 60)
print("FILTER FUNCTION")
print("=" * 60)

# filter(function, iterable) keeps elements where function returns True
numbers = list(range(1, 11))

# Filter even numbers
evens = list(filter(lambda x: x % 2 == 0, numbers))
print(f"Even numbers: {evens}")

# Filter with condition
words = ['apple', 'banana', 'cherry', 'date', 'elderberry']
long_words = list(filter(lambda x: len(x) > 5, words))
print(f"Long words (>5 chars): {long_words}")

# Filter with None (removes falsy values)
mixed = [0, 1, False, True, '', 'hello', None, [], [1, 2]]
truthy = list(filter(None, mixed))
print(f"\nTruthy values: {truthy}")

# Filter vs list comprehension
numbers = list(range(1, 11))

# Using filter
evens_filter = list(filter(lambda x: x % 2 == 0, numbers))

# Using list comprehension (often more readable)
evens_comp = [x for x in numbers if x % 2 == 0]

print(f"\nFilter: {evens_filter}")
print(f"Comprehension: {evens_comp}")

# Combining map and filter
numbers = list(range(1, 11))
result = list(map(lambda x: x ** 2, filter(lambda x: x % 2 == 0, numbers)))
print(f"\nSquares of evens: {result}")

# Same with list comprehension (more readable)
result_comp = [x ** 2 for x in numbers if x % 2 == 0]
print(f"Same with comprehension: {result_comp}")

# =============================================================================
# SECTION 5: REDUCE FUNCTION
# =============================================================================

print("\n" + "=" * 60)
print("REDUCE FUNCTION")
print("=" * 60)

from functools import reduce

# reduce(function, iterable) reduces to single value
numbers = [1, 2, 3, 4, 5]

# Sum using reduce
total = reduce(lambda x, y: x + y, numbers)
print(f"Sum: {total}")

# Product using reduce
product = reduce(lambda x, y: x * y, numbers)
print(f"Product: {product}")

# Find maximum
maximum = reduce(lambda x, y: x if x > y else y, numbers)
print(f"Maximum: {maximum}")

# With initial value
total_with_init = reduce(lambda x, y: x + y, numbers, 100)
print(f"\nSum with initial 100: {total_with_init}")

# Building a result
words = ['Hello', 'World', 'Python']
sentence = reduce(lambda x, y: f"{x} {y}", words)
print(f"Sentence: {sentence}")

# Practical example: flatten nested lists
nested = [[1, 2], [3, 4], [5, 6]]
flattened = reduce(lambda x, y: x + y, nested)
print(f"\nFlattened: {flattened}")

# =============================================================================
# SECTION 6: LAMBDA WITH SORTED
# =============================================================================

print("\n" + "=" * 60)
print("LAMBDA WITH SORTED")
print("=" * 60)

# Sort by custom key
students = [
    {'name': 'Alice', 'grade': 85},
    {'name': 'Bob', 'grade': 92},
    {'name': 'Charlie', 'grade': 78},
    {'name': 'Diana', 'grade': 95}
]

# Sort by grade
by_grade = sorted(students, key=lambda x: x['grade'], reverse=True)
print("Sorted by grade (descending):")
for student in by_grade:
    print(f"  {student['name']}: {student['grade']}")

# Sort by name length
by_name_length = sorted(students, key=lambda x: len(x['name']))
print("\nSorted by name length:")
for student in by_name_length:
    print(f"  {student['name']}")

# Sort tuple elements
items = [('apple', 3), ('banana', 1), ('cherry', 2)]
sorted_items = sorted(items, key=lambda x: x[1])
print(f"\nSorted by quantity: {sorted_items}")

# Sort by multiple keys
people = [
    ('Alice', 25, 'Engineer'),
    ('Bob', 25, 'Designer'),
    ('Charlie', 30, 'Engineer'),
    ('Diana', 30, 'Designer')
]

# Sort by age, then by name
sorted_people = sorted(people, key=lambda x: (x[1], x[0]))
print(f"\nSorted by age, then name: {sorted_people}")

# =============================================================================
# SECTION 7: LAMBDA WITH DATA STRUCTURES
# =============================================================================

print("\n" + "=" * 60)
print("LAMBDA WITH DATA STRUCTURES")
print("=" * 60)

# Dictionary of lambdas
operations = {
    'add': lambda x, y: x + y,
    'subtract': lambda x, y: x - y,
    'multiply': lambda x, y: x * y,
    'divide': lambda x, y: x / y if y != 0 else None
}

print("Calculator operations:")
print(f"  add(10, 5): {operations['add'](10, 5)}")
print(f"  multiply(10, 5): {operations['multiply'](10, 5)}")

# List of lambdas
transforms = [
    lambda x: x.upper(),
    lambda x: x.lower(),
    lambda x: x.title(),
    lambda x: x[::-1]
]

text = "Hello World"
print(f"\nTransformations of '{text}':")
for i, transform in enumerate(transforms):
    print(f"  Transform {i + 1}: {transform(text)}")

# =============================================================================
# SECTION 8: PRACTICAL EXAMPLES
# =============================================================================

print("\n" + "=" * 60)
print("PRACTICAL EXAMPLES")
print("=" * 60)


def process_data(data, operations):
    """
    Apply a series of operations to data.
    operations: list of (function, description) tuples
    """
    results = []
    current = data

    for operation, description in operations:
        current = operation(current)
        results.append((description, current))

    return results


data = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
ops = [
    (lambda x: list(filter(lambda n: n % 2 == 0, x)), "Filter evens"),
    (lambda x: list(map(lambda n: n ** 2, x)), "Square"),
    (lambda x: list(filter(lambda n: n < 50, x)), "Less than 50"),
    (lambda x: sum(x), "Sum")
]

print("Data processing pipeline:")
results = process_data(data, ops)
for desc, result in results:
    print(f"  {desc}: {result}")


def create_multiplier(n):
    """Create a multiplier function."""
    return lambda x: x * n


print("\nFunction factory:")
double = create_multiplier(2)
triple = create_multiplier(3)
print(f"  double(5): {double(5)}")
print(f"  triple(5): {triple(5)}")


def group_by(items, key_func):
    """Group items by a key function."""
    groups = {}
    for item in items:
        key = key_func(item)
        if key not in groups:
            groups[key] = []
        groups[key].append(item)
    return groups


words = ['apple', 'banana', 'cherry', 'apricot', 'blueberry', 'avocado']
by_first_letter = group_by(words, lambda x: x[0])

print("\nGroup by first letter:")
for letter, word_list in sorted(by_first_letter.items()):
    print(f"  {letter}: {word_list}")


def analyze_text(text):
    """Analyze text using various metrics."""
    words = text.split()

    metrics = {
        'word_count': len(words),
        'char_count': len(text),
        'avg_word_length': sum(map(len, words)) / len(words) if words else 0,
        'unique_words': len(set(map(str.lower, words))),
        'longest_word': max(words, key=len) if words else '',
        'shortest_word': min(words, key=len) if words else ''
    }

    return metrics


sample = "The quick brown fox jumps over the lazy dog"
print(f"\nText analysis of '{sample}':")
metrics = analyze_text(sample)
for key, value in metrics.items():
    print(f"  {key}: {value}")

# =============================================================================
# SECTION 9: LAMBDA PITFALLS
# =============================================================================

print("\n" + "=" * 60)
print("LAMBDA PITFALLS")
print("=" * 60)

# Pitfall 1: Late binding in loops
print("Pitfall 1: Late binding")
functions = [lambda x: x + i for i in range(5)]
print(f"  Wrong: {[f(10) for f in functions]}")  # All add 4!

# Correct way with default argument
functions = [lambda x, i=i: x + i for i in range(5)]
print(f"  Correct: {[f(10) for f in functions]}")

# Pitfall 2: Overly complex lambdas
# Don't write complex lambdas like this:
# complex_lambda = lambda x: (x**2 if x > 0 else -x**2) if isinstance(x, (int, float)) else None

# Instead, use a proper function:
def proper_function(x):
    if not isinstance(x, (int, float)):
        return None
    return x ** 2 if x > 0 else -(x ** 2)


print("\nPitfall 2: Complexity")
print(f"  Use proper functions for complex logic")

# Pitfall 3: Losing debug information
# Lambda functions have generic __name__
add_lambda = lambda x, y: x + y


def add_function(x, y):
    return x + y


print(f"\nPitfall 3: Debug info")
print(f"  Lambda name: {add_lambda.__name__}")
print(f"  Function name: {add_function.__name__}")

# =============================================================================
# MAIN EXECUTION
# =============================================================================

if __name__ == "__main__":
    print("\n" + "=" * 60)
    print("✅ You've learned about lambda functions!")
    print("📚 Next: Learn about decorators in decorators_intro.py")
    print("=" * 60)
