"""
Module: parameters.py
Topic: Function Parameters
Level: Intermediate

This file teaches you about:
- Positional arguments
- Keyword arguments
- Default arguments
- *args and **kwargs
- Positional-only and keyword-only arguments
"""

# =============================================================================
# SECTION 1: POSITIONAL ARGUMENTS
# =============================================================================

print("=" * 60)
print("POSITIONAL ARGUMENTS")
print("=" * 60)


def greet(name, message):
    """Greet with a message."""
    print(f"  {name}: {message}")


# Position matters
greet("Alice", "Hello!")
greet("Hello!", "Alice")  # Different result!

# Positional arguments must be provided
# greet("Alice")  # TypeError: missing required argument

# =============================================================================
# SECTION 2: KEYWORD ARGUMENTS
# =============================================================================

print("\n" + "=" * 60)
print("KEYWORD ARGUMENTS")
print("=" * 60)


def describe_person(name, age, city, occupation):
    """Describe a person with keyword arguments."""
    print(f"  {name}, {age}, from {city}, works as {occupation}")


# Order doesn't matter with keyword arguments
describe_person(name="Alice", age=25, city="NYC", occupation="Engineer")
describe_person(age=25, name="Alice", occupation="Engineer", city="NYC")

# Mix positional and keyword (positional must come first)
describe_person("Bob", 30, city="LA", occupation="Designer")

# =============================================================================
# SECTION 3: DEFAULT ARGUMENTS
# =============================================================================

print("\n" + "=" * 60)
print("DEFAULT ARGUMENTS")
print("=" * 60)


def greet_with_default(name, message="Hello"):
    """Greet with a default message."""
    print(f"  {message}, {name}!")


greet_with_default("Alice")  # Uses default message
greet_with_default("Bob", "Hi")  # Overrides default
greet_with_default("Charlie", message="Hey")  # Keyword override


def create_connection(host, port=5432, database="public", timeout=30):
    """Create a database connection with defaults."""
    print(f"  Connecting to {host}:{port}/{database} (timeout: {timeout}s)")


create_connection("localhost")
create_connection("localhost", 3306)
create_connection("localhost", database="mydb")
create_connection("localhost", port=3306, database="mydb", timeout=60)

# DANGER: Mutable default arguments
print("\nMutable default argument trap:")


def add_item_bad(item, items=[]):  # DON'T DO THIS!
    """Add item to list (bad example)."""
    items.append(item)
    return items


print(f"  Call 1: {add_item_bad('a')}")
print(f"  Call 2: {add_item_bad('b')}")  # Gets ['a', 'b']!
print(f"  Call 3: {add_item_bad('c')}")  # Gets ['a', 'b', 'c']!


# Correct way: Use None as default
def add_item_good(item, items=None):
    """Add item to list (correct way)."""
    if items is None:
        items = []
    items.append(item)
    return items


print("\nCorrect implementation:")
print(f"  Call 1: {add_item_good('a')}")
print(f"  Call 2: {add_item_good('b')}")  # Gets ['b'] - correct!
print(f"  Call 3: {add_item_good('c', ['x'])}")  # Can still pass list

# =============================================================================
# SECTION 4: *ARGS - VARIABLE POSITIONAL ARGUMENTS
# =============================================================================

print("\n" + "=" * 60)
print("*ARGS - VARIABLE POSITIONAL ARGUMENTS")
print("=" * 60)


def sum_all(*args):
    """Sum all arguments."""
    print(f"  Arguments: {args}, Type: {type(args)}")
    return sum(args)


print(f"sum_all(1, 2, 3): {sum_all(1, 2, 3)}")
print(f"sum_all(1, 2, 3, 4, 5): {sum_all(1, 2, 3, 4, 5)}")
print(f"sum_all(): {sum_all()}")


def greet_all(greeting, *names):
    """Greet multiple people."""
    for name in names:
        print(f"  {greeting}, {name}!")


greet_all("Hello", "Alice", "Bob", "Charlie")


def combine(separator, *items):
    """Combine items with separator."""
    return separator.join(str(item) for item in items)


print(f"\ncombine('-', 'a', 'b', 'c'): {combine('-', 'a', 'b', 'c')}")
print(f"combine(', ', 1, 2, 3): {combine(', ', 1, 2, 3)}")

# Unpacking with *
numbers = [1, 2, 3, 4, 5]
print(f"\nUnpacking list with *: sum_all(*numbers) = {sum_all(*numbers)}")

# =============================================================================
# SECTION 5: **KWARGS - VARIABLE KEYWORD ARGUMENTS
# =============================================================================

print("\n" + "=" * 60)
print("**KWARGS - VARIABLE KEYWORD ARGUMENTS")
print("=" * 60)


def print_info(**kwargs):
    """Print all keyword arguments."""
    print("  Keyword arguments:")
    for key, value in kwargs.items():
        print(f"    {key}: {value}")


print_info(name="Alice", age=25, city="NYC")


def create_element(tag, **attributes):
    """Create an HTML element with attributes."""
    attrs = " ".join(f'{k}="{v}"' for k, v in attributes.items())
    if attrs:
        return f"<{tag} {attrs}>"
    return f"<{tag}>"


print(f"\n{create_element('div')}")
print(f"{create_element('input', type='text', name='username', required=True)}")
print(f"{create_element('a', href='https://example.com', target='_blank')}")

# Unpacking with **
options = {'host': 'localhost', 'port': 5432, 'database': 'mydb'}
print(f"\nUnpacking dict with **: {create_element('connection', **options)}")

# =============================================================================
# SECTION 6: COMBINING *ARGS AND **KWARGS
# =============================================================================

print("\n" + "=" * 60)
print("COMBINING *ARGS AND **KWARGS")
print("=" * 60)


def flexible_function(*args, **kwargs):
    """Function that accepts any arguments."""
    print(f"  Args: {args}")
    print(f"  Kwargs: {kwargs}")


flexible_function(1, 2, 3, name="Alice", age=25)
flexible_function("hello")
flexible_function(status="active")


def format_message(template, *values, **options):
    """Format a message with values and options."""
    uppercase = options.get('uppercase', False)
    prefix = options.get('prefix', '')

    formatted = template.format(*values)
    if uppercase:
        formatted = formatted.upper()
    if prefix:
        formatted = f"{prefix}{formatted}"

    return formatted


print(f"\n{format_message('Hello, {}!', 'World')}")
print(f"{format_message('{} + {} = {}', 1, 2, 3)}")
print(f"{format_message('Hello, {}!', 'World', uppercase=True)}")
print(f"{format_message('Hello, {}!', 'World', prefix='>>> ')}")

# =============================================================================
# SECTION 7: POSITIONAL-ONLY AND KEYWORD-ONLY ARGUMENTS
# =============================================================================

print("\n" + "=" * 60)
print("POSITIONAL-ONLY AND KEYWORD-ONLY ARGUMENTS")
print("=" * 60)

# Python 3.8+: Positional-only parameters with /


def positional_only(a, b, /, c, d):
    """
    a and b are positional-only (before /)
    c and d can be positional or keyword
    """
    print(f"  a={a}, b={b}, c={c}, d={d}")


positional_only(1, 2, 3, 4)
positional_only(1, 2, c=3, d=4)
# positional_only(a=1, b=2, c=3, d=4)  # Error!

# Keyword-only parameters with *


def keyword_only(a, b, *, c, d):
    """
    a and b can be positional or keyword
    c and d are keyword-only (after *)
    """
    print(f"  a={a}, b={b}, c={c}, d={d}")


keyword_only(1, 2, c=3, d=4)
keyword_only(a=1, b=2, c=3, d=4)
# keyword_only(1, 2, 3, 4)  # Error!

# Combined


def combined(pos_only, /, normal, *, kw_only):
    """
    pos_only: positional-only
    normal: positional or keyword
    kw_only: keyword-only
    """
    print(f"  pos_only={pos_only}, normal={normal}, kw_only={kw_only}")


combined(1, 2, kw_only=3)
combined(1, normal=2, kw_only=3)

# =============================================================================
# SECTION 8: PRACTICAL EXAMPLES
# =============================================================================

print("\n" + "=" * 60)
print("PRACTICAL EXAMPLES")
print("=" * 60)


def build_url(base, *path_parts, **query_params):
    """Build a URL with path and query parameters."""
    from urllib.parse import urlencode

    # Join path parts
    path = "/".join(str(part).strip("/") for part in path_parts)

    # Build query string
    query = ""
    if query_params:
        query = "?" + urlencode(query_params)

    # Combine
    url = f"{base.rstrip('/')}/{path}{query}"
    return url


print("\nURL Builder:")
print(f"  {build_url('https://api.example.com', 'users', '123')}")
print(f"  {build_url('https://api.example.com', 'users', '123', 'posts')}")
print(f"  {build_url('https://api.example.com', 'search', q='python', limit=10)}")


def create_logger(name, *, level="INFO", format=None, output="console"):
    """Create a logger with configuration."""
    print(f"\nLogger '{name}' created:")
    print(f"  Level: {level}")
    print(f"  Format: {format or '[{level}] {message}'}")
    print(f"  Output: {output}")


create_logger("app")
create_logger("app", level="DEBUG", output="file")


def calculate(*numbers, operation="sum", round_result=False, decimals=2):
    """
    Perform calculation on numbers.

    Args:
        *numbers: Numbers to calculate
        operation: 'sum', 'avg', 'min', 'max', 'product'
        round_result: Whether to round the result
        decimals: Number of decimal places if rounding
    """
    if not numbers:
        return None

    operations = {
        'sum': sum,
        'avg': lambda x: sum(x) / len(x),
        'min': min,
        'max': max,
        'product': lambda x: eval('*'.join(map(str, x)))
    }

    if operation not in operations:
        raise ValueError(f"Unknown operation: {operation}")

    result = operations[operation](numbers)

    if round_result and isinstance(result, float):
        result = round(result, decimals)

    return result


print("\nCalculator:")
print(f"  sum(1,2,3,4,5): {calculate(1, 2, 3, 4, 5)}")
print(f"  avg(1,2,3,4,5): {calculate(1, 2, 3, 4, 5, operation='avg')}")
print(f"  avg(1,2,3,4,5) rounded: {calculate(1, 2, 3, 4, 5, operation='avg', round_result=True)}")
print(f"  max(1,2,3,4,5): {calculate(1, 2, 3, 4, 5, operation='max')}")


def configure_widget(name, /, size="medium", color="blue", **styles):
    """
    Configure a widget.

    Args:
        name: Widget name (positional-only)
        size: Widget size
        color: Widget color
        **styles: Additional CSS styles
    """
    config = {
        'name': name,
        'size': size,
        'color': color,
        'styles': styles
    }
    return config


print("\nWidget Configuration:")
widget = configure_widget("header", "large", "red", font_weight="bold", padding="20px")
print(f"  {widget}")

# =============================================================================
# MAIN EXECUTION
# =============================================================================

if __name__ == "__main__":
    print("\n" + "=" * 60)
    print("✅ You've learned about function parameters!")
    print("📚 Next: Learn about lambda functions in lambda_functions.py")
    print("=" * 60)
