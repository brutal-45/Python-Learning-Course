"""
Module: hello_world.py
Topic: Your First Python Program
Level: Beginner

This file teaches you how to write and run your first Python program.
It covers the basics of Python syntax, printing output, and program structure.
"""

# =============================================================================
# SECTION 1: YOUR FIRST PYTHON PROGRAM
# =============================================================================
# The classic "Hello, World!" program is traditionally the first program
# written when learning a new programming language.

# In Python, printing output is simple - use the print() function
print("Hello, World!")

# You can print multiple items by separating them with commas
print("Hello", "World", "!")  # Output: Hello World !

# The print function automatically adds a newline at the end
print("Line 1")
print("Line 2")

# =============================================================================
# SECTION 2: PRINT FUNCTION PARAMETERS
# =============================================================================

# The 'sep' parameter controls how multiple items are separated
print("Hello", "World", sep="-")  # Output: Hello-World
print("2024", "03", "21", sep="/")  # Output: 2024/03/21

# The 'end' parameter controls what's printed at the end
print("Same", end=" ")
print("Line")  # Output: Same Line

# Combining sep and end
print("A", "B", "C", sep="|", end=" END\n")  # Output: A|B|C END

# =============================================================================
# SECTION 3: STRING BASICS
# =============================================================================

# Strings can be defined with single or double quotes (they're equivalent)
print('Single quotes work fine')
print("Double quotes work too")

# Use double quotes when the string contains single quotes
print("It's a beautiful day!")

# Use single quotes when the string contains double quotes
print('He said, "Hello!"')

# Triple quotes for multi-line strings
print("""
This is a
multi-line
string
""")

# Escape sequences
print("Line 1\nLine 2")  # \n = newline
print("Tab\tSpace")  # \t = tab
print("Backslash: \\")  # \\ = backslash
print("Quote: \"")  # \" = quote

# =============================================================================
# SECTION 4: F-STRINGS (FORMATTED STRING LITERALS)
# =============================================================================
# F-strings are the modern, preferred way to format strings in Python 3.6+

name = "Alice"
age = 25

# Basic f-string
print(f"Hello, {name}!")  # Output: Hello, Alice!

# F-string with expressions
print(f"{name} is {age} years old")  # Output: Alice is 25 years old

# F-string with calculations
print(f"Next year, {name} will be {age + 1}")  # Output: Next year, Alice will be 26

# F-string with method calls
print(f"Uppercase: {name.upper()}")  # Output: Uppercase: ALICE

# F-string formatting options
pi = 3.14159265
print(f"Pi rounded: {pi:.2f}")  # Output: Pi rounded: 3.14
print(f"Pi with 4 decimals: {pi:.4f}")  # Output: Pi with 4 decimals: 3.1416

# Width and alignment
print(f"|{'Left':<10}|")  # Left-aligned, 10 characters wide
print(f"|{'Center':^10}|")  # Centered, 10 characters wide
print(f"|{'Right':>10}|")  # Right-aligned, 10 characters wide

# =============================================================================
# SECTION 5: OTHER STRING FORMATTING METHODS
# =============================================================================

# .format() method (older but still useful)
print("Hello, {}!".format("World"))
print("{0} is {1} years old".format("Bob", 30))
print("{name} is {age} years old".format(name="Charlie", age=35))

# % formatting (legacy, avoid in new code)
name = "Dave"
print("Hello, %s!" % name)

# =============================================================================
# SECTION 6: RAW STRINGS
# =============================================================================
# Raw strings treat backslashes as literal characters

# Normal string - \n is a newline
print("Normal:\nNew line")

# Raw string - \n is literally backslash-n
print(r"Raw:\nNo new line")

# Raw strings are useful for file paths and regular expressions
file_path = r"C:\Users\Documents\file.txt"
print(f"File path: {file_path}")

# =============================================================================
# SECTION 7: PRACTICAL EXAMPLES
# =============================================================================

def demonstrate_hello_world():
    """
    A comprehensive demonstration of print statements and string formatting.
    This function showcases various ways to display output in Python.
    """
    print("=" * 60)
    print("HELLO WORLD DEMONSTRATION")
    print("=" * 60)
    
    # Basic printing
    print("\n1. Basic Print Statements:")
    print("   Simple string")
    print("   Multiple", "arguments", "here")
    
    # Separator and end parameters
    print("\n2. Custom Separators and Endings:")
    print("   ", "A", "B", "C", sep="-")
    print("   ", "Same", end=" ")
    print("Line")
    
    # F-strings
    print("\n3. F-Strings (Recommended):")
    user = "Python Learner"
    day = "Monday"
    print(f"   Hello, {user}!")
    print(f"   Today is {day}")
    print(f"   String length: {len(user)}")
    
    print("\n" + "=" * 60)


# =============================================================================
# SECTION 8: RUNNING THE DEMONSTRATION
# =============================================================================

if __name__ == "__main__":
    # This block runs when the file is executed directly
    # It won't run when the file is imported as a module
    
    print("\n" + "=" * 60)
    print("PYTHON BASICS - HELLO WORLD")
    print("=" * 60 + "\n")
    
    # Run the demonstration
    demonstrate_hello_world()
    
    print("\n✅ Congratulations! You've written your first Python program!")
    print("📚 Next: Learn about variables in variables.py")
