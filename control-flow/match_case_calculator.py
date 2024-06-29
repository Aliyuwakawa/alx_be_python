#!/usr/bin/env python3
num1 = float(input("Enter the first number: "))
num2 = float(input("Enter the second number: "))

operation = input("Choose the operation (+, -, *, /): ")

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

print(f"The result is {result}")


