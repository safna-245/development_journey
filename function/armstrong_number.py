def is_armstrong(num):
    count = len(str(num))
    num_cpy = num
    sum = 0

    while(num != 0):

        digit = num % 10
        exponent = digit ** count
        sum = sum + exponent
        num = num //10
        
    if sum == num_cpy:

        print(True)

    else:

        print(False)

is_armstrong(153)
is_armstrong(159)








