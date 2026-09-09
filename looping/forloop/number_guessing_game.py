from random import randint

secret_number = randint(1,10)

for attempt in range(1,6):

    number = int(input("Guess the number--"))

    if(number == secret_number):

        print("Congratulations🎉🎉")

        break

else:

    print(f"Badluck🙅‍♀️🙅‍♀️  The Number is {secret_number} ")