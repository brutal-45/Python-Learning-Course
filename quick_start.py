"""
Python Learning Repository - Quick Start Guide
==============================================

This script provides a quick demonstration of key Python concepts.
Run this file to see a summary of what you'll learn.

python quick_start.py
"""

print("""
╔══════════════════════════════════════════════════════════════╗
║                   PYTHON LEARNING REPOSITORY                 ║
║                     Quick Start Guide                        ║
╚══════════════════════════════════════════════════════════════╝
""")

# =============================================================================
# 1. BASICS
# =============================================================================

print("📚 MODULE 01: BASICS")
print("-" * 40)

# Variables
name = "Python"
age = 33
print(f"  Variables: name={name}, age={age}")

# Data Types
print(f"  Types: str, int, float, bool, list, dict, set, tuple")

# Operators
a, b = 10, 3
print(f"  Operators: {a} + {b} = {a+b}, {a} / {b} = {a/b:.2f}")

# =============================================================================
# 2. DATA TYPES
# =============================================================================

print("\n📚 MODULE 02: DATA TYPES")
print("-" * 40)

# Lists
fruits = ["apple", "banana", "cherry"]
print(f"  List: {fruits}")

# Dictionaries
person = {"name": "Alice", "age": 25}
print(f"  Dict: {person}")

# Sets
unique = {1, 2, 3, 2, 1}
print(f"  Set: {unique}")

# =============================================================================
# 3. CONTROL FLOW
# =============================================================================

print("\n📚 MODULE 03: CONTROL FLOW")
print("-" * 40)

# Conditionals
score = 85
grade = "A" if score >= 90 else "B" if score >= 80 else "C"
print(f"  Score {score} -> Grade {grade}")

# Loops
print("  For loop:", end=" ")
for i in range(5):
    print(i, end=" ")
print()

# =============================================================================
# 4. FUNCTIONS
# =============================================================================

print("\n📚 MODULE 04: FUNCTIONS")
print("-" * 40)

def greet(name, greeting="Hello"):
    return f"{greeting}, {name}!"

print(f"  {greet('World')}")

# Lambda
square = lambda x: x ** 2
print(f"  Lambda: square(5) = {square(5)}")

# =============================================================================
# 5. MODULES
# =============================================================================

print("\n📚 MODULE 05: MODULES")
print("-" * 40)

import math
import random

print(f"  math.sqrt(16) = {math.sqrt(16)}")
print(f"  random.randint(1, 100) = {random.randint(1, 100)}")

# =============================================================================
# 6. OOP
# =============================================================================

print("\n📚 MODULE 06: OOP")
print("-" * 40)

class Animal:
    def __init__(self, name):
        self.name = name
    
    def speak(self):
        return "..."

class Dog(Animal):
    def speak(self):
        return f"{self.name} says Woof!"

dog = Dog("Buddy")
print(f"  {dog.speak()}")

# =============================================================================
# 7. FILE HANDLING
# =============================================================================

print("\n📚 MODULE 07: FILE HANDLING")
print("-" * 40)

print("  with open('file.txt', 'r') as f:")
print("      content = f.read()")

# =============================================================================
# 8. ERROR HANDLING
# =============================================================================

print("\n📚 MODULE 08: ERROR HANDLING")
print("-" * 40)

try:
    result = 10 / 2
except ZeroDivisionError:
    result = "Error"
else:
    print(f"  Try/Except: 10 / 2 = {result}")

# =============================================================================
# 9. ADVANCED FEATURES
# =============================================================================

print("\n📚 MODULE 09: ADVANCED FEATURES")
print("-" * 40)

# Generator
def countdown(n):
    while n > 0:
        yield n
        n -= 1

print(f"  Generator: {list(countdown(5))}")

# List comprehension
squares = [x**2 for x in range(5)]
print(f"  List comp: {squares}")

# =============================================================================
# 10. CONCURRENCY
# =============================================================================

print("\n📚 MODULE 10: CONCURRENCY")
print("-" * 40)

print("  Threading: for I/O-bound tasks")
print("  Asyncio: for concurrent I/O operations")
print("  Multiprocessing: for CPU-bound tasks")

# =============================================================================
# PROJECTS
# =============================================================================

print("\n🎮 PROJECTS")
print("-" * 40)

projects = [
    "Number Guessing Game",
    "Calculator",
    "Expense Tracker",
    "Task Manager",
    "Web Scraper"
]

for project in projects:
    print(f"  • {project}")

# =============================================================================
# NEXT STEPS
# =============================================================================

print("""
╔══════════════════════════════════════════════════════════════╗
║                       NEXT STEPS                             ║
╠══════════════════════════════════════════════════════════════╣
║  1. Start with 01-basics/hello_world.py                      ║
║  2. Progress through each module in order                    ║
║  3. Complete exercises after each module                     ║
║  4. Build projects to practice what you learn                ║
║  5. Explore the resources directory for more                 ║
╚══════════════════════════════════════════════════════════════╝

Happy Coding! 🐍
""")
