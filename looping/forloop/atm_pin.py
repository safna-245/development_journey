pin_num = 2026

for attempt in range(1,4):

    pin = int(input("Enter pin number"))

    if(pin == pin_num):

        print("unlocked successfullly")

        break

else:

    print("ATM Blocked")