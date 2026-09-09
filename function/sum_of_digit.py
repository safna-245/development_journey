def sum_of_n(num):

    sum = 0

    while(num != 0):

        digit = num % 10
        sum = sum + digit
        num = num //10

    print(sum)

sum_of_n(123)
sum_of_n(567)

