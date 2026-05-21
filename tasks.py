tasks = []

while True:
    print("\n--- TO-DO LIST MENU ---")
    print("1. Add Task\n2. View Tasks\n3. Delete Task\n4. Exit")
    
    choice = input("Choose an option: ")

    if choice == '1':
        task = input("Enter the task: ")
        tasks.append(task)
        print("Task added!")
    elif choice == '2':
        print("\nYour Tasks:")
        for index, task in enumerate(tasks, start=1):
            print(f"{index}. {task}")
    elif choice == '3':
        try:
            task_num = int(input("Enter the task number to delete: "))
            tasks.pop(task_num - 1)
            print("Task deleted!")
        except (ValueError, IndexError):
            print("Invalid task number.")
    elif choice == '4':
        print("Goodbye!")
        break
    else:
        print("Invalid choice, please try again.")