"""
Exercises: Variables and Data Types
Level: Beginner
Description: Practice problems for variables, data types, and basic operations.
"""

# =============================================================================
# EXERCISE 1: Variable Assignment and Naming
# =============================================================================

"""
Exercise 1.1: Create variables to store the following information:
- Your name (string)
- Your age (integer)
- Your height in meters (float)
- Whether you're a student (boolean)

Then print a formatted message using these variables.
"""


def exercise_1_1():
    """Solution for Exercise 1.1"""
    name = "Alice"
    age = 25
    height = 1.75
    is_student = True

    print(f"Name: {name}")
    print(f"Age: {age} years old")
    print(f"Height: {height} meters")
    print(f"Student: {'Yes' if is_student else 'No'}")


print("\n" + "=" * 50)
print("Exercise 1.1 Solution:")
exercise_1_1()


# =============================================================================
# EXERCISE 2: Type Conversion
# =============================================================================

"""
Exercise 2.1: Write a function that takes a string representing a number
and returns:
- The integer value
- The float value
- The number squared (as float)

Handle the case where the string is not a valid number.
"""


def convert_string_number(num_str):
    """
    Convert a string to various number types.

    Args:
        num_str: String representing a number

    Returns:
        Tuple of (int_value, float_value, squared) or None if invalid
    """
    try:
        int_val = int(float(num_str))
        float_val = float(num_str)
        squared = float_val ** 2
        return int_val, float_val, squared
    except ValueError:
        return None


print("\n" + "=" * 50)
print("Exercise 2.1 Solution:")
print(f"  convert_string_number('42'): {convert_string_number('42')}")
print(f"  convert_string_number('3.14'): {convert_string_number('3.14')}")
print(f"  convert_string_number('invalid'): {convert_string_number('invalid')}")


# =============================================================================
# EXERCISE 3: String Manipulation
# =============================================================================

"""
Exercise 3.1: Write a function that:
1. Takes a full name string (first and last name)
2. Returns a dictionary with:
   - first_name: First name capitalized
   - last_name: Last name capitalized
   - initials: Two-letter initials
   - full_name: Full name in proper case
"""


def process_name(full_name):
    """
    Process a full name string.

    Args:
        full_name: String with first and last name

    Returns:
        Dictionary with processed name information
    """
    parts = full_name.strip().split()

    if len(parts) < 2:
        return None

    first_name = parts[0].capitalize()
    last_name = parts[-1].capitalize()
    initials = f"{first_name[0]}{last_name[0]}"
    full_name_proper = f"{first_name} {last_name}"

    return {
        'first_name': first_name,
        'last_name': last_name,
        'initials': initials,
        'full_name': full_name_proper
    }


print("\n" + "=" * 50)
print("Exercise 3.1 Solution:")
result = process_name("john doe")
for key, value in result.items():
    print(f"  {key}: {value}")


# =============================================================================
# EXERCISE 4: List Operations
# =============================================================================

"""
Exercise 4.1: Write a function that takes a list of numbers and returns:
- The sum of all numbers
- The average
- The minimum and maximum
- A new list with only even numbers
"""


def analyze_numbers(numbers):
    """
    Analyze a list of numbers.

    Args:
        numbers: List of numbers

    Returns:
        Dictionary with analysis results
    """
    if not numbers:
        return None

    total = sum(numbers)
    average = total / len(numbers)
    minimum = min(numbers)
    maximum = max(numbers)
    evens = [n for n in numbers if n % 2 == 0]

    return {
        'sum': total,
        'average': average,
        'min': minimum,
        'max': maximum,
        'evens': evens
    }


print("\n" + "=" * 50)
print("Exercise 4.1 Solution:")
numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
result = analyze_numbers(numbers)
for key, value in result.items():
    print(f"  {key}: {value}")


# =============================================================================
# EXERCISE 5: Dictionary Operations
# =============================================================================

"""
Exercise 5.1: Create a student grade management system:
- Store student names and their grades (list of grades)
- Calculate average grade for each student
- Find the student with the highest average
"""


def manage_grades():
    """Student grade management system."""
    students = {
        'Alice': [85, 90, 78, 92],
        'Bob': [70, 75, 80, 85],
        'Charlie': [90, 88, 92, 95],
        'Diana': [82, 85, 88, 90]
    }

    # Calculate averages
    averages = {}
    for name, grades in students.items():
        avg = sum(grades) / len(grades)
        averages[name] = avg

    # Find top student
    top_student = max(averages, key=averages.get)

    return {
        'averages': averages,
        'top_student': top_student,
        'top_average': averages[top_student]
    }


print("\n" + "=" * 50)
print("Exercise 5.1 Solution:")
result = manage_grades()
print("  Student averages:")
for name, avg in result['averages'].items():
    print(f"    {name}: {avg:.1f}")
print(f"  Top student: {result['top_student']} ({result['top_average']:.1f})")


# =============================================================================
# CHALLENGE EXERCISES
# =============================================================================

"""
Challenge 1: Create a function that validates a password.
A valid password must:
- Be at least 8 characters long
- Contain at least one uppercase letter
- Contain at least one lowercase letter
- Contain at least one digit
- Contain at least one special character
"""


def validate_password(password):
    """
    Validate password strength.

    Args:
        password: Password string

    Returns:
        Tuple of (is_valid, list_of_issues)
    """
    issues = []

    if len(password) < 8:
        issues.append("Password must be at least 8 characters")

    if not any(c.isupper() for c in password):
        issues.append("Password must contain uppercase letter")

    if not any(c.islower() for c in password):
        issues.append("Password must contain lowercase letter")

    if not any(c.isdigit() for c in password):
        issues.append("Password must contain digit")

    special_chars = "!@#$%^&*()_+-=[]{}|;:,.<>?"
    if not any(c in special_chars for c in password):
        issues.append("Password must contain special character")

    return len(issues) == 0, issues


print("\n" + "=" * 50)
print("Challenge 1 Solution:")
test_passwords = ["password", "Password1", "P@ssw0rd!"]
for pwd in test_passwords:
    is_valid, issues = validate_password(pwd)
    print(f"  '{pwd}': {'Valid' if is_valid else 'Invalid'}")
    if issues:
        for issue in issues:
            print(f"    - {issue}")


# =============================================================================
# MAIN EXECUTION
# =============================================================================

if __name__ == "__main__":
    print("\n" + "=" * 50)
    print("✅ All exercises completed!")
    print("📚 Try modifying the code to learn more!")
    print("=" * 50)
