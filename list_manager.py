# 1. Create an empty list to store the tasks
todo_list = []

print("--- Mini To-Do List Manager ---")

# 2. Keep running the program until the user chooses to exit
while True:
    print("\n1. View Tasks")
    print("2. Add Task")
    print("3. Exit")
    
    choice = input("Choose an option (1, 2, or 3): ")
    
    if choice == '1':
        # View existing tasks
        if len(todo_list) == 0:
            print("\nYour to-do list is empty!")
        else:
            print("\nYour Current Tasks:")
            for index, task in enumerate(todo_list, start=1):
                print(f"{index}. {task}")
                
    elif choice == '2':
        # Add a new task
        new_task = input("\nEnter the task name: ")
        todo_list.append(new_task)
        print(f"'{new_task}' has been added successfully!")
        
    elif choice == '3':
        # Stop the loop and exit
        print("\nGoodbye! Have a productive day.")
        break
        
    else:
        print("\nInvalid choice! Please select 1, 2, or 3.")
