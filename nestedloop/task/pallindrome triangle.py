for r in range(1,5):

    for s in range(4-r+1):

        print(" ",end=" ")

    for c in range(r,0,-1):

        print(c,end=" ")

    for c in range(2,r+1):

        print(c,end=" ")
        
    print()