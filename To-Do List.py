tasks = []

def add_task(title):
    tasks.append({"title": title, "status": "Incomplete"})

def view_tasks():
    for index, task in enumerate(tasks):
        print(f"{index + 1}. {task['title']} - {task['status']}")

def update_task(index, status):
    tasks[index]["status"] = status

def delete_task(index):
    tasks.pop(index)

def main():
    while True:
        print("\n1. Add Task\n2. View Tasks\n3. Update Task\n4. Delete Task\n5. Exit")
        choice = input("Enter your choice: ")
        if choice == "1":
            title = input("Enter task title: ")
            add_task(title)
        elif choice == "2":
            view_tasks()
        elif choice == "3":
            view_tasks()
            task_index = int(input("Enter task number to update: ")) - 1
            status = input("Enter new status (Complete/Incomplete): ")
            update_task(task_index, status)
        elif choice == "4":
            view_tasks()
            task_index = int(input("Enter task number to delete: ")) - 1
            delete_task(task_index)
        elif choice == "5":
            break
        else:
            print("Invalid choice! Try again.")

if __name__ == "__main__":
    main()
