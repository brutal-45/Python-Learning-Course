"""
Module: sets.py
Topic: Sets in Python
Level: Beginner

This file teaches you about:
- Set creation and basics
- Set operations
- Set methods
- Frozen sets
- When to use sets
"""

# =============================================================================
# SECTION 1: SET CREATION
# =============================================================================

print("=" * 60)
print("SET CREATION")
print("=" * 60)

# Different ways to create sets
set1 = {1, 2, 3, 4, 5}              # Direct creation
set2 = set([1, 2, 3, 2, 1])          # From list (duplicates removed)
set3 = set("hello")                   # From string (unique chars)
set4 = set()                          # Empty set (NOT {} - that's a dict!)
set5 = {x for x in range(5)}          # Set comprehension

print(f"Direct: {set1}")
print(f"From list [1,2,3,2,1]: {set2}")  # Duplicates removed
print(f"From 'hello': {set3}")
print(f"Empty set(): {set4}")
print(f"Comprehension: {set5}")

# Common mistake: {} creates a dict, not a set!
empty_dict = {}
empty_set = set()
print(f"\n{{}} is a dict: {type(empty_dict)}")
print(f"set() is a set: {type(empty_set)}")

# Sets only contain hashable (immutable) types
valid_set = {1, 'hello', (1, 2)}  # OK
print(f"\nValid set with mixed types: {valid_set}")

try:
    invalid_set = {[1, 2]}  # Lists are not hashable
except TypeError as e:
    print(f"Lists in sets raise: {type(e).__name__}")

# =============================================================================
# SECTION 2: SET CHARACTERISTICS
# =============================================================================

print("\n" + "=" * 60)
print("SET CHARACTERISTICS")
print("=" * 60)

# Sets are unordered
my_set = {3, 1, 4, 1, 5, 9}
print(f"Set: {my_set}")  # Order not guaranteed

# Sets contain unique elements only
numbers = [1, 2, 2, 3, 3, 3, 4, 4, 4, 4]
unique = set(numbers)
print(f"\nRemoving duplicates:")
print(f"  Original: {numbers}")
print(f"  Unique: {unique}")
print(f"  Back to list: {list(unique)}")

# Sets are mutable
my_set = {1, 2, 3}
my_set.add(4)
print(f"\nMutable: {my_set}")

# =============================================================================
# SECTION 3: SET OPERATIONS
# =============================================================================

print("\n" + "=" * 60)
print("SET OPERATIONS")
print("=" * 60)

A = {1, 2, 3, 4, 5}
B = {4, 5, 6, 7, 8}

print(f"A = {A}")
print(f"B = {B}")

# Union - All elements from both sets
print(f"\nUnion:")
print(f"  A | B: {A | B}")
print(f"  A.union(B): {A.union(B)}")

# Intersection - Elements in both sets
print(f"\nIntersection:")
print(f"  A & B: {A & B}")
print(f"  A.intersection(B): {A.intersection(B)}")

# Difference - Elements in A but not in B
print(f"\nDifference:")
print(f"  A - B: {A - B}")
print(f"  A.difference(B): {A.difference(B)}")
print(f"  B - A: {B - A}")

# Symmetric Difference - Elements in A or B but not both
print(f"\nSymmetric Difference:")
print(f"  A ^ B: {A ^ B}")
print(f"  A.symmetric_difference(B): {A.symmetric_difference(B)}")

# Multiple operations
C = {5, 6, 9}
print(f"\nMultiple sets: A={A}, B={B}, C={C}")
print(f"  A | B | C: {A | B | C}")
print(f"  A & B & C: {A & B & C}")

# =============================================================================
# SECTION 4: SET COMPARISONS
# =============================================================================

print("\n" + "=" * 60)
print("SET COMPARISONS")
print("=" * 60)

A = {1, 2, 3}
B = {1, 2, 3, 4, 5}
C = {1, 2, 3}

print(f"A = {A}, B = {B}, C = {C}")

# Subset - All elements of A are in B
print(f"\nSubset:")
print(f"  A <= B: {A <= B}")  # A is subset of B
print(f"  A.issubset(B): {A.issubset(B)}")
print(f"  A < B (proper subset): {A < B}")  # Subset but not equal

# Superset - B contains all elements of A
print(f"\nSuperset:")
print(f"  B >= A: {B >= A}")  # B is superset of A
print(f"  B.issuperset(A): {B.issuperset(A)}")
print(f"  B > A (proper superset): {B > A}")

# Disjoint - No common elements
print(f"\nDisjoint:")
D = {6, 7, 8}
print(f"  A = {A}, D = {D}")
print(f"  A.isdisjoint(D): {A.isdisjoint(D)}")
print(f"  A.isdisjoint(B): {A.isdisjoint(B)}")

# Equality
print(f"\nEquality:")
print(f"  A == C: {A == C}")
print(f"  A == B: {A == B}")

# =============================================================================
# SECTION 5: SET METHODS - MODIFYING
# =============================================================================

print("\n" + "=" * 60)
print("SET METHODS - MODIFYING")
print("=" * 60)

# add() - Add single element
my_set = {1, 2, 3}
my_set.add(4)
print(f"After add(4): {my_set}")
my_set.add(2)  # Adding existing element does nothing
print(f"After add(2) (existing): {my_set}")

# update() - Add multiple elements
my_set.update([5, 6])
print(f"After update([5,6]): {my_set}")
my_set.update({7, 8}, [9])  # Multiple iterables
print(f"After update({{7,8}}, [9]): {my_set}")

# remove() - Remove element (raises error if not found)
my_set.remove(9)
print(f"After remove(9): {my_set}")

try:
    my_set.remove(100)
except KeyError:
    print(f"remove(100) raises KeyError")

# discard() - Remove element (no error if not found)
my_set.discard(8)
print(f"After discard(8): {my_set}")
my_set.discard(100)  # No error
print(f"After discard(100) (not found): {my_set}")

# pop() - Remove and return arbitrary element
popped = my_set.pop()
print(f"After pop(): {my_set}, popped: {popped}")

# clear() - Remove all elements
my_set.clear()
print(f"After clear(): {my_set}")

# =============================================================================
# SECTION 6: SET METHODS - OPERATIONS IN PLACE
# =============================================================================

print("\n" + "=" * 60)
print("SET METHODS - OPERATIONS IN PLACE")
print("=" * 60)

# These modify the set in place

# intersection_update()
A = {1, 2, 3, 4, 5}
B = {4, 5, 6, 7}
A.intersection_update(B)
print(f"intersection_update: {A}")  # A is now {4, 5}

# difference_update()
A = {1, 2, 3, 4, 5}
B = {4, 5, 6}
A.difference_update(B)
print(f"difference_update: {A}")  # A is now {1, 2, 3}

# symmetric_difference_update()
A = {1, 2, 3}
B = {3, 4, 5}
A.symmetric_difference_update(B)
print(f"symmetric_difference_update: {A}")  # A is now {1, 2, 4, 5}

# =============================================================================
# SECTION 7: SET COMPREHENSIONS
# =============================================================================

print("\n" + "=" * 60)
print("SET COMPREHENSIONS")
print("=" * 60)

# Basic set comprehension
squares = {x**2 for x in range(10)}
print(f"Squares: {squares}")

# With condition
even_squares = {x**2 for x in range(10) if x % 2 == 0}
print(f"Even squares: {even_squares}")

# From string
unique_chars = {char.upper() for char in "hello world" if char != ' '}
print(f"Unique chars: {unique_chars}")

# =============================================================================
# SECTION 8: FROZEN SETS
# =============================================================================

print("\n" + "=" * 60)
print("FROZEN SETS")
print("=" * 60)

# Frozen sets are immutable versions of sets
frozen = frozenset([1, 2, 3, 4])
print(f"Frozen set: {frozen}")

# Cannot modify
try:
    frozen.add(5)
except AttributeError as e:
    print(f"Cannot add to frozenset: {type(e).__name__}")

# Frozen sets can be used as dictionary keys or set elements
frozen_set = frozenset([1, 2])
set_with_frozen = {frozen_set, frozenset([3, 4])}
print(f"\nSet with frozen sets: {set_with_frozen}")

dict_with_frozen_keys = {
    frozenset(['a', 'b']): "first",
    frozenset(['c', 'd']): "second"
}
print(f"Dict with frozen keys: {dict_with_frozen_keys}")

# Operations work the same
A = frozenset([1, 2, 3])
B = frozenset([3, 4, 5])
print(f"\nFrozen set operations:")
print(f"  A | B: {A | B}")
print(f"  A & B: {A & B}")

# =============================================================================
# SECTION 9: PERFORMANCE BENEFITS
# =============================================================================

print("\n" + "=" * 60)
print("PERFORMANCE BENEFITS")
print("=" * 60)

import time

# Membership testing: set vs list
large_list = list(range(100000))
large_set = set(range(100000))
target = 99999

# List lookup time
start = time.time()
for _ in range(1000):
    _ = target in large_list
list_time = time.time() - start

# Set lookup time
start = time.time()
for _ in range(1000):
    _ = target in large_set
set_time = time.time() - start

print(f"Membership test (1000 iterations):")
print(f"  List: {list_time:.4f} seconds")
print(f"  Set: {set_time:.4f} seconds")
print(f"  Set is {list_time/set_time:.1f}x faster")

# =============================================================================
# SECTION 10: PRACTICAL EXAMPLES
# =============================================================================

print("\n" + "=" * 60)
print("PRACTICAL EXAMPLES")
print("=" * 60)


def find_duplicates(items):
    """Find duplicate items using a set."""
    seen = set()
    duplicates = set()
    for item in items:
        if item in seen:
            duplicates.add(item)
        else:
            seen.add(item)
    return duplicates


print("\nFind Duplicates:")
data = [1, 2, 3, 2, 4, 5, 3, 6, 1]
print(f"  Data: {data}")
print(f"  Duplicates: {find_duplicates(data)}")


def common_elements(list1, list2):
    """Find common elements between two lists."""
    return list(set(list1) & set(list2))


print(f"\nCommon Elements:")
list1 = [1, 2, 3, 4, 5]
list2 = [4, 5, 6, 7, 8]
print(f"  List 1: {list1}")
print(f"  List 2: {list2}")
print(f"  Common: {common_elements(list1, list2)}")


def unique_words(text):
    """Find unique words in text."""
    words = text.lower().split()
    return set(words)


print(f"\nUnique Words:")
sample = "the quick brown fox jumps over the lazy dog the fox was quick"
print(f"  Text: '{sample}'")
print(f"  Unique: {unique_words(sample)}")


def is_anagram(word1, word2):
    """Check if two words are anagrams using sets."""
    # Note: This only works if letters don't repeat
    # For full anagram check, use Counter
    return set(word1.lower()) == set(word2.lower())


print(f"\nAnagram Check (simple):")
print(f"  'listen' vs 'silent': {is_anagram('listen', 'silent')}")
print(f"  'hello' vs 'world': {is_anagram('hello', 'world')}")


def categorize_items(items, categories):
    """
    Categorize items based on their presence in category sets.
    Returns items in each category, in multiple categories, and in none.
    """
    category_sets = {name: set(items) for name, items in categories.items()}
    
    result = {name: [] for name in categories}
    result['multiple'] = []
    result['none'] = []
    
    all_categorized = set()
    for item in items:
        found_in = []
        for name, cat_set in category_sets.items():
            if item in cat_set:
                found_in.append(name)
                all_categorized.add(item)
        
        if len(found_in) == 0:
            result['none'].append(item)
        elif len(found_in) == 1:
            result[found_in[0]].append(item)
        else:
            result['multiple'].append((item, found_in))
    
    return result


print(f"\nCategorize Items:")
items = [1, 2, 3, 4, 5, 6, 7, 8, 9]
categories = {
    'even': [2, 4, 6, 8],
    'prime': [2, 3, 5, 7],
    'single_digit': [1, 2, 3, 4, 5, 6, 7, 8, 9]
}
result = categorize_items(items, categories)
for category, items_list in result.items():
    print(f"  {category}: {items_list}")

# =============================================================================
# MAIN EXECUTION
# =============================================================================

if __name__ == "__main__":
    print("\n" + "=" * 60)
    print("✅ You've learned about Python sets!")
    print("📚 Next: Move to 03-control-flow for conditionals and loops")
    print("=" * 60)
