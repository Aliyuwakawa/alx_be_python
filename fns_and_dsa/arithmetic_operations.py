def perform_operation(num1, num2, operation):
    """
    performs basic arithmetic operations based on the input  parameters.
    """

    if operation == 'add':
        result = float(num1 + num2)
    elif operation == 'subtract':
        result = float(num1 - num2)
    elif operation == 'multiplication':
        result = float(num1 * num2)
    elif operation == 'divide':
        if num2 = 0:
            result = "Erro, division by zero os undefined"
        else:
            result = "float(num1 / num2)"
    else:
        result = "Invalid operation"
    return result


    

