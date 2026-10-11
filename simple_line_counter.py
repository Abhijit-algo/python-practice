# 1. First, let's create a quick text file with a few lines
with open("story.txt", "w") as file:
    file.write("Hello World!\n")
    file.write("Python is very fun to learn.\n")
    file.write("This is the third line.\n")

# 2. Main Program: Count the lines inside the file
line_count = 0

with open("story.txt", "r") as file:
    # Loop through each line in the file
    for line in file:
        line_count += 1  # Add 1 to our counter for every line found

# 3. Print the final total
print("Total number of lines in the file:", line_count)
# Output: Total number of lines in the file: 3
