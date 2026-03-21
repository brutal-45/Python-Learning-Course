"""
Module: dictionaries.py
Topic: Dictionaries in Python
Level: Beginner

This file teaches you about:
- Dictionary creation and basics
- Accessing and modifying dictionaries
- Dictionary methods
- Dictionary comprehensions
- Nested dictionaries
"""

# =============================================================================
# SECTION 1: DICTIONARY CREATION
# =============================================================================

print("=" * 60)
print("DICTIONARY CREATION")
print("=" * 60)

# Different ways to create dictionaries
dict1 = {'name': 'Alice', 'age': 25}        # Direct creation
dict2 = dict(name='Bob', age=30)            # Using dict() with keyword args
dict3 = dict([('name', 'Charlie'), ('age', 35)])  # From list of tuples
dict4 = {}                                   # Empty dictionary
dict5 = dict()                               # Empty dictionary (constructor)

print(f"Direct: {dict1}")
print(f"dict(name='Bob', age=30): {dict2}")
print(f"From tuples: {dict3}")
print(f"Empty: {dict4}")

# Using dict.fromkeys()
keys = ['a', 'b', 'c']
new_dict = dict.fromkeys(keys, 0)
print(f"fromkeys(['a','b','c'], 0): {new_dict}")

# Dictionary with mixed key types
mixed = {'name': 'Alice', 1: 'one', (1, 2): 'tuple key'}
print(f"Mixed keys: {mixed}")

# =============================================================================
# SECTION 2: ACCESSING VALUES
# =============================================================================

print("\n" + "=" * 60)
print("ACCESSING VALUES")
print("=" * 60)

person = {'name': 'Alice', 'age': 25, 'city': 'New York'}

print(f"Dictionary: {person}")

# Using key
print(f"\nUsing key:")
print(f"  person['name']: {person['name']}")

# Using get() (safer, returns None or default if key missing)
print(f"\nUsing get():")
print(f"  person.get('name'): {person.get('name')}")
print(f"  person.get('job', 'Unknown'): {person.get('job', 'Unknown')}")

# KeyError when key doesn't exist
try:
    print(person['job'])
except KeyError as e:
    print(f"  person['job'] raises KeyError: {e}")

# get() vs [] operator
print(f"\nComparison:")
print(f"  person.get('job'): {person.get('job')}")  # Returns None
print(f"  person.get('job', 'N/A'): {person.get('job', 'N/A')}")  # Returns default

# =============================================================================
# SECTION 3: MODIFYING DICTIONARIES
# =============================================================================

print("\n" + "=" * 60)
print("MODIFYING DICTIONARIES")
print("=" * 60)

person = {'name': 'Alice', 'age': 25}
print(f"Original: {person}")

# Add or update
person['city'] = 'New York'    # Add new key
person['age'] = 26              # Update existing key
print(f"After add/update: {person}")

# update() - Add multiple key-value pairs
person.update({'job': 'Engineer', 'company': 'Tech Co'})
print(f"After update(): {person}")

# update() with keyword arguments
person.update(salary=75000, remote=True)
print(f"After update(kwargs): {person}")

# Delete operations
del person['remote']
print(f"After del: {person}")

removed = person.pop('company')
print(f"After pop('company'): {person}, removed: {removed}")

removed = person.pop('nonexistent', 'Not Found')
print(f"pop with default: {removed}")

# popitem() - Remove and return last item
last_item = person.popitem()
print(f"After popitem(): {person}, removed: {last_item}")

# clear() - Remove all items
temp = {'a': 1, 'b': 2}
temp.clear()
print(f"After clear(): {temp}")

# =============================================================================
# SECTION 4: DICTIONARY METHODS - KEYS, VALUES, ITEMS
# =============================================================================

print("\n" + "=" * 60)
print("KEYS, VALUES, ITEMS")
print("=" * 60)

person = {'name': 'Alice', 'age': 25, 'city': 'New York'}

print(f"Dictionary: {person}")

# keys() - Get all keys
print(f"\nkeys(): {list(person.keys())}")

# values() - Get all values
print(f"values(): {list(person.values())}")

# items() - Get all key-value pairs
print(f"items(): {list(person.items())}")

# Iterating
print(f"\nIterating:")
print("  By key:")
for key in person:
    print(f"    {key}: {person[key]}")

print("  By items:")
for key, value in person.items():
    print(f"    {key}: {value}")

# Membership test (checks keys)
print(f"\nMembership:")
print(f"  'name' in person: {'name' in person}")
print(f"  'Alice' in person: {'Alice' in person}")  # False - checks keys
print(f"  'Alice' in person.values(): {'Alice' in person.values()}")

# =============================================================================
# SECTION 5: DICTIONARY COMPREHENSIONS
# =============================================================================

print("\n" + "=" * 60)
print("DICTIONARY COMPREHENSIONS")
print("=" * 60)

# Basic syntax: {key: value for item in iterable}
squares = {x: x**2 for x in range(6)}
print(f"Squares: {squares}")

# With condition
even_squares = {x: x**2 for x in range(10) if x % 2 == 0}
print(f"Even squares: {even_squares}")

# Transform existing dictionary
prices = {'apple': 0.5, 'banana': 0.3, 'orange': 0.8}
taxed = {k: round(v * 1.1, 2) for k, v in prices.items()}
print(f"\nOriginal prices: {prices}")
print(f"With 10% tax: {taxed}")

# Swap keys and values
original = {'a': 1, 'b': 2, 'c': 3}
swapped = {v: k for k, v in original.items()}
print(f"\nOriginal: {original}")
print(f"Swapped: {swapped}")

# From two lists
keys = ['name', 'age', 'city']
values = ['Alice', 25, 'NYC']
combined = {k: v for k, v in zip(keys, values)}
print(f"\nFrom two lists: {combined}")

# =============================================================================
# SECTION 6: NESTED DICTIONARIES
# =============================================================================

print("\n" + "=" * 60)
print("NESTED DICTIONARIES")
print("=" * 60)

# Dictionary of dictionaries
employees = {
    'emp1': {
        'name': 'Alice',
        'age': 25,
        'skills': ['Python', 'JavaScript']
    },
    'emp2': {
        'name': 'Bob',
        'age': 30,
        'skills': ['Java', 'C++']
    }
}

print(f"Nested dictionary:")
for emp_id, details in employees.items():
    print(f"  {emp_id}: {details}")

# Accessing nested values
print(f"\nAccessing nested values:")
print(f"  employees['emp1']['name']: {employees['emp1']['name']}")
print(f"  employees['emp1']['skills']: {employees['emp1']['skills']}")

# Modifying nested values
employees['emp1']['age'] = 26
employees['emp1']['skills'].append('SQL')
print(f"  After modification: {employees['emp1']}")

# =============================================================================
# SECTION 7: SPECIAL DICTIONARY TYPES
# =============================================================================

print("\n" + "=" * 60)
print("SPECIAL DICTIONARY TYPES")
print("=" * 60)

# defaultdict - Returns default value for missing keys
from collections import defaultdict

# Default to 0 for counting
word_count = defaultdict(int)
text = "apple banana apple cherry banana apple"
for word in text.split():
    word_count[word] += 1

print(f"DefaultDict for counting: {dict(word_count)}")

# Default to list for grouping
from collections import defaultdict

grouped = defaultdict(list)
students = [('A', 'Alice'), ('B', 'Bob'), ('A', 'Amy')]
for grade, name in students:
    grouped[grade].append(name)

print(f"DefaultDict for grouping: {dict(grouped)}")

# Counter - Count occurrences
from collections import Counter

text = "mississippi"
counter = Counter(text)
print(f"\nCounter('{text}'): {counter}")
print(f"  Most common(2): {counter.most_common(2)}")

# OrderedDict - Preserves insertion order
from collections import OrderedDict

ordered = OrderedDict()
ordered['first'] = 1
ordered['second'] = 2
ordered['third'] = 3
print(f"\nOrderedDict: {list(ordered.keys())}")

# Note: In Python 3.7+, regular dict maintains insertion order

# =============================================================================
# SECTION 8: MERGING DICTIONARIES
# =============================================================================

print("\n" + "=" * 60)
print("MERGING DICTIONARIES")
print("=" * 60)

dict1 = {'a': 1, 'b': 2}
dict2 = {'b': 3, 'c': 4}

# Python 3.9+: Using | operator
merged = dict1 | dict2
print(f"dict1 | dict2: {merged}")  # dict2 values take precedence

# Python 3.9+: Using |= operator
dict1_copy = dict1.copy()
dict1_copy |= dict2
print(f"dict1 |= dict2: {dict1_copy}")

# Python 3.5+: Using ** unpacking
merged = {**dict1, **dict2}
print(f"{{**dict1, **dict2}}: {merged}")

# Using update()
merged = dict1.copy()
merged.update(dict2)
print(f"update(): {merged}")

# =============================================================================
# SECTION 9: PRACTICAL EXAMPLES
# =============================================================================

print("\n" + "=" * 60)
print("PRACTICAL EXAMPLES")
print("=" * 60)


def count_characters(text):
    """Count each character in a string."""
    char_count = {}
    for char in text.lower():
        if char.isalpha():
            char_count[char] = char_count.get(char, 0) + 1
    return char_count


print("\nCharacter Counter:")
sample = "Hello, World!"
counts = count_characters(sample)
print(f"  '{sample}' -> {counts}")


def group_by_length(words):
    """Group words by their length."""
    groups = {}
    for word in words:
        length = len(word)
        if length not in groups:
            groups[length] = []
        groups[length].append(word)
    return groups


words = ['apple', 'pie', 'banana', 'cat', 'dog', 'elephant']
print(f"\nGroup by length:")
print(f"  Words: {words}")
print(f"  Grouped: {group_by_length(words)}")


def invert_dict(d):
    """Invert a dictionary (swap keys and values)."""
    inverted = {}
    for key, value in d.items():
        if value not in inverted:
            inverted[value] = []
        inverted[value].append(key)
    return inverted


original = {'a': 1, 'b': 2, 'c': 1, 'd': 2}
print(f"\nInvert dictionary:")
print(f"  Original: {original}")
print(f"  Inverted: {invert_dict(original)}")


def safe_nested_get(d, *keys, default=None):
    """Safely get nested dictionary values."""
    for key in keys:
        try:
            d = d[key]
        except (KeyError, TypeError):
            return default
    return d


nested = {'user': {'profile': {'name': 'Alice', 'age': 25}}}
print(f"\nSafe nested access:")
print(f"  nested: {nested}")
print(f"  get(user, profile, name): {safe_nested_get(nested, 'user', 'profile', 'name')}")
print(f"  get(user, missing, key): {safe_nested_get(nested, 'user', 'missing', 'key', default='N/A')}")


# Cache/memoization example
def create_cache():
    """Create a simple function cache using a dictionary."""
    cache = {}

    def cached_fibonacci(n):
        if n in cache:
            return cache[n]
        if n <= 1:
            result = n
        else:
            result = cached_fibonacci(n - 1) + cached_fibonacci(n - 2)
        cache[n] = result
        return result

    return cached_fibonacci


print(f"\nMemoization with dictionary:")
fib = create_cache()
print(f"  fibonacci(10): {fib(10)}")

# =============================================================================
# MAIN EXECUTION
# =============================================================================

if __name__ == "__main__":
    print("\n" + "=" * 60)
    print("✅ You've learned about Python dictionaries!")
    print("📚 Next: Learn about sets in sets.py")
    print("=" * 60)
