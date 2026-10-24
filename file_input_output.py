def read_file_safely(filename):
    try:
        print(f"Attempting to open '{filename}'...")
        with open(filename, "r") as file:
            content = file.read()
            print("File Content successfully read:")
            print(content)
            
    except FileNotFoundError:
        print(f"Error: The file '{filename}' does not exist.")
        
    except PermissionError:
        print(f"Error: You do not have permission to read '{filename}'.")
        
    finally:
        print("Cleanup operations completed.\n")

read_file_safely("existing_log.txt") 
read_file_safely("missing_file.txt")   