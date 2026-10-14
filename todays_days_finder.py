from datetime import datetime

# 1. Get the current date details
today = datetime.now()

# 2. Extract just the day name using %A
# %A displays the full name of the weekday
day_name = today.strftime("%A")

# 3. Print the result
print(f"Today is: {day_name}")
