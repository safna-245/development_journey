from random import randint

secret_number = randint(1,10)

for attempt in range(1,6):

    number = int(input("Guess the number--"))

    if(number == secret_number):

        print("Congratulations🎉🎉")

        break

    elif(number > secret_number):

        print("too high")

    elif(number < secret_number):

        print("too low")

else:

    print(f"Badluck🙅‍♀️🙅‍♀️  The secret Number is {secret_number} ")