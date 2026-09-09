num = int(input("Enter the number:"))

num_copy = num

count = len(str(num))

sum = 0

while(num != 0):

        digit = num % 10

        exponent = digit ** count

        sum = sum + exponent

        num = num //10


if (sum == num_copy):
        
        print("Armstrong number")

else:
        print(" Not Armstrong number")

    