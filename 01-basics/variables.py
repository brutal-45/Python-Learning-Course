"""
Module: variables.py
Topic: Variables and Data Types
Level: Beginner

This file teaches you about variables in Python - how to create them,
name them properly, and understand Python's dynamic typing system.
"""

# =============================================================================
# SECTION 1: WHAT ARE VARIABLES?
# =============================================================================
# Variables are containers for storing data values.
# In Python, you don't need to declare variable types - Python figures it out!

# Creating variables is simple - just assign a value
x = 5  # x is now an integer
name = "Alice"  # name is now a string
price = 19.99  # price is now a float
is_active = True  # is_active is now a boolean

# Multiple assignment
a, b, c = 1, 2, 3  # a=1, b=2, c=3
print(f"a={a}, b={b}, c={c}")

# Same value to multiple variables
x = y = z = 0  # All three variables are 0
print(f"x={x}, y={y}, z={z}")

# =============================================================================
# SECTION 2: VARIABLE NAMING RULES (PEP 8)
# =============================================================================
# Python has rules and conventions for naming variables:

# ✅ VALID VARIABLE NAMES
user_name = "Alice"  # snake_case (recommended for variables)
userName = "Bob"  # camelCase (less common in Python)
_user = "Charlie"  # Starting with underscore (for private variables)
USER = "Dave"  # All caps (convention for constants)
user2 = "Eve"  # Can contain numbers (but not start with one)
_2user = "Frank"  # Underscore + number is valid

# ❌ INVALID VARIABLE NAMES (These will cause errors!)
# 2user = "Invalid"    # Can't start with a number
# user-name = "Invalid"  # Can't use hyphens
# class = "Invalid"    # Can't use reserved keywords

# NAMING CONVENTIONS (PEP 8)
# - Use descriptive names
# - Use snake_case for variables and functions
# - Use PascalCase for classes
# - Use ALL_CAPS for constants

# Good variable names
student_name = "Alice"
total_price = 99.99
is_logged_in = True
MAX_CONNECTIONS = 100  # Constant

# Poor variable names (avoid these)
x = "Alice"  # Not descriptive
n = 99.99  # Not clear what this represents
flag = True  # Better: is_logged_in, has_permission, etc.

# =============================================================================
# SECTION 3: DYNAMIC TYPING
# =============================================================================
# Python is dynamically typed - variables can change types!

var = 10  # var is an integer
print(f"var = {var}, type = {type(var)}")

var = "Hello"  # Now var is a string
print(f"var = {var}, type = {type(var)}")

var = 3.14  # Now var is a float
print(f"var = {var}, type = {type(var)}")

var = [1, 2, 3]  # Now var is a list
print(f"var = {var}, type = {type(var)}")

# =============================================================================
# SECTION 4: PYTHON KEYWORDS (RESERVED WORDS)
# =============================================================================
# These words have special meaning in Python and cannot be used as variable names

import keyword

print("\nPython Keywords:")
print(keyword.kwlist)

# List of keywords (Python 3.10+):
# False, None, True, and, as, assert, async, await, break, class,
# continue, def, del, elif, else, except, finally, for, from, global,
# if, import, in, is, lambda, nonlocal, not, or, pass, raise, return,
# try, while, with, yield

# =============================================================================
# SECTION 5: TYPE CHECKING AND CONVERSION
# =============================================================================

# Check type with type()
number = 42
print(f"Type of {number}: {type(number)}")

text = "Hello"
print(f"Type of '{text}': {type(text)}")

# Type conversion (casting)
# String to integer
str_num = "123"
int_num = int(str_num)
print(f"String '{str_num}' converted to int: {int_num}")

# Integer to string
num = 456
str_from_num = str(num)
print(f"Integer {num} converted to string: '{str_from_num}'")

# Float to integer (truncates, doesn't round)
float_val = 3.99
int_val = int(float_val)
print(f"Float {float_val} converted to int: {int_val}")  # Output: 3

# Integer to float
int_val = 5
float_val = float(int_val)
print(f"Integer {int_val} converted to float: {float_val}")

# Boolean conversion
print(bool(1))  # True - non-zero numbers are truthy
print(bool(0))  # False - zero is falsy
print(bool(""))  # False - empty string is falsy
print(bool("text"))  # True - non-empty string is truthy

# =============================================================================
# SECTION 6: VARIABLE SCOPE PREVIEW
# =============================================================================

# Global variable
global_var = "I'm global"


def my_function():
    # Local variable
    local_var = "I'm local"
    print(f"Inside function: {local_var}")
    print(f"Can access global: {global_var}")


my_function()
print(f"Outside function: {global_var}")
# print(local_var)  # This would raise an error - local_var is not accessible here

# =============================================================================
# SECTION 7: THE 'None' VALUE
# =============================================================================

# None represents the absence of a value
result = None
print(f"Result: {result}")  # Output: None
print(f"Type: {type(result)}")  # Output: <class 'NoneType'>

# None is often used as a default value
def find_item(items, target):
    """Return the index of target in items, or None if not found."""
    for i, item in enumerate(items):
        if item == target:
            return i
    return None


index = find_item([1, 2, 3], 2)
print(f"Index: {index}")  # Output: 1

index = find_item([1, 2, 3], 5)
print(f"Index: {index}")  # Output: None

# Checking for None - use 'is' not '=='
if result is None:
    print("Result is None")

if result is not None:
    print("Result has a value")

# =============================================================================
# SECTION 8: CONSTANTS
# =============================================================================
# Python doesn't have true constants, but convention is to use ALL_CAPS

# Convention: Treat these as constants (don't modify them)
PI = 3.14159
MAX_SIZE = 100
DEFAULT_NAME = "Guest"
APP_NAME = "My Python App"

# These can technically be modified (but shouldn't!)
# PI = 3.14  # Don't do this!

# =============================================================================
# SECTION 9: DELETING VARIABLES
# =============================================================================

temp_var = "Temporary"
print(f"Before delete: {temp_var}")

del temp_var
# print(temp_var)  # This would raise NameError

# =============================================================================
# SECTION 10: PRACTICAL EXAMPLES
# =============================================================================

def demonstrate_variables():
    """
    A comprehensive demonstration of variable concepts in Python.
    """
    print("\n" + "=" * 60)
    print("VARIABLE DEMONSTRATION")
    print("=" * 60)
    
    # Variable assignment
    print("\n1. Variable Assignment:")
    name = "Python Programmer"
    age = 25
    height = 5.9
    is_student = True
    
    print(f"   Name: {name} (type: {type(name).__name__})")
    print(f"   Age: {age} (type: {type(age).__name__})")
    print(f"   Height: {height} (type: {type(height).__name__})")
    print(f"   Is Student: {is_student} (type: {type(is_student).__name__})")
    
    # Multiple assignment
    print("\n2. Multiple Assignment:")
    x, y, z = 10, 20, 30
    print(f"   x={x}, y={y}, z={z}")
    
    # Swapping variables (Python makes this easy!)
    print("\n3. Swapping Variables:")
    print(f"   Before: x={x}, y={y}")
    x, y = y, x
    print(f"   After: x={x}, y={y}")
    
    # Type conversion
    print("\n4. Type Conversion:")
    num_str = "42"
    num_int = int(num_str)
    num_float = float(num_str)
    print(f"   String: '{num_str}'")
    print(f"   Integer: {num_int}")
    print(f"   Float: {num_float}")
    
    print("\n" + "=" * 60)


# =============================================================================
# RUNNING THE DEMONSTRATION
# =============================================================================

if __name__ == "__main__":
    print("\n" + "=" * 60)
    print("PYTHON BASICS - VARIABLES")
    print("=" * 60)
    
    demonstrate_variables()
    
    print("\n✅ You've learned about variables!")
    print("📚 Next: Learn about operators in operators.py")
