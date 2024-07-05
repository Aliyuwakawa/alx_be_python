def display_current_datetime():
    current_date = datetime.now()
    formatted_date = current_date.strftime("YYYY-MM-DD H:M:S")
    print("current date and time:", formatted_date)

def calculate_future_time():
    number_of_days = int(input("Enter the number of days to add to current date: "))
    current_date = datetime.now()
    future_date = current_date + number_of_days
    formatted_future_date = future_date.strftime("YYYY-MM-DD")
    print("future_date:", formatted_future_date)
