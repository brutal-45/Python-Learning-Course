"""
Module: input_output.py
Topic: Input and Output Operations
Level: Beginner

This file teaches you how to:
- Take user input with input()
- Format and display output
- Handle different input types
- Work with command-line arguments
"""

# =============================================================================
# SECTION 1: THE input() FUNCTION
# =============================================================================

print("=" * 60)
print("THE input() FUNCTION")
print("=" * 60)

# Basic input
# name = input("What is your name? ")
# print(f"Hello, {name}!")

# Note: input() always returns a STRING!
# age = input("How old are you? ")
# print(f"Next year you'll be {int(age) + 1}")

# =============================================================================
# SECTION 2: TYPE CONVERSION FOR INPUT
# =============================================================================

print("\n" + "=" * 60)
print("TYPE CONVERSION FOR INPUT")
print("=" * 60)

# When getting numeric input, you MUST convert the type

# Integer input
# age = int(input("Enter your age: "))
# print(f"You were born around {2024 - age}")

# Float input
# price = float(input("Enter the price: $"))
# print(f"With tax: ${price * 1.1:.2f}")

# Boolean input (need to handle manually)
# response = input("Continue? (yes/no): ")
# continue_program = response.lower() in ('yes', 'y', 'true', '1')

# =============================================================================
# SECTION 3: MULTIPLE INPUTS
# =============================================================================

print("\n" + "=" * 60)
print("MULTIPLE INPUTS")
print("=" * 60)

# Split input into multiple values
# coordinates = input("Enter x,y coordinates: ")
# x, y = coordinates.split(',')
# print(f"X: {x.strip()}, Y: {y.strip()}")

# Multiple inputs with map
# numbers = list(map(int, input("Enter numbers separated by space: ").split()))
# print(f"You entered: {numbers}")
# print(f"Sum: {sum(numbers)}")

# Using list comprehension
# numbers = [int(x) for x in input("Enter numbers: ").split()]
# print(f"Doubled: {[n * 2 for n in numbers]}")

# =============================================================================
# SECTION 4: FORMATTED OUTPUT
# =============================================================================

print("\n" + "=" * 60)
print("FORMATTED OUTPUT")
print("=" * 60)

# F-strings (Python 3.6+) - RECOMMENDED
name = "Alice"
age = 25
score = 95.5678

print(f"Name: {name}")
print(f"Age: {age}")
print(f"Score: {score:.2f}")  # 2 decimal places

# F-string formatting options
print(f"\n{'Formatted Output Examples':=^50}")

number = 42
print(f"Decimal: {number:d}")
print(f"Binary: {number:b}")
print(f"Octal: {number:o}")
print(f"Hexadecimal: {number:x}")
print(f"Hexadecimal (upper): {number:X}")

pi = 3.14159
print(f"\nFloat: {pi:f}")
print(f"Scientific: {pi:e}")
print(f"Percentage: {pi:.2%}")

# Width and alignment
print(f"\n{'Alignment':<15} | {'Value':>10}")
print(f"{'Left':<15} | {42:>10}")
print(f"{'Center':^15} | {42:^10}")
print(f"{'Right':>15} | {42:<10}")

# =============================================================================
# SECTION 5: PRINT OPTIONS
# =============================================================================

print("\n" + "=" * 60)
print("PRINT OPTIONS")
print("=" * 60)

# sep parameter - separator between items
print("2024", "03", "21", sep="-")  # 2024-03-21
print("A", "B", "C", sep=" | ")  # A | B | C

# end parameter - what to print at the end
print("Loading", end="")
for i in range(3):
    print(".", end="", flush=True)
    # time.sleep(0.5)  # Uncomment for animation effect
print(" Done!")

# Print to file
# with open('output.txt', 'w') as f:
#     print("This goes to a file", file=f)

# =============================================================================
# SECTION 6: ESCAPE SEQUENCES
# =============================================================================

print("\n" + "=" * 60)
print("ESCAPE SEQUENCES")
print("=" * 60)

print("New line: Line 1\nLine 2")
print("Tab:\tIndented")
print("Backslash: \\")
print("Quote: \"")
print("Single quote: \'")
print("Carriage return: ABC\rXYZ")  # XYZ replaces ABC
print("Backspace: ABC\bX")  # ABC with last char replaced by X

# =============================================================================
# SECTION 7: RAW STRINGS
# =============================================================================

print("\n" + "=" * 60)
print("RAW STRINGS")
print("=" * 60)

# Raw strings don't interpret escape sequences
normal_path = "C:\new\test"  # Problem! \n and \t are escape sequences
raw_path = r"C:\new\test"  # Solution: raw string

print(f"Normal string: {normal_path}")  # May produce unexpected output
print(f"Raw string: {raw_path}")  # Preserves backslashes

# Raw strings are essential for regular expressions
import re

pattern = r"\d+"  # Matches one or more digits
text = "I have 42 apples"
matches = re.findall(pattern, text)
print(f"Regex matches: {matches}")

# =============================================================================
# SECTION 8: FORMATTING METHODS COMPARISON
# =============================================================================

print("\n" + "=" * 60)
print("FORMATTING METHODS COMPARISON")
print("=" * 60)

item = "Apple"
price = 1.50
quantity = 3
total = price * quantity

# Method 1: F-strings (Python 3.6+) - RECOMMENDED
print(f"F-string: {quantity} {item}s at ${price:.2f} each = ${total:.2f}")

# Method 2: .format() method
print(".format(): {} {}s at ${:.2f} each = ${:.2f}".format(quantity, item, price, total))

# Method 3: % formatting (legacy)
print("%% formatting: %d %ss at $%.2f each = $%.2f" % (quantity, item, price, total))

# Method 4: String concatenation (not recommended)
print("Concat: " + str(quantity) + " " + item + "s at $" + str(round(price, 2)) + " each")

# =============================================================================
# SECTION 9: COMMAND-LINE ARGUMENTS
# =============================================================================

print("\n" + "=" * 60)
print("COMMAND-LINE ARGUMENTS")
print("=" * 60)

import sys

# sys.argv contains command-line arguments
# sys.argv[0] is the script name
# sys.argv[1:] are the actual arguments

print(f"Script name: {sys.argv[0]}")
print(f"Arguments: {sys.argv[1:]}")
print(f"Number of arguments: {len(sys.argv) - 1}")

# Example usage:
# python input_output.py arg1 arg2 arg3

# Better argument parsing with argparse (for real scripts)
import argparse

# Create a demo parser (in real use, you'd use this for actual arguments)
demo_parser = argparse.ArgumentParser(description='Demo argument parser')
demo_parser.add_argument('-n', '--name', type=str, default='World', help='Name to greet')
demo_parser.add_argument('-c', '--count', type=int, default=1, help='Number of greetings')
demo_parser.add_argument('-v', '--verbose', action='store_true', help='Verbose output')

# Note: In a real script, you would use:
# args = demo_parser.parse_args()
# print(f"Hello, {args.name}!" * args.count)

# =============================================================================
# SECTION 10: PRACTICAL EXAMPLES
# =============================================================================

print("\n" + "=" * 60)
print("PRACTICAL EXAMPLES")
print("=" * 60)


def simple_calculator():
    """
    A simple calculator that takes user input.
    """
    print("\n--- Simple Calculator ---")

    # In a real program, uncomment the input lines:
    # num1 = float(input("Enter first number: "))
    # operator = input("Enter operator (+, -, *, /): ")
    # num2 = float(input("Enter second number: "))

    # For demonstration, use fixed values:
    num1, operator, num2 = 10.0, '+', 5.0

    if operator == '+':
        result = num1 + num2
    elif operator == '-':
        result = num1 - num2
    elif operator == '*':
        result = num1 * num2
    elif operator == '/':
        if num2 != 0:
            result = num1 / num2
        else:
            return "Error: Division by zero!"
    else:
        return "Error: Invalid operator!"

    return f"{num1} {operator} {num2} = {result}"


print(simple_calculator())


def create_receipt():
    """
    Create a formatted receipt.
    """
    print("\n--- Receipt Generator ---")

    items = [
        ("Coffee", 4.50),
        ("Sandwich", 8.99),
        ("Cookie", 2.50),
    ]

    subtotal = sum(price for _, price in items)
    tax_rate = 0.08
    tax = subtotal * tax_rate
    total = subtotal + tax

    # Print formatted receipt
    print("\n" + "=" * 40)
    print(f"{'CAFE RECEIPT':^40}")
    print("=" * 40)

    for item, price in items:
        print(f"{item:<25} ${price:>10.2f}")

    print("-" * 40)
    print(f"{'Subtotal':<25} ${subtotal:>10.2f}")
    print(f"{'Tax (8%)':<25} ${tax:>10.2f}")
    print("=" * 40)
    print(f"{'TOTAL':<25} ${total:>10.2f}")
    print("=" * 40)
    print(f"{'Thank you for your visit!':^40}")


create_receipt()


def temperature_converter():
    """
    Convert temperature between Celsius and Fahrenheit.
    Demonstrates input handling and formatted output.
    """
    print("\n--- Temperature Converter ---")

    # For demonstration:
    temp = 25
    unit = 'C'

    # In real use:
    # temp = float(input("Enter temperature: "))
    # unit = input("Enter unit (C/F): ").upper()

    if unit.upper() == 'C':
        converted = (temp * 9/5) + 32
        print(f"{temp:.1f}°C = {converted:.1f}°F")
    elif unit.upper() == 'F':
        converted = (temp - 32) * 5/9
        print(f"{temp:.1f}°F = {converted:.1f}°C")
    else:
        print("Invalid unit! Use C or F.")


temperature_converter()

# =============================================================================
# SECTION 11: INPUT VALIDATION
# =============================================================================

print("\n" + "=" * 60)
print("INPUT VALIDATION")
print("=" * 60)


def get_valid_int(prompt, min_val=None, max_val=None):
    """
    Get a valid integer from user input with range validation.
    """
    while True:
        try:
            # value = int(input(prompt))  # Uncomment for real input
            value = 5  # Demo value
            if min_val is not None and value < min_val:
                print(f"Value must be at least {min_val}")
                continue
            if max_val is not None and value > max_val:
                print(f"Value must be at most {max_val}")
                continue
            return value
        except ValueError:
            print("Please enter a valid integer!")


def get_valid_email(prompt):
    """
    Get a valid email address from user input.
    """
    import re
    pattern = r'^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$'

    while True:
        # email = input(prompt)  # Uncomment for real input
        email = "user@example.com"  # Demo value
        if re.match(pattern, email):
            return email
        print("Please enter a valid email address!")


# Demo validation
print("\nValidation Examples:")
age = get_valid_int("Enter age (0-120): ", 0, 120)
print(f"Valid age: {age}")

email = get_valid_email("Enter email: ")
print(f"Valid email: {email}")

# =============================================================================
# MAIN EXECUTION
# =============================================================================

if __name__ == "__main__":
    print("\n" + "=" * 60)
    print("✅ You've learned about input and output in Python!")
    print("📚 Next: Learn about comments and documentation in comments.py")
    print("=" * 60)
