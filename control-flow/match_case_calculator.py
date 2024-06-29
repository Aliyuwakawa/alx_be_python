#!/usr/bin/env python
# match_case_calculator.py

def main():
    # Prompt the user for two numbers
    try:
        num1 = float(input("Enter the first number: "))
        num2 = float(input("Enter the second number: "))
    except ValueError:
        print("Invalid input. Please enter valid numbers.")
        return

    # Ask for the type of operation
    operation = input("Choose the operation (+, -, *, /): ")

    # Perform the calculation using a match-case statement
    result = None
    try:
        match operation:
            case '+':
                result = num1 + num2
            case '-':
                result = num1 - num2
            case '*':
                result = num1 * num2
            case '/':
                if num2 == 0:
                    print("Division by zero is not allowed.")
                    return
                result = num1 / num2
            case _:
                print("Invalid operation.")
                return
    except Exception as e:
        print(f"An error occurred: {e}")
        return

    # Output the result
    print(f"The result is {result}")

if __name__ == "__main__":
    main()

