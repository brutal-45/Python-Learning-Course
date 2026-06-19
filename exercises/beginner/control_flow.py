"""
Exercises: Control Flow
Level: Beginner
Description: Practice problems for conditionals and loops.
"""

# =============================================================================
# EXERCISE 1: FizzBuzz
# =============================================================================

"""
Exercise 1.1: Classic FizzBuzz problem
Print numbers 1 to 100, but:
- For multiples of 3, print "Fizz"
- For multiples of 5, print "Buzz"
- For multiples of both 3 and 5, print "FizzBuzz"
"""


def fizzbuzz(n):
    """
    Return FizzBuzz result for a number.

    Args:
        n: Number to check

    Returns:
        String result based on FizzBuzz rules
    """
    if n % 15 == 0:  # Divisible by both 3 and 5
        return "FizzBuzz"
    elif n % 3 == 0:
        return "Fizz"
    elif n % 5 == 0:
        return "Buzz"
    else:
        return str(n)


print("\n" + "=" * 50)
print("Exercise 1.1 Solution: FizzBuzz")
print("First 20 FizzBuzz results:")
for i in range(1, 21):
    print(f"  {i}: {fizzbuzz(i)}")


# =============================================================================
# EXERCISE 2: GRADE CALCULATOR
# =============================================================================

"""
Exercise 2.1: Create a grade calculator that:
- Takes a score (0-100)
- Returns the letter grade and whether it's passing
"""


def calculate_grade(score):
    """
    Calculate letter grade from numerical score.

    Args:
        score: Numerical score (0-100)

    Returns:
        Tuple of (letter_grade, is_passing)
    """
    if score < 0 or score > 100:
        return None, False

    if score >= 90:
        grade = 'A'
    elif score >= 80:
        grade = 'B'
    elif score >= 70:
        grade = 'C'
    elif score >= 60:
        grade = 'D'
    else:
        grade = 'F'

    is_passing = grade in ['A', 'B', 'C', 'D']
    return grade, is_passing


print("\n" + "=" * 50)
print("Exercise 2.1 Solution: Grade Calculator")
test_scores = [95, 82, 71, 65, 45, 100]
for score in test_scores:
    grade, passing = calculate_grade(score)
    status = "Passing" if passing else "Failing"
    print(f"  Score {score}: Grade {grade} ({status})")


# =============================================================================
# EXERCISE 3: PATTERN PRINTING
# =============================================================================

"""
Exercise 3.1: Print the following patterns:

Pattern A (Right Triangle):
*
**
***
****
*****

Pattern B (Pyramid):
    *
   ***
  *****
 *******

Pattern C (Number Triangle):
1
22
333
4444
55555
"""


def print_right_triangle(rows):
    """Print right triangle pattern."""
    for i in range(1, rows + 1):
        print("  " + "*" * i)


def print_pyramid(rows):
    """Print pyramid pattern."""
    for i in range(rows):
        spaces = " " * (rows - i - 1)
        stars = "*" * (2 * i + 1)
        print(f"  {spaces}{stars}")


def print_number_triangle(rows):
    """Print number triangle pattern."""
    for i in range(1, rows + 1):
        print("  " + str(i) * i)


print("\n" + "=" * 50)
print("Exercise 3.1 Solution: Pattern Printing")
print("\nRight Triangle (5 rows):")
print_right_triangle(5)

print("\nPyramid (4 rows):")
print_pyramid(4)

print("\nNumber Triangle (5 rows):")
print_number_triangle(5)


# =============================================================================
# EXERCISE 4: PRIME NUMBERS
# =============================================================================

"""
Exercise 4.1: Write functions to:
- Check if a number is prime
- Find all prime numbers up to n
- Find the first n prime numbers
"""


def is_prime(n):
    """Check if a number is prime."""
    if n < 2:
        return False
    if n == 2:
        return True
    if n % 2 == 0:
        return False
    for i in range(3, int(n ** 0.5) + 1, 2):
        if n % i == 0:
            return False
    return True


def primes_up_to(n):
    """Find all prime numbers up to n."""
    return [i for i in range(2, n + 1) if is_prime(i)]


def first_n_primes(n):
    """Find the first n prime numbers."""
    primes = []
    num = 2
    while len(primes) < n:
        if is_prime(num):
            primes.append(num)
        num += 1
    return primes


print("\n" + "=" * 50)
print("Exercise 4.1 Solution: Prime Numbers")
print(f"  is_prime(17): {is_prime(17)}")
print(f"  is_prime(18): {is_prime(18)}")
print(f"  Primes up to 30: {primes_up_to(30)}")
print(f"  First 10 primes: {first_n_primes(10)}")


# =============================================================================
# EXERCISE 5: PALINDROME CHECKER
# =============================================================================

"""
Exercise 5.1: Write a function to check if a string is a palindrome.
A palindrome reads the same forwards and backwards.
Ignore spaces, punctuation, and case.
"""


def is_palindrome(text):
    """
    Check if a string is a palindrome.

    Args:
        text: String to check

    Returns:
        Boolean indicating if palindrome
    """
    # Clean the text
    cleaned = ''.join(c.lower() for c in text if c.isalnum())
    return cleaned == cleaned[::-1]


print("\n" + "=" * 50)
print("Exercise 5.1 Solution: Palindrome Checker")
test_cases = [
    "racecar",
    "A man, a plan, a canal: Panama",
    "hello",
    "Madam, I'm Adam"
]
for text in test_cases:
    result = is_palindrome(text)
    print(f"  '{text}': {result}")


# =============================================================================
# CHALLENGE EXERCISES
# =============================================================================

"""
Challenge 1: Collatz Conjecture
Starting with any positive integer n:
- If n is even, divide by 2
- If n is odd, multiply by 3 and add 1
- Repeat until n equals 1

Write a function that returns the sequence for any starting number.
"""


def collatz_sequence(n):
    """
    Generate Collatz sequence.

    Args:
        n: Starting number

    Returns:
        List of the sequence
    """
    if n < 1:
        return []

    sequence = [n]
    while n != 1:
        if n % 2 == 0:
            n = n // 2
        else:
            n = n * 3 + 1
        sequence.append(n)

    return sequence


print("\n" + "=" * 50)
print("Challenge 1 Solution: Collatz Sequence")
for start in [7, 10, 15]:
    seq = collatz_sequence(start)
    print(f"  Collatz({start}): length={len(seq)}")


# =============================================================================
# MAIN EXECUTION
# =============================================================================

if __name__ == "__main__":
    print("\n" + "=" * 50)
    print("✅ All control flow exercises completed!")
    print("📚 Practice more by modifying the code!")
    print("=" * 50)
