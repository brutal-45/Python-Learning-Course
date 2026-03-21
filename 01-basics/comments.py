"""
Module: comments.py
Topic: Comments and Documentation
Level: Beginner

This file teaches you about:
- Single-line comments
- Multi-line comments
- Docstrings
- Documentation best practices
"""

# =============================================================================
# SECTION 1: SINGLE-LINE COMMENTS
# =============================================================================

# This is a single-line comment
# Comments start with the # symbol
# They are ignored by Python interpreter

# Comments can be on their own line
x = 5  # Or they can be at the end of a line

# Use comments to:
# 1. Explain complex logic
# 2. Document assumptions
# 3. Leave notes for other developers
# 4. Temporarily disable code during debugging

# =============================================================================
# SECTION 2: MULTI-LINE COMMENTS
# =============================================================================

# Python doesn't have true multi-line comments
# But you can use multiple single-line comments:

# This is a multi-line comment
# that spans several lines
# using multiple # symbols

# OR use triple-quoted strings (docstrings) as pseudo-comments:
"""
This is technically a multi-line string,
not a comment, but it's often used like one.
It's not assigned to a variable, so it's ignored.
"""

# =============================================================================
# SECTION 3: DOCSTRINGS
# =============================================================================

def calculate_area(length, width):
    """
    Calculate the area of a rectangle.

    This function takes the length and width of a rectangle
    and returns its area.

    Args:
        length (float): The length of the rectangle.
        width (float): The width of the rectangle.

    Returns:
        float: The area of the rectangle (length * width).

    Raises:
        ValueError: If length or width is negative.

    Example:
        >>> calculate_area(5, 3)
        15
        >>> calculate_area(2.5, 4)
        10.0
    """
    if length < 0 or width < 0:
        raise ValueError("Dimensions must be non-negative")
    return length * width


class BankAccount:
    """
    A class representing a bank account.

    This class provides basic banking operations including
    deposits, withdrawals, and balance inquiries.

    Attributes:
        owner (str): The name of the account owner.
        balance (float): The current account balance.

    Example:
        >>> account = BankAccount("Alice", 1000)
        >>> account.deposit(500)
        >>> account.balance
        1500
    """

    def __init__(self, owner, initial_balance=0):
        """
        Initialize a new BankAccount.

        Args:
            owner (str): The name of the account owner.
            initial_balance (float, optional): Starting balance. Defaults to 0.
        """
        self.owner = owner
        self.balance = initial_balance

    def deposit(self, amount):
        """
        Deposit money into the account.

        Args:
            amount (float): The amount to deposit.

        Returns:
            float: The new balance.

        Raises:
            ValueError: If amount is not positive.
        """
        if amount <= 0:
            raise ValueError("Deposit amount must be positive")
        self.balance += amount
        return self.balance

    def withdraw(self, amount):
        """
        Withdraw money from the account.

        Args:
            amount (float): The amount to withdraw.

        Returns:
            float: The new balance.

        Raises:
            ValueError: If amount is not positive or exceeds balance.
        """
        if amount <= 0:
            raise ValueError("Withdrawal amount must be positive")
        if amount > self.balance:
            raise ValueError("Insufficient funds")
        self.balance -= amount
        return self.balance


# =============================================================================
# SECTION 4: DOCSTRING FORMATS
# =============================================================================

def google_style_docstring(param1, param2):
    """Short description.

    Longer description if needed. This explains what the function does
    in more detail.

    Args:
        param1 (int): Description of param1.
        param2 (str): Description of param2.

    Returns:
        bool: Description of return value.

    Raises:
        TypeError: If param1 is not an integer.
    """
    return isinstance(param1, int)


def numpy_style_docstring(param1, param2):
    """
    Short description.

    Longer description if needed.

    Parameters
    ----------
    param1 : int
        Description of param1.
    param2 : str
        Description of param2.

    Returns
    -------
    bool
        Description of return value.

    Raises
    ------
    TypeError
        If param1 is not an integer.
    """
    return isinstance(param1, int)


def sphinx_style_docstring(param1, param2):
    """Short description.

    Longer description if needed.

    :param param1: Description of param1.
    :type param1: int
    :param param2: Description of param2.
    :type param2: str
    :return: Description of return value.
    :rtype: bool
    :raises TypeError: If param1 is not an integer.
    """
    return isinstance(param1, int)


# =============================================================================
# SECTION 5: ACCESSING DOCSTRINGS
# =============================================================================

print("=" * 60)
print("ACCESSING DOCSTRINGS")
print("=" * 60)

# Access docstring with __doc__ attribute
print("\nFunction docstring:")
print(calculate_area.__doc__)

# Or use help() for more details
# help(calculate_area)

# Built-in functions have docstrings too
print("\nprint function docstring (first 200 chars):")
print(print.__doc__[:200] + "...")


# =============================================================================
# SECTION 6: COMMENT BEST PRACTICES
# =============================================================================

# ✅ GOOD: Explain WHY, not WHAT
# Calculate compound interest using the formula A = P(1 + r/n)^(nt)
# where P is principal, r is rate, n is compounding frequency
def calculate_compound_interest(principal, rate, time, n=12):
    return principal * (1 + rate/n) ** (n * time)


# ❌ BAD: Obvious comments that don't add value
# Set x to 5
x = 5

# Increment x by 1
x = x + 1


# ✅ GOOD: Document assumptions and edge cases
def divide_numbers(a, b):
    """
    Divide two numbers safely.

    Note: This function assumes both inputs are numeric types.
    Division by zero returns None rather than raising an exception.
    """
    if b == 0:
        return None  # Avoid ZeroDivisionError
    return a / b


# ✅ GOOD: TODO comments for future work
# TODO: Add error handling for non-numeric inputs
# FIXME: This doesn't handle edge case where b is very small
# HACK: Temporary workaround for API rate limiting
# NOTE: This algorithm has O(n^2) complexity

# =============================================================================
# SECTION 7: TYPE HINTS (MODERN DOCUMENTATION)
# =============================================================================

from typing import List, Dict, Optional, Union, Tuple


def greet(name: str) -> str:
    """
    Greet a person by name.

    Args:
        name: The name of the person to greet.

    Returns:
        A greeting message.
    """
    return f"Hello, {name}!"


def process_data(
    data: List[int],
    threshold: float = 0.5,
    include_none: bool = False
) -> Dict[str, Union[int, float]]:
    """
    Process a list of integers with various options.

    Args:
        data: List of integers to process.
        threshold: Threshold value for filtering. Defaults to 0.5.
        include_none: Whether to include None values. Defaults to False.

    Returns:
        Dictionary with processing results.
    """
    return {
        "count": len(data),
        "sum": sum(data),
        "average": sum(data) / len(data) if data else 0
    }


def find_item(items: List[str], target: str) -> Optional[int]:
    """
    Find the index of an item in a list.

    Args:
        items: List to search.
        target: Item to find.

    Returns:
        Index of the item, or None if not found.
    """
    try:
        return items.index(target)
    except ValueError:
        return None


def get_coordinates() -> Tuple[float, float]:
    """Return latitude and longitude coordinates."""
    return (40.7128, -74.0060)


# =============================================================================
# SECTION 8: SELF-DOCUMENTING CODE
# =============================================================================

# ❌ BAD: Needs comments to explain
def calc(a, b, c):
    return (a + b) * c


# ✅ GOOD: Self-documenting with clear names
def calculate_total_price(base_price: float, tax_rate: float, quantity: int) -> float:
    """
    Calculate the total price including tax for multiple items.

    Self-documenting code uses clear names so comments are less needed.
    """
    subtotal = base_price * quantity
    tax = subtotal * tax_rate
    total = subtotal + tax
    return total


# =============================================================================
# SECTION 9: PRACTICAL EXAMPLE
# =============================================================================

print("\n" + "=" * 60)
print("PRACTICAL EXAMPLE: DOCUMENTED MODULE")
print("=" * 60)

import math


class Circle:
    """
    A class to represent a circle and perform circle-related calculations.

    This class provides methods to calculate various properties of a circle
    including area, circumference, and diameter. All calculations follow
    standard geometric formulas.

    Attributes:
        radius (float): The radius of the circle.

    Example:
        >>> circle = Circle(5)
        >>> circle.area()
        78.53981633974483
        >>> circle.circumference()
        31.41592653589793
    """

    def __init__(self, radius: float):
        """
        Initialize a Circle with the given radius.

        Args:
            radius: The radius of the circle. Must be non-negative.

        Raises:
            ValueError: If radius is negative.
        """
        if radius < 0:
            raise ValueError("Radius cannot be negative")
        self.radius = radius

    def area(self) -> float:
        """Calculate the area of the circle using πr²."""
        return math.pi * self.radius ** 2

    def circumference(self) -> float:
        """Calculate the circumference using 2πr."""
        return 2 * math.pi * self.radius

    def diameter(self) -> float:
        """Calculate the diameter (2 × radius)."""
        return 2 * self.radius

    def __repr__(self) -> str:
        """Return a string representation of the circle."""
        return f"Circle(radius={self.radius})"


# Demo the Circle class
circle = Circle(5)
print(f"\nCircle with radius {circle.radius}:")
print(f"  Area: {circle.area():.2f}")
print(f"  Circumference: {circle.circumference():.2f}")
print(f"  Diameter: {circle.diameter():.2f}")
print(f"  Representation: {circle}")

# =============================================================================
# SECTION 10: GENERATING DOCUMENTATION
# =============================================================================

print("\n" + "=" * 60)
print("GENERATING DOCUMENTATION")
print("=" * 60)

# Python can auto-generate documentation from docstrings
# using tools like pydoc, Sphinx, or pdoc

# Using pydoc from command line:
# pydoc comments.py  # View documentation
# pydoc -w comments  # Generate HTML documentation

# Accessing documentation programmatically
import pydoc

print("\nCircle class documentation:")
print(pydoc.render_doc(Circle, "Help on %s"))

# =============================================================================
# MAIN EXECUTION
# =============================================================================

if __name__ == "__main__":
    print("\n" + "=" * 60)
    print("✅ You've learned about comments and documentation!")
    print("📚 Next: Move to 02-data-types to learn about Python data types")
    print("=" * 60)
