"""
Module: basics.py
Topic: Function Basics
Level: Intermediate

This file teaches you about:
- Defining functions
- Calling functions
- Return values
- Docstrings
- Function annotations
- Best practices
"""

# =============================================================================
# SECTION 1: DEFINING FUNCTIONS
# =============================================================================

print("=" * 60)
print("DEFINING FUNCTIONS")
print("=" * 60)

# Basic function definition
def greet():
    """Print a greeting message."""
    print("Hello, World!")


# Calling the function
greet()

# Function with parameters
def greet_person(name):
    """Greet a person by name."""
    print(f"Hello, {name}!")


greet_person("Alice")
greet_person("Bob")

# Function with multiple parameters
def introduce(name, age, city):
    """Introduce a person with their details."""
    print(f"{name} is {age} years old and lives in {city}")


introduce("Charlie", 30, "New York")

# =============================================================================
# SECTION 2: RETURN VALUES
# =============================================================================

print("\n" + "=" * 60)
print("RETURN VALUES")
print("=" * 60)

# Function that returns a value
def add(a, b):
    """Add two numbers and return the result."""
    return a + b


result = add(5, 3)
print(f"add(5, 3) = {result}")

# Functions without explicit return return None
def no_return():
    print("This function doesn't return anything")


value = no_return()
print(f"no_return() returns: {value}")

# Multiple return values (actually returns a tuple)
def get_dimensions():
    """Return width and height."""
    return 1920, 1080


width, height = get_dimensions()
print(f"Dimensions: {width}x{height}")

# Return a tuple explicitly
def get_person_info():
    """Return person info as a tuple."""
    return ("Alice", 25, "Engineer")


info = get_person_info()
print(f"Person info: {info}")

# Early return
def divide(a, b):
    """Divide a by b, return None if b is 0."""
    if b == 0:
        return None
    return a / b


print(f"divide(10, 2) = {divide(10, 2)}")
print(f"divide(10, 0) = {divide(10, 0)}")

# =============================================================================
# SECTION 3: DOCSTRINGS
# =============================================================================

print("\n" + "=" * 60)
print("DOCSTRINGS")
print("=" * 60)

def calculate_compound_interest(principal, rate, years, compounds_per_year=12):
    """
    Calculate compound interest.

    Uses the formula: A = P(1 + r/n)^(nt)

    Args:
        principal (float): The initial investment amount.
        rate (float): Annual interest rate as a decimal (e.g., 0.05 for 5%).
        years (float): Number of years to invest.
        compounds_per_year (int, optional): Times interest compounds per year.
            Defaults to 12.

    Returns:
        float: The final amount after compound interest.

    Raises:
        ValueError: If principal, rate, or years is negative.

    Example:
        >>> calculate_compound_interest(10000, 0.05, 10)
        16470.094976902793
    """
    if principal < 0 or rate < 0 or years < 0:
        raise ValueError("Principal, rate, and years must be non-negative")

    amount = principal * (1 + rate / compounds_per_year) ** (compounds_per_year * years)
    return amount


# Accessing docstrings
print("Docstring:")
print(calculate_compound_interest.__doc__)

# Using help
# help(calculate_compound_interest)

# =============================================================================
# SECTION 4: FUNCTION ANNOTATIONS (TYPE HINTS)
# =============================================================================

print("\n" + "=" * 60)
print("FUNCTION ANNOTATIONS")
print("=" * 60)

from typing import List, Dict, Optional, Union, Tuple

# Basic type hints
def greet_typed(name: str) -> str:
    """Greet a person with type hints."""
    return f"Hello, {name}!"


print(greet_typed("Alice"))

# Multiple parameters with types
def calculate_total(prices: List[float], tax_rate: float = 0.1) -> float:
    """Calculate total price with tax."""
    subtotal = sum(prices)
    return subtotal * (1 + tax_rate)


total = calculate_total([10.0, 20.0, 30.0])
print(f"Total with tax: ${total:.2f}")

# Optional return type
def find_user(user_id: int, users: Dict[int, str]) -> Optional[str]:
    """Find a user by ID, return None if not found."""
    return users.get(user_id)


users = {1: "Alice", 2: "Bob", 3: "Charlie"}
print(f"User 2: {find_user(2, users)}")
print(f"User 99: {find_user(99, users)}")

# Union types
def process_value(value: Union[int, str]) -> str:
    """Process a value that could be int or string."""
    return str(value).upper()


print(f"process_value(42): {process_value(42)}")
print(f"process_value('hello'): {process_value('hello')}")

# Tuple return type
def get_min_max(numbers: List[int]) -> Tuple[int, int]:
    """Return minimum and maximum values."""
    return min(numbers), max(numbers)


print(f"Min/Max: {get_min_max([3, 1, 4, 1, 5, 9])}")

# =============================================================================
# SECTION 5: SCOPE
# =============================================================================

print("\n" + "=" * 60)
print("SCOPE")
print("=" * 60)

# Global variable
global_var = "I'm global"


def demonstrate_scope():
    """Demonstrate variable scope."""
    # Local variable
    local_var = "I'm local"
    print(f"  Inside function: {local_var}")
    print(f"  Can access global: {global_var}")


demonstrate_scope()
print(f"Outside function: {global_var}")
# print(local_var)  # This would raise NameError

# Modifying global variables (not recommended)
counter = 0


def increment_counter():
    """Increment the global counter."""
    global counter
    counter += 1
    print(f"  Counter inside: {counter}")


print("\nGlobal variable modification:")
increment_counter()
increment_counter()
print(f"Counter outside: {counter}")

# Nonlocal variable (in nested functions)
def outer_function():
    """Demonstrate nonlocal scope."""
    outer_var = "outer"

    def inner_function():
        nonlocal outer_var
        outer_var = "modified by inner"
        print(f"  Inner: {outer_var}")

    print(f"Before inner: {outer_var}")
    inner_function()
    print(f"After inner: {outer_var}")


print("\nNonlocal scope:")
outer_function()

# LEGB Rule: Local -> Enclosing -> Global -> Built-in
x = "global"


def outer():
    x = "enclosing"

    def inner():
        x = "local"
        print(f"  Inner x: {x}")

    inner()
    print(f"  Outer x: {x}")


print("\nLEGB Rule:")
outer()
print(f"Global x: {x}")

# =============================================================================
# SECTION 6: FUNCTIONS AS OBJECTS
# =============================================================================

print("\n" + "=" * 60)
print("FUNCTIONS AS OBJECTS")
print("=" * 60)

# Functions are first-class objects
def say_hello(name):
    return f"Hello, {name}"


# Assign function to variable
greeting = say_hello
print(f"greeting('Alice'): {greeting('Alice')}")

# Store functions in a list
def add(a, b):
    return a + b


def subtract(a, b):
    return a - b


def multiply(a, b):
    return a * b


operations = [add, subtract, multiply]

print("\nFunctions in a list:")
for op in operations:
    print(f"  {op.__name__}(10, 5) = {op(10, 5)}")

# Pass function as argument
def apply_operation(a, b, operation):
    """Apply an operation to two numbers."""
    return operation(a, b)


print(f"\napply_operation(10, 5, multiply): {apply_operation(10, 5, multiply)}")

# Return function from function
def get_operation(name):
    """Return a function based on name."""
    operations = {
        'add': add,
        'subtract': subtract,
        'multiply': multiply
    }
    return operations.get(name, add)


my_op = get_operation('multiply')
print(f"\nget_operation('multiply')(10, 5): {my_op(10, 5)}")

# =============================================================================
# SECTION 7: RECURSION
# =============================================================================

print("\n" + "=" * 60)
print("RECURSION")
print("=" * 60)


def factorial(n):
    """Calculate factorial recursively."""
    if n <= 1:
        return 1
    return n * factorial(n - 1)


print("Factorial:")
for i in range(6):
    print(f"  {i}! = {factorial(i)}")


def fibonacci(n):
    """Calculate nth Fibonacci number recursively."""
    if n <= 1:
        return n
    return fibonacci(n - 1) + fibonacci(n - 2)


print("\nFibonacci:")
for i in range(10):
    print(f"  F({i}) = {fibonacci(i)}")


# Memoization to improve recursive performance
def fibonacci_memo(n, memo=None):
    """Calculate Fibonacci with memoization."""
    if memo is None:
        memo = {}
    if n in memo:
        return memo[n]
    if n <= 1:
        return n
    memo[n] = fibonacci_memo(n - 1, memo) + fibonacci_memo(n - 2, memo)
    return memo[n]


print("\nFibonacci with memoization:")
print(f"  F(50) = {fibonacci_memo(50)}")

# =============================================================================
# SECTION 8: BEST PRACTICES
# =============================================================================

print("\n" + "=" * 60)
print("BEST PRACTICES")
print("=" * 60)

# 1. Functions should do one thing well
def calculate_discount(price, discount_rate):
    """Calculate discounted price."""
    return price * (1 - discount_rate)


def format_price(price):
    """Format price as currency string."""
    return f"${price:.2f}"


# 2. Use descriptive names
# Bad
def process(d):
    return d * 1.1


# Good
def apply_sales_tax(amount, tax_rate=0.1):
    """Apply sales tax to amount."""
    return amount * (1 + tax_rate)


# 3. Keep functions small (typically under 50 lines)
# 4. Use docstrings
# 5. Avoid side effects when possible

# Pure function (no side effects)
def add_pure(a, b):
    """Pure function - same input always gives same output."""
    return a + b


# Function with side effect
total = 0


def add_with_side_effect(a, b):
    """Function with side effect - modifies global state."""
    global total
    result = a + b
    total += result
    return result


# =============================================================================
# PRACTICAL EXAMPLES
# =============================================================================

print("\n" + "=" * 60)
print("PRACTICAL EXAMPLES")
print("=" * 60)


def create_counter():
    """Create a counter with encapsulation."""
    count = 0

    def increment():
        nonlocal count
        count += 1
        return count

    def decrement():
        nonlocal count
        count -= 1
        return count

    def get_count():
        return count

    return {'increment': increment, 'decrement': decrement, 'get_count': get_count}


print("Counter with closure:")
counter = create_counter()
print(f"  Count: {counter['get_count']()}")
print(f"  Increment: {counter['increment']()}")
print(f"  Increment: {counter['increment']()}")
print(f"  Decrement: {counter['decrement']()}")


def validate_input(data, validators):
    """
    Validate data against validators.

    Args:
        data: Dictionary of input data
        validators: Dictionary of field names to validator functions

    Returns:
        Tuple of (is_valid, errors)
    """
    errors = []

    for field, validator in validators.items():
        if field in data:
            result = validator(data[field])
            if result is not True:
                errors.append(f"{field}: {result}")

    return len(errors) == 0, errors


print("\nValidation framework:")
validators = {
    'age': lambda x: True if isinstance(x, int) and x >= 0 else "Must be non-negative integer",
    'name': lambda x: True if len(x) >= 2 else "Must be at least 2 characters",
    'email': lambda x: True if '@' in x else "Must be valid email"
}

data = {'age': 25, 'name': 'A', 'email': 'invalid'}
is_valid, errors = validate_input(data, validators)
print(f"  Valid: {is_valid}")
for error in errors:
    print(f"  Error: {error}")

# =============================================================================
# MAIN EXECUTION
# =============================================================================

if __name__ == "__main__":
    print("\n" + "=" * 60)
    print("✅ You've learned function basics!")
    print("📚 Next: Learn about parameters in parameters.py")
    print("=" * 60)
