for r in range(4):

    for s in range(4-r-1):

        print(" ",end="")

    num = 1

    for c in range(r+1):

        print(num,end=" ")

        num = num * (r-c)//(c+1)

    print()