"""
Module: conditionals.py
Topic: Conditional Statements in Python
Level: Beginner

This file teaches you about:
- if statement
- if-else statement
- if-elif-else statement
- Ternary operator
- Nested conditionals
- Logical operators in conditions
"""

# =============================================================================
# SECTION 1: BASIC IF STATEMENT
# =============================================================================

print("=" * 60)
print("BASIC IF STATEMENT")
print("=" * 60)

# Simple if statement
age = 18

if age >= 18:
    print("You are an adult")

# Multiple statements in if block
temperature = 30

if temperature > 25:
    print("It's warm outside")
    print("Remember to stay hydrated")
    print("Wear light clothing")

# Indentation is crucial in Python!
# All statements in the same block must have the same indentation

# =============================================================================
# SECTION 2: IF-ELSE STATEMENT
# =============================================================================

print("\n" + "=" * 60)
print("IF-ELSE STATEMENT")
print("=" * 60)

age = 16

if age >= 18:
    print("You are an adult")
else:
    print("You are a minor")

# Another example
number = 7

if number % 2 == 0:
    print(f"{number} is even")
else:
    print(f"{number} is odd")

# =============================================================================
# SECTION 3: IF-ELIF-ELSE STATEMENT
# =============================================================================

print("\n" + "=" * 60)
print("IF-ELIF-ELSE STATEMENT")
print("=" * 60)

# Multiple conditions with elif
score = 85

if score >= 90:
    grade = "A"
elif score >= 80:
    grade = "B"
elif score >= 70:
    grade = "C"
elif score >= 60:
    grade = "D"
else:
    grade = "F"

print(f"Score {score} gets grade: {grade}")

# Day of week example
day_number = 3

if day_number == 1:
    day_name = "Monday"
elif day_number == 2:
    day_name = "Tuesday"
elif day_number == 3:
    day_name = "Wednesday"
elif day_number == 4:
    day_name = "Thursday"
elif day_number == 5:
    day_name = "Friday"
elif day_number == 6:
    day_name = "Saturday"
elif day_number == 7:
    day_name = "Sunday"
else:
    day_name = "Invalid day"

print(f"Day {day_number} is {day_name}")

# =============================================================================
# SECTION 4: TERNARY OPERATOR (CONDITIONAL EXPRESSION)
# =============================================================================

print("\n" + "=" * 60)
print("TERNARY OPERATOR")
print("=" * 60)

# Syntax: value_if_true if condition else value_if_false
age = 20

# Traditional if-else
if age >= 18:
    status = "adult"
else:
    status = "minor"
print(f"Traditional: {status}")

# Ternary operator (one-liner)
status = "adult" if age >= 18 else "minor"
print(f"Ternary: {status}")

# More examples
number = 5
result = "positive" if number > 0 else "non-positive"
print(f"\n{number} is {result}")

# Nested ternary (not recommended for complex logic)
score = 75
grade = "A" if score >= 90 else "B" if score >= 80 else "C" if score >= 70 else "D"
print(f"Score {score}: {grade}")

# Ternary with function calls
def format_name(name):
    return name.title() if name else "Unknown"


print(f"\nformat_name('alice'): {format_name('alice')}")
print(f"format_name(''): {format_name('')}")

# =============================================================================
# SECTION 5: LOGICAL OPERATORS IN CONDITIONS
# =============================================================================

print("\n" + "=" * 60)
print("LOGICAL OPERATORS IN CONDITIONS")
print("=" * 60)

# AND operator
age = 25
has_license = True

if age >= 18 and has_license:
    print("You can drive")

# OR operator
day = "Saturday"

if day == "Saturday" or day == "Sunday":
    print("It's the weekend!")

# NOT operator
is_raining = False

if not is_raining:
    print("No need for an umbrella")

# Combining operators (use parentheses for clarity)
age = 25
is_student = True
has_id = True

if (age >= 18 or is_student) and has_id:
    print("Entry allowed")

# =============================================================================
# SECTION 6: NESTED CONDITIONALS
# =============================================================================

print("\n" + "=" * 60)
print("NESTED CONDITIONALS")
print("=" * 60)

# Nested if statements
age = 25
has_license = True

if age >= 18:
    if has_license:
        print("You can drive")
    else:
        print("You need a license to drive")
else:
    print("You are too young to drive")

# Alternative: using logical operators (preferred)
if age >= 18 and has_license:
    print("You can drive")
elif age >= 18 and not has_license:
    print("You need a license to drive")
else:
    print("You are too young to drive")

# Nested example with multiple levels
score = 95
attendance = 90

if score >= 90:
    if attendance >= 90:
        grade = "A+"
    elif attendance >= 80:
        grade = "A"
    else:
        grade = "A-"
elif score >= 80:
    if attendance >= 90:
        grade = "B+"
    else:
        grade = "B"
else:
    grade = "C"

print(f"\nScore: {score}, Attendance: {attendance}% -> Grade: {grade}")

# =============================================================================
# SECTION 7: TRUTHY AND FALSY VALUES
# =============================================================================

print("\n" + "=" * 60)
print("TRUTHY AND FALSY VALUES")
print("=" * 60)

# Values that evaluate to False (Falsy)
falsy_values = [False, None, 0, 0.0, "", '', [], {}, (), set()]

print("Falsy values:")
for val in falsy_values:
    if not val:
        print(f"  {repr(val)} is falsy")

# Values that evaluate to True (Truthy)
truthy_examples = [True, 1, -1, "hello", [1], {'a': 1}, (1,)]

print("\nTruthy values:")
for val in truthy_examples:
    if val:
        print(f"  {repr(val)} is truthy")

# Practical usage
name = ""
if name:
    print(f"Hello, {name}")
else:
    print("Name not provided")

items = []
if items:
    print(f"Items: {items}")
else:
    print("No items")

# Default values using truthy/falsy
user_input = ""
value = user_input or "default"
print(f"\nEmpty string or 'default': '{value}'")

user_input = "hello"
value = user_input or "default"
print(f"'hello' or 'default': '{value}'")

# =============================================================================
# SECTION 8: MATCH-CASE (Python 3.10+)
# =============================================================================

print("\n" + "=" * 60)
print("MATCH-CASE (Python 3.10+)")
print("=" * 60)

# Structural pattern matching (Python 3.10+)
# This is similar to switch-case in other languages

status_code = 404

match status_code:
    case 200:
        message = "OK"
    case 201:
        message = "Created"
    case 400:
        message = "Bad Request"
    case 404:
        message = "Not Found"
    case 500:
        message = "Internal Server Error"
    case _:
        message = "Unknown status"

print(f"Status {status_code}: {message}")

# Match with patterns
point = (3, 4)

match point:
    case (0, 0):
        print("Origin")
    case (x, 0):
        print(f"On x-axis at {x}")
    case (0, y):
        print(f"On y-axis at {y}")
    case (x, y):
        print(f"Point at ({x}, {y})")

# Match with guards
number = 15

match number:
    case n if n < 0:
        result = "negative"
    case n if n == 0:
        result = "zero"
    case n if n > 0 and n <= 10:
        result = "small positive"
    case n if n > 10:
        result = "large positive"
    case _:
        result = "unknown"

print(f"\n{number} is {result}")

# =============================================================================
# SECTION 9: COMMON PATTERNS
# =============================================================================

print("\n" + "=" * 60)
print("COMMON PATTERNS")
print("=" * 60)


# Validating input
def validate_age(age):
    """Validate age input."""
    if age is None:
        return False, "Age is required"
    if not isinstance(age, (int, float)):
        return False, "Age must be a number"
    if age < 0:
        return False, "Age cannot be negative"
    if age > 150:
        return False, "Age seems unrealistic"
    return True, "Valid age"


print("Age validation:")
test_ages = [25, -5, 200, "twenty", None]
for test_age in test_ages:
    valid, message = validate_age(test_age)
    print(f"  {test_age}: {message}")


# Multiple conditions
def get_ticket_price(age, is_student, is_member):
    """Calculate ticket price based on conditions."""
    if age < 0 or age > 120:
        return "Invalid age"

    if age < 5:
        return "Free"
    elif age < 18:
        price = 10
    elif age >= 65:
        price = 12
    else:
        price = 15

    # Apply discounts
    if is_student:
        price *= 0.8  # 20% discount
    if is_member:
        price *= 0.9  # Additional 10% discount

    return f"${price:.2f}"


print(f"\nTicket prices:")
print(f"  Child (4): {get_ticket_price(4, False, False)}")
print(f"  Teen (16, student): {get_ticket_price(16, True, False)}")
print(f"  Adult (30): {get_ticket_price(30, False, False)}")
print(f"  Senior (70, member): {get_ticket_price(70, False, True)}")


# Guard clauses (early returns)
def process_user(user):
    """Process user with guard clauses."""
    # Guard clauses check for invalid conditions early
    if user is None:
        return "No user provided"

    if not user.get('name'):
        return "User name is required"

    if not user.get('email'):
        return "User email is required"

    if user.get('age', 0) < 18:
        return "User must be 18 or older"

    # Main logic here
    return f"Processing user: {user['name']}"


print(f"\nGuard clause examples:")
print(f"  None: {process_user(None)}")
print(f"  No name: {process_user({'email': 'test@test.com'})}")
print(f"  Valid: {process_user({'name': 'Alice', 'email': 'alice@test.com', 'age': 25})}")

# =============================================================================
# SECTION 10: PRACTICAL EXAMPLES
# =============================================================================

print("\n" + "=" * 60)
print("PRACTICAL EXAMPLES")
print("=" * 60)


def calculate_tax(income, filing_status="single"):
    """
    Calculate tax based on income and filing status.
    Simplified tax bracket calculation.
    """
    # 2023 US Tax Brackets (simplified)
    brackets = {
        "single": [
            (11000, 0.10),
            (44725, 0.12),
            (95375, 0.22),
            (182050, 0.24),
            (231250, 0.32),
            (578125, 0.35),
            (float('inf'), 0.37)
        ],
        "married": [
            (22000, 0.10),
            (89450, 0.12),
            (190750, 0.22),
            (364200, 0.24),
            (462500, 0.32),
            (693750, 0.35),
            (float('inf'), 0.37)
        ]
    }

    if filing_status not in brackets:
        return "Invalid filing status"

    tax = 0
    prev_limit = 0

    for limit, rate in brackets[filing_status]:
        if income <= prev_limit:
            break
        taxable = min(income, limit) - prev_limit
        tax += taxable * rate
        prev_limit = limit

    return tax


income = 75000
tax = calculate_tax(income, "single")
print(f"\nTax calculation:")
print(f"  Income: ${income:,.2f}")
print(f"  Tax (single): ${tax:,.2f}")
print(f"  Effective rate: {tax/income*100:.1f}%")


def password_strength(password):
    """Check password strength."""
    score = 0
    feedback = []

    if len(password) >= 8:
        score += 1
    else:
        feedback.append("Use at least 8 characters")

    if any(c.isupper() for c in password):
        score += 1
    else:
        feedback.append("Add uppercase letters")

    if any(c.islower() for c in password):
        score += 1
    else:
        feedback.append("Add lowercase letters")

    if any(c.isdigit() for c in password):
        score += 1
    else:
        feedback.append("Add numbers")

    if any(c in "!@#$%^&*()_+-=[]{}|;:,.<>?" for c in password):
        score += 1
    else:
        feedback.append("Add special characters")

    strength = ["Very Weak", "Weak", "Fair", "Good", "Strong", "Very Strong"][score]

    return strength, feedback


print(f"\nPassword Strength:")
passwords = ["abc", "abc123", "Abc123!", "MyP@ssw0rd2024"]
for pwd in passwords:
    strength, feedback = password_strength(pwd)
    print(f"  '{pwd}': {strength}")

# =============================================================================
# MAIN EXECUTION
# =============================================================================

if __name__ == "__main__":
    print("\n" + "=" * 60)
    print("✅ You've learned about conditional statements!")
    print("📚 Next: Learn about loops in loops.py")
    print("=" * 60)
