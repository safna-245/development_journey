db_username = "safna"

db_password = 1234

user_name = (input("Enter username:"))

if user_name == db_username:

    password = int(input("Enter password:"))

    if password == db_password:

        print("LOGIN SUCCESSFULL")

    else:

        print("INVALID PASSWORD")

else:

    print("INVALID USERNAME")