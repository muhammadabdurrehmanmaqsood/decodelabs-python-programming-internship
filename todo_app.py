import json
import os
from typing import List, Dict

class TaskModel:
    """Handles data logic and persistence for the To-Do application."""
    
    def __init__(self, filepath: str = 'tasks.json'):
        self.filepath = filepath
        self.tasks: List[Dict[str, any]] = self._load_tasks()

    def _load_tasks(self) -> List[Dict[str, any]]:
        """Loads serialized JSON data from disk."""
        if os.path.exists(self.filepath):
            with open(self.filepath, 'r') as file:
                return json.load(file)
        return []

    def save_tasks(self) -> None:
        """Serializes task data from RAM to Disk."""
        with open(self.filepath, 'w') as file:
            json.dump(self.tasks, file, indent=4)

    def add_task(self, task_name: str) -> None:
        """Appends a new task dictionary to the collection."""
        task_id = len(self.tasks) + 1
        self.tasks.append({"id": task_id, "task": task_name})
        self.save_tasks()

    def get_tasks(self) -> List[Dict[str, any]]:
        return self.tasks

def display_tasks(tasks: List[Dict[str, any]]) -> None:
    """View layer to display tasks using the iterator protocol."""
    print("\n--- Your To-Do List ---")
    if not tasks:
        print("No tasks currently stored.")
        
    for index, task in enumerate(tasks):
        print(f"[{index}] ID: {task['id']} | Task: {task['task']}")
    print("-----------------------\n")

def main() -> None:
    """Main application loop executing the IPO model (Input, Process, Output)."""
    model = TaskModel()
    
    while True:
        print("\n1. Add Task\n2. View Tasks\n3. Exit")
        choice = input("Select an option: ")
        
        if choice == '1':
            task_name = input("Enter task (e.g., 'Finish Python assignment'): ")
            model.add_task(task_name)
            print("Task successfully committed to storage.")
        elif choice == '2':
            display_tasks(model.get_tasks())
        elif choice == '3':
            print("Terminating process...")
            break
        else:
            print("Invalid input. Please try again.")

if __name__ == "__main__":
    main()