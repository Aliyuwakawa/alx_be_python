
from datetime import datetime, timedelta

def display_current_datetime():
    current_date_time = datetime.now()
    formatted_date_time = current_date_time.strftime("%Y-%m-%d %H:%M:%S")
    print("Current date and time:", formatted_date_time)

def calculate_future_date():
    days_to_add = int(input("Enter the number of days to add to the current date: "))
    future_date = datetime.now() + timedelta(days=days_to_add)
    formatted_future_date = future_date.strftime("%Y-%m-%d")
    print("Future date after adding", days_to_add, "days:", formatted_future_date)

# Function calls
display_current_datetime()
calculate_future_date()

