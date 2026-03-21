"""
Module: standard_library.py
Topic: Python Standard Library
Level: Intermediate

This file teaches you about essential standard library modules.
"""

# =============================================================================
# SECTION 1: OS MODULE
# =============================================================================

print("=" * 60)
print("OS MODULE - OPERATING SYSTEM INTERFACE")
print("=" * 60)

import os

# Environment variables
print(f"HOME: {os.environ.get('HOME', 'Not set')}")
print(f"USER: {os.environ.get('USER', 'Not set')}")

# Current directory
print(f"Current directory: {os.getcwd()}")

# Path operations
path = "/home/user/documents/file.txt"
print(f"basename: {os.path.basename(path)}")
print(f"dirname: {os.path.dirname(path)}")

# =============================================================================
# SECTION 2: PATHLIB MODULE
# =============================================================================

print("\n" + "=" * 60)
print("PATHLIB MODULE - OBJECT-ORIENTED PATHS")
print("=" * 60)

from pathlib import Path

# Creating paths
p = Path.home() / "documents" / "file.txt"
print(f"Path: {p}")
print(f"name: {p.name}")
print(f"stem: {p.stem}")
print(f"suffix: {p.suffix}")
print(f"parent: {p.parent}")

# =============================================================================
# SECTION 3: COLLECTIONS MODULE
# =============================================================================

print("\n" + "=" * 60)
print("COLLECTIONS MODULE")
print("=" * 60)

from collections import Counter, defaultdict, namedtuple

# Counter - count occurrences
text = "mississippi"
counter = Counter(text)
print(f"Counter('{text}'): {counter}")
print(f"Most common(2): {counter.most_common(2)}")

# defaultdict - dictionary with default values
dd = defaultdict(list)
dd['fruits'].append('apple')
print(f"defaultdict: {dict(dd)}")

# namedtuple - tuple with named fields
Point = namedtuple('Point', ['x', 'y'])
p = Point(10, 20)
print(f"namedtuple: {p}, p.x = {p.x}")

# =============================================================================
# SECTION 4: DATETIME MODULE
# =============================================================================

print("\n" + "=" * 60)
print("DATETIME MODULE")
print("=" * 60)

from datetime import datetime, date, timedelta

now = datetime.now()
today = date.today()
print(f"Current datetime: {now}")
print(f"Today: {today}")
print(f"Formatted: {now.strftime('%Y-%m-%d %H:%M:%S')}")

# Timedelta
week_later = today + timedelta(days=7)
print(f"Week later: {week_later}")

# =============================================================================
# SECTION 5: JSON MODULE
# =============================================================================

print("\n" + "=" * 60)
print("JSON MODULE")
print("=" * 60)

import json

# Python to JSON
data = {"name": "Alice", "age": 25, "skills": ["Python", "JavaScript"]}
json_string = json.dumps(data, indent=2)
print(f"JSON:\n{json_string}")

# JSON to Python
parsed = json.loads(json_string)
print(f"Parsed name: {parsed['name']}")

# =============================================================================
# SECTION 6: RE MODULE - REGULAR EXPRESSIONS
# =============================================================================

print("\n" + "=" * 60)
print("RE MODULE - REGULAR EXPRESSIONS")
print("=" * 60)

import re

text = "Contact: email@example.com or 555-123-4567"

# Search for email
email = re.search(r'\b[\w.-]+@[\w.-]+\.\w+\b', text)
print(f"Email found: {email.group() if email else 'None'}")

# Find all digits
digits = re.findall(r'\d+', text)
print(f"Digits: {digits}")

# Substitution
redacted = re.sub(r'\d', 'X', text)
print(f"Redacted: {redacted}")

# =============================================================================
# SECTION 7: ITERTOOLS MODULE
# =============================================================================

print("\n" + "=" * 60)
print("ITERTOOLS MODULE")
print("=" * 60)

from itertools import count, chain, product, permutations, combinations

# Chain - combine iterables
print(f"chain([1,2], [3,4]): {list(chain([1, 2], [3, 4]))}")

# Combinatorics
print(f"product('AB', '12'): {list(product('AB', '12'))}")
print(f"permutations('ABC', 2): {list(permutations('ABC', 2))}")
print(f"combinations('ABC', 2): {list(combinations('ABC', 2))}")

# =============================================================================
# MAIN EXECUTION
# =============================================================================

if __name__ == "__main__":
    print("\n" + "=" * 60)
    print("✅ You've learned about the Python Standard Library!")
    print("=" * 60)
