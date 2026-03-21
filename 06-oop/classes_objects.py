"""
Module: classes_objects.py
Topic: Classes and Objects in Python
Level: Intermediate

This file teaches you about:
- Class definition
- Instance attributes vs class attributes
- Instance methods
- The __init__ method
- Creating and using objects
"""

# =============================================================================
# SECTION 1: BASIC CLASS DEFINITION
# =============================================================================

print("=" * 60)
print("BASIC CLASS DEFINITION")
print("=" * 60)


class Person:
    """A simple class representing a person."""

    def __init__(self, name, age):
        """
        Initialize a new Person.

        Args:
            name: The person's name
            age: The person's age
        """
        self.name = name
        self.age = age

    def greet(self):
        """Return a greeting message."""
        return f"Hello, I'm {self.name} and I'm {self.age} years old."

    def have_birthday(self):
        """Increment age by 1."""
        self.age += 1
        return f"Happy birthday! Now I'm {self.age}."


# Creating objects (instances)
alice = Person("Alice", 25)
bob = Person("Bob", 30)

print("Creating objects:")
print(f"  {alice.greet()}")
print(f"  {bob.greet()}")

print("\nCalling methods:")
print(f"  {alice.have_birthday()}")

# Accessing attributes
print(f"\nAccessing attributes:")
print(f"  alice.name: {alice.name}")
print(f"  alice.age: {alice.age}")

# Modifying attributes
alice.age = 26
print(f"  After modification, alice.age: {alice.age}")

# =============================================================================
# SECTION 2: CLASS ATTRIBUTES VS INSTANCE ATTRIBUTES
# =============================================================================

print("\n" + "=" * 60)
print("CLASS ATTRIBUTES VS INSTANCE ATTRIBUTES")
print("=" * 60)


class Dog:
    """A class representing a dog."""

    # Class attribute - shared by all instances
    species = "Canis familiaris"
    total_dogs = 0

    def __init__(self, name, breed):
        # Instance attributes - unique to each instance
        self.name = name
        self.breed = breed
        Dog.total_dogs += 1

    def bark(self):
        return f"{self.name} says Woof!"

    @classmethod
    def get_total_dogs(cls):
        """Class method to get total dogs created."""
        return cls.total_dogs


# Creating instances
dog1 = Dog("Buddy", "Golden Retriever")
dog2 = Dog("Max", "German Shepherd")

print("Instance attributes:")
print(f"  dog1.name: {dog1.name}")
print(f"  dog2.name: {dog2.name}")

print("\nClass attributes (shared):")
print(f"  dog1.species: {dog1.species}")
print(f"  dog2.species: {dog2.species}")
print(f"  Dog.species: {Dog.species}")

print(f"\nTotal dogs created: {Dog.get_total_dogs()}")

# Modifying class attribute
Dog.species = "Canis lupus familiaris"
print(f"\nAfter modifying Dog.species:")
print(f"  dog1.species: {dog1.species}")
print(f"  dog2.species: {dog2.species}")

# Modifying instance attribute doesn't affect class attribute
dog1.species = "Custom species"
print(f"\nAfter modifying dog1.species:")
print(f"  dog1.species: {dog1.species}")
print(f"  dog2.species: {dog2.species}")
print(f"  Dog.species: {Dog.species}")

# =============================================================================
# SECTION 3: INSTANCE, CLASS, AND STATIC METHODS
# =============================================================================

print("\n" + "=" * 60)
print("INSTANCE, CLASS, AND STATIC METHODS")
print("=" * 60)


class Calculator:
    """A class demonstrating different method types."""

    brand = "PythonCalc"
    calculation_count = 0

    def __init__(self, name):
        self.name = name

    # Instance method - can access instance and class data
    def add(self, a, b):
        """Instance method for addition."""
        Calculator.calculation_count += 1
        return a + b

    # Class method - receives class as first argument
    @classmethod
    def get_brand(cls):
        """Class method to get brand."""
        return cls.brand

    @classmethod
    def create_scientific(cls):
        """Factory method to create scientific calculator."""
        return cls("Scientific Calculator")

    # Static method - doesn't receive instance or class
    @staticmethod
    def multiply(a, b):
        """Static method for multiplication."""
        Calculator.calculation_count += 1
        return a * b

    @staticmethod
    def is_positive(number):
        """Static utility method."""
        return number > 0


calc = Calculator("Basic Calculator")

print("Instance method:")
print(f"  calc.add(5, 3) = {calc.add(5, 3)}")

print("\nClass method:")
print(f"  Calculator.get_brand(): {Calculator.get_brand()}")
print(f"  calc.get_brand(): {calc.get_brand()}")

print("\nStatic method:")
print(f"  Calculator.multiply(4, 5) = {Calculator.multiply(4, 5)}")
print(f"  calc.multiply(4, 5) = {calc.multiply(4, 5)}")
print(f"  Calculator.is_positive(10): {Calculator.is_positive(10)}")

print(f"\nTotal calculations: {Calculator.calculation_count}")

# Factory method
scientific = Calculator.create_scientific()
print(f"\nFactory method created: {scientific.name}")

# =============================================================================
# SECTION 4: THE __init__ METHOD AND OTHER SPECIAL METHODS
# =============================================================================

print("\n" + "=" * 60)
print("THE __init__ METHOD AND OTHER SPECIAL METHODS")
print("=" * 60)


class Book:
    """A class representing a book."""

    def __init__(self, title, author, pages):
        """Initialize a Book."""
        self.title = title
        self.author = author
        self.pages = pages

    def __str__(self):
        """String representation for users."""
        return f"'{self.title}' by {self.author}"

    def __repr__(self):
        """Official representation for developers."""
        return f"Book('{self.title}', '{self.author}', {self.pages})"

    def __len__(self):
        """Return number of pages."""
        return self.pages

    def __eq__(self, other):
        """Check equality based on title and author."""
        if not isinstance(other, Book):
            return False
        return self.title == other.title and self.author == other.author

    def __lt__(self, other):
        """Compare by number of pages."""
        return self.pages < other.pages

    def __contains__(self, keyword):
        """Check if keyword is in title or author."""
        return keyword.lower() in self.title.lower() or keyword.lower() in self.author.lower()


book1 = Book("Python Programming", "John Doe", 350)
book2 = Book("Learn Python", "Jane Smith", 250)
book3 = Book("Python Programming", "John Doe", 400)

print("Special methods:")
print(f"  __str__: {book1}")
print(f"  __repr__: {repr(book1)}")
print(f"  __len__: {len(book1)} pages")
print(f"  __eq__: book1 == book3? {book1 == book3}")
print(f"  __lt__: book1 < book2? {book1 < book2}")
print(f"  __contains__: 'Python' in book1? {'Python' in book1}")

# =============================================================================
# SECTION 5: ENCAPSULATION
# =============================================================================

print("\n" + "=" * 60)
print("ENCAPSULATION")
print("=" * 60)


class BankAccount:
    """A class demonstrating encapsulation."""

    def __init__(self, owner, initial_balance=0):
        self.owner = owner
        self._balance = initial_balance  # Protected attribute
        self.__account_number = self._generate_account_number()  # Private attribute

    def _generate_account_number(self):
        """Protected method to generate account number."""
        import random
        return ''.join(str(random.randint(0, 9)) for _ in range(10))

    def deposit(self, amount):
        """Public method to deposit money."""
        if amount > 0:
            self._balance += amount
            return f"Deposited ${amount}. New balance: ${self._balance}"
        return "Invalid amount"

    def withdraw(self, amount):
        """Public method to withdraw money."""
        if 0 < amount <= self._balance:
            self._balance -= amount
            return f"Withdrew ${amount}. New balance: ${self._balance}"
        return "Invalid amount or insufficient funds"

    def get_balance(self):
        """Public getter for balance."""
        return self._balance

    def get_account_number(self):
        """Public getter for account number."""
        return self.__account_number[:4] + "******"


account = BankAccount("Alice", 1000)

print("Encapsulation:")
print(f"  Owner: {account.owner}")
print(f"  Balance (via getter): ${account.get_balance()}")
print(f"  Account number: {account.get_account_number()}")

print(f"\n  {account.deposit(500)}")
print(f"  {account.withdraw(200)}")

# Accessing protected attribute (not recommended but possible)
print(f"\n  Accessing _balance directly: ${account._balance}")

# Name mangling for private attributes
print(f"  Private attribute name mangled: {account._BankAccount__account_number}")

# =============================================================================
# SECTION 6: PROPERTIES
# =============================================================================

print("\n" + "=" * 60)
print("PROPERTIES")
print("=" * 60)


class Temperature:
    """A class demonstrating properties."""

    def __init__(self, celsius=0):
        self._celsius = celsius

    @property
    def celsius(self):
        """Get temperature in Celsius."""
        return self._celsius

    @celsius.setter
    def celsius(self, value):
        """Set temperature in Celsius."""
        if value < -273.15:
            raise ValueError("Temperature below absolute zero!")
        self._celsius = value

    @property
    def fahrenheit(self):
        """Get temperature in Fahrenheit."""
        return self._celsius * 9 / 5 + 32

    @fahrenheit.setter
    def fahrenheit(self, value):
        """Set temperature in Fahrenheit."""
        celsius = (value - 32) * 5 / 9
        if celsius < -273.15:
            raise ValueError("Temperature below absolute zero!")
        self._celsius = celsius

    @property
    def kelvin(self):
        """Get temperature in Kelvin (read-only)."""
        return self._celsius + 273.15


temp = Temperature(25)

print("Properties:")
print(f"  Celsius: {temp.celsius}°C")
print(f"  Fahrenheit: {temp.fahrenheit}°F")
print(f"  Kelvin: {temp.kelvin}K")

print("\n  Setting Fahrenheit to 100°F")
temp.fahrenheit = 100
print(f"  Celsius is now: {temp.celsius}°C")

# Read-only property
# temp.kelvin = 300  # This would raise AttributeError

# =============================================================================
# SECTION 7: PRACTICAL EXAMPLES
# =============================================================================

print("\n" + "=" * 60)
print("PRACTICAL EXAMPLES")
print("=" * 60)


class Student:
    """A class representing a student."""

    school_name = "Python Academy"
    total_students = 0

    def __init__(self, name, student_id):
        self.name = name
        self.student_id = student_id
        self._grades = []
        Student.total_students += 1

    def add_grade(self, grade):
        """Add a grade."""
        if 0 <= grade <= 100:
            self._grades.append(grade)
        else:
            raise ValueError("Grade must be between 0 and 100")

    @property
    def average(self):
        """Calculate average grade."""
        if not self._grades:
            return 0
        return sum(self._grades) / len(self._grades)

    @property
    def letter_grade(self):
        """Get letter grade."""
        avg = self.average
        if avg >= 90:
            return 'A'
        elif avg >= 80:
            return 'B'
        elif avg >= 70:
            return 'C'
        elif avg >= 60:
            return 'D'
        return 'F'

    def __str__(self):
        return f"Student({self.name}, ID: {self.student_id})"

    def __repr__(self):
        return f"Student('{self.name}', '{self.student_id}')"


print("Student Management:")

students = [
    Student("Alice", "S001"),
    Student("Bob", "S002"),
    Student("Charlie", "S003")
]

for student in students:
    grades = [85, 90, 78, 92]
    for grade in grades:
        student.add_grade(grade)
    print(f"  {student}")
    print(f"    Grades: {student._grades}")
    print(f"    Average: {student.average:.1f}")
    print(f"    Letter Grade: {student.letter_grade}")

print(f"\nTotal students: {Student.total_students}")


class Inventory:
    """A class to manage inventory."""

    def __init__(self):
        self._items = {}

    def add_item(self, name, quantity, price):
        """Add an item to inventory."""
        if name in self._items:
            self._items[name]['quantity'] += quantity
        else:
            self._items[name] = {'quantity': quantity, 'price': price}

    def remove_item(self, name, quantity):
        """Remove items from inventory."""
        if name not in self._items:
            raise KeyError(f"Item '{name}' not found")
        if self._items[name]['quantity'] < quantity:
            raise ValueError("Insufficient quantity")
        self._items[name]['quantity'] -= quantity
        if self._items[name]['quantity'] == 0:
            del self._items[name]

    def get_item(self, name):
        """Get item details."""
        return self._items.get(name)

    @property
    def total_value(self):
        """Calculate total inventory value."""
        return sum(item['quantity'] * item['price'] for item in self._items.values())

    def __len__(self):
        return len(self._items)

    def __contains__(self, name):
        return name in self._items

    def __iter__(self):
        return iter(self._items.items())


print("\nInventory System:")
inventory = Inventory()

inventory.add_item("Laptop", 10, 999.99)
inventory.add_item("Mouse", 50, 29.99)
inventory.add_item("Keyboard", 30, 79.99)

print(f"  Items in inventory: {len(inventory)}")
print(f"  'Mouse' in inventory: {'Mouse' in inventory}")

for name, details in inventory:
    print(f"    {name}: {details['quantity']} @ ${details['price']}")

print(f"  Total value: ${inventory.total_value:,.2f}")

# =============================================================================
# MAIN EXECUTION
# =============================================================================

if __name__ == "__main__":
    print("\n" + "=" * 60)
    print("✅ You've learned about classes and objects!")
    print("📚 Next: Learn about inheritance in inheritance.py")
    print("=" * 60)
