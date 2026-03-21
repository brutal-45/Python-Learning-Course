"""
Module: custom_exceptions.py
Topic: Creating Custom Exceptions
Level: Intermediate

This file teaches you about:
- Creating custom exception classes
- Exception hierarchy
- Adding custom attributes
- Best practices for custom exceptions
"""

# =============================================================================
# SECTION 1: BASIC CUSTOM EXCEPTION
# =============================================================================

print("=" * 60)
print("BASIC CUSTOM EXCEPTION")
print("=" * 60)


class CustomError(Exception):
    """A simple custom exception."""
    pass


try:
    raise CustomError("Something went wrong!")
except CustomError as e:
    print(f"  Caught: {e}")

# =============================================================================
# SECTION 2: EXCEPTION WITH CUSTOM ATTRIBUTES
# =============================================================================

print("\n" + "=" * 60)
print("EXCEPTION WITH CUSTOM ATTRIBUTES")
print("=" * 60)


class ValidationError(Exception):
    """Exception raised for validation errors."""

    def __init__(self, message, field=None, value=None):
        super().__init__(message)
        self.field = field
        self.value = value

    def __str__(self):
        result = super().__str__()
        if self.field:
            result = f"[{self.field}] {result}"
        return result


def validate_user(username, age):
    """Validate user data."""
    if not username or len(username) < 3:
        raise ValidationError("Username too short", field="username", value=username)
    if age < 0 or age > 150:
        raise ValidationError("Invalid age", field="age", value=age)
    return True


try:
    validate_user("ab", 25)
except ValidationError as e:
    print(f"  Error: {e}")
    print(f"  Field: {e.field}")
    print(f"  Value: {e.value}")

# =============================================================================
# SECTION 3: EXCEPTION HIERARCHY
# =============================================================================

print("\n" + "=" * 60)
print("EXCEPTION HIERARCHY")
print("=" * 60)


# Base exception for our application
class AppError(Exception):
    """Base exception for application errors."""
    pass


# Database-related exceptions
class DatabaseError(AppError):
    """Base exception for database errors."""
    pass


class ConnectionError(DatabaseError):
    """Database connection failed."""
    pass


class QueryError(DatabaseError):
    """Database query failed."""
    pass


# API-related exceptions
class APIError(AppError):
    """Base exception for API errors."""
    pass


class AuthenticationError(APIError):
    """Authentication failed."""
    pass


class RateLimitError(APIError):
    """Rate limit exceeded."""
    def __init__(self, message, retry_after=None):
        super().__init__(message)
        self.retry_after = retry_after


# Handle different exception types
def handle_error(error):
    """Handle errors based on their type."""
    if isinstance(error, ConnectionError):
        return "Database connection issue"
    elif isinstance(error, QueryError):
        return "Database query issue"
    elif isinstance(error, AuthenticationError):
        return "Authentication failed"
    elif isinstance(error, RateLimitError):
        return f"Rate limited. Retry after {error.retry_after}s"
    elif isinstance(error, DatabaseError):
        return "Generic database error"
    elif isinstance(error, APIError):
        return "Generic API error"
    elif isinstance(error, AppError):
        return "Generic application error"
    else:
        return "Unknown error"


# Test the hierarchy
errors = [
    ConnectionError("Cannot connect to DB"),
    RateLimitError("Too many requests", retry_after=60),
    AuthenticationError("Invalid token"),
]

print("Error handling:")
for error in errors:
    print(f"  {type(error).__name__}: {handle_error(error)}")

# =============================================================================
# SECTION 4: PRACTICAL EXAMPLE - VALIDATION FRAMEWORK
# =============================================================================

print("\n" + "=" * 60)
print("PRACTICAL EXAMPLE - VALIDATION FRAMEWORK")
print("=" * 60)


class ValidationException(Exception):
    """Base validation exception."""

    def __init__(self, errors):
        """
        Initialize with a list of errors.

        Args:
            errors: List of (field, message) tuples
        """
        self.errors = errors
        super().__init__(self._format_errors())

    def _format_errors(self):
        return "; ".join(f"{field}: {msg}" for field, msg in self.errors)


class Validator:
    """A simple validation framework."""

    def __init__(self):
        self.errors = []

    def required(self, value, field):
        """Check if value is not empty."""
        if value is None or value == "":
            self.errors.append((field, f"{field} is required"))
        return self

    def min_length(self, value, field, min_len):
        """Check minimum length."""
        if value and len(value) < min_len:
            self.errors.append((field, f"{field} must be at least {min_len} characters"))
        return self

    def max_length(self, value, field, max_len):
        """Check maximum length."""
        if value and len(value) > max_len:
            self.errors.append((field, f"{field} must be at most {max_len} characters"))
        return self

    def email(self, value, field):
        """Validate email format."""
        import re
        pattern = r'^[\w.-]+@[\w.-]+\.\w+$'
        if value and not re.match(pattern, value):
            self.errors.append((field, f"{field} must be a valid email"))
        return self

    def range(self, value, field, min_val, max_val):
        """Check if value is within range."""
        if value is not None and (value < min_val or value > max_val):
            self.errors.append((field, f"{field} must be between {min_val} and {max_val}"))
        return self

    def validate(self):
        """Raise exception if there are errors."""
        if self.errors:
            raise ValidationException(self.errors)
        return True


# Using the validation framework
def create_user(username, email, age):
    """Create a user with validation."""
    validator = Validator()
    validator.required(username, "username").min_length(username, "username", 3)
    validator.required(email, "email").email(email, "email")
    validator.range(age, "age", 0, 120)
    validator.validate()

    # If we get here, validation passed
    return {"username": username, "email": email, "age": age}


# Test validation
test_cases = [
    ("ab", "invalid", 200),  # Multiple errors
    ("valid_user", "test@example.com", 25),  # Valid
]

for username, email, age in test_cases:
    try:
        user = create_user(username, email, age)
        print(f"  Created: {user}")
    except ValidationException as e:
        print(f"  Validation failed: {e}")

# =============================================================================
# SECTION 5: CONTEXT MANAGER FOR EXCEPTIONS
# =============================================================================

print("\n" + "=" * 60)
print("CONTEXT MANAGER FOR EXCEPTIONS")
print("=" * 60)


class ErrorCollector:
    """Collect errors without raising exceptions."""

    def __init__(self):
        self.errors = []

    def __enter__(self):
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        if exc_type is not None:
            self.errors.append((exc_type.__name__, str(exc_val)))
            return True  # Suppress the exception
        return False

    def has_errors(self):
        return len(self.errors) > 0


# Using the error collector
print("Error collector:")
with ErrorCollector() as collector:
    result = 10 / 0  # This won't crash

if collector.has_errors():
    print(f"  Errors collected: {collector.errors}")

# =============================================================================
# MAIN EXECUTION
# =============================================================================

if __name__ == "__main__":
    print("\n" + "=" * 60)
    print("✅ You've learned about custom exceptions!")
    print("📚 Next: Move to advanced features module")
    print("=" * 60)
