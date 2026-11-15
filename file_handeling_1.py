print("--- Write to Your Diary ---")
diary_entry = input("Type your thoughts for today: ")

with open("diary.txt", "w") as file:
    file.write(diary_entry)

print("Saved successfully to 'diary.txt'!\n")

print("--- Reading Your Diary File ---")

try:
    with open("diary.txt", "r") as file:
        saved_content = file.read()
        print("Here is what was saved inside the file:")
        print(f"-> {saved_content}")
except FileNotFoundError:
    print("Error: The diary file could not be found.")