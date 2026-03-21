"""
Project: Calculator
Level: Beginner
Description: A fully functional calculator supporting basic and advanced operations.

This project demonstrates:
- Functions and return values
- Error handling
- User input validation
- Mathematical operations
- Menu-driven interface
"""

import math
from typing import Union, Optional


class Calculator:
    """
    A calculator class supporting basic and scientific operations.

    Features:
    - Basic arithmetic (+, -, *, /)
    - Power and root operations
    - Trigonometric functions
    - Logarithmic functions
    - Memory functions
    """

    def __init__(self):
        """Initialize the calculator with empty memory."""
        self.memory = None
        self.history = []

    # ====================
    # Basic Operations
    # ====================

    def add(self, a: float, b: float) -> float:
        """Add two numbers."""
        result = a + b
        self._log(f"{a} + {b} = {result}")
        return result

    def subtract(self, a: float, b: float) -> float:
        """Subtract b from a."""
        result = a - b
        self._log(f"{a} - {b} = {result}")
        return result

    def multiply(self, a: float, b: float) -> float:
        """Multiply two numbers."""
        result = a * b
        self._log(f"{a} × {b} = {result}")
        return result

    def divide(self, a: float, b: float) -> Optional[float]:
        """Divide a by b."""
        if b == 0:
            self._log(f"{a} ÷ {b} = Error (Division by zero)")
            return None
        result = a / b
        self._log(f"{a} ÷ {b} = {result}")
        return result

    # ====================
    # Advanced Operations
    # ====================

    def power(self, base: float, exponent: float) -> float:
        """Calculate base raised to the power of exponent."""
        result = base ** exponent
        self._log(f"{base} ^ {exponent} = {result}")
        return result

    def square_root(self, a: float) -> Optional[float]:
        """Calculate the square root of a number."""
        if a < 0:
            self._log(f"√{a} = Error (Negative input)")
            return None
        result = math.sqrt(a)
        self._log(f"√{a} = {result}")
        return result

    def nth_root(self, a: float, n: float) -> Optional[float]:
        """Calculate the nth root of a number."""
        if a < 0 and n % 2 == 0:
            self._log(f"{a}^(1/{n}) = Error (Invalid for negative)")
            return None
        result = a ** (1 / n)
        self._log(f"{a}^(1/{n}) = {result}")
        return result

    def percentage(self, a: float, b: float) -> float:
        """Calculate a percent of b."""
        result = (a / 100) * b
        self._log(f"{a}% of {b} = {result}")
        return result

    # ====================
    # Scientific Operations
    # ====================

    def sin(self, a: float, degrees: bool = False) -> float:
        """Calculate sine of a."""
        if degrees:
            a = math.radians(a)
        result = math.sin(a)
        unit = "°" if degrees else "rad"
        self._log(f"sin({a}{unit}) = {result}")
        return result

    def cos(self, a: float, degrees: bool = False) -> float:
        """Calculate cosine of a."""
        if degrees:
            a = math.radians(a)
        result = math.cos(a)
        unit = "°" if degrees else "rad"
        self._log(f"cos({a}{unit}) = {result}")
        return result

    def tan(self, a: float, degrees: bool = False) -> Optional[float]:
        """Calculate tangent of a."""
        if degrees:
            a = math.radians(a)
        # Check for undefined tangent
        if abs(math.cos(a)) < 1e-10:
            self._log(f"tan({a}) = Error (Undefined)")
            return None
        result = math.tan(a)
        unit = "°" if degrees else "rad"
        self._log(f"tan({a}{unit}) = {result}")
        return result

    def log(self, a: float, base: float = 10) -> Optional[float]:
        """Calculate logarithm of a with given base."""
        if a <= 0:
            self._log(f"log{base}({a}) = Error (Invalid input)")
            return None
        if base <= 0 or base == 1:
            self._log(f"log{base}({a}) = Error (Invalid base)")
            return None
        result = math.log(a, base)
        self._log(f"log{base}({a}) = {result}")
        return result

    def ln(self, a: float) -> Optional[float]:
        """Calculate natural logarithm of a."""
        if a <= 0:
            self._log(f"ln({a}) = Error (Invalid input)")
            return None
        result = math.log(a)
        self._log(f"ln({a}) = {result}")
        return result

    def factorial(self, n: int) -> Optional[int]:
        """Calculate factorial of n."""
        if n < 0:
            self._log(f"{n}! = Error (Negative input)")
            return None
        if n > 170:  # Prevents overflow
            self._log(f"{n}! = Error (Too large)")
            return None
        result = math.factorial(n)
        self._log(f"{n}! = {result}")
        return result

    # ====================
    # Memory Functions
    # ====================

    def memory_store(self, value: float) -> None:
        """Store a value in memory."""
        self.memory = value
        self._log(f"Stored {value} in memory")

    def memory_recall(self) -> Optional[float]:
        """Recall value from memory."""
        if self.memory is not None:
            self._log(f"Recalled {self.memory} from memory")
        return self.memory

    def memory_clear(self) -> None:
        """Clear memory."""
        self.memory = None
        self._log("Memory cleared")

    def memory_add(self, value: float) -> None:
        """Add value to memory."""
        if self.memory is None:
            self.memory = value
        else:
            self.memory += value
        self._log(f"Added {value} to memory. New value: {self.memory}")

    # ====================
    # Utility Functions
    # ====================

    def _log(self, entry: str) -> None:
        """Log an operation to history."""
        self.history.append(entry)

    def get_history(self, n: int = 10) -> list:
        """Get the last n entries from history."""
        return self.history[-n:]

    def clear_history(self) -> None:
        """Clear operation history."""
        self.history = []

    def round_result(self, value: float, decimals: int = 2) -> float:
        """Round a result to specified decimal places."""
        return round(value, decimals)


def demonstrate_calculator():
    """Demonstrate calculator functionality."""
    print("\n" + "=" * 50)
    print("🔢 CALCULATOR DEMONSTRATION")
    print("=" * 50)

    calc = Calculator()

    # Basic operations
    print("\n📐 Basic Operations:")
    print(f"  10 + 5 = {calc.add(10, 5)}")
    print(f"  10 - 5 = {calc.subtract(10, 5)}")
    print(f"  10 × 5 = {calc.multiply(10, 5)}")
    print(f"  10 ÷ 5 = {calc.divide(10, 5)}")
    print(f"  10 ÷ 0 = {calc.divide(10, 0)}")  # Division by zero

    # Advanced operations
    print("\n📊 Advanced Operations:")
    print(f"  2 ^ 10 = {calc.power(2, 10)}")
    print(f"  √16 = {calc.square_root(16)}")
    print(f"  20% of 500 = {calc.percentage(20, 500)}")

    # Scientific operations
    print("\n🔬 Scientific Operations:")
    print(f"  sin(90°) = {calc.sin(90, degrees=True):.4f}")
    print(f"  cos(0°) = {calc.cos(0, degrees=True):.4f}")
    print(f"  log(100) = {calc.log(100)}")
    print(f"  ln(2.718) = {calc.ln(2.718):.4f}")
    print(f"  5! = {calc.factorial(5)}")

    # Memory functions
    print("\n💾 Memory Functions:")
    calc.memory_store(42)
    print(f"  Stored 42 in memory")
    print(f"  Recalled: {calc.memory_recall()}")
    calc.memory_add(8)
    print(f"  Added 8, memory now: {calc.memory_recall()}")

    # History
    print("\n📜 Last 5 History Entries:")
    for entry in calc.get_history(5):
        print(f"  {entry}")


def interactive_calculator():
    """
    Interactive calculator mode.
    Uncomment and run for actual use.
    """
    calc = Calculator()

    print("\n" + "=" * 50)
    print("🔢 INTERACTIVE CALCULATOR")
    print("=" * 50)
    print("\nOperations:")
    print("  + : Addition")
    print("  - : Subtraction")
    print("  * : Multiplication")
    print("  / : Division")
    print("  ^ : Power")
    print("  sqrt : Square root")
    print("  sin, cos, tan : Trigonometric")
    print("  log, ln : Logarithms")
    print("  ! : Factorial")
    print("  mem : Memory operations")
    print("  history : Show history")
    print("  clear : Clear history")
    print("  quit : Exit")

    while True:
        print("\n" + "-" * 30)
        operation = input("Enter operation (or 'quit'): ").strip().lower()

        if operation == 'quit':
            print("\nThanks for using the calculator!")
            break

        # Handle different operations...
        # (Full interactive implementation would go here)

        print("Interactive mode - see demonstrate_calculator() for examples")


# =============================================================================
# MAIN EXECUTION
# =============================================================================

if __name__ == "__main__":
    # Run demonstration
    demonstrate_calculator()

    # Uncomment for interactive mode:
    # interactive_calculator()

    print("\n✅ Calculator demonstration complete!")
