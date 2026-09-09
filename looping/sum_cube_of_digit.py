num = int(input("enter the number--"))
sum = 0


while(num != 0):

    digit = num % 10

    cube = digit ** 3

    print(cube)

    sum = sum + cube

    num = num // 10

print(f"sum of cube={sum}")


