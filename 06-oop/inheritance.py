"""
Module: inheritance.py
Topic: Inheritance in Python
Level: Intermediate

This file teaches you about:
- Single inheritance
- Multiple inheritance
- Method overriding
- super() function
- Method Resolution Order (MRO)
"""

# =============================================================================
# SECTION 1: SINGLE INHERITANCE
# =============================================================================

print("=" * 60)
print("SINGLE INHERITANCE")
print("=" * 60)


class Animal:
    """Base class for animals."""

    def __init__(self, name, age):
        self.name = name
        self.age = age

    def speak(self):
        """Make a sound."""
        return "Some generic sound"

    def info(self):
        """Return animal info."""
        return f"{self.name} is {self.age} years old"


class Dog(Animal):
    """Dog class inheriting from Animal."""

    def __init__(self, name, age, breed):
        # Call parent class constructor
        super().__init__(name, age)
        self.breed = breed

    def speak(self):
        """Override parent's speak method."""
        return f"{self.name} says Woof!"

    def fetch(self):
        """Dog-specific method."""
        return f"{self.name} is fetching the ball!"


class Cat(Animal):
    """Cat class inheriting from Animal."""

    def __init__(self, name, age, color):
        super().__init__(name, age)
        self.color = color

    def speak(self):
        """Override parent's speak method."""
        return f"{self.name} says Meow!"

    def climb(self):
        """Cat-specific method."""
        return f"{self.name} is climbing!"


# Create instances
dog = Dog("Buddy", 3, "Golden Retriever")
cat = Cat("Whiskers", 5, "Orange")

print("Single inheritance:")
print(f"  {dog.info()}")
print(f"  {dog.speak()}")
print(f"  {dog.fetch()}")
print(f"  Breed: {dog.breed}")

print(f"\n  {cat.info()}")
print(f"  {cat.speak()}")
print(f"  {cat.climb()}")
print(f"  Color: {cat.color}")

# isinstance and issubclass
print(f"\ninstanceof checks:")
print(f"  isinstance(dog, Dog): {isinstance(dog, Dog)}")
print(f"  isinstance(dog, Animal): {isinstance(dog, Animal)}")
print(f"  isinstance(dog, Cat): {isinstance(dog, Cat)}")

print(f"\nissubclass checks:")
print(f"  issubclass(Dog, Animal): {issubclass(Dog, Animal)}")
print(f"  issubclass(Cat, Animal): {issubclass(Cat, Animal)}")
print(f"  issubclass(Dog, Cat): {issubclass(Dog, Cat)}")

# =============================================================================
# SECTION 2: THE super() FUNCTION
# =============================================================================

print("\n" + "=" * 60)
print("THE super() FUNCTION")
print("=" * 60)


class Vehicle:
    """Base class for vehicles."""

    def __init__(self, brand, model, year):
        self.brand = brand
        self.model = model
        self.year = year
        print(f"  Vehicle __init__ called: {brand} {model}")

    def start_engine(self):
        return "Engine started"

    def info(self):
        return f"{self.year} {self.brand} {self.model}"


class Car(Vehicle):
    """Car class inheriting from Vehicle."""

    def __init__(self, brand, model, year, doors):
        super().__init__(brand, model, year)
        self.doors = doors
        print(f"  Car __init__ called: {doors} doors")

    def start_engine(self):
        # Call parent method and add to it
        base_message = super().start_engine()
        return f"{base_message} - Vroom Vroom!"

    def info(self):
        base_info = super().info()
        return f"{base_info} ({self.doors} doors)"


class ElectricCar(Car):
    """Electric car inheriting from Car."""

    def __init__(self, brand, model, year, doors, battery_capacity):
        super().__init__(brand, model, year, doors)
        self.battery_capacity = battery_capacity
        print(f"  ElectricCar __init__ called: {battery_capacity}kWh battery")

    def start_engine(self):
        return "Electric motor activated - Silent startup"

    def info(self):
        base_info = super().info()
        return f"{base_info} - Electric ({self.battery_capacity}kWh)"


print("super() function:")
print("\nCreating ElectricCar:")
tesla = ElectricCar("Tesla", "Model 3", 2023, 4, 75)

print(f"\nInfo: {tesla.info()}")
print(f"Start: {tesla.start_engine()}")

# =============================================================================
# SECTION 3: MULTIPLE INHERITANCE
# =============================================================================

print("\n" + "=" * 60)
print("MULTIPLE INHERITANCE")
print("=" * 60)


class Flyable:
    """Mixin class for flying ability."""

    def fly(self):
        return f"{self.name} is flying!"

    def altitude(self):
        return 1000


class Swimmable:
    """Mixin class for swimming ability."""

    def swim(self):
        return f"{self.name} is swimming!"

    def depth(self):
        return 50


class Duck(Animal, Flyable, Swimmable):
    """Duck class with multiple inheritance."""

    def __init__(self, name, age):
        super().__init__(name, age)

    def speak(self):
        return f"{self.name} says Quack!"


duck = Duck("Donald", 5)

print("Multiple inheritance:")
print(f"  {duck.speak()}")
print(f"  {duck.fly()}")
print(f"  {duck.swim()}")


# Diamond problem
class A:
    def method(self):
        return "A.method()"


class B(A):
    def method(self):
        return "B.method() -> " + super().method()


class C(A):
    def method(self):
        return "C.method() -> " + super().method()


class D(B, C):
    def method(self):
        return "D.method() -> " + super().method()


print("\nDiamond problem resolution:")
d = D()
print(f"  {d.method()}")

# Method Resolution Order
print(f"\n  MRO for D: {[cls.__name__ for cls in D.__mro__]}")

# =============================================================================
# SECTION 4: METHOD RESOLUTION ORDER (MRO)
# =============================================================================

print("\n" + "=" * 60)
print("METHOD RESOLUTION ORDER (MRO)")
print("=" * 60)


class First:
    def action(self):
        print("  First.action()")


class Second:
    def action(self):
        print("  Second.action()")


class Third(First, Second):
    pass


class Fourth(Second, First):
    pass


print("MRO Examples:")
print("\nThird(First, Second):")
print(f"  MRO: {[cls.__name__ for cls in Third.__mro__]}")
t = Third()
t.action()

print("\nFourth(Second, First):")
print(f"  MRO: {[cls.__name__ for cls in Fourth.__mro__]}")
f = Fourth()
f.action()

# =============================================================================
# SECTION 5: ABSTRACT BASE CLASSES
# =============================================================================

print("\n" + "=" * 60)
print("ABSTRACT BASE CLASSES")
print("=" * 60)

from abc import ABC, abstractmethod


class Shape(ABC):
    """Abstract base class for shapes."""

    @abstractmethod
    def area(self):
        """Calculate area."""
        pass

    @abstractmethod
    def perimeter(self):
        """Calculate perimeter."""
        pass

    def describe(self):
        """Non-abstract method."""
        return f"This shape has area {self.area()} and perimeter {self.perimeter()}"


class Rectangle(Shape):
    """Rectangle implementation."""

    def __init__(self, width, height):
        self.width = width
        self.height = height

    def area(self):
        return self.width * self.height

    def perimeter(self):
        return 2 * (self.width + self.height)


class Circle(Shape):
    """Circle implementation."""

    def __init__(self, radius):
        self.radius = radius

    def area(self):
        import math
        return math.pi * self.radius ** 2

    def perimeter(self):
        import math
        return 2 * math.pi * self.radius


# Cannot instantiate abstract class
# shape = Shape()  # TypeError

print("Abstract base classes:")
rect = Rectangle(5, 3)
circle = Circle(4)

print(f"  Rectangle: {rect.describe()}")
print(f"  Circle: {circle.describe()}")

# =============================================================================
# SECTION 6: PRACTICAL EXAMPLES
# =============================================================================

print("\n" + "=" * 60)
print("PRACTICAL EXAMPLES")
print("=" * 60)


class Employee:
    """Base class for employees."""

    def __init__(self, name, employee_id, base_salary):
        self.name = name
        self.employee_id = employee_id
        self.base_salary = base_salary

    def calculate_salary(self):
        """Calculate total salary."""
        return self.base_salary

    def __str__(self):
        return f"Employee({self.name}, ID: {self.employee_id})"


class Manager(Employee):
    """Manager class with bonus."""

    def __init__(self, name, employee_id, base_salary, bonus_percentage, team_size):
        super().__init__(name, employee_id, base_salary)
        self.bonus_percentage = bonus_percentage
        self.team_size = team_size

    def calculate_salary(self):
        """Override to include bonus."""
        base = super().calculate_salary()
        bonus = base * (self.bonus_percentage / 100)
        # Additional bonus for team size
        team_bonus = self.team_size * 100
        return base + bonus + team_bonus

    def __str__(self):
        return f"Manager({self.name}, Team: {self.team_size})"


class Developer(Employee):
    """Developer class with overtime pay."""

    def __init__(self, name, employee_id, base_salary, hourly_rate, overtime_hours=0):
        super().__init__(name, employee_id, base_salary)
        self.hourly_rate = hourly_rate
        self.overtime_hours = overtime_hours

    def calculate_salary(self):
        """Override to include overtime."""
        base = super().calculate_salary()
        overtime = self.overtime_hours * self.hourly_rate
        return base + overtime

    def add_overtime(self, hours):
        """Add overtime hours."""
        self.overtime_hours += hours

    def __str__(self):
        return f"Developer({self.name}, Overtime: {self.overtime_hours}h)"


class Contractor(Employee):
    """Contractor with fixed hourly rate."""

    def __init__(self, name, employee_id, hourly_rate, hours_worked):
        # Base salary is calculated
        super().__init__(name, employee_id, 0)
        self.hourly_rate = hourly_rate
        self.hours_worked = hours_worked

    def calculate_salary(self):
        """Contractors are paid hourly."""
        return self.hourly_rate * self.hours_worked

    def __str__(self):
        return f"Contractor({self.name}, Hours: {self.hours_worked})"


print("Employee Management System:")
employees = [
    Manager("Alice", "M001", 80000, 15, 5),
    Developer("Bob", "D001", 70000, 50, 10),
    Developer("Charlie", "D002", 75000, 55),
    Contractor("Dave", "C001", 80, 160)
]

for emp in employees:
    print(f"\n  {emp}")
    print(f"    Salary: ${emp.calculate_salary():,.2f}")

# =============================================================================
# MAIN EXECUTION
# =============================================================================

if __name__ == "__main__":
    print("\n" + "=" * 60)
    print("✅ You've learned about inheritance!")
    print("📚 Next: Learn about special methods in special_methods.py")
    print("=" * 60)
