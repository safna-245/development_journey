user_name = "safna"

db_password = 1234

db_otp = 3456

password = int(input("Enter password:"))

if password == db_password:

    otp = int(input("Enter otp:"))

    if otp == db_otp:
        
        print("Login successfull")

    else:
        print("Inalid otp")

else:
    print("Invalid password")


    

