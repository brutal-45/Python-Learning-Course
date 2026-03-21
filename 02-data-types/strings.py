"""
Module: strings.py
Topic: String Type in Python
Level: Beginner

This file teaches you about:
- String creation and basics
- String indexing and slicing
- String methods
- String formatting
- String operations
"""

# =============================================================================
# SECTION 1: STRING CREATION
# =============================================================================

print("=" * 60)
print("STRING CREATION")
print("=" * 60)

# Different ways to create strings
single_quotes = 'Hello, World!'
double_quotes = "Hello, World!"
triple_quotes = '''Hello,
World!'''

print(f"Single quotes: {single_quotes}")
print(f"Double quotes: {double_quotes}")
print(f"Triple quotes: {triple_quotes}")

# Raw strings (ignore escape sequences)
raw_string = r"C:\Users\Documents\file.txt"
print(f"Raw string: {raw_string}")

# Escape sequences
escaped = "Line 1\nLine 2\tTabbed"
print(f"Escaped string:\n{escaped}")

# Converting to string
num = 42
str_num = str(num)
print(f"\nstr(42) = '{str_num}'")

# Empty string
empty = ""
empty_alt = str()
print(f"Empty string: '{empty}' (length: {len(empty)})")

# =============================================================================
# SECTION 2: STRING INDEXING AND SLICING
# =============================================================================

print("\n" + "=" * 60)
print("STRING INDEXING AND SLICING")
print("=" * 60)

text = "Python"

print(f"String: '{text}'")
print(f"\nIndexing (positive and negative):")
for i, char in enumerate(text):
    print(f"  text[{i}] = '{char}' (also text[{i - len(text)}])")

# Slicing syntax: string[start:end:step]
print(f"\nSlicing:")
print(f"  text[0:3]: '{text[0:3]}'")     # 'Pyt'
print(f"  text[:3]: '{text[:3]}'")       # 'Pyt' (start omitted)
print(f"  text[3:]: '{text[3:]}'")       # 'hon' (end omitted)
print(f"  text[::2]: '{text[::2]}'")     # 'Pto' (every 2nd char)
print(f"  text[::-1]: '{text[::-1]}'")   # 'nohtyP' (reversed)

# Slicing with negative indices
print(f"\nNegative slicing:")
print(f"  text[-3:]: '{text[-3:]}'")     # 'hon' (last 3 chars)
print(f"  text[:-2]: '{text[:-2]}'")     # 'Pyth' (all except last 2)

# Strings are immutable
print(f"\nStrings are immutable:")
try:
    text[0] = 'J'  # This raises TypeError
except TypeError as e:
    print(f"  text[0] = 'J' raises TypeError")

# =============================================================================
# SECTION 3: STRING METHODS - CASE MANIPULATION
# =============================================================================

print("\n" + "=" * 60)
print("STRING METHODS - CASE MANIPULATION")
print("=" * 60)

text = "Hello, Python World!"

print(f"Original: '{text}'")
print(f"  upper(): '{text.upper()}'")
print(f"  lower(): '{text.lower()}'")
print(f"  title(): '{text.title()}'")
print(f"  capitalize(): '{text.capitalize()}'")
print(f"  swapcase(): '{text.swapcase()}'")

# Case checking
print(f"\nCase checking:")
print(f"  'hello'.islower(): {'hello'.islower()}")
print(f"  'HELLO'.isupper(): {'HELLO'.isupper()}")
print(f"  'Hello World'.istitle(): {'Hello World'.istitle()}")

# =============================================================================
# SECTION 4: STRING METHODS - SEARCHING
# =============================================================================

print("\n" + "=" * 60)
print("STRING METHODS - SEARCHING")
print("=" * 60)

text = "Hello, Python World! Python is great."

print(f"String: '{text}'")

# Find position
print(f"\nFinding positions:")
print(f"  find('Python'): {text.find('Python')}")       # 7
print(f"  find('Python', 10): {text.find('Python', 10)}")  # 21
print(f"  rfind('Python'): {text.rfind('Python')}")     # 21
print(f"  find('Java'): {text.find('Java')}")           # -1 (not found)

# Index (raises error if not found)
print(f"\nIndex (raises ValueError if not found):")
print(f"  index('Python'): {text.index('Python')}")
try:
    text.index('Java')
except ValueError:
    print(f"  index('Java'): raises ValueError")

# Count occurrences
print(f"\nCounting:")
print(f"  count('Python'): {text.count('Python')}")
print(f"  count('o'): {text.count('o')}")

# Start/End with
print(f"\nStart/End checks:")
print(f"  startswith('Hello'): {text.startswith('Hello')}")
print(f"  endswith('great.'): {text.endswith('great.')}")
print(f"  endswith('!'): {text.endswith('!')}")

# =============================================================================
# SECTION 5: STRING METHODS - MODIFYING
# =============================================================================

print("\n" + "=" * 60)
print("STRING METHODS - MODIFYING")
print("=" * 60)

# Strip whitespace
text = "   Hello, World!   "
print(f"Original: '{text}'")
print(f"  strip(): '{text.strip()}'")
print(f"  lstrip(): '{text.lstrip()}'")
print(f"  rstrip(): '{text.rstrip()}'")

# Strip specific characters
text2 = "xxHello, World!xx"
print(f"\nOriginal: '{text2}'")
print(f"  strip('x'): '{text2.strip('x')}'")

# Replace
text = "Hello, World!"
print(f"\nReplace:")
print(f"  '{text}' -> replace('World', 'Python'): '{text.replace('World', 'Python')}'")
print(f"  'aaa'.replace('a', 'b', 2): '{'aaa'.replace('a', 'b', 2)}'")

# Split and Join
text = "apple,banana,cherry"
print(f"\nSplit and Join:")
print(f"  Split by comma: {text.split(',')}")
print(f"  Split with maxsplit: {text.split(',', maxsplit=1)}")

words = ['Hello', 'Python', 'World']
print(f"  Join with space: '{' '.join(words)}'")
print(f"  Join with comma: '{','.join(words)}'")

# Partition
text = "user@example.com"
print(f"\nPartition:")
print(f"  '{text}'.partition('@'): {text.partition('@')}")

# =============================================================================
# SECTION 6: STRING METHODS - CHECKING
# =============================================================================

print("\n" + "=" * 60)
print("STRING METHODS - CHECKING")
print("=" * 60)

# Character type checks
print("Character type checks:")
print(f"  '123'.isdigit(): {'123'.isdigit()}")
print(f"  'abc'.isalpha(): {'abc'.isalpha()}")
print(f"  'abc123'.isalnum(): {'abc123'.isalnum()}")
print(f"  '   '.isspace(): {'   '.isspace()}")
print(f"  'hello_world'.isidentifier(): {'hello_world'.isidentifier()}")

# Numeric checks
print(f"\nNumeric checks:")
print(f"  '123'.isnumeric(): {'123'.isnumeric()}")
print(f"  '²'.isdigit(): {'²'.isdigit()}")  # Superscript 2
print(f"  '½'.isnumeric(): {'½'.isnumeric()}")

# ASCII checks
print(f"\nASCII checks:")
print(f"  'Hello'.isascii(): {'Hello'.isascii()}")
print(f"  'Héllo'.isascii(): {'Héllo'.isascii()}")

# =============================================================================
# SECTION 7: STRING FORMATTING
# =============================================================================

print("\n" + "=" * 60)
print("STRING FORMATTING")
print("=" * 60)

name = "Alice"
age = 25
score = 95.5678

# F-strings (Python 3.6+) - RECOMMENDED
print("F-strings (recommended):")
print(f"  Hello, {name}!")
print(f"  Age: {age}")
print(f"  Score: {score:.2f}")  # 2 decimal places
print(f"  Expression: {age * 2}")

# Format specifiers
print(f"\nFormat specifiers:")
num = 42
print(f"  Decimal: {num:d}")
print(f"  Binary: {num:b}")
print(f"  Hex: {num:x}")
print(f"  Octal: {num:o}")
print(f"  Percentage: {0.42:.0%}")

# Width and alignment
print(f"\nWidth and alignment:")
print(f"  Left: |{name:<10}|")
print(f"  Center: |{name:^10}|")
print(f"  Right: |{name:>10}|")
print(f"  With fill: |{name:*^10}|")

# .format() method
print(f"\n.format() method:")
print("  Hello, {}!".format(name))
print("  {0} is {1} years old".format(name, age))
print("  {name} is {age}".format(name="Bob", age=30))

# % formatting (legacy)
print(f"\n% formatting (legacy):")
print("  Hello, %s!" % name)
print("  Age: %d" % age)
print("  Score: %.2f" % score)

# =============================================================================
# SECTION 8: STRING OPERATIONS
# =============================================================================

print("\n" + "=" * 60)
print("STRING OPERATIONS")
print("=" * 60)

# Concatenation
str1 = "Hello"
str2 = "World"

print("Concatenation:")
print(f"  str1 + ' ' + str2 = '{str1 + ' ' + str2}'")
print(f"  str1 * 3 = '{str1 * 3}'")

# Membership
print(f"\nMembership:")
text = "Hello, Python!"
print(f"  'Python' in text: {'Python' in text}")
print(f"  'Java' not in text: {'Java' not in text}")

# Comparison
print(f"\nComparison:")
print(f"  'apple' < 'banana': {'apple' < 'banana'}")  # Alphabetical
print(f"  'Apple' < 'apple': {'Apple' < 'apple'}")    # ASCII order

# Length
print(f"\nLength:")
print(f"  len('Hello'): {len('Hello')}")

# Iteration
print(f"\nIteration:")
for char in "ABC":
    print(f"    Character: {char}")

# =============================================================================
# SECTION 9: UNICODE AND ENCODING
# =============================================================================

print("\n" + "=" * 60)
print("UNICODE AND ENCODING")
print("=" * 60)

# Unicode characters
emoji = "😀"
chinese = "你好"
print(f"Unicode characters:")
print(f"  Emoji: {emoji}")
print(f"  Chinese: {chinese}")

# Character codes
print(f"\nCharacter codes:")
print(f"  ord('A'): {ord('A')}")
print(f"  ord('😀'): {ord('😀')}")
print(f"  chr(65): '{chr(65)}'")
print(f"  chr(128512): '{chr(128512)}'")

# Encoding/Decoding
text = "Hello, 世界"
print(f"\nEncoding/Decoding:")
print(f"  Original: {text}")
utf8_bytes = text.encode('utf-8')
print(f"  UTF-8 bytes: {utf8_bytes}")
decoded = utf8_bytes.decode('utf-8')
print(f"  Decoded back: {decoded}")

# =============================================================================
# SECTION 10: PRACTICAL EXAMPLES
# =============================================================================

print("\n" + "=" * 60)
print("PRACTICAL EXAMPLES")
print("=" * 60)


def is_palindrome(text):
    """Check if a string is a palindrome."""
    # Remove spaces and convert to lowercase
    cleaned = ''.join(char.lower() for char in text if char.isalnum())
    return cleaned == cleaned[::-1]


print("\nPalindrome Checker:")
test_cases = ["racecar", "A man, a plan, a canal: Panama", "hello"]
for test in test_cases:
    result = is_palindrome(test)
    print(f"  '{test}': {result}")


def word_count(text):
    """Count words in a text."""
    words = text.lower().split()
    word_freq = {}
    for word in words:
        # Remove punctuation
        word = ''.join(char for char in word if char.isalnum())
        if word:
            word_freq[word] = word_freq.get(word, 0) + 1
    return word_freq


sample_text = "The quick brown fox jumps over the lazy dog. The dog was not impressed."
print(f"\nWord Count:")
print(f"  Text: '{sample_text}'")
counts = word_count(sample_text)
print(f"  Counts: {counts}")


def mask_email(email):
    """Mask an email address for privacy."""
    if '@' not in email:
        return email
    local, domain = email.split('@', 1)
    if len(local) <= 2:
        masked_local = '*' * len(local)
    else:
        masked_local = local[0] + '*' * (len(local) - 2) + local[-1]
    return f"{masked_local}@{domain}"


print(f"\nEmail Masking:")
emails = ["john.doe@example.com", "a@b.com", "alice@company.org"]
for email in emails:
    print(f"  {email} -> {mask_email(email)}")


def format_phone(phone):
    """Format a phone number string."""
    # Remove all non-digit characters
    digits = ''.join(char for char in phone if char.isdigit())
    if len(digits) == 10:
        return f"({digits[:3]}) {digits[3:6]}-{digits[6:]}"
    elif len(digits) == 11 and digits[0] == '1':
        return f"+1 ({digits[1:4]}) {digits[4:7]}-{digits[7:]}"
    return phone


print(f"\nPhone Formatting:")
phones = ["1234567890", "1-800-555-1234", "(555) 123-4567"]
for phone in phones:
    print(f"  {phone} -> {format_phone(phone)}")

# =============================================================================
# MAIN EXECUTION
# =============================================================================

if __name__ == "__main__":
    print("\n" + "=" * 60)
    print("✅ You've learned about Python strings!")
    print("📚 Next: Learn about lists in lists.py")
    print("=" * 60)
