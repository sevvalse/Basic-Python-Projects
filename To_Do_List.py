import os

# List to store tasks
todo_list = []

# Main menu function
def menu():
    os.system("clear" if os.name == "posix" else "cls")  # Clears the screen
    print("To-Do List Application")
    print("1. List Tasks")
    print("2. Add Task")
    print("3. Delete Task")
    print("4. Mark Task as Completed")
    print("5. Exit")

# Function to add a task
def add_task():
    task = input("Task to add: ")
    todo_list.append({"task": task, "done": False})
    print(f"'{task}' has been added to the list!")

# Function to list tasks
def list_tasks():
    if not todo_list:
        print("No tasks yet!")
    else:
        for i, task in enumerate(todo_list):
            status = "[X]" if task["done"] else "[ ]"
            print(f"{i + 1}. {status} {task['task']}")

# Function to delete a task
def delete_task():
    list_tasks()
    try:
        index = int(input("Enter the number of the task to delete: ")) - 1
        removed = todo_list.pop(index)
        print(f"'{removed['task']}' has been deleted!")
    except (IndexError, ValueError):
        print("Invalid selection.")

# Function to mark a task as completed
def mark_done():
    list_tasks()
    try:
        index = int(input("Enter the number of the task to mark as completed: ")) - 1
        todo_list[index]["done"] = True
        print(f"'{todo_list[index]['task']}' has been marked as completed!")
    except (IndexError, ValueError):
        print("Invalid selection.")

# Main loop
while True:
    menu()
    choice = input("Make your selection: ")
    if choice == "1":
        list_tasks()
    elif choice == "2":
        add_task()
    elif choice == "3":
        delete_task()
    elif choice == "4":
        mark_done()
    elif choice == "5":
        print("Exiting...")
        break
    else:
        print("Invalid selection!")
    input("Press Enter to continue...")  # Waiting message
