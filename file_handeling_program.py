def manage_file():
    print("--- Python File Handling with Exception Demo ---")
    filename = "example_log.txt"
    
    # 1. Writing to a file safely
    try:
        with open(filename, "w", encoding="utf-8") as file:
            file.write("Line 1: Initialize system log.\n")
            file.write("Line 2: System running smoothly.\n")
        print(f"Success: Data written to '{filename}'.")
    except IOError as e:
        print(f" Write Error: Could not write to the file. Details: {e}")

    try:
        with open(filename, "a", encoding="utf-8") as file:
            file.write("Line 3: New event appended automatically.\n")
        print(f" Success: Data appended to '{filename}'.")
    except IOError as e:
        print(f" Append Error: Could not append data. Details: {e}")

    try:
        with open(filename, "r", encoding="utf-8") as file:
            content = file.read()
            print("\nReading File Content:")
            print("-" * 30)
            print(content.strip())
            print("-" * 30)
            
    except FileNotFoundError:
        print(f"Read Error: The file '{filename}' does not exist.")
    except PermissionError:
        print(f"Read Error: You do not have permission to access '{filename}'.")
    except Exception as e:
        print(f"Unexpected Error: {e}")


manage_file()
