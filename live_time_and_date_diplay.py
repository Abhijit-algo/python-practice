from datetime import datetime

# 1. Get the current date and time
now = datetime.now()

clean_date_time = now.strftime("%Y-%m-%d %I:%M %p")

print("Current Date and Time is:")
print(clean_date_time)
