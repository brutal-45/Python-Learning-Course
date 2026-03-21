"""
Project: Task Manager
Level: Intermediate
Description: A task management application with priorities and due dates.

This project demonstrates:
- Class inheritance
- Data persistence
- Sorting and filtering
- Date handling
"""

import json
import os
from datetime import datetime, timedelta
from typing import List, Dict, Optional
from enum import Enum


class Priority(Enum):
    """Task priority levels."""
    LOW = 1
    MEDIUM = 2
    HIGH = 3
    URGENT = 4

    def __str__(self):
        icons = {1: "🟢", 2: "🟡", 3: "🟠", 4: "🔴"}
        return f"{icons[self.value]} {self.name}"


class Status(Enum):
    """Task status."""
    TODO = "todo"
    IN_PROGRESS = "in_progress"
    DONE = "done"

    def __str__(self):
        return self.value.replace('_', ' ').title()


class Task:
    """Represents a task."""

    def __init__(self, title: str, description: str = "", priority: Priority = Priority.MEDIUM,
                 due_date: str = None, status: Status = Status.TODO):
        self.id = None  # Assigned when added to manager
        self.title = title
        self.description = description
        self.priority = priority
        self.due_date = due_date  # YYYY-MM-DD format
        self.status = status
        self.created_at = datetime.now().strftime("%Y-%m-%d %H:%M")
        self.completed_at = None

    def mark_done(self):
        """Mark task as completed."""
        self.status = Status.DONE
        self.completed_at = datetime.now().strftime("%Y-%m-%d %H:%M")

    def is_overdue(self) -> bool:
        """Check if task is overdue."""
        if not self.due_date or self.status == Status.DONE:
            return False
        return datetime.now().date() > datetime.strptime(self.due_date, "%Y-%m-%d").date()

    def days_until_due(self) -> Optional[int]:
        """Get days until due date."""
        if not self.due_date:
            return None
        due = datetime.strptime(self.due_date, "%Y-%m-%d").date()
        return (due - datetime.now().date()).days

    def to_dict(self) -> dict:
        return {
            'id': self.id,
            'title': self.title,
            'description': self.description,
            'priority': self.priority.value,
            'due_date': self.due_date,
            'status': self.status.value,
            'created_at': self.created_at,
            'completed_at': self.completed_at
        }

    @classmethod
    def from_dict(cls, data: dict) -> 'Task':
        task = cls(
            title=data['title'],
            description=data['description'],
            priority=Priority(data['priority']),
            due_date=data['due_date'],
            status=Status(data['status'])
        )
        task.id = data['id']
        task.created_at = data['created_at']
        task.completed_at = data['completed_at']
        return task

    def __str__(self):
        status_icon = "✅" if self.status == Status.DONE else "⬜"
        overdue = " ⚠️ OVERDUE!" if self.is_overdue() else ""

        result = f"{status_icon} [{self.id}] {self.title}"
        if self.due_date:
            result += f" (Due: {self.due_date})"
        result += f" - {self.priority}{overdue}"
        return result


class TaskManager:
    """Manages a collection of tasks."""

    def __init__(self, data_file: str = "tasks.json"):
        self.data_file = data_file
        self.tasks: List[Task] = []
        self.next_id = 1
        self.load_tasks()

    def add_task(self, title: str, description: str = "", priority: Priority = Priority.MEDIUM,
                 due_date: str = None) -> Task:
        """Add a new task."""
        task = Task(title, description, priority, due_date)
        task.id = self.next_id
        self.next_id += 1
        self.tasks.append(task)
        self.save_tasks()
        return task

    def get_task(self, task_id: int) -> Optional[Task]:
        """Get a task by ID."""
        for task in self.tasks:
            if task.id == task_id:
                return task
        return None

    def complete_task(self, task_id: int) -> bool:
        """Mark a task as completed."""
        task = self.get_task(task_id)
        if task:
            task.mark_done()
            self.save_tasks()
            return True
        return False

    def delete_task(self, task_id: int) -> bool:
        """Delete a task."""
        task = self.get_task(task_id)
        if task:
            self.tasks.remove(task)
            self.save_tasks()
            return True
        return False

    def list_tasks(self, status: Status = None, priority: Priority = None,
                   overdue_only: bool = False) -> List[Task]:
        """List tasks with optional filters."""
        result = self.tasks

        if status:
            result = [t for t in result if t.status == status]
        if priority:
            result = [t for t in result if t.priority == priority]
        if overdue_only:
            result = [t for t in result if t.is_overdue()]

        # Sort by priority (descending) then due date
        result.sort(key=lambda t: (-t.priority.value, t.due_date or "9999-99-99"))
        return result

    def get_statistics(self) -> dict:
        """Get task statistics."""
        total = len(self.tasks)
        done = sum(1 for t in self.tasks if t.status == Status.DONE)
        overdue = sum(1 for t in self.tasks if t.is_overdue())

        by_priority = {}
        for priority in Priority:
            by_priority[priority.name] = sum(1 for t in self.tasks if t.priority == priority)

        return {
            'total': total,
            'completed': done,
            'pending': total - done,
            'overdue': overdue,
            'completion_rate': (done / total * 100) if total > 0 else 0,
            'by_priority': by_priority
        }

    def save_tasks(self):
        """Save tasks to file."""
        data = {
            'next_id': self.next_id,
            'tasks': [t.to_dict() for t in self.tasks]
        }
        with open(self.data_file, 'w') as f:
            json.dump(data, f, indent=2)

    def load_tasks(self):
        """Load tasks from file."""
        if os.path.exists(self.data_file):
            try:
                with open(self.data_file, 'r') as f:
                    data = json.load(f)
                self.next_id = data.get('next_id', 1)
                self.tasks = [Task.from_dict(t) for t in data.get('tasks', [])]
            except (json.JSONDecodeError, KeyError):
                self.tasks = []


def display_tasks(tasks: List[Task], title: str = "Tasks"):
    """Display a list of tasks."""
    print(f"\n📋 {title}")
    print("-" * 60)
    if not tasks:
        print("No tasks found.")
        return

    for task in tasks:
        print(f"  {task}")
        if task.description:
            print(f"     📝 {task.description}")

    print("-" * 60)


def demo():
    """Run a demonstration."""
    print("\n" + "=" * 60)
    print("TASK MANAGER DEMONSTRATION")
    print("=" * 60)

    manager = TaskManager("demo_tasks.json")

    # Add tasks
    print("\n➕ Adding tasks...")
    manager.add_task("Learn Python", "Complete the Python course", Priority.HIGH, "2024-03-20")
    manager.add_task("Buy groceries", "Milk, eggs, bread", Priority.MEDIUM, "2024-03-18")
    manager.add_task("Read book", "Finish chapter 5", Priority.LOW)
    manager.add_task("Fix bug", "Critical bug in production", Priority.URGENT, "2024-03-15")

    # List all tasks
    display_tasks(manager.list_tasks(), "All Tasks")

    # Complete a task
    print("\n✅ Completing task 1...")
    manager.complete_task(1)

    # Show pending tasks
    display_tasks(manager.list_tasks(status=Status.TODO), "Pending Tasks")

    # Show statistics
    stats = manager.get_statistics()
    print("\n📊 Statistics:")
    print(f"  Total: {stats['total']}")
    print(f"  Completed: {stats['completed']}")
    print(f"  Pending: {stats['pending']}")
    print(f"  Overdue: {stats['overdue']}")
    print(f"  Completion Rate: {stats['completion_rate']:.1f}%")

    # Cleanup
    if os.path.exists("demo_tasks.json"):
        os.remove("demo_tasks.json")


if __name__ == "__main__":
    demo()
    print("\n✅ Task Manager demonstration complete!")
