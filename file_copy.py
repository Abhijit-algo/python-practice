# 1. Create a sample original text file
with open("original.txt", "w") as file:
    file.write("This is highly important data that needs to be copied!")

print("Step 1: 'original.txt' has been created.")

# 2. Open the original file to read and the backup file to write at the same time
with open("original.txt", "r") as source_file:
    with open("backup.txt", "w") as destination_file:
        # Read content from original and write it directly into backup
        content = source_file.read()
        destination_file.write(content)

print("Step 2: Content successfully copied to 'backup.txt'!")

# 3. Read the new backup file to double check the result
with open("backup.txt", "r") as file:
    print("\nContent inside backup.txt:")
    print(file.read())
