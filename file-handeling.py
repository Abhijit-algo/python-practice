# 1. Writing to a text file
print("--- Write to Your Diary ---")
diary_entry = input("Type your thoughts for today: ")

# The 'w' mode opens the file to write text (overwrites old content)
with open("diary.txt", "w") as file:
    file.write(diary_entry)

print("Saved successfully to 'diary.txt'!\n")

# 2. Reading from the text file
print("--- Reading Your Diary File ---")

try:
    # The 'r' mode opens the file to read its contents
    with open("diary.txt", "r") as file:
        saved_content = file.read()
        print("Here is what was saved inside the file:")
        print(f"-> {saved_content}")
except FileNotFoundError:
    print("Error: The diary file could not be found.")
