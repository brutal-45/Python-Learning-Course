"""
Module: try_except.py
Topic: Try-Except Exception Handling
Level: Intermediate

This file teaches you about:
- Basic try-except
- Multiple exceptions
- finally and else clauses
- Exception information
- Best practices
"""

# =============================================================================
# SECTION 1: BASIC TRY-EXCEPT
# =============================================================================

print("=" * 60)
print("BASIC TRY-EXCEPT")
print("=" * 60)

# Simple exception handling
try:
    result = 10 / 0
except ZeroDivisionError:
    print("  Cannot divide by zero!")

# Catching the exception object
try:
    result = 10 / 0
except ZeroDivisionError as e:
    print(f"  Error: {e}")
    print(f"  Type: {type(e).__name__}")

# =============================================================================
# SECTION 2: MULTIPLE EXCEPTIONS
# =============================================================================

print("\n" + "=" * 60)
print("MULTIPLE EXCEPTIONS")
print("=" * 60)


def divide(a, b):
    """Divide two numbers with exception handling."""
    try:
        return a / b
    except ZeroDivisionError:
        print("  Cannot divide by zero!")
        return None
    except TypeError:
        print("  Invalid types!")
        return None


print(f"divide(10, 2) = {divide(10, 2)}")
print(f"divide(10, 0) = {divide(10, 0)}")
print(f"divide('10', 2) = {divide('10', 2)}")

# Multiple exceptions in one block
try:
    value = int("abc")
except (ValueError, TypeError) as e:
    print(f"\n  Caught: {type(e).__name__}: {e}")

# Catching all exceptions (use sparingly!)
try:
    result = 10 / 0
except Exception as e:
    print(f"\n  Caught exception: {e}")

# =============================================================================
# SECTION 3: ELSE AND FINALLY
# =============================================================================

print("\n" + "=" * 60)
print("ELSE AND FINALLY CLAUSES")
print("=" * 60)

# else: runs if no exception occurred
# finally: always runs

def safe_divide(a, b):
    """Divide with complete exception handling."""
    try:
        result = a / b
    except ZeroDivisionError:
        print("  Division by zero!")
        return None
    except TypeError:
        print("  Invalid types!")
        return None
    else:
        print("  Division successful!")
        return result
    finally:
        print("  Cleanup complete.")


print("safe_divide(10, 2):")
safe_divide(10, 2)

print("\nsafe_divide(10, 0):")
safe_divide(10, 0)

# =============================================================================
# SECTION 4: EXCEPTION INFORMATION
# =============================================================================

print("\n" + "=" * 60)
print("EXCEPTION INFORMATION")
print("=" * 60)

import sys
import traceback

try:
    result = 10 / 0
except ZeroDivisionError:
    exc_type, exc_value, exc_traceback = sys.exc_info()
    print(f"  Exception type: {exc_type.__name__}")
    print(f"  Exception value: {exc_value}")
    print(f"  Traceback: {exc_traceback}")

# Using traceback module
try:
    def inner():
        return 10 / 0
    inner()
except ZeroDivisionError:
    print("\n  Traceback (formatted):")
    traceback.print_exc()

# =============================================================================
# SECTION 5: RAISING EXCEPTIONS
# =============================================================================

print("\n" + "=" * 60)
print("RAISING EXCEPTIONS")
print("=" * 60)


def validate_age(age):
    """Validate age with custom exceptions."""
    if not isinstance(age, int):
        raise TypeError("Age must be an integer")
    if age < 0:
        raise ValueError("Age cannot be negative")
    if age > 150:
        raise ValueError("Age seems unrealistic")
    return age


try:
    validate_age(-5)
except ValueError as e:
    print(f"  Validation error: {e}")

# Re-raising exceptions
try:
    try:
        result = 10 / 0
    except ZeroDivisionError:
        print("  Logging the error...")
        raise  # Re-raise the same exception
except ZeroDivisionError:
    print("  Caught re-raised exception")

# =============================================================================
# SECTION 6: EXCEPTION CHAINING
# =============================================================================

print("\n" + "=" * 60)
print("EXCEPTION CHAINING")
print("=" * 60)


def load_config(filename):
    """Load configuration from file."""
    try:
        with open(filename, 'r') as f:
            return f.read()
    except FileNotFoundError as e:
        raise RuntimeError(f"Config file not found: {filename}") from e


try:
    load_config("nonexistent.txt")
except RuntimeError as e:
    print(f"  Error: {e}")
    print(f"  Cause: {e.__cause__}")

# =============================================================================
# SECTION 7: BEST PRACTICES
# =============================================================================

print("\n" + "=" * 60)
print("BEST PRACTICES")
print("=" * 60)

BEST_PRACTICES = """
1. BE SPECIFIC
   - Catch specific exceptions, not bare except:
   - Good: except ValueError:
   - Bad: except: (catches everything including KeyboardInterrupt)

2. DON'T SILENCE ERRORS
   - At least log the error
   - Bad:
     try:
         do_something()
     except:
         pass  # Silently ignores all errors!

3. USE FINALLY FOR CLEANUP
   - Close files, connections, etc. in finally block

4. KEEP TRY BLOCKS SMALL
   - Only wrap code that might raise exceptions
   - Makes debugging easier

5. PROVIDE HELPFUL ERROR MESSAGES
   - Include context in error messages

6. USE CUSTOM EXCEPTIONS
   - Create your own exception classes for clarity
"""

print(BEST_PRACTICES)

# =============================================================================
# SECTION 8: COMMON EXCEPTIONS
# =============================================================================

print("\n" + "=" * 60)
print("COMMON BUILT-IN EXCEPTIONS")
print("=" * 60)

COMMON_EXCEPTIONS = """
Exception               Description
---------               -----------
ValueError              Invalid value for operation
TypeError               Wrong type for operation
KeyError                Key not found in dictionary
IndexError              Index out of range
FileNotFoundError       File doesn't exist
ZeroDivisionError       Division by zero
AttributeError          Attribute doesn't exist
ImportError             Module import failed
RuntimeError            Generic runtime error
StopIteration           End of iterator
PermissionError         Insufficient permissions
TimeoutError            Operation timed out
"""

print(COMMON_EXCEPTIONS)

# =============================================================================
# MAIN EXECUTION
# =============================================================================

if __name__ == "__main__":
    print("\n" + "=" * 60)
    print("✅ You've learned exception handling!")
    print("📚 Next: Learn about custom exceptions")
    print("=" * 60)
