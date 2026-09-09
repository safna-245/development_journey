""" **Login System**: Verify username and password and display success or failure.

"""
db_username = "safna"

db_password = 1234

user_name = (input("Enter username:"))

password = int(input("Enter password:"))


if user_name == db_username and  password == db_password:

        print("LOGIN SUCCESSFULL")

else:

        print("LOGIN FAILURE")


    