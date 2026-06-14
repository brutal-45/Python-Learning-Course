"""
Module: loops.py
Topic: Loops in Python
Level: Beginner

This file teaches you about:
- for loops
- while loops
- range() function
- enumerate() function
- zip() function
- Nested loops
- Loop else clause
"""

# =============================================================================
# SECTION 1: FOR LOOPS - BASICS
# =============================================================================

print("=" * 60)
print("FOR LOOPS - BASICS")
print("=" * 60)

# Iterating over a list
fruits = ['apple', 'banana', 'cherry']

print("Iterating over a list:")
for fruit in fruits:
    print(f"  I like {fruit}")

# Iterating over a string
print("\nIterating over a string:")
for char in "Python":
    print(f"  Character: {char}")

# Iterating over a dictionary
person = {'name': 'Alice', 'age': 25, 'city': 'NYC'}

print("\nIterating over dictionary keys:")
for key in person:
    print(f"  {key}")

print("\nIterating over dictionary values:")
for value in person.values():
    print(f"  {value}")

print("\nIterating over dictionary items:")
for key, value in person.items():
    print(f"  {key}: {value}")

# =============================================================================
# SECTION 2: RANGE FUNCTION
# =============================================================================

print("\n" + "=" * 60)
print("RANGE FUNCTION")
print("=" * 60)

# range(stop) - 0 to stop-1
print("range(5):")
for i in range(5):
    print(f"  {i}", end="")
print()

# range(start, stop) - start to stop-1
print("\nrange(2, 7):")
for i in range(2, 7):
    print(f"  {i}", end="")
print()

# range(start, stop, step) - with step
print("\nrange(0, 10, 2):")
for i in range(0, 10, 2):
    print(f"  {i}", end="")
print()

# Negative step
print("\nrange(10, 0, -1):")
for i in range(10, 0, -1):
    print(f"  {i}", end="")
print()

# Converting range to list
numbers = list(range(5))
print(f"\nlist(range(5)): {numbers}")

# Using range with len()
words = ['hello', 'world', 'python']
print("\nUsing range with len():")
for i in range(len(words)):
    print(f"  Index {i}: {words[i]}")

# =============================================================================
# SECTION 3: ENUMERATE FUNCTION
# =============================================================================

print("\n" + "=" * 60)
print("ENUMERATE FUNCTION")
print("=" * 60)

# enumerate() returns index and value
fruits = ['apple', 'banana', 'cherry']

print("enumerate(fruits):")
for index, fruit in enumerate(fruits):
    print(f"  {index}: {fruit}")

# Starting index from a different number
print("\nenumerate(fruits, start=1):")
for index, fruit in enumerate(fruits, start=1):
    print(f"  {index}: {fruit}")

# Getting pairs
print("\nGetting index-value pairs:")
for pair in enumerate(fruits):
    print(f"  {pair}")

# =============================================================================
# SECTION 4: ZIP FUNCTION
# =============================================================================

print("\n" + "=" * 60)
print("ZIP FUNCTION")
print("=" * 60)

# zip() combines multiple iterables
names = ['Alice', 'Bob', 'Charlie']
ages = [25, 30, 35]
cities = ['NYC', 'LA', 'Chicago']

print("Combining with zip:")
for name, age, city in zip(names, ages, cities):
    print(f"  {name}, {age}, {city}")

# Creating a dictionary from two lists
keys = ['name', 'age', 'city']
values = ['Alice', 25, 'NYC']
person = dict(zip(keys, values))
print(f"\nDictionary from zip: {person}")

# zip with different length iterables
short = [1, 2, 3]
long = ['a', 'b', 'c', 'd', 'e']
print(f"\nzip stops at shortest:")
for num, letter in zip(short, long):
    print(f"  {num}: {letter}")

# zip_longest from itertools
from itertools import zip_longest

print(f"\nzip_longest fills missing with None:")
for num, letter in zip_longest(short, long, fillvalue='N/A'):
    print(f"  {num}: {letter}")

# =============================================================================
# SECTION 5: WHILE LOOPS
# =============================================================================

print("\n" + "=" * 60)
print("WHILE LOOPS")
print("=" * 60)

# Basic while loop
count = 0
print("Counting with while:")
while count < 5:
    print(f"  Count: {count}")
    count += 1

# While loop with user input simulation
print("\nSimulating user input:")
response = ""
attempts = 0
responses = ['', '', 'quit']
while response != 'quit' and attempts < 3:
    response = responses[attempts]
    print(f"  Attempt {attempts + 1}: response = '{response}'")
    attempts += 1
print("  Loop ended")

# While loop with condition
print("\nFinding first number > 100 divisible by 7:")
number = 101
while number % 7 != 0:
    number += 1
print(f"  Found: {number}")

# =============================================================================
# SECTION 6: LOOP ELSE CLAUSE
# =============================================================================

print("\n" + "=" * 60)
print("LOOP ELSE CLAUSE")
print("=" * 60)

# Else runs if loop completes without break
numbers = [1, 3, 5, 7, 9]
target = 4

print(f"Searching for {target} in {numbers}:")
for num in numbers:
    if num == target:
        print(f"  Found {target}!")
        break
else:
    print(f"  {target} not found in the list")

# Another example
print("\nChecking if all numbers are positive:")
numbers = [1, 2, 3, 4, 5]
for num in numbers:
    if num < 0:
        print("  Found negative number!")
        break
else:
    print("  All numbers are positive!")

# While with else
print("\nWhile with else:")
count = 0
while count < 3:
    print(f"  Count: {count}")
    count += 1
else:
    print("  Loop completed normally")

# =============================================================================
# SECTION 7: NESTED LOOPS
# =============================================================================

print("\n" + "=" * 60)
print("NESTED LOOPS")
print("=" * 60)

# Nested for loops
print("Multiplication table:")
for i in range(1, 4):
    for j in range(1, 4):
        product = i * j
        print(f"  {i} × {j} = {product}")
    print()

# Processing nested structures
matrix = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]

print("Processing a matrix:")
for row_idx, row in enumerate(matrix):
    for col_idx, value in enumerate(row):
        print(f"  matrix[{row_idx}][{col_idx}] = {value}")

# Pattern printing
print("\nPrinting a pattern:")
for i in range(1, 6):
    for j in range(i):
        print("*", end="")
    print()

# =============================================================================
# SECTION 8: ITERATING OVER COMPLEX STRUCTURES
# =============================================================================

print("\n" + "=" * 60)
print("ITERATING OVER COMPLEX STRUCTURES")
print("=" * 60)

# Dictionary of lists
students = {
    'Alice': [85, 90, 78],
    'Bob': [92, 88, 95],
    'Charlie': [75, 82, 80]
}

print("Student grades:")
for name, grades in students.items():
    average = sum(grades) / len(grades)
    print(f"  {name}: grades={grades}, average={average:.1f}")

# List of dictionaries
employees = [
    {'name': 'Alice', 'department': 'Engineering', 'salary': 80000},
    {'name': 'Bob', 'department': 'Marketing', 'salary': 65000},
    {'name': 'Charlie', 'department': 'Engineering', 'salary': 90000}
]

print("\nEmployees by department:")
departments = {}
for emp in employees:
    dept = emp['department']
    if dept not in departments:
        departments[dept] = []
    departments[dept].append(emp['name'])

for dept, names in departments.items():
    print(f"  {dept}: {names}")

# =============================================================================
# SECTION 9: ITERATING WITH ITEMS
# =============================================================================

print("\n" + "=" * 60)
print("ITERATING WITH ITEMS() AND DICT METHODS")
print("=" * 60)

# Safe iteration over dictionary
prices = {'apple': 0.5, 'banana': 0.3, 'orange': 0.8}

print("Calculating totals:")
quantities = {'apple': 3, 'banana': 5, 'grape': 2}

for item, price in prices.items():
    if item in quantities:
        total = price * quantities[item]
        print(f"  {item}: {quantities[item]} × ${price} = ${total:.2f}")
    else:
        print(f"  {item}: not in cart")

# Using get() for safe access
print("\nUsing get() for safe access:")
for item, qty in quantities.items():
    price = prices.get(item, 0)
    if price:
        print(f"  {item}: {qty} × ${price} = ${qty * price:.2f}")
    else:
        print(f"  {item}: price not found")

# =============================================================================
# SECTION 10: PRACTICAL EXAMPLES
# =============================================================================

print("\n" + "=" * 60)
print("PRACTICAL EXAMPLES")
print("=" * 60)


def find_primes(limit):
    """Find all prime numbers up to limit."""
    primes = []
    for num in range(2, limit + 1):
        is_prime = True
        for i in range(2, int(num ** 0.5) + 1):
            if num % i == 0:
                is_prime = False
                break
        if is_prime:
            primes.append(num)
    return primes


print("\nPrime numbers up to 30:")
print(f"  {find_primes(30)}")


def fibonacci_sequence(n):
    """Generate Fibonacci sequence with n terms."""
    if n <= 0:
        return []
    if n == 1:
        return [0]

    fib = [0, 1]
    while len(fib) < n:
        fib.append(fib[-1] + fib[-2])
    return fib


print(f"\nFibonacci sequence (10 terms):")
print(f"  {fibonacci_sequence(10)}")


def calculate_factorial(n):
    """Calculate factorial using a loop."""
    if n < 0:
        return None
    result = 1
    for i in range(1, n + 1):
        result *= i
    return result


print(f"\nFactorials:")
for i in range(6):
    print(f"  {i}! = {calculate_factorial(i)}")


def word_frequency(text):
    """Count word frequency in text."""
    words = text.lower().split()
    frequency = {}
    for word in words:
        # Remove punctuation
        word = ''.join(c for c in word if c.isalnum())
        if word:
            frequency[word] = frequency.get(word, 0) + 1
    return frequency


sample = "The quick brown fox jumps over the lazy dog. The dog was not impressed."
print(f"\nWord frequency:")
freq = word_frequency(sample)
for word, count in sorted(freq.items(), key=lambda x: x[1], reverse=True)[:5]:
    print(f"  '{word}': {count}")


def simulate_game():
    """Simulate a simple game with while loop."""
    position = 0
    moves = 0
    max_moves = 20

    # Simulated dice rolls
    rolls = [3, 4, 6, 2, 5, 1, 4, 3]

    print("\nGame simulation:")
    while position < 20 and moves < max_moves:
        roll = rolls[moves % len(rolls)]
        position += roll
        moves += 1
        print(f"  Move {moves}: rolled {roll}, position = {position}")

    if position >= 20:
        print(f"  Won in {moves} moves!")
    else:
        print(f"  Game over after {max_moves} moves")


simulate_game()


def transpose_matrix(matrix):
    """Transpose a matrix using nested loops."""
    if not matrix:
        return []

    rows = len(matrix)
    cols = len(matrix[0])

    # Create empty transposed matrix
    transposed = []
    for j in range(cols):
        new_row = []
        for i in range(rows):
            new_row.append(matrix[i][j])
        transposed.append(new_row)

    return transposed


matrix = [[1, 2, 3], [4, 5, 6]]
print(f"\nMatrix transposition:")
print(f"  Original: {matrix}")
print(f"  Transposed: {transpose_matrix(matrix)}")

# =============================================================================
# MAIN EXECUTION
# =============================================================================

if __name__ == "__main__":
    print("\n" + "=" * 60)
    print("✅ You've learned about loops!")
    print("📚 Next: Learn about loop control in loop_control.py")
    print("=" * 60)
