def max_of_three(num1,num2,num3):

    if(num1 > num2 and num1 > num3):

        print(f"{num1} is maximum number")

    elif(num2 > num1 and num2 > num3):

        print(f"{num2} is maximum number")


    else:

        print(f"{num3} is maximum number")


max_of_three(10,15,19)
max_of_three(10,5,25)