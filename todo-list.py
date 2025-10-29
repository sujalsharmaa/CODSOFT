# A list to store tasks. Each task will be a dictionary.
tasks = []

def add_task():
    """Adds a new task to the list."""
    task_description = input("Enter the task description: ")
    task = {
        "description": task_description,
        "completed": False
    }
    tasks.append(task)
    print(f"\n✅ Task added: '{task_description}'")

def view_tasks():
    """Displays all current tasks with their status."""
    if not tasks:
        print("\nYour to-do list is empty.")
        return

    print("\n--- Your To-Do List ---")
    # enumerate adds a counter (i) to the list
    for i, task in enumerate(tasks):
        # Show [X] for completed, [ ] for pending
        status = "X" if task["completed"] else " "
        print(f"{i + 1}. [{status}] {task['description']}")
    print("-------------------------")

def mark_task_complete():
    """Marks a specific task as completed."""
    view_tasks()
    if not tasks:
        return
    
    try:
        task_num = int(input("Enter the task number to mark as complete: "))
        if 0 < task_num <= len(tasks):
            # Adjust for 0-based index
            tasks[task_num - 1]["completed"] = True
            print(f"\n✅ Task {task_num} marked as complete.")
        else:
            print("\nInvalid task number.")
    except ValueError:
        print("\nInvalid input. Please enter a number.")

def delete_task():
    """Removes a task from the list."""
    view_tasks()
    if not tasks:
        return

    try:
        task_num = int(input("Enter the task number to delete: "))
        if 0 < task_num <= len(tasks):
            # Adjust for 0-based index and use pop() to remove
            removed_task = tasks.pop(task_num - 1)
            print(f"\n🗑️ Task deleted: '{removed_task['description']}'")
        else:
            print("\nInvalid task number.")
    except ValueError:
        print("\nInvalid input. Please enter a number.")

def show_menu():
    """Displays the main menu and handles user input."""
    print("\n--- To-Do List Menu ---")
    print("1. Add a new task")
    print("2. View all tasks")
    print("3. Mark a task as complete")
    print("4. Delete a task")
    print("5. Exit")
    print("-------------------------")

def main():
    """Main loop for the application."""
    while True:
        show_menu()
        choice = input("Enter your choice (1-5): ")

        if choice == '1':
            add_task()
        elif choice == '2':
            view_tasks()
        elif choice == '3':
            mark_task_complete()
        elif choice == '4':
            delete_task()
        elif choice == '5':
            print("\nGoodbye! 👋")
            break
        else:
            print("\nInvalid choice. Please select from 1-5.")

# Run the main function when the script is executed
if __name__ == "__main__":
    main()