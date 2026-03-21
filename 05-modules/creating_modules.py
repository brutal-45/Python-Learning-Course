"""
Module: creating_modules.py
Topic: Creating Your Own Modules
Level: Intermediate

This file teaches you about:
- Creating a module
- Module structure
- __name__ == '__main__'
- Module best practices
"""

# =============================================================================
# MODULE STRUCTURE
# =============================================================================

"""
A Python module is simply a .py file that can be imported.

Best practice structure:
- Module docstring at top
- Imports grouped (stdlib, third-party, local)
- Constants
- Classes
- Functions
- __all__ definition
- if __name__ == "__main__" block
"""

# =============================================================================
# THE __NAME__ VARIABLE
# =============================================================================

print("=" * 60)
print("THE __NAME__ VARIABLE")
print("=" * 60)

print(f"""
When a module is imported, __name__ is set to the module's name.
When a module is run directly, __name__ is set to '__main__'.

Current __name__: {__name__!r}

Example:
    if __name__ == "__main__":
        # This only runs when file is executed directly
        main()
""")

# =============================================================================
# PRACTICAL EXAMPLE: MATH UTILITIES
# =============================================================================

import math

# Constants
PI = math.pi
E = math.e
GOLDEN_RATIO = (1 + math.sqrt(5)) / 2


def is_prime(n: int) -> bool:
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


def fibonacci(n: int) -> int:
    """Calculate the nth Fibonacci number."""
    if n <= 0:
        return 0
    if n == 1:
        return 1
    return fibonacci(n - 1) + fibonacci(n - 2)


def gcd(a: int, b: int) -> int:
    """Calculate greatest common divisor."""
    while b:
        a, b = b, a % b
    return a


# Define public API
__all__ = ['PI', 'E', 'GOLDEN_RATIO', 'is_prime', 'fibonacci', 'gcd']


print("=" * 60)
print("MATH UTILITIES MODULE DEMO")
print("=" * 60)

print(f"Is 17 prime? {is_prime(17)}")
print(f"Fibonacci(10) = {fibonacci(10)}")
print(f"GCD(48, 18) = {gcd(48, 18)}")

# =============================================================================
# MAIN EXECUTION
# =============================================================================

if __name__ == "__main__":
    print("\n" + "=" * 60)
    print("✅ You've learned about creating modules!")
    print("=" * 60)
