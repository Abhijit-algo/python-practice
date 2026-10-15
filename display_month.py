import calendar

# 1. Set the year and month you want to see
# Let's see the calendar for October 2026
year = 2026
month = 10

# 2. Generate and print the calendar text sheet
month_calendar = calendar.month(year, month)

print("--- Calendar Display ---")
print(month_calendar)
