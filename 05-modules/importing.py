"""
Module: importing.py
Topic: Python Import System
Level: Intermediate

This file teaches you about:
- Different import styles
- How Python finds modules
- The import system
- Module caching
"""

# =============================================================================
# SECTION 1: BASIC IMPORTS
# =============================================================================

print("=" * 60)
print("BASIC IMPORTS")
print("=" * 60)

# Import entire module
import math
print(f"math.sqrt(16) = {math.sqrt(16)}")

# Import with alias
import datetime as dt
print(f"Current date: {dt.date.today()}")

# Import specific items
from math import sqrt, pi, e
print(f"sqrt(25) = {sqrt(25)}")
print(f"π = {pi}")

# Import with alias (specific items)
from math import factorial as fact
print(f"5! = {fact(5)}")

# Import all (not recommended - pollutes namespace)
from math import ceil
print(f"ceil(3.2) = {ceil(3.2)}")

# =============================================================================
# SECTION 2: HOW PYTHON FINDS MODULES
# =============================================================================

print("\n" + "=" * 60)
print("HOW PYTHON FINDS MODULES")
print("=" * 60)

import sys

print("Python's module search path (sys.path):")
for i, path in enumerate(sys.path[:5]):
    print(f"  {i}: {path}")

# Viewing module information
print(f"\nModule location:")
print(f"  math module: {math.__file__}")

# =============================================================================
# SECTION 3: MODULE CACHING
# =============================================================================

print("\n" + "=" * 60)
print("MODULE CACHING")
print("=" * 60)

# Module caching
print(f"'math' in sys.modules: {'math' in sys.modules}")

# Force reimport (rarely needed)
import importlib
importlib.reload(math)

# =============================================================================
# SECTION 4: CONDITIONAL IMPORTS
# =============================================================================

print("\n" + "=" * 60)
print("CONDITIONAL IMPORTS")
print("=" * 60)

# Try/except for optional imports
try:
    import numpy as np
    HAS_NUMPY = True
    print("NumPy is available")
except ImportError:
    HAS_NUMPY = False
    print("NumPy is not available - some features disabled")

# =============================================================================
# MAIN EXECUTION
# =============================================================================

if __name__ == "__main__":
    print("\n" + "=" * 60)
    print("✅ You've learned about Python imports!")
    print("=" * 60)
