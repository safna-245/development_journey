num1 = int(input("Enter the number 1..."))
num2 = int(input("Enter the number 2..."))

operation = input("Enter operation(+,-,*,/):")


match operation:

    case "+": print("Addition=",num1 + num2)

    case "-": print("Subtraction=",num1 - num2)

    case "*": print("Multiplication=",num1 * num2)

    case "/": print("Division=",num1 / num2)
    
    case _: print("Invalid")