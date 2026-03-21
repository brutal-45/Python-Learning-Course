"""
Solutions: Variables and Data Types
Level: Beginner
Description: Complete solutions for variables exercises.
"""

# =============================================================================
# SOLUTION 1: Variable Assignment
# =============================================================================


def create_profile(name, age, height, is_student):
    """
    Create and display a personal profile.

    Args:
        name: Person's name
        age: Person's age in years
        height: Person's height in meters
        is_student: Whether the person is a student

    Returns:
        Dictionary containing profile information
    """
    profile = {
        'name': name,
        'age': age,
        'height': height,
        'is_student': is_student
    }

    print(f"\n{'='*40}")
    print("PERSONAL PROFILE")
    print(f"{'='*40}")
    print(f"Name: {name}")
    print(f"Age: {age} years old")
    print(f"Height: {height} meters")
    print(f"Student Status: {'Yes' if is_student else 'No'}")
    print(f"{'='*40}")

    return profile


# =============================================================================
# SOLUTION 2: Type Conversion
# =============================================================================


def safe_convert(value, target_type='int'):
    """
    Safely convert a value to a specified type.

    Args:
        value: Value to convert
        target_type: Target type ('int', 'float', 'str', 'bool')

    Returns:
        Tuple of (success, converted_value or error_message)
    """
    converters = {
        'int': int,
        'float': float,
        'str': str,
        'bool': bool
    }

    if target_type not in converters:
        return False, f"Unknown type: {target_type}"

    try:
        result = converters[target_type](value)
        return True, result
    except (ValueError, TypeError) as e:
        return False, str(e)


# =============================================================================
# SOLUTION 3: String Processing
# =============================================================================


def advanced_name_processor(full_name):
    """
    Advanced name processing with multiple outputs.

    Args:
        full_name: Full name string (can have multiple parts)

    Returns:
        Dictionary with various name formats
    """
    # Clean and split the name
    parts = full_name.strip().split()

    if not parts:
        return None

    # Process each part
    capitalized_parts = [p.capitalize() for p in parts]

    result = {
        'original': full_name,
        'first_name': capitalized_parts[0],
        'last_name': capitalized_parts[-1] if len(parts) > 1 else '',
        'middle_names': capitalized_parts[1:-1] if len(parts) > 2 else [],
        'initials': ''.join(p[0].upper() for p in parts),
        'full_name': ' '.join(capitalized_parts),
        'short_form': f"{capitalized_parts[0]} {capitalized_parts[-1][0]}." if len(parts) > 1 else capitalized_parts[0],
        'length': len(full_name.strip())
    }

    return result


# =============================================================================
# SOLUTION 4: List Analysis
# =============================================================================


def comprehensive_list_analysis(numbers):
    """
    Comprehensive analysis of a list of numbers.

    Args:
        numbers: List of numeric values

    Returns:
        Dictionary with complete analysis
    """
    if not numbers:
        return {'error': 'Empty list'}

    sorted_nums = sorted(numbers)

    analysis = {
        'count': len(numbers),
        'sum': sum(numbers),
        'average': sum(numbers) / len(numbers),
        'min': min(numbers),
        'max': max(numbers),
        'range': max(numbers) - min(numbers),
        'sorted': sorted_nums,
        'reversed': list(reversed(sorted_nums)),
        'evens': [n for n in numbers if n % 2 == 0],
        'odds': [n for n in numbers if n % 2 != 0],
        'positives': [n for n in numbers if n > 0],
        'negatives': [n for n in numbers if n < 0],
        'unique': list(set(numbers)),
        'duplicates': [n for n in numbers if numbers.count(n) > 1]
    }

    # Calculate median
    n = len(sorted_nums)
    if n % 2 == 0:
        analysis['median'] = (sorted_nums[n // 2 - 1] + sorted_nums[n // 2]) / 2
    else:
        analysis['median'] = sorted_nums[n // 2]

    return analysis


# =============================================================================
# DEMONSTRATION
# =============================================================================

if __name__ == "__main__":
    print("\n" + "=" * 60)
    print("COMPLETE SOLUTIONS DEMONSTRATION")
    print("=" * 60)

    # Solution 1
    print("\n1. Profile Creation:")
    create_profile("Alice", 25, 1.75, True)

    # Solution 2
    print("\n2. Type Conversion:")
    test_values = ["42", "3.14", "hello", "True"]
    for val in test_values:
        success, result = safe_convert(val, 'int')
        print(f"   '{val}' -> int: {result if success else f'Error: {result}'}")

    # Solution 3
    print("\n3. Name Processing:")
    name_result = advanced_name_processor("john william doe")
    for key, value in name_result.items():
        print(f"   {key}: {value}")

    # Solution 4
    print("\n4. List Analysis:")
    numbers = [3, 1, 4, 1, 5, 9, 2, 6, 5, 3, 5]
    analysis = comprehensive_list_analysis(numbers)
    for key, value in analysis.items():
        print(f"   {key}: {value}")

    print("\n" + "=" * 60)
    print("✅ All solutions demonstrated!")
    print("=" * 60)
