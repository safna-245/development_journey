num1 = int(input("enter num1:"))

num2 = int(input("enter num2:"))

operation = input("select operation + - * /:")

try:

    result = 0

    if operation == "+":

        result = num2 + num1

    elif operation == "-":

        result = num1 -num2

    elif operation == "*":
    
            result = num1 * num2

    elif operation == "/":
    
            result = num1 / num2

    else:

          print("invalid operation")

   
except Exception as e:

      print(e)

else:
      
      print(result)