for r in range(1,5):

    for c in range(1,8):

        if r + c == 5 or c-r == 3 or (r == 3 and c == 4):

            print(r,end=" ")


        elif r ==4 and c%2 != 0:

            print(r,end=" ")

        else:
            print(" ",end=" ")

    print()

        