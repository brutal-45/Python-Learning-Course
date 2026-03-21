"""
Module: numbers.py
Topic: Numeric Types in Python
Level: Beginner

This file teaches you about:
- Integer type (int)
- Float type (float)
- Complex type (complex)
- Mathematical operations
- Type conversion
- Math module functions
"""

# =============================================================================
# SECTION 1: INTEGER TYPE (int)
# =============================================================================

print("=" * 60)
print("INTEGER TYPE (int)")
print("=" * 60)

# Integer literals
positive_int = 42
negative_int = -17
zero = 0

print(f"Positive: {positive_int}, Type: {type(positive_int)}")
print(f"Negative: {negative_int}, Type: {type(negative_int)}")
print(f"Zero: {zero}, Type: {type(zero)}")

# Different integer representations
decimal = 42      # Base 10
binary = 0b101010 # Base 2 (prefix: 0b)
octal = 0o52      # Base 8 (prefix: 0o)
hexadecimal = 0x2a # Base 16 (prefix: 0x)

print(f"\nDecimal 42 in different bases:")
print(f"  Binary: {binary} (0b101010)")
print(f"  Octal: {octal} (0o52)")
print(f"  Hexadecimal: {hexadecimal} (0x2a)")

# Converting between bases
print(f"\nConverting 42 to other bases:")
print(f"  bin(42) = {bin(42)}")
print(f"  oct(42) = {oct(42)}")
print(f"  hex(42) = {hex(42)}")

# Python integers have unlimited precision!
huge_number = 10 ** 100  # A googol
print(f"\nPython can handle very large integers:")
print(f"  10^100 = {huge_number}")

# Underscore separators for readability (Python 3.6+)
million = 1_000_000
credit_card = 1234_5678_9012_3456
print(f"\nUnderscore separators:")
print(f"  million = {million}")
print(f"  credit card = {credit_card}")

# =============================================================================
# SECTION 2: FLOAT TYPE (float)
# =============================================================================

print("\n" + "=" * 60)
print("FLOAT TYPE (float)")
print("=" * 60)

# Float literals
float1 = 3.14
float2 = -0.001
float3 = 2.0
float4 = 1e10     # Scientific notation: 1 × 10^10
float5 = 1.5e-3   # Scientific notation: 1.5 × 10^-3

print(f"Standard float: {float1}")
print(f"Negative float: {float2}")
print(f"Whole number float: {float3}")
print(f"Scientific notation (1e10): {float4}")
print(f"Scientific notation (1.5e-3): {float5}")

# Special float values
import math

print(f"\nSpecial float values:")
print(f"  Infinity: {float('inf')}")
print(f"  Negative infinity: {float('-inf')}")
print(f"  Not a Number (NaN): {float('nan')}")
print(f"  math.inf: {math.inf}")
print(f"  math.nan: {math.nan}")

# Float precision issues
print(f"\nFloat precision warnings:")
print(f"  0.1 + 0.2 = {0.1 + 0.2}")  # Not exactly 0.3!
print(f"  0.1 + 0.2 == 0.3: {0.1 + 0.2 == 0.3}")  # False!

# Solving precision issues with decimal module
from decimal import Decimal, getcontext

getcontext().prec = 28
a = Decimal('0.1')
b = Decimal('0.2')
print(f"\nUsing Decimal for precision:")
print(f"  Decimal('0.1') + Decimal('0.2') = {a + b}")
print(f"  (a + b) == Decimal('0.3'): {(a + b) == Decimal('0.3')}")

# =============================================================================
# SECTION 3: COMPLEX TYPE (complex)
# =============================================================================

print("\n" + "=" * 60)
print("COMPLEX TYPE (complex)")
print("=" * 60)

# Complex number literals
c1 = 3 + 4j       # Real part: 3, Imaginary part: 4
c2 = complex(3, 4)  # Same as above
c3 = 2j           # Pure imaginary number
c4 = -1j          # Negative imaginary

print(f"Complex literal: {c1}")
print(f"complex() function: {c2}")
print(f"Pure imaginary: {c3}")

# Accessing real and imaginary parts
print(f"\nAccessing parts of {c1}:")
print(f"  Real part: {c1.real}")
print(f"  Imaginary part: {c1.imag}")

# Complex conjugate
print(f"  Conjugate: {c1.conjugate()}")

# Magnitude (absolute value)
magnitude = abs(c1)  # sqrt(3^2 + 4^2) = 5
print(f"  Magnitude |{c1}|: {magnitude}")

# Complex arithmetic
print(f"\nComplex arithmetic:")
a = 1 + 2j
b = 3 + 4j
print(f"  {a} + {b} = {a + b}")
print(f"  {a} * {b} = {a * b}")
print(f"  {a} / {b} = {a / b}")

# =============================================================================
# SECTION 4: MATHEMATICAL OPERATIONS
# =============================================================================

print("\n" + "=" * 60)
print("MATHEMATICAL OPERATIONS")
print("=" * 60)

# Basic operations
a, b = 17, 5
print(f"a = {a}, b = {b}")
print(f"  Addition: {a} + {b} = {a + b}")
print(f"  Subtraction: {a} - {b} = {a - b}")
print(f"  Multiplication: {a} * {b} = {a * b}")
print(f"  Division: {a} / {b} = {a / b}")
print(f"  Floor division: {a} // {b} = {a // b}")
print(f"  Modulo: {a} % {b} = {a % b}")
print(f"  Power: {a} ** {b} = {a ** b}")

# Built-in functions
numbers = [3, 1, 4, 1, 5, 9, 2, 6]
print(f"\nBuilt-in functions on {numbers}:")
print(f"  sum(): {sum(numbers)}")
print(f"  max(): {max(numbers)}")
print(f"  min(): {min(numbers)}")
print(f"  abs(-42): {abs(-42)}")
print(f"  round(3.14159, 2): {round(3.14159, 2)}")
print(f"  pow(2, 10): {pow(2, 10)}")

# =============================================================================
# SECTION 5: MATH MODULE
# =============================================================================

print("\n" + "=" * 60)
print("MATH MODULE")
print("=" * 60)

import math

print("Math constants:")
print(f"  π (pi): {math.pi}")
print(f"  e (Euler's number): {math.e}")
print(f"  τ (tau): {math.tau}")
print(f"  infinity: {math.inf}")

print("\nMath functions:")
print(f"  sqrt(16): {math.sqrt(16)}")
print(f"  ceil(4.3): {math.ceil(4.3)}")
print(f"  floor(4.7): {math.floor(4.7)}")
print(f"  factorial(5): {math.factorial(5)}")
print(f"  gcd(12, 18): {math.gcd(12, 18)}")

print("\nTrigonometric functions:")
print(f"  sin(π/2): {math.sin(math.pi/2)}")
print(f"  cos(0): {math.cos(0)}")
print(f"  tan(π/4): {math.tan(math.pi/4)}")

print("\nLogarithmic functions:")
print(f"  log(e): {math.log(math.e)}")  # Natural log
print(f"  log10(100): {math.log10(100)}")
print(f"  log2(8): {math.log2(8)}")
print(f"  exp(1): {math.exp(1)}")

# =============================================================================
# SECTION 6: RANDOM MODULE
# =============================================================================

print("\n" + "=" * 60)
print("RANDOM MODULE")
print("=" * 60)

import random

print("Random numbers:")
print(f"  random(): {random.random()}")  # 0.0 to 1.0
print(f"  uniform(1, 10): {random.uniform(1, 10)}")  # Float in range
print(f"  randint(1, 100): {random.randint(1, 100)}")  # Integer in range

print("\nRandom choices:")
items = ['apple', 'banana', 'cherry', 'date']
print(f"  Items: {items}")
print(f"  choice(): {random.choice(items)}")  # Single random item
print(f"  sample(items, 2): {random.sample(items, 2)}")  # Multiple unique items
print(f"  choices(items, k=3): {random.choices(items, k=3)}")  # With replacement

print("\nShuffling:")
numbers = [1, 2, 3, 4, 5]
random.shuffle(numbers)
print(f"  Shuffled [1,2,3,4,5]: {numbers}")

# Seeding for reproducible results
random.seed(42)
print(f"\nWith seed(42):")
print(f"  First random(): {random.random()}")
random.seed(42)
print(f"  After re-seeding: {random.random()}")  # Same as above

# =============================================================================
# SECTION 7: TYPE CONVERSION
# =============================================================================

print("\n" + "=" * 60)
print("TYPE CONVERSION")
print("=" * 60)

# String to number
str_int = "42"
str_float = "3.14"

converted_int = int(str_int)
converted_float = float(str_float)

print(f"String to number:")
print(f"  int('{str_int}') = {converted_int}")
print(f"  float('{str_float}') = {converted_float}")

# Number to number
print(f"\nNumber to number:")
print(f"  int(3.7) = {int(3.7)}")  # Truncates toward zero
print(f"  int(-3.7) = {int(-3.7)}")  # Truncates toward zero
print(f"  float(42) = {float(42)}")

# Invalid conversions
print(f"\nHandling invalid conversions:")
try:
    int("not a number")
except ValueError as e:
    print(f"  int('not a number') raises ValueError")

# Safe conversion with error handling
def safe_int(value, default=0):
    """Safely convert to int, returning default on failure."""
    try:
        return int(value)
    except (ValueError, TypeError):
        return default

print(f"\nSafe conversion:")
print(f"  safe_int('42') = {safe_int('42')}")
print(f"  safe_int('invalid') = {safe_int('invalid')}")
print(f"  safe_int('invalid', default=-1) = {safe_int('invalid', -1)}")

# =============================================================================
# SECTION 8: BITWISE OPERATIONS
# =============================================================================

print("\n" + "=" * 60)
print("BITWISE OPERATIONS")
print("=" * 60)

a, b = 0b1010, 0b1100  # 10 and 12 in decimal

print(f"a = {bin(a)} ({a}), b = {bin(b)} ({b})")
print(f"\nBitwise operations:")
print(f"  AND (a & b): {bin(a & b)} ({a & b})")
print(f"  OR (a | b): {bin(a | b)} ({a | b})")
print(f"  XOR (a ^ b): {bin(a ^ b)} ({a ^ b})")
print(f"  NOT (~a): {bin(~a)} ({~a})")
print(f"  Left shift (a << 2): {bin(a << 2)} ({a << 2})")
print(f"  Right shift (a >> 2): {bin(a >> 2)} ({a >> 2})")

# Common bit tricks
print(f"\nCommon bit tricks:")
n = 42
print(f"  {n} is even: {(n & 1) == 0}")
print(f"  {n} in binary: {bin(n)}")
print(f"  {n} has how many bits set: {bin(n).count('1')}")

# =============================================================================
# PRACTICAL EXAMPLES
# =============================================================================

print("\n" + "=" * 60)
print("PRACTICAL EXAMPLES")
print("=" * 60)


def calculate_compound_interest(principal, rate, years, compounds_per_year=12):
    """
    Calculate compound interest.

    A = P(1 + r/n)^(nt)
    """
    amount = principal * (1 + rate / compounds_per_year) ** (compounds_per_year * years)
    return amount


print("\nCompound Interest Calculator:")
principal = 10000
rate = 0.05  # 5%
years = 10
amount = calculate_compound_interest(principal, rate, years)
print(f"  Principal: ${principal:,.2f}")
print(f"  Rate: {rate * 100}%")
print(f"  Years: {years}")
print(f"  Final amount: ${amount:,.2f}")
print(f"  Interest earned: ${amount - principal:,.2f}")


def is_prime(n):
    """Check if a number is prime."""
    if n < 2:
        return False
    if n == 2:
        return True
    if n % 2 == 0:
        return False
    for i in range(3, int(math.sqrt(n)) + 1, 2):
        if n % i == 0:
            return False
    return True


print("\nPrime Number Checker:")
test_numbers = [1, 2, 17, 42, 97, 100]
for num in test_numbers:
    print(f"  {num} is prime: {is_prime(num)}")


def fibonacci(n):
    """Generate Fibonacci sequence up to n numbers."""
    fib = [0, 1]
    while len(fib) < n:
        fib.append(fib[-1] + fib[-2])
    return fib[:n]


print(f"\nFibonacci sequence (first 15 numbers):")
print(f"  {fibonacci(15)}")

# =============================================================================
# MAIN EXECUTION
# =============================================================================

if __name__ == "__main__":
    print("\n" + "=" * 60)
    print("✅ You've learned about Python numeric types!")
    print("📚 Next: Learn about strings in strings.py")
    print("=" * 60)
