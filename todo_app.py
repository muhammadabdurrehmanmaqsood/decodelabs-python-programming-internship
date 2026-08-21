"""Command-line to-do list application with JSON-backed persistence.

Demonstrates basic data modeling with lists and dictionaries, and
serialization of application state to disk between sessions.
"""

import json
import os
from typing import Dict, List, Union

Task = Dict[str, Union[int, str]]


class TaskModel:
    """Handles data logic and persistence for the to-do application."""

    def __init__(self, filepath: str = "tasks.json") -> None:
        """Initialize the model and load any existing tasks from disk.

        Args:
            filepath: Path to the JSON file used for persistent storage.
        """
        self.filepath = filepath
        self.tasks: List[Task] = self._load_tasks()

    def _load_tasks(self) -> List[Task]:
        """Load serialized task data from disk, if it exists.

        Returns:
            A list of task dictionaries, or an empty list if no
            storage file is present yet.
        """
        if os.path.exists(self.filepath):
            with open(self.filepath, "r", encoding="utf-8") as file:
                return json.load(file)
        return []

    def save_tasks(self) -> None:
        """Persist the current in-memory task list to disk as JSON."""
        with open(self.filepath, "w", encoding="utf-8") as file:
            json.dump(self.tasks, file, indent=4)

    def add_task(self, task_name: str) -> None:
        """Add a new task and immediately persist the updated list.

        Args:
            task_name: Human-readable description of the task.
        """
        task_id = len(self.tasks) + 1
        self.tasks.append({"id": task_id, "task": task_name})
        self.save_tasks()

    def get_tasks(self) -> List[Task]:
        """Return all currently stored tasks.

        Returns:
            The list of task dictionaries held in memory.
        """
        return self.tasks


def display_tasks(tasks: List[Task]) -> None:
    """Print a formatted view of the given tasks to the terminal.

    Args:
        tasks: The list of task dictionaries to display.
    """
    print("\n--- Your To-Do List ---")
    if not tasks:
        print("No tasks currently stored.")

    for index, task in enumerate(tasks):
        print(f"[{index}] ID: {task['id']} | Task: {task['task']}")
    print("-----------------------\n")


def main() -> None:
    """Run the interactive to-do list menu loop."""
    model = TaskModel()

    while True:
        print("\n1. Add Task\n2. View Tasks\n3. Exit")
        choice = input("Select an option: ")

        if choice == "1":
            task_name = input("Enter task (e.g., 'Finish Python assignment'): ")
            model.add_task(task_name)
            print("Task successfully saved.")
        elif choice == "2":
            display_tasks(model.get_tasks())
        elif choice == "3":
            print("Goodbye!")
            break
        else:
            print("Invalid input. Please try again.")


if __name__ == "__main__":
    main()
