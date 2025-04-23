tasks = []

def add_task(task):
    tasks.append({"task": task, "completed": False})
    print(f'Task "{task}" added!')

def mark_completed(task_index):
    if 0 <= task_index < len(tasks):
        tasks[task_index]["completed"] = True
        print(f'Task "{tasks[task_index]["task"]}" marked as completed!')
    else:
        print("Invalid task number!")

def view_tasks():
    if not tasks:
        print("No tasks available.")
    else:
        print("\nTo-Do List:")
        for i, task in enumerate(tasks):
            status = "[✓]" if task["completed"] else "[ ]"
            print(f'{i + 1}. {status} {task["task"]}')

def todo_list():
    while True:
        print("\nBasic To-Do List")
        print("1. Add Task")
        print("2. Mark Task as Completed")
        print("3. View Tasks")
        print("4. Exit")
        
        choice = input("Enter choice (1/2/3/4): ")
        
        if choice == '1':
            task = input("Enter the task: ")
            add_task(task)
        elif choice == '2':
            view_tasks()
            try:
                task_index = int(input("Enter task number to mark as completed: ")) - 1
                mark_completed(task_index)
            except ValueError:
                print("Invalid input! Please enter a number.")
        elif choice == '3':
            view_tasks()
        elif choice == '4':
            print("Exiting To-Do List. Goodbye!")
            break
        else:
            print("Invalid input! Please select a valid option.")

if __name__ == "__main__":
    todo_list()