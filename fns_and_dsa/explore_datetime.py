# Import the necessary modules from datetime
from datetime import datetime, timedelta

def display_current_datetime():
    # Obtain the current date and time
    current_date_time = datetime.now()
    # Format the current date and time as a string in the format YYYY-MM-DD HH:MM:SS
    formatted_date_time = current_date_time.strftime("%Y-%m-%d %H:%M:%S")
    # Print the formatted date and time
    print("Current date and time:", formatted_date_time)

def calculate_future_date():
    # Prompt the user to enter the number of days to add to the current date
    days_to_add = int(input("Enter the number of days to add to the current date: "))
    # Calculate the future date by adding the specified number of days to the current date
    future_date = datetime.now() + timedelta(days=days_to_add)
    # Format the future date as a string in the format YYYY-MM-DD
    formatted_future_date = future_date.strftime("%Y-%m-%d")
    # Print the future date
    print("Future date after adding", days_to_add, "days:", formatted_future_date)

# Function calls
display_current_datetime()
calculate_future_date()

