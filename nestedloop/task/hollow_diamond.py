for r in range(1,5):

    for s in range(1,4-r+1):

        print(" ",end=" ")

    for c in range(1,2*r):

        if c==1 or c==2*r-1:

            print("*",end=" ")

        else:

            print(" ",end=" ")

    print()

for r in range(3,0,-1):

    for s in range(1,4-r+1):

        print(" ",end=" ")

    for c in range(1,2*r):

        if c==1 or c==2*r-1:

            print("*",end=" ")

        else:

            print(" ",end=" ")

    print()