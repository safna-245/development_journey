num = int(input("enter the number--"))

while(num != 0):

    digit = num % 10

    cube = digit ** 3

    print(f"cube of {digit} = {cube}")

    num = num // 10

