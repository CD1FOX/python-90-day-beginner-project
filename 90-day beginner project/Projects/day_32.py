# Simple Task Manager

tasks = []  # list to store tasks

def show_tasks():
    if not tasks:
        print("\nNo tasks yet.")
    else:
        print("\nYour tasks:")
        for i, task in enumerate(tasks, start=1):
            print(f"{i}. {task}")

def add_task():
    task = input("Enter a new task: ")
    tasks.append(task)
    print(f"Task '{task}' added!")

def remove_task():
    show_tasks()
    if tasks:
        try:
            task_num = int(input("Enter the task number to remove: "))
            removed = tasks.pop(task_num - 1)
            print(f"Task '{removed}' removed!")
        except (ValueError, IndexError):
            print("Invalid task number!")

def main():
    while True:
        print("\nOptions: [1] Show tasks  [2] Add task  [3] Remove task  [4] Quit")
        choice = input("Choose an option: ")

        if choice == "1":
            show_tasks()
        elif choice == "2":
            add_task()
        elif choice == "3":
            remove_task()
        elif choice == "4":
            print("Goodbye!")
            break
        else:
            print("Invalid choice, try again!")

main()
