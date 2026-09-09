num1 = int(input("Enter the number 1..."))
num2 = int(input("Enter the number 2..."))

option = (input("Enter the min/max..."))

match option:
    case "min":
        if num1 < num2:
          
          print("Minimum is",num1)

        else:
           
           print("Minimum is",num2)
     

    case "max":
        if num1 > num2:
          
          print("Maximum is",num1)

        else:
           
           print("Maximum is",num2)
     
    case _: print("Invalid")