# daily_reminder.py

def main():
    # Prompt the user for task details
    task = input("Enter your task: ")
    priority = input("Priority (high/medium/low): ")
    time_bound = input("Is it time-bound? (yes/no): ")

    # Initialize the reminder message
    reminder = ""

    # Process the task based on priority using match case
    match priority.lower():
        case "high":
            reminder = f"'{task}' is a high priority task"
        case "medium":
            reminder = f"'{task}' is a medium priority task"
        case "low":
            reminder = f"'{task}' is a low priority task"
        case _:
            reminder = "Unknown priority level"

    # Modify the reminder if the task is time-bound
    if time_bound.lower() == "yes":
        reminder += " that requires immediate attention today!"
    elif time_bound.lower() == "no":
        reminder += ". Consider completing it when you have free time."
    else:
        reminder += ". Time sensitivity unknown."

    # Print the customized reminder
    print("\nReminder:", reminder)

# Run the main function
if __name__ == "__main__":
    main()
