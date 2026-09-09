status_code = int(input("Enter status_code(2,3,4,5):"))

match status_code:

    case 2: print("Success")

    case 3: print("redirect")

    case 4: print("Client error")

    case 5: print("Server error")
    
    case _: print("Invalid")