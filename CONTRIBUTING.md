# Contributing to Python Learning Repository

Thank you for your interest in contributing! This document provides guidelines for contributing to this repository.

## How to Contribute

### Reporting Issues

If you find a bug or have a suggestion:
1. Check if the issue already exists
2. Create a new issue with a clear description
3. Include code examples if applicable

### Submitting Changes

1. **Fork the Repository**
   ```bash
   git clone https://github.com/yourusername/python-learning-repo.git
   ```

2. **Create a Branch**
   ```bash
   git checkout -b feature/your-feature-name
   ```

3. **Make Your Changes**
   - Follow PEP 8 style guidelines
   - Add docstrings to all functions
   - Include example usage
   - Add comments for complex logic

4. **Test Your Code**
   ```bash
   python -m pytest tests/
   ```

5. **Commit Your Changes**
   ```bash
   git commit -m "Description of your changes"
   ```

6. **Push and Create Pull Request**
   ```bash
   git push origin feature/your-feature-name
   ```

## Code Style Guidelines

### General Rules

- Follow [PEP 8](https://peps.python.org/pep-0008/) style guide
- Use 4 spaces for indentation
- Maximum line length: 88 characters
- Use meaningful variable and function names

### Documentation

- All modules should have docstrings
- All functions should have docstrings with:
  - Brief description
  - Args section
  - Returns section
  - Examples (optional but encouraged)

### Example Function

```python
def calculate_average(numbers: list) -> float:
    """
    Calculate the average of a list of numbers.

    Args:
        numbers: List of numeric values

    Returns:
        The arithmetic mean of the numbers

    Raises:
        ValueError: If the list is empty

    Example:
        >>> calculate_average([1, 2, 3, 4, 5])
        3.0
    """
    if not numbers:
        raise ValueError("Cannot calculate average of empty list")
    return sum(numbers) / len(numbers)
```

## Project Structure

When adding new content, follow this structure:

```
python-learning-repo/
├── 01-basics/           # Beginner basics
├── 02-data-types/       # Data types
├── 03-control-flow/     # Control flow
├── 04-functions/        # Functions
├── 05-modules/          # Modules
├── 06-oop/              # Object-oriented programming
├── 07-file-handling/    # File operations
├── 08-error-handling/   # Error handling
├── 09-advanced-features/# Advanced features
├── 10-concurrency/      # Concurrency
├── projects/            # Practice projects
├── exercises/           # Practice problems
├── solutions/           # Exercise solutions
└── resources/           # Additional resources
```

## Types of Contributions

### Code Examples
- Add new examples to existing modules
- Create new modules for missing topics
- Ensure examples are well-commented

### Documentation
- Fix typos and improve clarity
- Add missing documentation
- Translate documentation

### Exercises
- Create new practice problems
- Provide complete solutions
- Include difficulty levels

### Projects
- Add practical projects
- Include setup instructions
- Provide solution code

## Questions?

Feel free to open an issue for any questions about contributing!

Thank you for helping make this a great learning resource! 🐍
