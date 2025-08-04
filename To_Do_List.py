import os


todo_list = []


def menu():
    os.system("clear" if os.name == "posix" else "cls")
    print("To-Do List Application")
    print("1. List Tasks")
    print("2. Add Task")
    print("3. Delete Task")
    print("4. Mark Task as Completed")
    print("5. Exit")


def add_task():
    task = input("Task to add: ")
    todo_list.append({"task": task, "done": False})
    print(f"'{task}' has been added to the list!")


def list_tasks():
    if not todo_list:
        print("No tasks yet!")
    else:
        for i, task in enumerate(todo_list):
            status = "[X]" if task["done"] else "[ ]"
            print(f"{i + 1}. {status} {task['task']}")


def delete_task():
    list_tasks()
    try:
        index = int(input("Enter the number of the task to delete: ")) - 1
        removed = todo_list.pop(index)
        print(f"'{removed['task']}' has been deleted!")
    except (IndexError, ValueError):
        print("Invalid selection.")


def mark_done():
    list_tasks()
    try:
        index = int(input("Enter the number of the task to mark as completed: ")) - 1
        todo_list[index]["done"] = True
        print(f"'{todo_list[index]['task']}' has been marked as completed!")
    except (IndexError, ValueError):
        print("Invalid selection.")


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
    input("Press Enter to continue...")
