"""
Module: loop_control.py
Topic: Loop Control Statements
Level: Beginner

This file teaches you about:
- break statement
- continue statement
- pass statement
- Loop else with break
- Return from loops
"""

# =============================================================================
# SECTION 1: BREAK STATEMENT
# =============================================================================

print("=" * 60)
print("BREAK STATEMENT")
print("=" * 60)

# break terminates the loop immediately
print("Finding first even number:")
for num in range(1, 20):
    if num % 2 == 0:
        print(f"  Found: {num}")
        break
print("  Loop ended")

# break in while loop
print("\nCounting down with break:")
count = 10
while True:  # Infinite loop
    print(f"  Count: {count}")
    if count == 5:
        print("  Stopping at 5!")
        break
    count -= 1

# break in nested loops (only breaks inner loop)
print("\nBreak in nested loops:")
for i in range(3):
    for j in range(5):
        if j == 2:
            break  # Only breaks inner loop
        print(f"  i={i}, j={j}")

# Breaking out of nested loops using flag
print("\nBreaking out of nested loops with flag:")
found = False
for i in range(3):
    for j in range(5):
        if i == 1 and j == 2:
            found = True
            break  # Break inner loop
        print(f"  i={i}, j={j}")
    if found:
        break  # Break outer loop
print("  Exited both loops")

# Using function to break out of nested loops
print("\nUsing function to exit nested loops:")


def find_in_matrix(matrix, target):
    """Find target in a 2D matrix."""
    for i, row in enumerate(matrix):
        for j, value in enumerate(row):
            if value == target:
                return i, j
    return None


matrix = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
target = 5
result = find_in_matrix(matrix, target)
print(f"  Found {target} at position: {result}")

# =============================================================================
# SECTION 2: CONTINUE STATEMENT
# =============================================================================

print("\n" + "=" * 60)
print("CONTINUE STATEMENT")
print("=" * 60)

# continue skips the rest of current iteration
print("Printing odd numbers only:")
for num in range(10):
    if num % 2 == 0:
        continue  # Skip even numbers
    print(f"  {num}")

# Continue in different scenarios
print("\nProcessing data with continue:")
data = [1, None, 3, "", 5, 0, 7]
total = 0
for item in data:
    if not item:  # Skip falsy values
        continue
    total += item
    print(f"  Added {item}, total = {total}")

print("\nFiltering with continue:")
words = ["apple", "", "banana", None, "cherry", "  ", "date"]
for word in words:
    if not word or not word.strip():
        continue
    print(f"  Valid word: '{word.strip()}'")

# =============================================================================
# SECTION 3: PASS STATEMENT
# =============================================================================

print("\n" + "=" * 60)
print("PASS STATEMENT")
print("=" * 60)

# pass does nothing - it's a placeholder
print("Pass as placeholder:")

# Placeholder for future code
for i in range(5):
    if i == 2:
        pass  # TODO: Handle i == 2 case later
    print(f"  i = {i}")

# Empty class or function
class EmptyClass:
    pass


def empty_function():
    pass


print(f"\nEmptyClass exists: {EmptyClass}")
print(f"empty_function returns: {empty_function()}")

# Using pass in if-else
x = 10
if x > 5:
    print("  x is greater than 5")
else:
    pass  # Do nothing for small values

# =============================================================================
# SECTION 4: BREAK AND LOOP ELSE
# =============================================================================

print("\n" + "=" * 60)
print("BREAK AND LOOP ELSE")
print("=" * 60)

# else clause runs if loop wasn't broken
def search_list(items, target):
    """Search for target in list."""
    for i, item in enumerate(items):
        if item == target:
            print(f"  Found {target} at index {i}")
            break
    else:
        print(f"  {target} not found in list")


print("Search results:")
search_list([1, 2, 3, 4, 5], 3)
search_list([1, 2, 3, 4, 5], 7)

# Prime number check using for-else
def is_prime(n):
    """Check if n is prime using for-else."""
    if n < 2:
        return False
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False  # Found a divisor, not prime
    else:
        return True  # No divisor found, prime!


print("\nPrime number check:")
for num in range(2, 11):
    result = "prime" if is_prime(num) else "not prime"
    print(f"  {num} is {result}")

# While with else
def wait_for_condition():
    """Simulate waiting with timeout."""
    max_attempts = 5
    attempt = 0

    while attempt < max_attempts:
        print(f"  Attempt {attempt + 1}")
        if attempt == 3:  # Simulate success on attempt 4
            print("  Condition met!")
            break
        attempt += 1
    else:
        print("  Timeout - condition not met")


print("\nWaiting with timeout:")
wait_for_condition()

# =============================================================================
# SECTION 5: EARLY RETURN FROM LOOPS
# =============================================================================

print("\n" + "=" * 60)
print("EARLY RETURN FROM LOOPS")
print("=" * 60)


def find_first_negative(numbers):
    """Find first negative number, return its index or -1."""
    for i, num in enumerate(numbers):
        if num < 0:
            return i
    return -1


print("Finding first negative:")
print(f"  [1, 2, -3, 4]: index {find_first_negative([1, 2, -3, 4])}")
print(f"  [1, 2, 3, 4]: index {find_first_negative([1, 2, 3, 4])}")


def find_all_indices(items, target):
    """Find all indices of target."""
    indices = []
    for i, item in enumerate(items):
        if item == target:
            indices.append(i)
    return indices if indices else None


print("\nFinding all indices:")
print(f"  [1, 2, 3, 2, 4, 2] target=2: {find_all_indices([1, 2, 3, 2, 4, 2], 2)}")
print(f"  [1, 2, 3, 4] target=5: {find_all_indices([1, 2, 3, 4], 5)}")

# =============================================================================
# SECTION 6: COMPLEX LOOP PATTERNS
# =============================================================================

print("\n" + "=" * 60)
print("COMPLEX LOOP PATTERNS")
print("=" * 60)


def batch_process(items, batch_size=3):
    """Process items in batches."""
    results = []
    for i in range(0, len(items), batch_size):
        batch = items[i:i + batch_size]
        print(f"  Processing batch: {batch}")
        results.append(batch)
    return results


print("Batch processing:")
items = list(range(1, 11))
batch_process(items)


def sliding_window(items, window_size):
    """Generate sliding windows over items."""
    for i in range(len(items) - window_size + 1):
        yield items[i:i + window_size]


print("\nSliding window:")
numbers = [1, 2, 3, 4, 5]
for window in sliding_window(numbers, 3):
    print(f"  Window: {window}")


def pairwise(iterable):
    """Iterate over pairs: s -> (s0,s1), (s1,s2), ..."""
    iterator = iter(iterable)
    prev = next(iterator)
    for current in iterator:
        yield prev, current
        prev = current


print("\nPairwise iteration:")
numbers = [1, 2, 3, 4, 5]
for a, b in pairwise(numbers):
    print(f"  {a} -> {b}")

# =============================================================================
# SECTION 7: PRACTICAL EXAMPLES
# =============================================================================

print("\n" + "=" * 60)
print("PRACTICAL EXAMPLES")
print("=" * 60)


def validate_input(data, rules):
    """
    Validate data against rules.
    Returns (is_valid, errors).
    """
    errors = []

    for field, value in data.items():
        if field not in rules:
            continue

        rule = rules[field]

        # Check required
        if rule.get('required') and not value:
            errors.append(f"{field} is required")
            continue

        # Check min length
        if 'min_length' in rule:
            if len(str(value)) < rule['min_length']:
                errors.append(f"{field} must be at least {rule['min_length']} characters")

        # Check max length
        if 'max_length' in rule:
            if len(str(value)) > rule['max_length']:
                errors.append(f"{field} must be at most {rule['max_length']} characters")

        # Check pattern
        if 'pattern' in rule:
            import re
            if not re.match(rule['pattern'], str(value)):
                errors.append(f"{field} has invalid format")

    return len(errors) == 0, errors


print("Input validation:")
data = {
    'username': 'alice',
    'email': 'alice@example.com',
    'password': '123'  # Too short
}
rules = {
    'username': {'required': True, 'min_length': 3},
    'email': {'required': True, 'pattern': r'^[^@]+@[^@]+\.[^@]+$'},
    'password': {'required': True, 'min_length': 8}
}
is_valid, errors = validate_input(data, rules)
print(f"  Valid: {is_valid}")
for error in errors:
    print(f"  Error: {error}")


def find_duplicates(items):
    """Find duplicate items using loop control."""
    seen = set()
    duplicates = set()

    for item in items:
        if item in seen:
            duplicates.add(item)
            continue
        seen.add(item)

    return duplicates


print("\nFinding duplicates:")
data = [1, 2, 3, 2, 4, 5, 3, 6, 7, 5]
print(f"  Data: {data}")
print(f"  Duplicates: {find_duplicates(data)}")


def parse_config(lines):
    """Parse simple config file format."""
    config = {}

    for line in lines:
        # Skip empty lines and comments
        line = line.strip()
        if not line or line.startswith('#'):
            continue

        # Parse key=value
        if '=' in line:
            key, value = line.split('=', 1)
            config[key.strip()] = value.strip()

    return config


config_lines = [
    "# Database settings",
    "host = localhost",
    "port = 5432",
    "",
    "# Credentials",
    "user = admin",
    "password = secret123"
]
print("\nConfig parsing:")
config = parse_config(config_lines)
for key, value in config.items():
    print(f"  {key}: {value}")


def merge_sorted_arrays(arr1, arr2):
    """Merge two sorted arrays into one sorted array."""
    result = []
    i = j = 0

    while i < len(arr1) and j < len(arr2):
        if arr1[i] <= arr2[j]:
            result.append(arr1[i])
            i += 1
        else:
            result.append(arr2[j])
            j += 1

    # Add remaining elements
    result.extend(arr1[i:])
    result.extend(arr2[j:])

    return result


print("\nMerging sorted arrays:")
arr1 = [1, 3, 5, 7]
arr2 = [2, 4, 6, 8]
print(f"  Array 1: {arr1}")
print(f"  Array 2: {arr2}")
print(f"  Merged: {merge_sorted_arrays(arr1, arr2)}")

# =============================================================================
# SECTION 8: PERFORMANCE TIPS
# =============================================================================

print("\n" + "=" * 60)
print("PERFORMANCE TIPS")
print("=" * 60)

# Avoid unnecessary work in loops
print("Tip 1: Minimize work inside loops")

# Bad: Function called every iteration
# for item in items:
#     result = expensive_function() * item  # expensive_function called every time

# Good: Calculate once before loop
# constant = expensive_function()
# for item in items:
#     result = constant * item

print("Tip 2: Use local variables")
# Local variable access is faster than global

import time

# Global variable
global_var = 10

def test_global():
    """Access global variable."""
    total = 0
    for i in range(100000):
        total += global_var
    return total

def test_local():
    """Access local variable."""
    local_var = 10
    total = 0
    for i in range(100000):
        total += local_var
    return total

start = time.time()
test_global()
global_time = time.time() - start

start = time.time()
test_local()
local_time = time.time() - start

print(f"  Global access: {global_time:.4f}s")
print(f"  Local access: {local_time:.4f}s")

print("\nTip 3: Use built-in functions when possible")

# Manual sum
def manual_sum(numbers):
    total = 0
    for n in numbers:
        total += n
    return total

numbers = list(range(10000))

start = time.time()
manual_sum(numbers)
manual_time = time.time() - start

start = time.time()
sum(numbers)
builtin_time = time.time() - start

print(f"  Manual sum: {manual_time:.6f}s")
print(f"  Built-in sum: {builtin_time:.6f}s")

# =============================================================================
# MAIN EXECUTION
# =============================================================================

if __name__ == "__main__":
    print("\n" + "=" * 60)
    print("✅ You've learned about loop control statements!")
    print("📚 Next: Move to 04-functions to learn about functions")
    print("=" * 60)
