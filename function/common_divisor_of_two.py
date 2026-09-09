def common_divisor(num1,num2):

    for i in range(1,min(num1,num2)+1):

        if num1 %i == 0 and num2 %i == 0:

            print(i)


common_divisor(7,9)
common_divisor(6,8)
common_divisor(7,11)
common_divisor(24,30)