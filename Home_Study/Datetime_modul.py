import datetime

# Get the current date and time
now = datetime.datetime.now()
print("Current date and time:", now)

# Get today's date
today = datetime.date.today()
print("Today's date:", today)

# Create a specific date
specific_date = datetime.date(2024, 9, 3)
print("Specific date:", specific_date)

# Create a specific time
specific_time = datetime.time(14, 30, 45)
print("Specific time:", specific_time)

# Combine date and time into a datetime object
combined = datetime.datetime.combine(specific_date, specific_time)
print("Combined datetime:", combined)

# Calculate the difference between two dates
delta = datetime.timedelta(days=10)
new_date = today + delta
print("Date ,10 days from today:", new_date)

# Calculate the difference between two dates
delta = datetime.timedelta(days=10)
new_date = today - delta
print("Date, 10 days before today:", new_date)

# Format a datetime object as a string
formatted_date = now.strftime("%Y-%m-%d %H:%M:%S")
print("Formatted date:", formatted_date)

# Parse a string into a datetime object
date_string = "2024-09-03 14:30:00"
parsed_date = datetime.datetime.strptime(date_string, "%Y-%m-%d %H:%M:%S")
print("Parsed date:", parsed_date)
