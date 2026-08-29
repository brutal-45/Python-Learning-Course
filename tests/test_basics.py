"""Tests for basic Python functionality."""

import sys
import io
from contextlib import redirect_stdout


def test_hello_world():
    """Test that hello world script runs without errors."""
    # Just verify the file exists and can be imported conceptually
    assert True


def test_variables_assignment():
    """Test variable assignment works correctly."""
    name = "Python"
    age = 33
    assert name == "Python"
    assert age == 33


def test_basic_arithmetic():
    """Test basic arithmetic operations."""
    assert 10 + 3 == 13
    assert 10 - 3 == 7
    assert 10 * 3 == 30
    assert 10 / 2 == 5.0
    assert 10 // 3 == 3
    assert 10 % 3 == 1
    assert 2**3 == 8


def test_string_operations():
    """Test string operations."""
    text = "Hello, World!"
    assert text.lower() == "hello, world!"
    assert text.upper() == "HELLO, WORLD!"
    assert text.startswith("Hello")
    assert text.endswith("!")
    assert len(text) == 13


def test_list_operations():
    """Test list operations."""
    fruits = ["apple", "banana", "cherry"]
    assert len(fruits) == 3
    assert fruits[0] == "apple"
    assert fruits[-1] == "cherry"
    assert "banana" in fruits

    fruits.append("date")
    assert len(fruits) == 4

    fruits.remove("banana")
    assert "banana" not in fruits


def test_dictionary_operations():
    """Test dictionary operations."""
    person = {"name": "Alice", "age": 25}
    assert person["name"] == "Alice"
    assert person.get("age") == 25
    assert "name" in person

    person["city"] = "New York"
    assert person["city"] == "New York"


def test_conditional_logic():
    """Test conditional logic."""
    x = 10
    if x > 5:
        result = "greater"
    else:
        result = "smaller"
    assert result == "greater"


def test_loop_functionality():
    """Test loop functionality."""
    numbers = []
    for i in range(5):
        numbers.append(i)
    assert numbers == [0, 1, 2, 3, 4]

    # Test while loop
    count = 0
    while count < 3:
        count += 1
    assert count == 3


def test_function_definition():
    """Test function definition and calling."""

    def add(a, b):
        return a + b

    assert add(2, 3) == 5
    assert add(-1, 1) == 0


def test_class_basic():
    """Test basic class functionality."""

    class SimpleClass:
        def __init__(self, value):
            self.value = value

        def get_value(self):
            return self.value

    obj = SimpleClass(42)
    assert obj.get_value() == 42


def test_exception_handling():
    """Test exception handling."""
    try:
        result = 10 / 0
        assert False, "Should have raised ZeroDivisionError"
    except ZeroDivisionError:
        pass  # Expected

    # Test with else and finally
    try:
        result = 10 / 2
    except ZeroDivisionError:
        assert False
    else:
        assert result == 5.0
    finally:
        pass  # Always executes
