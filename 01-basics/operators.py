"""
Module: operators.py
Topic: Python Operators
Level: Beginner

This file teaches you about all the operators in Python:
- Arithmetic Operators
- Comparison Operators
- Logical Operators
- Assignment Operators
- Identity Operators
- Membership Operators
- Bitwise Operators
"""

# =============================================================================
# SECTION 1: ARITHMETIC OPERATORS
# =============================================================================

print("=" * 60)
print("ARITHMETIC OPERATORS")
print("=" * 60)

a, b = 10, 3

# Addition
print(f"{a} + {b} = {a + b}")  # Output: 13

# Subtraction
print(f"{a} - {b} = {a - b}")  # Output: 7

# Multiplication
print(f"{a} * {b} = {a * b}")  # Output: 30

# Division (always returns float)
print(f"{a} / {b} = {a / b}")  # Output: 3.333...

# Floor Division (returns integer, rounds down)
print(f"{a} // {b} = {a // b}")  # Output: 3

# Modulo (remainder)
print(f"{a} % {b} = {a % b}")  # Output: 1

# Exponentiation (power)
print(f"{a} ** {b} = {a ** b}")  # Output: 1000

# Negative numbers with floor division
print(f"-7 // 3 = {-7 // 3}")  # Output: -3 (rounds toward negative infinity)

# Modulo with negative numbers
print(f"-7 % 3 = {-7 % 3}")  # Output: 2

# =============================================================================
# SECTION 2: COMPARISON OPERATORS
# =============================================================================

print("\n" + "=" * 60)
print("COMPARISON OPERATORS")
print("=" * 60)

x, y = 5, 10

# Equal to
print(f"{x} == {y}: {x == y}")  # False

# Not equal to
print(f"{x} != {y}: {x != y}")  # True

# Greater than
print(f"{x} > {y}: {x > y}")  # False

# Less than
print(f"{x} < {y}: {x < y}")  # True

# Greater than or equal to
print(f"{x} >= {y}: {x >= y}")  # False

# Less than or equal to
print(f"{x} <= {y}: {x <= y}")  # True

# Comparing strings
print("\nString Comparison:")
print(f"'apple' < 'banana': {'apple' < 'banana'}")  # True (alphabetical)
print(f"'Apple' < 'apple': {'Apple' < 'apple'}")  # True (uppercase < lowercase in ASCII)

# Chained comparisons
print("\nChained Comparisons:")
age = 25
print(f"18 <= {age} <= 65: {18 <= age <= 65}")  # True

# =============================================================================
# SECTION 3: LOGICAL OPERATORS
# =============================================================================

print("\n" + "=" * 60)
print("LOGICAL OPERATORS")
print("=" * 60)

p, q = True, False

# AND - True only if both are True
print(f"{p} and {p}: {p and p}")  # True
print(f"{p} and {q}: {p and q}")  # False

# OR - True if at least one is True
print(f"{p} or {q}: {p or q}")  # True
print(f"{q} or {q}: {q or q}")  # False

# NOT - Inverts the boolean
print(f"not {p}: {not p}")  # False
print(f"not {q}: {not q}")  # True

# Short-circuit evaluation
print("\nShort-circuit Evaluation:")


def returns_true():
    print("   returns_true() was called")
    return True


def returns_false():
    print("   returns_false() was called")
    return False


print("False and returns_true():")
result = False and returns_true()  # returns_true() is NOT called
print(f"Result: {result}")

print("\nTrue or returns_false():")
result = True or returns_false()  # returns_false() is NOT called
print(f"Result: {result}")

# Truthy and Falsy values
print("\nTruthy and Falsy Values:")

# Falsy values
print(f"bool(0): {bool(0)}")  # False
print(f"bool(0.0): {bool(0.0)}")  # False
print(f"bool(''): {bool('')}")  # False
print(f"bool([]): {bool([])}")  # False
print(f"bool(None): {bool(None)}")  # False

# Truthy values
print(f"bool(1): {bool(1)}")  # True
print(f"bool(-1): {bool(-1)}")  # True
print(f"bool('hello'): {bool('hello')}")  # True
print(f"bool([1, 2]): {bool([1, 2])}")  # True

# =============================================================================
# SECTION 4: ASSIGNMENT OPERATORS
# =============================================================================

print("\n" + "=" * 60)
print("ASSIGNMENT OPERATORS")
print("=" * 60)

# Simple assignment
num = 10
print(f"num = 10: {num}")

# Addition assignment
num += 5  # Same as: num = num + 5
print(f"num += 5: {num}")  # 15

# Subtraction assignment
num -= 3  # Same as: num = num - 3
print(f"num -= 3: {num}")  # 12

# Multiplication assignment
num *= 2  # Same as: num = num * 2
print(f"num *= 2: {num}")  # 24

# Division assignment
num /= 4  # Same as: num = num / 4
print(f"num /= 4: {num}")  # 6.0

# Floor division assignment
num //= 2  # Same as: num = num // 2
print(f"num //= 2: {num}")  # 3.0

# Modulo assignment
num %= 2  # Same as: num = num % 2
print(f"num %= 2: {num}")  # 1.0

# Exponentiation assignment
num **= 3  # Same as: num = num ** 3
print(f"num **= 3: {num}")  # 1.0

# Walrus operator (Python 3.8+)
print("\nWalrus Operator (:=):")
# Assign and use in the same expression
if (n := 10) > 5:
    print(f"   n is {n} which is greater than 5")

# Useful in while loops
print("   Counting down:")
countdown = 5
while (countdown := countdown - 1) >= 0:
    print(f"   {countdown}", end=" ")
print()

# =============================================================================
# SECTION 5: IDENTITY OPERATORS
# =============================================================================

print("\n" + "=" * 60)
print("IDENTITY OPERATORS")
print("=" * 60)

# 'is' - Returns True if both variables point to the same object
# 'is not' - Returns True if variables point to different objects

a = [1, 2, 3]
b = [1, 2, 3]
c = a

print(f"a = {a}")
print(f"b = {b}")
print(f"c = a")

# Equality (values are equal)
print(f"\na == b: {a == b}")  # True (same values)

# Identity (same object in memory)
print(f"a is b: {a is b}")  # False (different objects)
print(f"a is c: {a is c}")  # True (same object)
print(f"a is not b: {a is not b}")  # True

# Memory addresses
print(f"\nid(a): {id(a)}")
print(f"id(b): {id(b)}")
print(f"id(c): {id(c)}")

# Small integers are cached (interning)
x = 256
y = 256
print(f"\nSmall integers (256):")
print(f"x = 256, y = 256")
print(f"x is y: {x is y}")  # True (cached)

x = 257
y = 257
print(f"\nLarger integers (257):")
print(f"x = 257, y = 257")
print(f"x is y: {x is y}")  # May be False (not cached)

# String interning
s1 = "hello"
s2 = "hello"
print(f"\nString interning:")
print(f"'hello' is 'hello': {s1 is s2}")  # True

# =============================================================================
# SECTION 6: MEMBERSHIP OPERATORS
# =============================================================================

print("\n" + "=" * 60)
print("MEMBERSHIP OPERATORS")
print("=" * 60)

# 'in' - Returns True if value is found in sequence
# 'not in' - Returns True if value is NOT found in sequence

fruits = ["apple", "banana", "cherry"]

print(f"fruits = {fruits}")
print(f"'apple' in fruits: {'apple' in fruits}")  # True
print(f"'grape' in fruits: {'grape' in fruits}")  # False
print(f"'grape' not in fruits: {'grape' not in fruits}")  # True

# Works with strings
message = "Hello, World!"
print(f"\nmessage = '{message}'")
print(f"'Hello' in message: {'Hello' in message}")  # True
print(f"'Python' in message: {'Python' in message}")  # False

# Works with dictionaries (checks keys)
person = {"name": "Alice", "age": 25}
print(f"\nperson = {person}")
print(f"'name' in person: {'name' in person}")  # True
print(f"'Alice' in person: {'Alice' in person}")  # False (checks keys, not values)
print(f"'Alice' in person.values(): {'Alice' in person.values()}")  # True

# Works with tuples and sets
coordinates = (0, 0)
print(f"\ncoordinates = {coordinates}")
print(f"0 in coordinates: {0 in coordinates}")  # True

numbers = {1, 2, 3, 4, 5}
print(f"\nnumbers = {numbers}")
print(f"3 in numbers: {3 in numbers}")  # True

# =============================================================================
# SECTION 7: BITWISE OPERATORS
# =============================================================================

print("\n" + "=" * 60)
print("BITWISE OPERATORS")
print("=" * 60)

a, b = 10, 6  # a = 1010 in binary, b = 0110 in binary

print(f"a = {a} (binary: {bin(a)})")
print(f"b = {b} (binary: {bin(b)})")

# AND
print(f"\na & b = {a & b} (binary: {bin(a & b)})")  # 2 (0010)

# OR
print(f"a | b = {a | b} (binary: {bin(a | b)})")  # 14 (1110)

# XOR
print(f"a ^ b = {a ^ b} (binary: {bin(a ^ b)})")  # 12 (1100)

# NOT (inverts all bits)
print(f"~a = {~a} (binary: {bin(~a)})")  # -11 (two's complement)

# Left shift
print(f"a << 2 = {a << 2} (binary: {bin(a << 2)})")  # 40 (101000)

# Right shift
print(f"a >> 2 = {a >> 2} (binary: {bin(a >> 2)})")  # 2 (0010)

# =============================================================================
# SECTION 8: OPERATOR PRECEDENCE
# =============================================================================

print("\n" + "=" * 60)
print("OPERATOR PRECEDENCE (Highest to Lowest)")
print("=" * 60)

# 1. Parentheses ()
# 2. Exponentiation **
# 3. Unary +x, -x, ~x
# 4. *, /, //, %
# 5. +, -
# 6. <<, >>
# 7. &
# 8. ^
# 9. |
# 10. Comparison operators (==, !=, >, <, >=, <=)
# 11. Identity operators (is, is not)
# 12. Membership operators (in, not in)
# 13. Logical NOT (not)
# 14. Logical AND (and)
# 15. Logical OR (or)

# Examples
result1 = 2 + 3 * 4  # 14, not 20
result2 = (2 + 3) * 4  # 20
result3 = 2 ** 3 ** 2  # 512 (right-to-left), not 64
result4 = (2 ** 3) ** 2  # 64

print(f"2 + 3 * 4 = {result1}")
print(f"(2 + 3) * 4 = {result2}")
print(f"2 ** 3 ** 2 = {result3}")
print(f"(2 ** 3) ** 2 = {result4}")

# =============================================================================
# PRACTICAL EXAMPLES
# =============================================================================

print("\n" + "=" * 60)
print("PRACTICAL EXAMPLES")
print("=" * 60)


def calculate_grade(score, attendance):
    """
    Calculate if a student passes based on score and attendance.
    Demonstrates logical operators.
    """
    min_score = 60
    min_attendance = 75

    # Student passes if they have both adequate score AND attendance
    passes = score >= min_score and attendance >= min_attendance

    # Student gets distinction if score >= 90 with good attendance
    distinction = score >= 90 and attendance >= 90

    return passes, distinction


# Test cases
print("\nGrade Calculator:")
students = [
    ("Alice", 85, 90),
    ("Bob", 55, 95),
    ("Charlie", 75, 70),
    ("Diana", 92, 95),
]

for name, score, attendance in students:
    passes, distinction = calculate_grade(score, attendance)
    status = "Distinction" if distinction else "Pass" if passes else "Fail"
    print(f"   {name}: Score={score}, Attendance={attendance}% -> {status}")


def is_valid_password(password):
    """
    Check if a password meets security requirements.
    Demonstrates membership and logical operators.
    """
    if len(password) < 8:
        return False, "Password must be at least 8 characters"

    has_upper = any(c.isupper() for c in password)
    has_lower = any(c.islower() for c in password)
    has_digit = any(c.isdigit() for c in password)
    special_chars = "!@#$%^&*()_+-=[]{}|;:,.<>?"
    has_special = any(c in special_chars for c in password)

    if not (has_upper and has_lower):
        return False, "Password must contain both uppercase and lowercase letters"
    if not has_digit:
        return False, "Password must contain at least one digit"
    if not has_special:
        return False, "Password must contain at least one special character"

    return True, "Password is valid"


print("\nPassword Validator:")
test_passwords = ["abc123", "ABC123", "Abc123!@", "MyP@ssw0rd"]
for pwd in test_passwords:
    valid, message = is_valid_password(pwd)
    status = "✓" if valid else "✗"
    print(f"   {status} '{pwd}': {message}")

# =============================================================================
# MAIN EXECUTION
# =============================================================================

if __name__ == "__main__":
    print("\n✅ You've learned about all Python operators!")
    print("📚 Next: Learn about input/output in input_output.py")
