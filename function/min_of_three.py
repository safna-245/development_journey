def min_of_three(num1,num2,num3):

    if(num1 < num2 and num1 < num3):

        print(f"{num1} is minimum number")

    elif(num2 < num1 and num2 < num3):

        print(f"{num2} is minimum number")


    else:

        print(f"{num3} is minimum number")


min_of_three(10,15,19)
min_of_three(10,5,25)