"""
Python Learning Resources
========================

A curated collection of resources to enhance your Python learning journey.
"""

# =============================================================================
# OFFICIAL RESOURCES
# =============================================================================

OFFICIAL_RESOURCES = {
    "Python Documentation": "https://docs.python.org/3/",
    "Python Tutorial": "https://docs.python.org/3/tutorial/",
    "PEP 8 Style Guide": "https://peps.python.org/pep-0008/",
    "Python Package Index (PyPI)": "https://pypi.org/",
    "Python GitHub": "https://github.com/python/cpython"
}

# =============================================================================
# RECOMMENDED BOOKS
# =============================================================================

BOOKS = [
    {
        "title": "Python Crash Course",
        "author": "Eric Matthes",
        "level": "Beginner",
        "description": "Hands-on, project-based introduction to Python"
    },
    {
        "title": "Automate the Boring Stuff with Python",
        "author": "Al Sweigart",
        "level": "Beginner",
        "description": "Practical programming for total beginners"
    },
    {
        "title": "Fluent Python",
        "author": "Luciano Ramalho",
        "level": "Intermediate-Advanced",
        "description": "Clear, concise, and effective programming"
    },
    {
        "title": "Effective Python",
        "author": "Brett Slatkin",
        "level": "Intermediate",
        "description": "90 specific ways to write better Python"
    },
    {
        "title": "Python Cookbook",
        "author": "David Beazley & Brian K. Jones",
        "level": "Intermediate-Advanced",
        "description": "Recipes for mastering Python 3"
    }
]

# =============================================================================
# ONLINE PLATFORMS
# =============================================================================

ONLINE_PLATFORMS = [
    {
        "name": "LeetCode",
        "url": "https://leetcode.com",
        "focus": "Algorithm practice and interview prep"
    },
    {
        "name": "HackerRank",
        "url": "https://hackerrank.com",
        "focus": "Challenges and certifications"
    },
    {
        "name": "Codewars",
        "url": "https://codewars.com",
        "focus": "Gamified coding challenges"
    },
    {
        "name": "Real Python",
        "url": "https://realpython.com",
        "focus": "Tutorials and in-depth articles"
    },
    {
        "name": "PyBites",
        "url": "https://pybites.blogspot.com",
        "focus": "Python tips and challenges"
    }
]

# =============================================================================
# ESSENTIAL LIBRARIES
# =============================================================================

ESSENTIAL_LIBRARIES = {
    "Web Development": {
        "Flask": "Lightweight web framework",
        "Django": "Full-featured web framework",
        "FastAPI": "Modern, fast web API framework",
        "Requests": "HTTP library for humans"
    },
    "Data Science": {
        "NumPy": "Scientific computing",
        "Pandas": "Data manipulation and analysis",
        "Matplotlib": "Data visualization",
        "Seaborn": "Statistical data visualization"
    },
    "Machine Learning": {
        "Scikit-learn": "Machine learning library",
        "TensorFlow": "Deep learning framework",
        "PyTorch": "Deep learning framework",
        "Keras": "High-level neural networks API"
    },
    "Testing": {
        "pytest": "Testing framework",
        "unittest": "Built-in testing framework",
        "coverage": "Code coverage measurement"
    },
    "Utilities": {
        "Click": "Command-line interface creation",
        "Rich": "Rich text and beautiful formatting",
        "Pydantic": "Data validation using Python type hints"
    }
}

# =============================================================================
# CHEAT SHEETS
# =============================================================================

PYTHON_CHEAT_SHEET = """
# =============================================================================
# PYTHON QUICK REFERENCE CHEAT SHEET
# =============================================================================

# --------------------------------------
# DATA TYPES
# --------------------------------------
integer = 42
float_num = 3.14
string = "Hello"
boolean = True
list_data = [1, 2, 3]
tuple_data = (1, 2, 3)
dict_data = {"key": "value"}
set_data = {1, 2, 3}

# --------------------------------------
# STRINGS
# --------------------------------------
s = "Hello World"
s.upper()          # "HELLO WORLD"
s.lower()          # "hello world"
s.split()          # ["Hello", "World"]
"-".join(["a","b"])  # "a-b"
s[0]               # "H"
s[1:5]             # "ello"
f"Value: {42}"     # "Value: 42"

# --------------------------------------
# LISTS
# --------------------------------------
lst = [1, 2, 3]
lst.append(4)      # [1, 2, 3, 4]
lst.extend([5, 6]) # [1, 2, 3, 4, 5, 6]
lst.pop()          # Removes and returns last
lst.sort()         # Sorts in place
lst.reverse()      # Reverses in place
len(lst)           # Length
[x**2 for x in lst]  # List comprehension

# --------------------------------------
# DICTIONARIES
# --------------------------------------
d = {"a": 1, "b": 2}
d["c"] = 3         # Add item
d.get("x", 0)      # Get with default
d.keys()           # All keys
d.values()         # All values
d.items()          # Key-value pairs
{k: v*2 for k, v in d.items()}  # Dict comprehension

# --------------------------------------
# CONTROL FLOW
# --------------------------------------
if condition:
    pass
elif other:
    pass
else:
    pass

for item in iterable:
    pass

while condition:
    pass

# --------------------------------------
# FUNCTIONS
# --------------------------------------
def func(*args, **kwargs):
    pass

lambda x: x**2     # Anonymous function

# --------------------------------------
# CLASSES
# --------------------------------------
class MyClass:
    def __init__(self, value):
        self.value = value

    def method(self):
        return self.value

# --------------------------------------
# FILE I/O
# --------------------------------------
with open("file.txt", "r") as f:
    content = f.read()

with open("file.txt", "w") as f:
    f.write("content")

# --------------------------------------
# EXCEPTIONS
# --------------------------------------
try:
    pass
except Exception as e:
    pass
finally:
    pass

# --------------------------------------
# IMPORTS
# --------------------------------------
import module
from module import function
import module as alias
"""

# =============================================================================
# COMMON PATTERNS
# =============================================================================

COMMON_PATTERNS = """
# =============================================================================
# COMMON PYTHON PATTERNS
# =============================================================================

# 1. Context Manager Pattern
with open('file.txt', 'r') as f:
    data = f.read()

# 2. List Comprehension
squares = [x**2 for x in range(10)]
evens = [x for x in range(10) if x % 2 == 0]

# 3. Dictionary Comprehension
squares_dict = {x: x**2 for x in range(5)}

# 4. Generator Expression
sum_squares = sum(x**2 for x in range(1000000))

# 5. Enumerate Pattern
for index, value in enumerate(items):
    print(f"{index}: {value}")

# 6. Zip Pattern
for a, b in zip(list1, list2):
    print(a, b)

# 7. Unpacking
first, *middle, last = [1, 2, 3, 4, 5]

# 8. Default Dictionary
from collections import defaultdict
word_count = defaultdict(int)

# 9. Counter
from collections import Counter
counts = Counter(['a', 'b', 'a', 'c', 'a'])

# 10. Named Tuple
from collections import namedtuple
Point = namedtuple('Point', ['x', 'y'])

# 11. Data Class (Python 3.7+)
from dataclasses import dataclass

@dataclass
class Person:
    name: str
    age: int

# 12. Context Manager Class
class MyContext:
    def __enter__(self):
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        pass

# 13. Property Pattern
class Temperature:
    @property
    def celsius(self):
        return self._celsius

    @celsius.setter
    def celsius(self, value):
        self._celsius = value

# 14. Singleton Pattern
class Singleton:
    _instance = None

    def __new__(cls):
        if cls._instance is None:
            cls._instance = super().__new__(cls)
        return cls._instance

# 15. Factory Pattern
def create_object(type_):
    types = {'a': ClassA, 'b': ClassB}
    return types[type_]()
"""

# =============================================================================
# MAIN EXECUTION
# =============================================================================

if __name__ == "__main__":
    print("\n" + "=" * 60)
    print("PYTHON LEARNING RESOURCES")
    print("=" * 60)

    print("\n📚 OFFICIAL RESOURCES:")
    for name, url in OFFICIAL_RESOURCES.items():
        print(f"   • {name}: {url}")

    print("\n📖 RECOMMENDED BOOKS:")
    for book in BOOKS:
        print(f"   • {book['title']} by {book['author']} ({book['level']})")

    print("\n🌐 ONLINE PLATFORMS:")
    for platform in ONLINE_PLATFORMS:
        print(f"   • {platform['name']}: {platform['focus']}")

    print("\n📦 ESSENTIAL LIBRARIES:")
    for category, libs in ESSENTIAL_LIBRARIES.items():
        print(f"\n   {category}:")
        for lib, desc in libs.items():
            print(f"      • {lib}: {desc}")

    print("\n" + "=" * 60)
    print("✅ Resources loaded! Check the variables for detailed information.")
    print("=" * 60)
