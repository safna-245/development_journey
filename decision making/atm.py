
db_pin = 2026

db_balance = 5000

pin = int(input("Enter pin number"))

if pin == db_pin:

    amount = int(input("Enter withdrawal amount:"))

    if amount <= db_balance:

        print("Withdrawal successfull")

    else:

        print("Insufficient balance")

else:

    print("Incorrect pin")