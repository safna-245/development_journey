age = int(input("Enter age:"))

if age >= 18:
    
    test = input("Did you pass driving test (yes/no):")

    if test == "yes":

        print("License approved")

    else:

        print("Test not cleared")

else:
    
    print("No eligible due to age")