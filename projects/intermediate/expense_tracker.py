"""
Project: Expense Tracker
Level: Intermediate
Description: A command-line expense tracking application.

This project demonstrates:
- Object-oriented programming
- File I/O (JSON)
- User input handling
- Data analysis with collections
"""

import json
import os
from datetime import datetime
from collections import defaultdict
from typing import List, Dict, Optional


class Expense:
    """Represents a single expense."""

    def __init__(self, amount: float, category: str, description: str, date: str = None):
        self.amount = amount
        self.category = category.lower()
        self.description = description
        self.date = date or datetime.now().strftime("%Y-%m-%d")

    def to_dict(self) -> dict:
        return {
            'amount': self.amount,
            'category': self.category,
            'description': self.description,
            'date': self.date
        }

    @classmethod
    def from_dict(cls, data: dict) -> 'Expense':
        return cls(
            amount=data['amount'],
            category=data['category'],
            description=data['description'],
            date=data['date']
        )

    def __str__(self):
        return f"${self.amount:.2f} | {self.category} | {self.description} | {self.date}"


class ExpenseTracker:
    """Main expense tracking application."""

    def __init__(self, data_file: str = "expenses.json"):
        self.data_file = data_file
        self.expenses: List[Expense] = []
        self.load_expenses()

    def add_expense(self, amount: float, category: str, description: str) -> None:
        """Add a new expense."""
        expense = Expense(amount, category, description)
        self.expenses.append(expense)
        self.save_expenses()
        print(f"✅ Added: {expense}")

    def remove_expense(self, index: int) -> bool:
        """Remove an expense by index."""
        if 0 <= index < len(self.expenses):
            removed = self.expenses.pop(index)
            self.save_expenses()
            print(f"✅ Removed: {removed}")
            return True
        print("❌ Invalid index")
        return False

    def list_expenses(self, category: str = None) -> None:
        """List all expenses, optionally filtered by category."""
        filtered = self.expenses
        if category:
            filtered = [e for e in self.expenses if e.category == category.lower()]

        if not filtered:
            print("No expenses found.")
            return

        print(f"\n{'ID':<5} {'Amount':<10} {'Category':<15} {'Description':<25} {'Date'}")
        print("-" * 70)

        for i, expense in enumerate(filtered):
            print(f"{i:<5} ${expense.amount:<9.2f} {expense.category:<15} {expense.description[:24]:<25} {expense.date}")

        total = sum(e.amount for e in filtered)
        print("-" * 70)
        print(f"Total: ${total:.2f}")

    def get_summary(self) -> Dict:
        """Get expense summary by category."""
        summary = defaultdict(float)
        for expense in self.expenses:
            summary[expense.category] += expense.amount

        return dict(sorted(summary.items(), key=lambda x: x[1], reverse=True))

    def get_monthly_summary(self) -> Dict:
        """Get expense summary by month."""
        summary = defaultdict(float)
        for expense in self.expenses:
            month = expense.date[:7]  # YYYY-MM
            summary[month] += expense.amount

        return dict(sorted(summary.items()))

    def get_statistics(self) -> Dict:
        """Calculate expense statistics."""
        if not self.expenses:
            return {}

        amounts = [e.amount for e in self.expenses]
        return {
            'total': sum(amounts),
            'count': len(amounts),
            'average': sum(amounts) / len(amounts),
            'min': min(amounts),
            'max': max(amounts),
            'categories': len(set(e.category for e in self.expenses))
        }

    def save_expenses(self) -> None:
        """Save expenses to JSON file."""
        data = [e.to_dict() for e in self.expenses]
        with open(self.data_file, 'w') as f:
            json.dump(data, f, indent=2)

    def load_expenses(self) -> None:
        """Load expenses from JSON file."""
        if os.path.exists(self.data_file):
            try:
                with open(self.data_file, 'r') as f:
                    data = json.load(f)
                self.expenses = [Expense.from_dict(d) for d in data]
            except (json.JSONDecodeError, KeyError):
                self.expenses = []

    def clear_all(self) -> None:
        """Clear all expenses."""
        self.expenses = []
        self.save_expenses()
        print("✅ All expenses cleared.")


def display_menu():
    """Display the main menu."""
    print("\n" + "=" * 50)
    print("💸 EXPENSE TRACKER")
    print("=" * 50)
    print("1. Add Expense")
    print("2. List Expenses")
    print("3. Remove Expense")
    print("4. Category Summary")
    print("5. Monthly Summary")
    print("6. Statistics")
    print("7. Clear All")
    print("8. Exit")
    print("-" * 50)


def get_float_input(prompt: str) -> float:
    """Get a valid float input from user."""
    while True:
        try:
            return float(input(prompt))
        except ValueError:
            print("Please enter a valid number.")


def demo():
    """Run a demonstration of the expense tracker."""
    print("\n" + "=" * 50)
    print("EXPENSE TRACKER DEMONSTRATION")
    print("=" * 50)

    # Create tracker with demo data
    tracker = ExpenseTracker("demo_expenses.json")

    # Add sample expenses
    tracker.add_expense(45.99, "Food", "Grocery shopping")
    tracker.add_expense(120.00, "Transportation", "Gas")
    tracker.add_expense(35.50, "Entertainment", "Movie tickets")
    tracker.add_expense(89.99, "Utilities", "Electric bill")
    tracker.add_expense(25.00, "Food", "Restaurant dinner")

    # List expenses
    print("\n📋 All Expenses:")
    tracker.list_expenses()

    # Category summary
    print("\n📊 Category Summary:")
    summary = tracker.get_summary()
    for category, total in summary.items():
        print(f"  {category}: ${total:.2f}")

    # Statistics
    print("\n📈 Statistics:")
    stats = tracker.get_statistics()
    for key, value in stats.items():
        if isinstance(value, float):
            print(f"  {key}: ${value:.2f}")
        else:
            print(f"  {key}: {value}")

    # Cleanup
    if os.path.exists("demo_expenses.json"):
        os.remove("demo_expenses.json")


def interactive():
    """Run the interactive expense tracker."""
    tracker = ExpenseTracker()

    while True:
        display_menu()
        choice = input("Enter choice (1-8): ").strip()

        if choice == '1':
            amount = get_float_input("Amount: $")
            category = input("Category: ").strip()
            description = input("Description: ").strip()
            tracker.add_expense(amount, category, description)

        elif choice == '2':
            category = input("Category (leave empty for all): ").strip()
            tracker.list_expenses(category or None)

        elif choice == '3':
            tracker.list_expenses()
            index = int(input("Enter expense ID to remove: "))
            tracker.remove_expense(index)

        elif choice == '4':
            summary = tracker.get_summary()
            print("\n📊 Category Summary:")
            for category, total in summary.items():
                print(f"  {category}: ${total:.2f}")

        elif choice == '5':
            summary = tracker.get_monthly_summary()
            print("\n📅 Monthly Summary:")
            for month, total in summary.items():
                print(f"  {month}: ${total:.2f}")

        elif choice == '6':
            stats = tracker.get_statistics()
            print("\n📈 Statistics:")
            for key, value in stats.items():
                if isinstance(value, float):
                    print(f"  {key}: ${value:.2f}")
                else:
                    print(f"  {key}: {value}")

        elif choice == '7':
            confirm = input("Are you sure? (yes/no): ").lower()
            if confirm == 'yes':
                tracker.clear_all()

        elif choice == '8':
            print("👋 Goodbye!")
            break

        else:
            print("Invalid choice. Try again.")


if __name__ == "__main__":
    # Run demonstration
    demo()

    # Uncomment for interactive mode:
    # interactive()

    print("\n✅ Expense Tracker demonstration complete!")
